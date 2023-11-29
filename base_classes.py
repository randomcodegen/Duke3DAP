from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Set, Union

from BaseClasses import Entrance, Item, Location, Region

from .rules import RULETYPE, LambdaRule, Rule, Rules

if TYPE_CHECKING:
    from ..d3d import D3DWorld


class D3DItem(Item):
    game = "Duke3D"


class D3DLocation(Location):
    game = "Duke3D"


@dataclass(frozen=True)
class LocationDef:
    name: str
    type: str  # "exit", "sprite", "sector
    game_id: int  # Sprite number, sector number or exit lotag
    mp_only: bool = False
    sprite_type: str = ""  # additional data for sprites
    density: int = 0  # defines what density settings it appears in. Higher values require more locations enabled
    x: int = 0
    y: int = 0
    z: int = 0


@dataclass(frozen=True)
class ItemDef:
    name: str
    ap_id: int  # The id for the item
    type: str  # The type of item
    props: Dict[str, Any]  # Additional type specific properties
    unique: bool = False  # Can only have one of these
    persistent: bool = False  # These are persisted in the game save
    progression: bool = False  # Marks an item as being a progression item. Persistent non-progression are marked useful
    silent: bool = False  # These are acquired but not notified to the player


class D3DLevel(object):
    name: str
    levelnum: int
    volumenum: int
    location_defs: List[dict]
    keys: List[str]

    def __init__(self):
        self.world: Optional["D3DWorld"] = None
        self.prefix = f"E{self.volumenum + 1}L{self.levelnum + 1}"
        self.locations: Dict[str, LocationDef] = self._make_locations()
        self.used_locations: Set[
            str
        ] = set()  # locations actually filled in make_region

    def _make_locations(self) -> Dict[str, LocationDef]:
        ret = {}
        for loc_def in self.location_defs:
            loc_name = f'{self.prefix} {loc_def["name"]}'
            ret[loc_name] = LocationDef(
                name=loc_name,
                type=loc_def["type"],
                game_id=loc_def["id"],
                mp_only=loc_def.get("mp", False),
                sprite_type=loc_def.get("sprite_type"),
            )
        return ret

    def create_region(self, world: "D3DWorld") -> Region:
        self.world = world
        self.used_locations = set()
        ret = self.main_region()
        self.world = None
        return ret

    def main_region(self) -> Region:
        """
        To be implemented by each level
        """
        raise NotImplementedError

    def region(self, name: str, hint: Optional[str] = None) -> Region:
        return Region(
            f"{self.prefix} {name}", self.world.player, self.world.multiworld, hint
        )

    def add_location(self, location: str, region: Region):
        location = f"{self.prefix} {location}"
        if self.world.use_location(self.locations.get(location)):
            region.locations.append(
                D3DLocation(
                    self.world.player,
                    location,
                    self.world.location_name_to_id[location],
                    region,
                )
            )
            self.used_locations.add(location)

    def add_locations(self, locations: List[str], region: Region):
        for loc in locations:
            self.add_location(loc, region)

    def get_location(self, name) -> Optional[Location]:
        try:
            return self.world.multiworld.get_location(name, self.world.player)
        except KeyError:
            return None

    @staticmethod
    def _resolve_rule_type(rules: Union[RULETYPE, List[RULETYPE]]) -> Optional[Rule]:
        if not isinstance(rules, List):
            rules = [rules]
        if not rules:
            return None
        rule = rules[0]
        if not isinstance(rule, Rule):
            rule = LambdaRule(rule)
        for other_rule in rules[1:]:
            if not isinstance(other_rule, Rule):
                other_rule = LambdaRule(other_rule)
            rule |= other_rule
        return rule

    def connect(
        self, start: Region, end: Region, rules: Union[RULETYPE, List[RULETYPE]]
    ):
        start.connect(end, None, self._resolve_rule_type(rules))

    def restrict(
        self,
        spot: Optional[Union[Location, Entrance]],
        rules: Union[RULETYPE, List[RULETYPE]],
    ):
        if spot is not None:
            spot.access_rule = self._resolve_rule_type(rules)

    @property
    def red_key(self) -> Rule:
        return self.world.rules.has(f"{self.prefix} Red Key Card")

    @property
    def blue_key(self) -> Rule:
        return self.world.rules.has(f"{self.prefix} Blue Key Card")

    @property
    def yellow_key(self) -> Rule:
        return self.world.rules.has(f"{self.prefix} Yellow Key Card")

    @property
    def unlock(self) -> str:
        return f"{self.prefix} Unlock"

    @property
    def rules(self) -> Rules:
        return self.world.rules

    @property
    def items(self) -> List[str]:
        ret = []
        for color in ("Red", "Blue", "Yellow"):
            if color in self.keys:
                ret.append(f"{self.prefix} {color} Key Card")
        return ret


class D3DEpisode(object):
    name: str
    volumenum: int
    levels: List[D3DLevel]
