from Constants import *
from Util import createRewardsCSVRowFromDict
from Util import convert_dict_to_yaml
import os
from TemplateClasses.Crate import Crate
import yaml

TWO_DIE_ROLL_CHANCES = {
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 6,
    8: 5,
    9: 4,
    10: 3,
    11: 2,
    12: 1
}

TWO_DIE_ROLL_TOTAL_CHANCE = sum(TWO_DIE_ROLL_CHANCES.values())

CRAPS_DEFAULTS = {
    RewardCSVConstants.DISPLAY_NAME: "",
    RewardCSVConstants.DISPLAY_ITEM: "TRIPWIRE_HOOK",
    RewardCSVConstants.DISPLAY_AMOUNT: 1,
    RewardCSVConstants.LORE: "",
    RewardCSVConstants.MAX_RANGE: "",
    RewardCSVConstants.CHANCE: -1,
    RewardCSVConstants.PERCENT_CHANCE: -1,
    RewardCSVConstants.ITEMS: "AIR",
    RewardCSVConstants.AMOUNTS: "1",
    RewardCSVConstants.COMMANDS: "",
    RewardCSVConstants.TIMES_TO_EXECUTE_COMMANDS: 1,
    RewardCSVConstants.MESSAGES: "",
}

FIRST_ROLL_WINS = {7}
FIRST_ROLL_LOSSES = {2, 3, 12}

CRAPS_CSV_DIR = f"../CrateCSVs/Craps"
CRAPS_YML_DIR = f"../Crates/Craps"

CRAPS_ENTRY_AMOUNT_DEFAULT = 25000

CRAPS_RESULT_AMOUNTS_DEFAULT = {
    "WIN": 50000,
    "LOSE": 0,
    "REROLL": 0
}

# print(os.listdir("../CrateCSVs/Craps"))

def createCraps(amountsDict=CRAPS_RESULT_AMOUNTS_DEFAULT, crapsEntryAmount=CRAPS_ENTRY_AMOUNT_DEFAULT):
    curCrapsCSVDir = f"{CRAPS_CSV_DIR}/{crapsEntryAmount}"
    curCrapsYMLDir = f"{CRAPS_YML_DIR}/{crapsEntryAmount}"

    crapsKeyName = f"Craps{crapsEntryAmount}"

    if str(crapsEntryAmount) not in os.listdir(CRAPS_CSV_DIR):
        os.mkdir(curCrapsCSVDir)

    if str(crapsEntryAmount) not in os.listdir(CRAPS_YML_DIR):
        os.mkdir(curCrapsYMLDir)

    with open(f"{curCrapsCSVDir}/Craps{crapsEntryAmount}Crate-FirstRoll.csv", 'w') as outfile:
        crapsRows = list()
        crapsRows.append("DisplayName,DisplayItem,DisplayAmount,Lore,MaxRange,Chance,PercentChance,Items,Amounts,Commands,TimesToExecuteCommands,Messages")
        for i in range(2, 13):
            crapsInfoDict = CRAPS_DEFAULTS
            curNumChance = TWO_DIE_ROLL_CHANCES[i]
            crapsInfoDict[RewardCSVConstants.DISPLAY_NAME] = f"&a&l{i}!!! "
            crapsInfoDict[RewardCSVConstants.CHANCE] = curNumChance
            crapsInfoDict[RewardCSVConstants.PERCENT_CHANCE] = round(100 * curNumChance/TWO_DIE_ROLL_TOTAL_CHANCE, 2)
            crapsInfoDict[RewardCSVConstants.LORE] = f"ROLL {i}"
            if i in FIRST_ROLL_WINS:
                setWinInDict(crapsInfoDict, amountsDict)
            elif i in FIRST_ROLL_LOSSES:
                setLossInDict(crapsInfoDict, amountsDict)
            else:
                setReRollInDict(crapsInfoDict, amountsDict, crapsKeyName, i)
            crapsRows.append(createRewardsCSVRowFromDict(crapsInfoDict))
        outfile.write("\n".join(crapsRows))
    createCrapsInfo(crapsEntryAmount, "FirstRoll")

    for roll in range(2, 13):
        if roll in FIRST_ROLL_LOSSES or roll in FIRST_ROLL_WINS:
            continue
        with open(f"{curCrapsCSVDir}/Craps{crapsEntryAmount}Crate-{roll}.csv", 'w') as outfile:
            crapsRows = list()
            crapsRows.append(
                "DisplayName,DisplayItem,DisplayAmount,Lore,MaxRange,Chance,PercentChance,Items,Amounts,Commands,TimesToExecuteCommands,Messages")
            for i in range(2, 13):
                crapsInfoDict = CRAPS_DEFAULTS
                curNumChance = TWO_DIE_ROLL_CHANCES[i]
                crapsInfoDict[RewardCSVConstants.DISPLAY_NAME] = f"&a&l{i}!!! "
                crapsInfoDict[RewardCSVConstants.CHANCE] = curNumChance
                crapsInfoDict[RewardCSVConstants.PERCENT_CHANCE] = round(100 * curNumChance / TWO_DIE_ROLL_TOTAL_CHANCE, 2)
                crapsInfoDict[RewardCSVConstants.LORE] = f"ROLL {i}"
                if i == roll:
                    setWinInDict(crapsInfoDict, amountsDict)
                elif i == 7:
                    setLossInDict(crapsInfoDict, amountsDict)
                else:
                    setReRollInDict(crapsInfoDict, amountsDict, crapsKeyName, roll)
                crapsRows.append(createRewardsCSVRowFromDict(crapsInfoDict))
            outfile.write("\n".join(crapsRows))

        createCrapsInfo(crapsEntryAmount, roll)

def setWinInDict(crapsInfoDict, amountsDict):
    crapsInfoDict[RewardCSVConstants.DISPLAY_NAME] += f"YOU WON!"
    crapsInfoDict[RewardCSVConstants.MESSAGES] = "&7You won!"
    crapsInfoDict[RewardCSVConstants.DISPLAY_ITEM] = "EMERALD"
    crapsInfoDict[RewardCSVConstants.COMMANDS] = f"eco give %player% {amountsDict['WIN']}"

def setLossInDict(crapsInfoDict, amountsDict):
    crapsInfoDict[RewardCSVConstants.DISPLAY_NAME] += f"YOU LOSE!"
    crapsInfoDict[RewardCSVConstants.DISPLAY_ITEM] = "BONE"
    crapsInfoDict[RewardCSVConstants.MESSAGES] = "&7You lost!"
    crapsInfoDict[RewardCSVConstants.COMMANDS] = f"eco give %player% {amountsDict['LOSE']}"

def setReRollInDict(crapsInfoDict, amountsDict, crapsKeyName, newKeyNum):
    crapsInfoDict[RewardCSVConstants.DISPLAY_NAME] += f"RE-ROLL!"
    crapsInfoDict[RewardCSVConstants.DISPLAY_ITEM] = "TRIPWIRE_HOOK"
    crapsInfoDict[RewardCSVConstants.COMMANDS] = f"eco give %player% {amountsDict['LOSE']}, " \
                                                 f"crates give physical {crapsKeyName}Crate-{newKeyNum} 1 %playername%"
    crapsInfoDict[RewardCSVConstants.MESSAGES] = "&7Re-Roll!"

def createCrapsInfo(crapsEntryAmount, roll):
    crapsCrateInfo = {
        CrateCSVConstants.REWARD_SHEET_NAME: f"Craps{crapsEntryAmount}Crate-{roll}",
        CrateCSVConstants.CRATE_NAME: f"&fCraps{crapsEntryAmount}Crate-{roll}",
        CrateCSVConstants.CRATE_TYPE: f"QuickCrate",
        CrateCSVConstants.PREVIEW_NAME: f"&fCraps{crapsEntryAmount}Crate-{roll}",
        CrateCSVConstants.STARTING_KEYS: 0,
        CrateCSVConstants.MAX_MASS_OPEN: 10,
        CrateCSVConstants.IN_GUI: f"FALSE",
        CrateCSVConstants.SLOT: 14,
        CrateCSVConstants.OPENING_BROADCAST: f"FALSE",
        CrateCSVConstants.BROADCAST: f"%prefix%&6&l%player%&r &7is opening a &f&lCraps Crate&7.",
        CrateCSVConstants.ITEM: f"CHEST",
        CrateCSVConstants.GLOWING: f"FALSE",
        CrateCSVConstants.NAME: f"&f&lCraps{crapsEntryAmount}Crate-{roll}",
        CrateCSVConstants.LORE: f"&f&lCraps Crate,&7This crate is used in the craps game.\\n&7You have &6%Keys% keys &7to open this crate with.\\n&7&l(&f&l!&7&l) Right click to view rewards.",
        CrateCSVConstants.PREVIEW_TOGGLE: f"TRUE",
        CrateCSVConstants.PREVIEW_CHEST_LINES: 3,
        CrateCSVConstants.PREVIEW_GLASS_TOGGLE: "TRUE",
        CrateCSVConstants.PREVIEW_GLASS_NAME: "",
        CrateCSVConstants.PREVIEW_GLASS_ITEM: "BLACK_STAINED_GLASS_PANE",
        CrateCSVConstants.PHYSICAL_KEY_NAME: f"&f&lCraps{crapsEntryAmount}Crate-{roll} &c&lKey",
        CrateCSVConstants.PHYSICAL_KEY_LORE: f"&7A Craps{crapsEntryAmount}-{roll} Key\\n&7For a Craps Crate.",
        CrateCSVConstants.PHYSICAL_KEY_ITEM: "TRIPWIRE_HOOK",
        CrateCSVConstants.PHYSICAL_KEY_GLOWING: "TRUE",
        CrateCSVConstants.HOLOGRAM_TOGGLE: "TRUE",
        CrateCSVConstants.HOLOGRAM_HEIGHT: 1.5,
        CrateCSVConstants.HOLOGRAM_MESSAGE: f"&f&lCraps{crapsEntryAmount}-{roll} Crate",
        CrateCSVConstants.CRAPS_AMOUNT: 25000
    }
    curCrate = Crate(crapsCrateInfo)
    curCrateYML = convert_dict_to_yaml(curCrate.dict)
    curFileName = f"../Crates/Craps/{crapsEntryAmount}/{curCrate.CrateName[2:].replace(' ', '')}.yml"
    with open(curFileName, "w") as outfile:
        yaml.dump(curCrate.dict, outfile, sort_keys=False)

createCraps()

