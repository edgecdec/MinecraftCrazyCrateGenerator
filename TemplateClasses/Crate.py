from Constants import CrateCSVConstants
from TemplateClasses.CratePreview import CratePreview
from Constants import CrateFields


class Crate:
    def __init__(self, info):
        self.CrateType = info[CrateCSVConstants.CRATE_TYPE]
        self.CrateName = info[CrateCSVConstants.CRATE_NAME]
        self.Preview_Name = info[CrateCSVConstants.PREVIEW_NAME] or self.CrateName
        self.StartingKeys = int(info[CrateCSVConstants.STARTING_KEYS] or 0)
        self.Max_Mass_Open = int(info[CrateCSVConstants.MAX_MASS_OPEN] or 10)
        self.InGUI = info[CrateCSVConstants.IN_GUI] == 'True' or False
        self.Slot = int(info[CrateCSVConstants.SLOT] or 14)
        self.OpeningBroadCast = info[CrateCSVConstants.OPENING_BROADCAST] == 'True' or False
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
        self.Hologram_Height = info[CrateCSVConstants.HOLOGRAM_HEIGHT] or 1.5
        self.Hologram_Message = info[CrateCSVConstants.HOLOGRAM_MESSAGE].split("\\n") or [f"{self.CrateName}"]
        self.Preview = CratePreview(info)
        self.dict = {}
        self.createDict()

    def createDict(self):
        physicalKeyDict = {
            CrateFields.PHYSICAL_KEY_NAME: self.PhysicalKey_Name,
            CrateFields.PHYSICAL_KEY_LORE: self.PhysicalKey_Lore,
            CrateFields.PHYSICAL_KEY_ITEM: self.PhysicalKey_Glowing,
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
            CrateFields.HOLOGRAM: hologramDict
        }
        self.dict = {"Crate": crateDict}
