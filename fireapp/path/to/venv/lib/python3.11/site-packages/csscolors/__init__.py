"""
.. include:: ../README.md
"""


from typing import Iterator as _Iterator, Tuple as _Tuple


__all__ = [
    "ALICE_BLUE",
    "ANTIQUEWHITE",
    "AQUA",
    "AQUAMARINE",
    "AZURE",
    "BEIGE",
    "BISQUE",
    "BLACK",
    "BLANCHED_ALMOND",
    "BLUE",
    "BLUE_VIOLET",
    "BROWN",
    "BURLYWOOD",
    "CADET_BLUE",
    "CHARTREUSE",
    "CHOCOLATE",
    "CORAL",
    "CORNFLOWER_BLUE",
    "CORNSILK",
    "CRIMSON",
    "CYAN",
    "DARK_BLUE",
    "DARK_CYAN",
    "DARK_GOLDEN_ROD",
    "DARK_GRAY",
    "DARK_GREY",
    "DARK_GREEN",
    "DARK_KHAKI",
    "DARK_MAGENTA",
    "DARK_OLIVE_GREEN",
    "DARK_ORANGE",
    "DARK_ORCHID",
    "DARK_RED",
    "DARK_SALMON",
    "DARK_SEA_GREEN",
    "DARK_SLATE_BLUE",
    "DARK_SLATE_GRAY",
    "DARK_SLATE_GREY",
    "DARK_TURQUOISE",
    "DARK_VIOLET",
    "DEEP_PINK",
    "DEEP_SKY_BLUE",
    "DIM_GRAY",
    "DIM_GREY",
    "DODGER_BLUE",
    "FIRE_BRICK",
    "FLORALWHITE",
    "FOREST_GREEN",
    "FUCHSIA",
    "GAINSBORO",
    "GHOSTWHITE",
    "GOLD",
    "GOLDEN_ROD",
    "GRAY",
    "GREY",
    "GREEN",
    "GREEN_YELLOW",
    "HONEY_DEW",
    "HOT_PINK",
    "INDIAN_RED",
    "INDIGO",
    "IVORY",
    "KHAKI",
    "LAVENDER",
    "LAVENDER_BLUSH",
    "LAWN_GREEN",
    "LEMON_CHIFFON",
    "LIGHT_BLUE",
    "LIGHT_CORAL",
    "LIGHT_CYAN",
    "LIGHT_GOLDEN_ROD_YELLOW",
    "LIGHT_GRAY",
    "LIGHT_GREY",
    "LIGHT_GREEN",
    "LIGHT_PINK",
    "LIGHT_SALMON",
    "LIGHT_SEA_GREEN",
    "LIGHT_SKY_BLUE",
    "LIGHT_SLATE_GRAY",
    "LIGHT_SLATE_GREY",
    "LIGHT_STEEL_BLUE",
    "LIGHT_YELLOW",
    "LIME",
    "LIME_GREEN",
    "LINEN",
    "MAGENTA",
    "MAROON",
    "MEDIUM_AQUA_MARINE",
    "MEDIUM_BLUE",
    "MEDIUM_ORCHID",
    "MEDIUM_PURPLE",
    "MEDIUM_SEA_GREEN",
    "MEDIUM_SLATE_BLUE",
    "MEDIUM_SPRING_GREEN",
    "MEDIUM_TURQUOISE",
    "MEDIUM_VIOLET_RED",
    "MIDNIGHT_BLUE",
    "MINT_CREAM",
    "MISTY_ROSE",
    "MOCCASIN",
    "NAVAJOWHITE",
    "NAVY",
    "OLD_LACE",
    "OLIVE",
    "OLIVE_DRAB",
    "ORANGE",
    "ORANGE_RED",
    "ORCHID",
    "PALE_GOLDEN_ROD",
    "PALE_GREEN",
    "PALE_TURQUOISE",
    "PALE_VIOLET_RED",
    "PAPAYAWHIP",
    "PEACH_PUFF",
    "PERU",
    "PINK",
    "PLUM",
    "POWDER_BLUE",
    "PURPLE",
    "REBECCA_PURPLE",
    "RED",
    "ROSY_BROWN",
    "ROYAL_BLUE",
    "SADDLE_BROWN",
    "SALMON",
    "SANDY_BROWN",
    "SEA_GREEN",
    "SEA_SHELL",
    "SIENNA",
    "SILVER",
    "SKY_BLUE",
    "SLATE_BLUE",
    "SLATE_GRAY",
    "SLATE_GREY",
    "SNOW",
    "SPRING_GREEN",
    "STEEL_BLUE",
    "TAN",
    "TEAL",
    "THISTLE",
    "TOMATO",
    "TURQUOISE",
    "VIOLET",
    "WHEAT",
    "WHITE",
    "WHITE_SMOKE",
    "YELLOW",
    "YELLOW_GREEN",
    "iterator"
]
__version__ = "<%<%VERSION%>%>"


ALICE_BLUE = "#f0f8ff"
"""Hex code `#f0f8ff`"""
ANTIQUEWHITE = "#faebd7"
"""Hex code `#faebd7`"""
AQUA = "#00ffff"
"""Hex code `#00ffff`"""
AQUAMARINE = "#7fffd4"
"""Hex code `#7fffd4`"""
AZURE = "#f0ffff"
"""Hex code `#f0ffff`"""
BEIGE = "#f5f5dc"
"""Hex code `#f5f5dc`"""
BISQUE = "#ffe4c4"
"""Hex code `#ffe4c4`"""
BLACK = "#000000"
"""Hex code `#000000`"""
BLANCHED_ALMOND = "#ffebcd"
"""Hex code `#ffebcd`"""
BLUE = "#0000ff"
"""Hex code `#0000ff`"""
BLUE_VIOLET = "#8a2be2"
"""Hex code `#8a2be2`"""
BROWN = "#a52a2a"
"""Hex code `#a52a2a`"""
BURLYWOOD = "#deb887"
"""Hex code `#deb887`"""
CADET_BLUE = "#5f9ea0"
"""Hex code `#5f9ea0`"""
CHARTREUSE = "#7fff00"
"""Hex code `#7fff00`"""
CHOCOLATE = "#d2691e"
"""Hex code `#d2691e`"""
CORAL = "#ff7f50"
"""Hex code `#ff7f50`"""
CORNFLOWER_BLUE = "#6495ed"
"""Hex code `#6495ed`"""
CORNSILK = "#fff8dc"
"""Hex code `#fff8dc`"""
CRIMSON = "#dc143c"
"""Hex code `#dc143c`"""
CYAN = "#00ffff"
"""Hex code `#00ffff`"""
DARK_BLUE = "#00008b"
"""Hex code `#00008b`"""
DARK_CYAN = "#008b8b"
"""Hex code `#008b8b`"""
DARK_GOLDEN_ROD = "#b8860b"
"""Hex code `#b8860b`"""
DARK_GRAY = "#a9a9a9"
"""Hex code `#a9a9a9`"""
DARK_GREY = "#a9a9a9"
"""Hex code `#a9a9a9`"""
DARK_GREEN = "#006400"
"""Hex code `#006400`"""
DARK_KHAKI = "#bdb76b"
"""Hex code `#bdb76b`"""
DARK_MAGENTA = "#8b008b"
"""Hex code `#8b008b`"""
DARK_OLIVE_GREEN = "#556b2f"
"""Hex code `#556b2f`"""
DARK_ORANGE = "#ff8c00"
"""Hex code `#ff8c00`"""
DARK_ORCHID = "#9932cc"
"""Hex code `#9932cc`"""
DARK_RED = "#8b0000"
"""Hex code `#8b0000`"""
DARK_SALMON = "#e9967a"
"""Hex code `#e9967a`"""
DARK_SEA_GREEN = "#8fbc8f"
"""Hex code `#8fbc8f`"""
DARK_SLATE_BLUE = "#483d8b"
"""Hex code `#483d8b`"""
DARK_SLATE_GRAY = "#2f4f4f"
"""Hex code `#2f4f4f`"""
DARK_SLATE_GREY = "#2f4f4f"
"""Hex code `#2f4f4f`"""
DARK_TURQUOISE = "#00ced1"
"""Hex code `#00ced1`"""
DARK_VIOLET = "#9400d3"
"""Hex code `#9400d3`"""
DEEP_PINK = "#ff1493"
"""Hex code `#ff1493`"""
DEEP_SKY_BLUE = "#00bfff"
"""Hex code `#00bfff`"""
DIM_GRAY = "#696969"
"""Hex code `#696969`"""
DIM_GREY = "#696969"
"""Hex code `#696969`"""
DODGER_BLUE = "#1e90ff"
"""Hex code `#1e90ff`"""
FIRE_BRICK = "#b22222"
"""Hex code `#b22222`"""
FLORALWHITE = "#fffaf0"
"""Hex code `#fffaf0`"""
FOREST_GREEN = "#228b22"
"""Hex code `#228b22`"""
FUCHSIA = "#ff00ff"
"""Hex code `#ff00ff`"""
GAINSBORO = "#dcdcdc"
"""Hex code `#dcdcdc`"""
GHOSTWHITE = "#f8f8ff"
"""Hex code `#f8f8ff`"""
GOLD = "#ffd700"
"""Hex code `#ffd700`"""
GOLDEN_ROD = "#daa520"
"""Hex code `#daa520`"""
GRAY = "#808080"
"""Hex code `#808080`"""
GREY = "#808080"
"""Hex code `#808080`"""
GREEN = "#008000"
"""Hex code `#008000`"""
GREEN_YELLOW = "#adff2f"
"""Hex code `#adff2f`"""
HONEY_DEW = "#f0fff0"
"""Hex code `#f0fff0`"""
HOT_PINK = "#ff69b4"
"""Hex code `#ff69b4`"""
INDIAN_RED = "#cd5c5c"
"""Hex code `#cd5c5c`"""
INDIGO = "#4b0082"
"""Hex code `#4b0082`"""
IVORY = "#fffff0"
"""Hex code `#fffff0`"""
KHAKI = "#f0e68c"
"""Hex code `#f0e68c`"""
LAVENDER = "#e6e6fa"
"""Hex code `#e6e6fa`"""
LAVENDER_BLUSH = "#fff0f5"
"""Hex code `#fff0f5`"""
LAWN_GREEN = "#7cfc00"
"""Hex code `#7cfc00`"""
LEMON_CHIFFON = "#fffacd"
"""Hex code `#fffacd`"""
LIGHT_BLUE = "#add8e6"
"""Hex code `#add8e6`"""
LIGHT_CORAL = "#f08080"
"""Hex code `#f08080`"""
LIGHT_CYAN = "#e0ffff"
"""Hex code `#e0ffff`"""
LIGHT_GOLDEN_ROD_YELLOW = "#fafad2"
"""Hex code `#fafad2`"""
LIGHT_GRAY = "#d3d3d3"
"""Hex code `#d3d3d3`"""
LIGHT_GREY = "#d3d3d3"
"""Hex code `#d3d3d3`"""
LIGHT_GREEN = "#90ee90"
"""Hex code `#90ee90`"""
LIGHT_PINK = "#ffb6c1"
"""Hex code `#ffb6c1`"""
LIGHT_SALMON = "#ffa07a"
"""Hex code `#ffa07a`"""
LIGHT_SEA_GREEN = "#20b2aa"
"""Hex code `#20b2aa`"""
LIGHT_SKY_BLUE = "#87cefa"
"""Hex code `#87cefa`"""
LIGHT_SLATE_GRAY = "#778899"
"""Hex code `#778899`"""
LIGHT_SLATE_GREY = "#778899"
"""Hex code `#778899`"""
LIGHT_STEEL_BLUE = "#b0c4de"
"""Hex code `#b0c4de`"""
LIGHT_YELLOW = "#ffffe0"
"""Hex code `#ffffe0`"""
LIME = "#00ff00"
"""Hex code `#00ff00`"""
LIME_GREEN = "#32cd32"
"""Hex code `#32cd32`"""
LINEN = "#faf0e6"
"""Hex code `#faf0e6`"""
MAGENTA = "#ff00ff"
"""Hex code `#ff00ff`"""
MAROON = "#800000"
"""Hex code `#800000`"""
MEDIUM_AQUA_MARINE = "#66cdaa"
"""Hex code `#66cdaa`"""
MEDIUM_BLUE = "#0000cd"
"""Hex code `#0000cd`"""
MEDIUM_ORCHID = "#ba55d3"
"""Hex code `#ba55d3`"""
MEDIUM_PURPLE = "#9370db"
"""Hex code `#9370db`"""
MEDIUM_SEA_GREEN = "#3cb371"
"""Hex code `#3cb371`"""
MEDIUM_SLATE_BLUE = "#7b68ee"
"""Hex code `#7b68ee`"""
MEDIUM_SPRING_GREEN = "#00fa9a"
"""Hex code `#00fa9a`"""
MEDIUM_TURQUOISE = "#48d1cc"
"""Hex code `#48d1cc`"""
MEDIUM_VIOLET_RED = "#c71585"
"""Hex code `#c71585`"""
MIDNIGHT_BLUE = "#191970"
"""Hex code `#191970`"""
MINT_CREAM = "#f5fffa"
"""Hex code `#f5fffa`"""
MISTY_ROSE = "#ffe4e1"
"""Hex code `#ffe4e1`"""
MOCCASIN = "#ffe4b5"
"""Hex code `#ffe4b5`"""
NAVAJOWHITE = "#ffdead"
"""Hex code `#ffdead`"""
NAVY = "#000080"
"""Hex code `#000080`"""
OLD_LACE = "#fdf5e6"
"""Hex code `#fdf5e6`"""
OLIVE = "#808000"
"""Hex code `#808000`"""
OLIVE_DRAB = "#6b8e23"
"""Hex code `#6b8e23`"""
ORANGE = "#ffa500"
"""Hex code `#ffa500`"""
ORANGE_RED = "#ff4500"
"""Hex code `#ff4500`"""
ORCHID = "#da70d6"
"""Hex code `#da70d6`"""
PALE_GOLDEN_ROD = "#eee8aa"
"""Hex code `#eee8aa`"""
PALE_GREEN = "#98fb98"
"""Hex code `#98fb98`"""
PALE_TURQUOISE = "#afeeee"
"""Hex code `#afeeee`"""
PALE_VIOLET_RED = "#db7093"
"""Hex code `#db7093`"""
PAPAYAWHIP = "#ffefd5"
"""Hex code `#ffefd5`"""
PEACH_PUFF = "#ffdab9"
"""Hex code `#ffdab9`"""
PERU = "#cd853f"
"""Hex code `#cd853f`"""
PINK = "#ffc0cb"
"""Hex code `#ffc0cb`"""
PLUM = "#dda0dd"
"""Hex code `#dda0dd`"""
POWDER_BLUE = "#b0e0e6"
"""Hex code `#b0e0e6`"""
PURPLE = "#800080"
"""Hex code `#800080`"""
REBECCA_PURPLE = "#663399"
"""Hex code `#663399`"""
RED = "#ff0000"
"""Hex code `#ff0000`"""
ROSY_BROWN = "#bc8f8f"
"""Hex code `#bc8f8f`"""
ROYAL_BLUE = "#4169e1"
"""Hex code `#4169e1`"""
SADDLE_BROWN = "#8b4513"
"""Hex code `#8b4513`"""
SALMON = "#fa8072"
"""Hex code `#fa8072`"""
SANDY_BROWN = "#f4a460"
"""Hex code `#f4a460`"""
SEA_GREEN = "#2e8b57"
"""Hex code `#2e8b57`"""
SEA_SHELL = "#fff5ee"
"""Hex code `#fff5ee`"""
SIENNA = "#a0522d"
"""Hex code `#a0522d`"""
SILVER = "#c0c0c0"
"""Hex code `#c0c0c0`"""
SKY_BLUE = "#87ceeb"
"""Hex code `#87ceeb`"""
SLATE_BLUE = "#6a5acd"
"""Hex code `#6a5acd`"""
SLATE_GRAY = "#708090"
"""Hex code `#708090`"""
SLATE_GREY = "#708090"
"""Hex code `#708090`"""
SNOW = "#fffafa"
"""Hex code `#fffafa`"""
SPRING_GREEN = "#00ff7f"
"""Hex code `#00ff7f`"""
STEEL_BLUE = "#4682b4"
"""Hex code `#4682b4`"""
TAN = "#d2b48c"
"""Hex code `#d2b48c`"""
TEAL = "#008080"
"""Hex code `#008080`"""
THISTLE = "#d8bfd8"
"""Hex code `#d8bfd8`"""
TOMATO = "#ff6347"
"""Hex code `#ff6347`"""
TURQUOISE = "#40e0d0"
"""Hex code `#40e0d0`"""
VIOLET = "#ee82ee"
"""Hex code `#ee82ee`"""
WHEAT = "#f5deb3"
"""Hex code `#f5deb3`"""
WHITE = "#ffffff"
"""Hex code `#ffffff`"""
WHITE_SMOKE = "#f5f5f5"
"""Hex code `#f5f5f5`"""
YELLOW = "#ffff00"
"""Hex code `#ffff00`"""
YELLOW_GREEN = "#9acd32"
"""Hex code `#9acd32`"""


def iterator() -> _Iterator[_Tuple[str, str]]:
    """Iterates through the available colors.

    Returns:
        Iterator[Tuple[str, str]]: Yields pairs of color name and color hex code.
    """
    for key, value in globals().items():
        if not key.startswith("_") and key[0].isupper():
            yield key, value


def _fix_pdoc():
    import os
    import queue
    from types import ModuleType

    root = os.path.dirname(__file__)
    modules = queue.Queue()
    for module in __all__:
        modules.put_nowait((module,))

    while not modules.empty():
        module_name = modules.get_nowait()
        module = eval(".".join(module_name))
        if not isinstance(module, ModuleType):
            continue
        if "__pdoc__" not in dir(module):
            module.__pdoc__ = {}
        if "__all__" not in dir(module):
            module.__all__ = []

        for obj in module.__all__:
            obj = eval(".".join(module_name) + f".{obj}")
            if not isinstance(obj, ModuleType):
                obj.__module__ = "csscolors." + ".".join(module_name)

        for submodule in os.listdir(os.path.join(root, *module_name)):
            submodule_path = os.path.join(root, *module_name, submodule)
            if submodule.startswith("_"):
                continue
            if os.path.isdir(submodule_path) and "__init__.py" in os.listdir(
                submodule_path
            ):
                module.__pdoc__[submodule] = submodule in module.__all__
                if submodule in module.__all__:
                    modules.put_nowait(module_name + (submodule,))
            elif submodule.endswith(".py"):
                submodule = submodule[:-3]
                module.__pdoc__[submodule] = submodule in module.__all__


_fix_pdoc()
