from Constants import CrateCSVConstants
from Constants import CratePreviewFields

class CratePreview():
    def __init__(self, info):
        self.Toggle = info[CrateCSVConstants.PREVIEW_TOGGLE] == 'TRUE'
        self.ChestLines = int(info[CrateCSVConstants.PREVIEW_CHEST_LINES] or 6)
        self.Glass_Toggle = info[CrateCSVConstants.PREVIEW_GLASS_TOGGLE] == 'TRUE'
        self.Glass_Name = info[CrateCSVConstants.PREVIEW_GLASS_NAME] or ' '
        self.Glass_Item = info[CrateCSVConstants.PREVIEW_GLASS_ITEM] or 'YELLOW_STAINED_GLASS_PANE'
        self.dict = {}
        self.createDict()

    def createDict(self):
        glassDict = {
            CratePreviewFields.GLASS_ITEM: self.Glass_Item,
            CratePreviewFields.GLASS_NAME: self.Glass_Name,
            CratePreviewFields.GLASS_TOGGLE: self.Glass_Toggle
        }
        self.dict = {
            CratePreviewFields.TOGGLE: self.Toggle,
            CratePreviewFields.CHEST_LINES: self.ChestLines,
            CratePreviewFields.GLASS: glassDict
        }

