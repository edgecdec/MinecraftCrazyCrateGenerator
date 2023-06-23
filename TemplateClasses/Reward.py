from Constants import RewardCSVConstants
from Constants import RewardFields

class Reward():
    def __init__(self, rewardInfo, crateInfo):
        self.crateInfo = crateInfo
        self.Lore = rewardInfo[RewardCSVConstants.LORE].split("\\n") or "???"
        if RewardCSVConstants.PERCENT_CHANCE in rewardInfo.keys():
            self.PercentChance = float(rewardInfo[RewardCSVConstants.PERCENT_CHANCE])
            self.Lore.append(f"({self.PercentChance}%)")
        self.MaxRange = int(rewardInfo[RewardCSVConstants.MAX_RANGE] or 100)
        self.Chance = int(rewardInfo[RewardCSVConstants.CHANCE] or 1)
        self.ItemsList = rewardInfo[RewardCSVConstants.ITEMS].split(",") or []
        self.ItemsAmountsList = rewardInfo[RewardCSVConstants.AMOUNTS].split(",") or []
        self.DisplayItem = rewardInfo[RewardCSVConstants.DISPLAY_ITEM] or self.ItemsList[0]
        self.DisplayName = rewardInfo[RewardCSVConstants.DISPLAY_NAME] or self.ItemsList[0]
        self.DisplayAmount = rewardInfo[RewardCSVConstants.DISPLAY_AMOUNT] or self.ItemsAmountsList[0]
        self.Items = []
        self.populateItems()
        self.Commands = rewardInfo[RewardCSVConstants.COMMANDS].split(", ") or []
        self.Messages = rewardInfo[RewardCSVConstants.MESSAGES].split(", ") or ['&7You just won a &r%reward%.']
        self.dict = {}
        self.createDict()

    def createDict(self):
        self.dict = {
            RewardFields.DISPLAY_NAME: self.DisplayName,
            RewardFields.DISPLAY_ITEM: self.DisplayItem,
            RewardFields.DISPLAY_AMOUNT: self.DisplayAmount,
            RewardFields.LORE: self.Lore,
            RewardFields.MAX_RANGE: self.MaxRange,
            RewardFields.CHANCE: self.Chance,
            RewardFields.ITEMS: self.Items,
            RewardFields.COMMANDS: self.Commands,
            RewardFields.MESSAGES: self.Messages
        }

    def populateItems(self):
        for i in range(len(self.ItemsList)):
            curAmount = 1
            if len(self.ItemsAmountsList) > i:
                curAmount = self.ItemsAmountsList[i]
            self.Items.append(f"Item:{self.ItemsList[i]}, Amount:{curAmount}")
