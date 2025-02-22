from BaseClasses import Region

from ..base_classes import D3DLevel


# This is a bit of a meme level with no exit, deathmatch only
# But it theoretically can be reached via glitches in the vanilla game, so might as well map it out
class E1L7(D3DLevel):
    name = "Faces of Death"
    levelnum = 6
    volumenum = 0
    keys = ["Blue"]
    location_defs = [
        # Don't think there's a way to get in here in single player for these two items
        {"name": "MP Side Room Devastator", "id": 0, "type": "sprite", "mp": True},
        {"name": "MP Side Room RPG", "id": 1, "type": "sprite", "mp": True},
        {"name": "Waterfall 2 Atomic Health", "id": 21, "type": "sprite"},
        {"name": "Waterfall 2 Armor", "id": 22, "type": "sprite"},
        {"name": "Waterfall 1 Armor", "id": 23, "type": "sprite"},
        {"name": "Waterfall 1 Atomic Health", "id": 24, "type": "sprite"},
        {"name": "Center Room Atomic Health 1", "id": 97, "type": "sprite"},
        {"name": "Center Room Atomic Health 2", "id": 98, "type": "sprite"},
        {"name": "Center Room Armor", "id": 107, "type": "sprite"},
        {"name": "Center Room Holo Duke", "id": 108, "type": "sprite"},
        {"name": "Center Atomic Health", "id": 109, "type": "sprite"},
        {"name": "Center Armor", "id": 110, "type": "sprite"},
        {"name": "Center Protective Boots", "id": 111, "type": "sprite"},
        {"name": "Center Night Vision Goggles", "id": 112, "type": "sprite"},
        {"name": "Center Steroids", "id": 113, "type": "sprite"},
        {"name": "Center Room Tripmine 1", "id": 121, "type": "sprite"},
        {"name": "Center Room Tripmine 2", "id": 122, "type": "sprite"},
        {"name": "Side Room Pipebombs", "id": 127, "type": "sprite"},
        {"name": "Water Tank Shotgun", "id": 179, "type": "sprite"},
        {"name": "Water Tank Devastator", "id": 231, "type": "sprite"},
        {"name": "Water Tank Freezethrower", "id": 232, "type": "sprite"},
        {"name": "Water Tank Chaingun", "id": 233, "type": "sprite"},
        {"name": "Main Room RPG", "id": 234, "type": "sprite"},
        {"name": "Water Tank Jetpack", "id": 235, "type": "sprite"},
        {"name": "Water Tank Tripmine 1", "id": 236, "type": "sprite"},
        {"name": "Water Tank Tripmine 2", "id": 237, "type": "sprite"},
        {"name": "Water Tank Shrinker", "id": 238, "type": "sprite"},
        {"name": "Main Room Pipebombs", "id": 248, "type": "sprite"},
        {"name": "Blue Key Card", "id": 302, "type": "sprite"},
        {"name": "Behind Waterfall 1", "id": 110, "type": "sector"},
        {"name": "Behind Waterfall 2", "id": 111, "type": "sector"},
    ]
    must_dive = True

    def main_region2(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            ["Side Room Pipebombs", "Main Room Pipebombs"],
        )

        water_tanks = self.region(
            "Water Tanks",
            [
                "Water Tank Chaingun",
                "Water Tank Shotgun",
                "Water Tank Jetpack",
                "Water Tank Tripmine 1",
                "Water Tank Tripmine 2",
                "Water Tank Shrinker",
                "Water Tank Freezethrower",
                "Water Tank Devastator",
            ],
        )
        self.connect(ret, water_tanks, r.can_dive)

        waterfall = self.region(
            "Waterfall Secrets",
            [
                "Behind Waterfall 1",
                "Behind Waterfall 2",
                "Waterfall 1 Armor",
                "Waterfall 2 Armor",
                "Waterfall 1 Atomic Health",
                "Waterfall 1 Atomic Health",
            ],
        )
        # Need to jump on a battlelord to get in
        self.connect(
            ret, waterfall, r.jetpack(50) | (r.difficulty("medium") & r.can_jump)
        )

        central_platform = self.region(
            "Central Platform",
            [
                "Center Steroids",
                "Center Atomic Health",
                "Blue Key Card",
                "Center Protective Boots",
                "Center Night Vision Goggles",
                "Center Armor",
            ],
        )
        self.connect(ret, central_platform, r.jump)

        center_room = self.region(
            "Center Room",
            [
                "Center Room Armor",
                "Center Room Tripmine 1",
                "Center Room Tripmine 2",
                "Center Room Holo Duke",
                "Center Room Atomic Health 1",
                "Center Room Atomic Health 2",
            ],
        )
        self.connect(ret, center_room, self.blue_key)
        return ret
