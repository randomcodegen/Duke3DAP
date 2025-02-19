from BaseClasses import Region

from ..base_classes import D3DLevel


class E4L10(D3DLevel):
    name = "The Queen"
    levelnum = 9
    volumenum = 3
    keys = ["Red", "Blue", "Yellow"]
    location_defs = [
        {"id": 29, "name": "R-Side Dive Jetpack", "type": "sprite"},
        {"id": 150, "name": "R-Side Protective Boots", "type": "sprite"},
        {"id": 151, "name": "L-Side Protective Boots", "type": "sprite"},
        {"id": 260, "name": "Yellow Dive Atomic Health 1", "type": "sprite"},
        {"id": 297, "mp": True, "name": "MP Start Shotgun 1", "type": "sprite"},
        {"id": 298, "mp": True, "name": "MP Start Shotgun 2", "type": "sprite"},
        {"id": 299, "mp": True, "name": "MP Start Shotgun 3", "type": "sprite"},
        {"id": 300, "mp": True, "name": "MP Start Shotgun 4", "type": "sprite"},
        {"id": 312, "name": "L-Side Vent Pipebombs", "type": "sprite"},
        {"id": 315, "name": "Center Pipebombs 1", "type": "sprite"},
        {"id": 316, "name": "Center Pipebombs 2", "type": "sprite"},
        {"id": 331, "name": "Queen Medkit", "type": "sprite"},
        {"id": 332, "name": "Queen Atomic Health", "type": "sprite"},
        {"id": 333, "name": "Queen Armor", "type": "sprite"},
        {"id": 337, "name": "L-Side Scuba Gear", "type": "sprite"},
        {"id": 338, "name": "R-Side Protective Boots", "type": "sprite"},
        {"id": 374, "name": "L-Side Dive Armor", "type": "sprite"},
        {"id": 375, "name": "L-Side Dive Atomic Health", "type": "sprite"},
        {"id": 388, "mp": True, "name": "MP Center Devastator 1", "type": "sprite"},
        {"id": 424, "name": "Red Medkit", "type": "sprite"},
        {"id": 453, "name": "R-Side RPG", "type": "sprite"},
        {"id": 561, "name": "561 Jetpack", "type": "sprite"},
        {"id": 579, "name": "L-Side RPG", "type": "sprite"},
        {"id": 613, "mp": True, "name": "MP Lobby Shotgun 4", "type": "sprite"},
        {"id": 614, "mp": True, "name": "MP Lobby Shotgun 1", "type": "sprite"},
        {"id": 615, "name": "Lobby Shotgun Shotgun 1", "type": "sprite"},
        {"id": 616, "mp": True, "name": "MP Lobby Shotgun 3", "type": "sprite"},
        {"id": 624, "name": "L-Side Jetpack", "type": "sprite"},
        {"id": 669, "mp": True, "name": "MP Center Devastator 2", "type": "sprite"},
        {"id": 686, "name": "Lobby Pipebombs 1", "type": "sprite"},
        {"id": 701, "mp": True, "name": "MP Lobby Shotgun 5", "type": "sprite"},
        {"id": 702, "mp": True, "name": "MP Lobby Shotgun 2", "type": "sprite"},
        {"id": 776, "name": "Blue Medkit", "type": "sprite"},
        {"id": 789, "name": "L-Side Dive Blue Key Card", "type": "sprite"},
        {"id": 823, "name": "R-Side Dive Red Key Card", "type": "sprite"},
        {"id": 824, "name": "R-Side Dive Atomic Health", "type": "sprite"},
        {"id": 825, "name": "R-Side Dive Armor", "type": "sprite"},
        {"id": 840, "name": "L-Side Armor", "type": "sprite"},
        {"id": 841, "name": "R-Side Armor", "type": "sprite"},
        {"id": 842, "name": "Red Room Yellow Key Card", "type": "sprite"},
        {"id": 844, "name": "Yellow Steroids", "type": "sprite"},
        {"id": 852, "name": "Yellow Dive Atomic Health 2", "type": "sprite"},
        {"id": 859, "mp": True, "name": "MP Pillar 1 Chaingun", "type": "sprite"},
        {"id": 860, "mp": True, "name": "MP Pillar 3 Chaingun", "type": "sprite"},
        {"id": 861, "mp": True, "name": "MP Pillar 4 Chaingun", "type": "sprite"},
        {"id": 862, "mp": True, "name": "MP Pillar 2 Chaingun", "type": "sprite"},
        {"id": 891, "name": "Lobby Pipebombs 4", "type": "sprite"},
        {"id": 892, "name": "Lobby Pipebombs 2", "type": "sprite"},
        {"id": 893, "name": "Lobby Pipebombs 3", "type": "sprite"},
        {"id": 894, "mp": True, "name": "MP Lobby Chaingun 2", "type": "sprite"},
        {"id": 895, "mp": True, "name": "MP Lobby Chaingun 1", "type": "sprite"},
        {"id": 896, "name": "Lobby Chaingun 1", "type": "sprite"},
        {"id": 897, "name": "Lobby Chaingun 2", "type": "sprite"},
        {"id": 903, "name": "L-Side Devastator", "type": "sprite"},
        {"id": 904, "name": "R-Side Devastator", "type": "sprite"},
        {"id": 933, "name": "DukeTag RPG 1", "type": "sprite"},
        {"id": 934, "name": "DukeTag RPG 2", "type": "sprite"},
        {"id": 964, "name": "R-Side Vent Pipebombs", "type": "sprite"},
        {"id": 65, "name": "Pillar 1 Secret", "type": "sector"},
        {"id": 67, "name": "Pillar 2 Secret", "type": "sector"},
        {"id": 70, "name": "Pillar 3 Secret", "type": "sector"},
        {"id": 72, "name": "Pillar 4 Secret", "type": "sector"},
        {"id": 197, "name": "L-Side Vent Secret", "type": "sector"},
        {"id": 357, "name": "R-Side Vent Secret", "type": "sector"},
        {"id": 630, "name": "Queen Secret", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
    def main_region(self) -> Region:
        r = self.rules
        ret = self.region(
            self.name,
            [
                "MP Start Shotgun 1",
                "MP Start Shotgun 2",
                "MP Start Shotgun 3",
                "MP Start Shotgun 4",
                "MP Lobby Shotgun 1",
                "MP Lobby Shotgun 2",
                "MP Lobby Shotgun 3",
                "MP Lobby Shotgun 4",
                "MP Lobby Shotgun 5",
                "Lobby Pipebombs 1",
                "Lobby Pipebombs 2",
                "Lobby Pipebombs 3",
                "Lobby Pipebombs 4",
                "Lobby Chaingun 1",
                "Lobby Chaingun 2",
                "MP Lobby Chaingun 1",
                "MP Lobby Chaingun 2",
                "Lobby Shotgun Shotgun 1",
                "Center Pipebombs 1",
                "Center Pipebombs 2",
                "MP Center Devastator 1",
                "MP Center Devastator 2",
                "L-Side Scuba Gear",
                "L-Side RPG",
                "L-Side Devastator",
            ],
        )

        lside_upper = self.region(
            "L-Side Upper",
            [
                "L-Side Vent Pipebombs",
                "L-Side Vent Secret",
                "L-Side Armor",
            ],
        )
        self.connect(ret, lside_upper, r.jump)

        lside_dive = self.region(
            "L-Side Dive",
            [
                "L-Side Dive Armor",
                "L-Side Dive Atomic Health",
                "L-Side Dive Blue Key Card",
            ],
        )
        self.connect(ret, lside_dive, r.dive(1000))

        blue_key_room = self.region(
            "Blue Key Room",
            [
                "Blue Medkit",
            ],
        )
        self.connect(ret, blue_key_room, r.jump & self.blue_key)
        
        rside = self.region(
            "Right Side",
            [
                "R-Side Protective Boots",
                "R-Side RPG",
                "R-Side Devastator",
                "R-Side Vent Secret",
                "R-Side Vent Pipebombs",
            ],
        )
        self.connect(blue_key_room, rside)

        rside_upper = self.region(
            "Right Side Upper",
            [
                "R-Side Armor",
            ],
        )
        self.connect(rside, rside_upper, r.jump)

        pillar_secrets = self.region(
            "Pillar Secrets",
            [
                "Pillar 1 Secret",
                "MP Pillar 1 Chaingun",
                "Pillar 2 Secret",
                "MP Pillar 2 Chaingun",
                "Pillar 3 Secret",
                "MP Pillar 3 Chaingun",
                "Pillar 4 Secret",
                "MP Pillar 4 Chaingun",
            ],
        )
        # 50 might also be enough but very tight
        self.connect(ret, pillar_secrets, r.jetpack(75))
        
        red_key_room = self.region(
            "Red Key Room",
            [
                "Red Medkit",
                "Red Room Yellow Key Card",
            ],
        )
        self.connect(rside, red_key_room, r.jetpack & self.red_key)

        rside_dive = self.region(
            "Red Dive",
            [
                "R-Side Dive Jetpack", 
                "R-Side Dive Red Key Card", 
                "R-Side Dive Atomic Health",
                "R-Side Dive Armor",
            ],
        )
        self.connect(rside, rside_dive, r.dive(1000))
        
        yellow_key_room = self.region(
            "Yellow Key Room",
            [
                "Yellow Steroids",
            ],
        )
        self.connect(red_key_room, yellow_key_room, self.yellow_key & r.jetpack(150) |
                     (r.crouch_jump & r.steroids))

        yellow_dive = self.region(
            "Yellow Dive",
            [
                "Yellow Dive Atomic Health 1",
                "Yellow Dive Atomic Health 2",
                "Queen Secret",
                "Queen Medkit",
                "Queen Atomic Health",
                "Queen Armor",
                "Exit",
            ],
        )
        # 30 RPG Ammo required, 1600 Scuba is cutting it close
        self.connect(yellow_key_room, yellow_dive, r.dive(1800) & r.has_group("RPG"))
        # Unreachable DukeTag MP Locations at the Start:
        # {"id": 933, "name": "DukeTag RPG 1", "type": "sprite"},
        # {"id": 934, "name": "DukeTag RPG 2", "type": "sprite"},
        # R-Side MP Only {"id": 150, "name": "R-Side Protective Boots", "type": "sprite"},
        # R-Side MP Only 
        # L-Side MP Only {"id": 151, "name": "L-Side Protective Boots", "type": "sprite"},
        # L-Side MP Only {"id": 624, "name": "L-Side Jetpack", "type": "sprite"},