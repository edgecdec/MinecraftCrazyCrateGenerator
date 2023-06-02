from Constants import CrateCSVConstants
from TemplateClasses.CratePreview import CratePreview
from Constants import CrateFields
from TemplateClasses.Reward import Reward
from Util import *


class Crate:
    def __init__(self, info):
        self.info = info
        self.RewardSheetName = info[CrateCSVConstants.REWARD_SHEET_NAME]
        self.CrateType = info[CrateCSVConstants.CRATE_TYPE]
        self.CrateName = info[CrateCSVConstants.CRATE_NAME]
        self.Preview_Name = info[CrateCSVConstants.PREVIEW_NAME] or f"{self.CrateName} Preview"
        self.StartingKeys = int(info[CrateCSVConstants.STARTING_KEYS] or 0)
        self.Max_Mass_Open = int(info[CrateCSVConstants.MAX_MASS_OPEN] or 10)
        self.InGUI = info[CrateCSVConstants.IN_GUI] == 'True' or False
        self.Slot = int(info[CrateCSVConstants.SLOT] or 14)
        self.OpeningBroadCast = info[CrateCSVConstants.OPENING_BROADCAST] == 'True' or True
        self.Item = info[CrateCSVConstants.ITEM] or 'CHEST'
        self.Glowing = info[CrateCSVConstants.GLOWING] == 'True' or False
        self.Name = info[CrateCSVConstants.NAME] or self.CrateName
        self.BroadCast = info[CrateCSVConstants.BROADCAST] or f'%prefix%&6&l%player%&r &7is opening a {self.Name}&7.'
        self.Lore = info[CrateCSVConstants.LORE].split("\\n") or [f"&7This is a {self.CrateName}", "&7You have &6%Keys% keys &7to open this crate with.&7&l(&e&l!&7&l)", "Right click to view rewards."]
        self.PhysicalKey_Name = info[CrateCSVConstants.PHYSICAL_KEY_NAME] or f'{self.Name} &c&lKey'
        self.PhysicalKey_Lore = info[CrateCSVConstants.PHYSICAL_KEY_LORE].split("\\n") or [f'A {self.Name} Key.', f'For a {self.CrateName}']
        self.PhysicalKey_Item = info[CrateCSVConstants.PHYSICAL_KEY_ITEM] or 'TRIPWIRE_HOOK'
        self.PhysicalKey_Glowing = info[CrateCSVConstants.PHYSICAL_KEY_GLOWING] == 'TRUE' or True
        self.Hologram_Toggle = info[CrateCSVConstants.HOLOGRAM_TOGGLE] == 'True' or True
        self.Hologram_Height = round(float(info[CrateCSVConstants.HOLOGRAM_HEIGHT] or 1.5), 1)
        self.Hologram_Message = info[CrateCSVConstants.HOLOGRAM_MESSAGE].split("\\n") or [f"{self.CrateName}"]
        self.Preview = CratePreview(info)
        self.rewards = []
        self.populateRewards()
        self.dict = {}
        self.createDict()

    def populateRewards(self):
        rewardsInfo = convert_csv_to_dict(f"CrateCSVs/IMLCrateInfo - {self.RewardSheetName}.csv")
        for i in range(len(rewardsInfo)):
            curReward = Reward(rewardsInfo[i], self.info)
            self.rewards.append(curReward.dict)


    def createDict(self):
        physicalKeyDict = {
            CrateFields.PHYSICAL_KEY_NAME: self.PhysicalKey_Name,
            CrateFields.PHYSICAL_KEY_LORE: self.PhysicalKey_Lore,
            CrateFields.PHYSICAL_KEY_ITEM: self.PhysicalKey_Item,
            CrateFields.PHYSICAL_KEY_GLOWING: self.PhysicalKey_Glowing
        }

        hologramDict = {
            CrateFields.HOLOGRAM_TOGGLE: self.Hologram_Toggle,
            CrateFields.HOLOGRAM_HEIGHT: self.Hologram_Height,
            CrateFields.HOLOGRAM_MESSAGE: self.Hologram_Message
        }

        crateDict = {
            CrateFields.CRATE_TYPE: self.CrateType,
            CrateFields.CRATE_NAME: self.CrateName,
            CrateFields.PREVIEW_NAME: self.Preview_Name,
            CrateFields.STARTING_KEYS: self.StartingKeys,
            CrateFields.MAX_MASS_OPEN: self.Max_Mass_Open,
            CrateFields.IN_GUI: self.InGUI,
            CrateFields.SLOT: self.Slot,
            CrateFields.OPENING_BROADCAST: self.OpeningBroadCast,
            CrateFields.BROADCAST: self.BroadCast,
            CrateFields.ITEM: self.Item,
            CrateFields.GLOWING: self.Glowing,
            CrateFields.NAME: self.Name,
            CrateFields.LORE: self.Lore,
            CrateFields.PREVIEW: self.Preview.dict,
            CrateFields.PHYSICAL_KEY: physicalKeyDict,
            CrateFields.HOLOGRAM: hologramDict,
        }

        for i in range(len(self.rewards)):
            crateDict[i] = self.rewards[i]

        self.dict = {"Crate": crateDict}
