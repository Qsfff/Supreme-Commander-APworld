from dataclasses import dataclass

from Options import Choice, OptionGroup, OptionList, PerGameCommonOptions, Range, Toggle

# In this file, we define the options the player can pick.
# The most common types of options are Toggle, Range and Choice.

# Options will be in the game's template yaml.
# They will be represented by checkboxes, sliders etc. on the game's options page on the website.
# (Note: Options can also be made invisible from either of these places by overriding Option.visibility.
#  APQuest doesn't have an example of this, but this can be used for secret / hidden / advanced options.)

# For further reading on options, you can also read the Options API Document:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/options%20api.md


# The first type of Option we'll discuss is the Toggle.
# A toggle is an option that can either be on or off. This will be represented by a checkbox on the website.
# The default for a toggle is "off".
# If you want a toggle to be on by default, you can use the "DefaultOnToggle" class instead of the "Toggle" class.

factions = ["uef", "cybran", "aeon", "sera"]
class Difficulty(Range):
    """
    Difficulty
    1 = easy
    2 = medium
    3 = hard
    """

    display_name = "Difficulty"

    range_start = 1
    range_end = 3
    default = 2
 
class LocAmount(Range):
    """
    Amount of locations per objective
    To unlock full faction you would need a bit less than 2 for 6 level campaign
    If you want to have 1 campaign and all 4 factions you would obviously need 4 times more unlocks resulting with 8 locations per objective
    I allowed to put up to 16 for future when i add filler
    """

    display_name = "Amount of Locations"

    range_start = 1
    range_end = 16
    default = 1
 
class RandFacs(Toggle):
    """
    If on, factions will be randomised
    If off, factions will not be randomised and levels will be unique regardless of other options
    """
    display_name = "Randomised factions"
    default = True
   
class Faction(OptionList):
    """
    Choose which factions to play with
    Available options: uef, cybran, aeon, sera
    """
    display_name = "Faction"

    valid_keys = factions

    default = ["cybran"]
    
 
class Mapset(Choice):
    """
    Unique means each level would be unique
    All means levels would be duplicated for each faction selected
    """
    display_name = "Level selection"

    option_unique = 0
    option_all = 1

    # Choice options must define an explicit default value.
    default = option_unique


# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class SupComOptions(PerGameCommonOptions):
    difficulty: Difficulty
    locamount: LocAmount
    randfacs: RandFacs
    faction: Faction
    mapset: Mapset


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Difficulty options",
        [Difficulty , LocAmount],
    ),
    OptionGroup(
        "Faction options",
        [RandFacs, Faction, Mapset],
    ),
]

# Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
option_presets = {
    "basic": {
        "difficulty": 1,
        "locamount": 2,
        "randfacs": False,
        "mapset": Mapset.option_unique,
        "faction": ["cybran"],
    },
    "largw": {
        "difficulty": 3,
        "locamount": 3,
        "randfacs": True,
        "mapset": Mapset.option_all,
        "faction": ["uef", "cybran", "aeon", "sera"],
    },
}
