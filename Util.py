import os

import yaml
import csv
from Constants import *


def convert_csv_to_dict(filename):
    dict_list = []
    # print(f"ListDirs: {os.listdir(f'{filename}/..')}")

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(dict(row))

    return dict_list

def str_representer(dumper, data):
    if isinstance(data, str):
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style="'")
    return dumper.represent_data(data)

def convert_dict_to_yaml(dictionary):
    yaml.add_representer(str, str_representer)
    yaml_string = yaml.dump(dictionary, sort_keys=False)
    return yaml_string


def remove_quotes_from_yaml_keys(yaml_file):
    with open(yaml_file, 'r') as file:
        yaml_content = file.read()
        data = yaml.safe_load(yaml_content)

    modified_data = remove_quotes_from_dict_keys(data)
    modified_yaml_content = yaml.dump(modified_data, sort_keys=False)

    return modified_yaml_content

def remove_quotes_from_dict_keys(data):
    if isinstance(data, dict):
        return {key.strip("'"): remove_quotes_from_dict_keys(value) for key, value in data.items()}
    if isinstance(data, list):
        return [remove_quotes_from_dict_keys(item) for item in data]
    return data

def createRewardsCSVRowFromDict(dataDict):
    "DisplayName,DisplayItem,DisplayAmount,Lore,MaxRange,Chance,PercentChance,Items,Amounts,Commands,TimesToExecuteCommands,Messages"
    return f"{dataDict[RewardCSVConstants.DISPLAY_NAME]}," \
           f"{dataDict[RewardCSVConstants.DISPLAY_ITEM]}," \
           f"{dataDict[RewardCSVConstants.DISPLAY_AMOUNT]}," \
           f"{dataDict[RewardCSVConstants.LORE]}," \
           f"{dataDict[RewardCSVConstants.MAX_RANGE]}," \
           f"{dataDict[RewardCSVConstants.CHANCE]}," \
           f"{dataDict[RewardCSVConstants.PERCENT_CHANCE]}," \
           f"{dataDict[RewardCSVConstants.ITEMS]}," \
           f"{dataDict[RewardCSVConstants.AMOUNTS]}," \
           f"\"{dataDict[RewardCSVConstants.COMMANDS]}\"," \
           f"{dataDict[RewardCSVConstants.TIMES_TO_EXECUTE_COMMANDS]}," \
           f"{dataDict[RewardCSVConstants.MESSAGES]}"

def getDefaultCrateString(crateName):
    return f"{crateName}Crate,QuickCrate,&e{crateName} Crate,&e{crateName} Crate,0,10,FALSE,14,TRUE,%prefix%&6&l%player%&r &7is opening a &e&l{crateName} Crate&7.,CHEST,FALSE,&e&l{crateName} Crate,&7This crate contains some awesome items!!!\\n&7You have &6%Keys% keys &7to open this crate with.\\n&7&l(&e&l!&7&l) Right click to view rewards.,TRUE,6,TRUE,,ORANGE_STAINED_GLASS,&e&lC++ Crate &c&lKey,&7A {crateName} Key\\n&7For a {crateName} Crate.,TRIPWIRE_HOOK,TRUE,TRUE,1.5,&e&l{crateName} Crate"
