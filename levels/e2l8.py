from BaseClasses import Region

from ..base_classes import D3DLevel


class E2L8(D3DLevel):
    name = "Dark Side"
    levelnum = 7
    volumenum = 1
    keys = ["Red"]
    location_defs = [
        {"id": 42, "mp": True, "name": "MP 42 Pipebombs", "type": "sprite"},
        {"id": 156, "mp": True, "name": "MP 156 Atomic Health", "type": "sprite"},
        {"id": 157, "mp": True, "name": "MP 157 Atomic Health", "type": "sprite"},
        {"id": 203, "mp": True, "name": "MP 203 Shrinker", "type": "sprite"},
        {"id": 206, "mp": True, "name": "MP 206 Pipebombs", "type": "sprite"},
        {"id": 207, "mp": True, "name": "MP 207 Pipebombs", "type": "sprite"},
        {"id": 211, "mp": True, "name": "MP 211 RPG", "type": "sprite"},
        {"id": 212, "mp": True, "name": "MP 212 Devastator", "type": "sprite"},
        {"id": 226, "mp": True, "name": "MP 226 Armor", "type": "sprite"},
        {"id": 242, "mp": True, "name": "MP 242 Pipebombs", "type": "sprite"},
        {"id": 247, "mp": True, "name": "MP 247 Armor", "type": "sprite"},
        {"id": 251, "mp": True, "name": "MP 251 Shotgun", "type": "sprite"},
        {"id": 257, "mp": True, "name": "MP 257 Atomic Health", "type": "sprite"},
        {"id": 261, "mp": True, "name": "MP 261 Medkit", "type": "sprite"},
        {"id": 265, "mp": True, "name": "MP 265 Chaingun", "type": "sprite"},
        {"id": 266, "mp": True, "name": "MP 266 RPG", "type": "sprite"},
        {"id": 269, "mp": True, "name": "MP 269 Devastator", "type": "sprite"},
        {"id": 342, "mp": True, "name": "MP 342 Atomic Health", "type": "sprite"},
        {"id": 343, "mp": True, "name": "MP 343 Atomic Health", "type": "sprite"},
        {"id": 347, "mp": True, "name": "MP 347 Armor", "type": "sprite"},
        {"id": 348, "mp": True, "name": "MP 348 Atomic Health", "type": "sprite"},
        {"id": 359, "mp": True, "name": "MP 359 Pipebombs", "type": "sprite"},
        {"id": 361, "mp": True, "name": "MP 361 Tripbomb", "type": "sprite"},
        {"id": 363, "mp": True, "name": "MP 363 Pipebombs", "type": "sprite"},
        {"id": 364, "mp": True, "name": "MP 364 Medkit", "type": "sprite"},
        {"id": 372, "mp": True, "name": "MP 372 Shotgun", "type": "sprite"},
        {"id": 374, "mp": True, "name": "MP 374 Atomic Health", "type": "sprite"},
        {"id": 375, "mp": True, "name": "MP 375 Chaingun", "type": "sprite"},
        {"id": 406, "name": "406 Chaingun", "type": "sprite"},
        {"id": 407, "mp": True, "name": "MP 407 Shrinker", "type": "sprite"},
        {"id": 520, "mp": True, "name": "MP 520 Blue Key Card", "type": "sprite"},
        {"id": 790, "mp": True, "name": "MP 790 Freezethrower", "type": "sprite"},
        {"id": 797, "mp": True, "name": "MP 797 Armor", "type": "sprite"},
        {"id": 801, "mp": True, "name": "MP 801 Devastator", "type": "sprite"},
        {"id": 836, "name": "836 RPG", "type": "sprite"},
        {"id": 837, "mp": True, "name": "MP 837 Pipebombs", "type": "sprite"},
        {"id": 843, "name": "843 Yellow Key Card", "type": "sprite"},
        {"id": 932, "mp": True, "name": "MP 932 Armor", "type": "sprite"},
        {
            "id": 952,
            "mp": True,
            "name": "MP 952 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 953, "mp": True, "name": "MP 953 Steroids", "type": "sprite"},
        {"id": 954, "mp": True, "name": "MP 954 Holo Duke", "type": "sprite"},
        {"id": 955, "mp": True, "name": "MP 955 Protective Boots", "type": "sprite"},
        {
            "id": 989,
            "mp": True,
            "name": "MP 989 Night Vision Goggles",
            "type": "sprite",
        },
        {"id": 990, "mp": True, "name": "MP 990 Armor", "type": "sprite"},
        {"id": 991, "name": "991 Jetpack", "type": "sprite"},
        {"id": 992, "name": "992 Atomic Health", "type": "sprite"},
        {"id": 993, "name": "993 Atomic Health", "type": "sprite"},
        {"id": 994, "name": "994 Steroids", "type": "sprite"},
        {"id": 995, "name": "995 Jetpack", "type": "sprite"},
        {"id": 996, "name": "996 Shrinker", "type": "sprite"},
        {"id": 997, "name": "997 RPG", "type": "sprite"},
        {"id": 998, "name": "998 Freezethrower", "type": "sprite"},
        {"id": 1007, "mp": True, "name": "MP 1007 Tripbomb", "type": "sprite"},
        {"id": 1008, "mp": True, "name": "MP 1008 Shrinker", "type": "sprite"},
        {"id": 1009, "mp": True, "name": "MP 1009 Tripbomb", "type": "sprite"},
        {"id": 1016, "mp": True, "name": "MP 1016 Atomic Health", "type": "sprite"},
        {"id": 1017, "mp": True, "name": "MP 1017 Pipebombs", "type": "sprite"},
        {"id": 1018, "mp": True, "name": "MP 1018 Pipebombs", "type": "sprite"},
        {"id": 1019, "mp": True, "name": "MP 1019 Pipebombs", "type": "sprite"},
        {"id": 352, "name": "Secret 1", "type": "sector"},
        {"id": 579, "name": "Secret 2", "type": "sector"},
        {"id": 647, "name": "Secret 3", "type": "sector"},
        {"id": 675, "name": "Secret 4", "type": "sector"},
        {"id": 701, "name": "Secret 5", "type": "sector"},
        {"id": 713, "name": "Secret 6", "type": "sector"},
        {"id": 726, "name": "Secret 7", "type": "sector"},
        {"id": 0, "name": "Exit", "type": "exit"},
    ]
