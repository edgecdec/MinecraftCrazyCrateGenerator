# 🎲 Generalized Craps System

A complete, generalized craps game generator for Minecraft CrazyCrates that works with any item type and payout amounts.

## 🎯 Features

- **Any Item Type**: Works with diamonds, emeralds, gold_ingots, netherite_ingots, or any Minecraft item
- **Configurable Payouts**: Set custom win and loss amounts
- **Proper Game Mechanics**: Authentic craps rules with correct dice probabilities
- **Complete System**: Generates both CSV data files and YAML crate files
- **Organized Structure**: Follows existing craps crate architecture

## 🚀 Quick Start

```bash
python3 craps_generator.py
```

Follow the interactive prompts:
1. **Item Type**: `diamond`, `emerald`, `gold_ingot`, etc.
2. **Win Amount**: Number of items for wins (e.g., `10`)
3. **Loss Amount**: Number of items for losses (usually `0`)

## 📋 Examples

### Diamond Craps (10 diamonds for wins)
```
Item: diamond
Win: 10
Loss: 0
→ Creates: Diamond10 system
```

### Emerald Craps (5 emeralds for wins, 1 for losses)
```
Item: emerald  
Win: 5
Loss: 1
→ Creates: Emerald5 system
```

### Gold Craps (25 gold ingots for wins)
```
Item: gold_ingot
Win: 25
Loss: 0
→ Creates: Gold_Ingot25 system
```

## 🎲 Game Rules

### First Roll (Come Out Roll)
- **Natural 7 or 11**: Instant WIN
- **Snake Eyes (2), 3, or 12**: Instant LOSS  
- **4, 5, 6, 8, 9, 10**: Establish POINT

### Point Rolls
- **Roll your point again**: WIN
- **Roll a 7**: LOSS (Seven Out)
- **Any other number**: Re-roll

## 📁 Generated Files

Each system creates:

### CSV Data Files (in `CrateCSVs/Craps/{ItemType}{Count}/`)
- `Craps{ItemType}{Count}Crate-FirstRoll.csv` - Main crate data
- `Craps{ItemType}{Count}Crate-4.csv` - Point 4 crate data
- `Craps{ItemType}{Count}Crate-5.csv` - Point 5 crate data
- `Craps{ItemType}{Count}Crate-6.csv` - Point 6 crate data
- `Craps{ItemType}{Count}Crate-8.csv` - Point 8 crate data
- `Craps{ItemType}{Count}Crate-9.csv` - Point 9 crate data
- `Craps{ItemType}{Count}Crate-10.csv` - Point 10 crate data

### YAML Crate Files (in `Crates/Craps/{ItemType}{Count}/`)
- `Craps{ItemType}{Count}Crate-FirstRoll.yml` - Main crate (players interact with this)
- `Craps{ItemType}{Count}Crate-{4,5,6,8,9,10}.yml` - Point crates

## 🎮 How to Use in Minecraft

1. **Copy files** to your CrazyCrates plugin folder
2. **Restart server** or reload CrazyCrates
3. **Give players keys**:
   ```
   /crates give physical Craps{ItemType}{Count}Crate-FirstRoll 1 <player>
   ```

### Example Commands
```bash
# Diamond10 system
/crates give physical CrapsDiamond10Crate-FirstRoll 1 Steve

# Emerald5 system  
/crates give physical CrapsEmerald5Crate-FirstRoll 1 Alex

# Gold_Ingot25 system
/crates give physical CrapsGold_Ingot25Crate-FirstRoll 1 Notch
```

## 🔧 Architecture

The system follows the same architecture as existing craps crates:
- **No main CSV entries** (matches existing 25000, 250000, etc. craps)
- **All files in subdirectories** under `Craps/`
- **FirstRoll crate is the main entry point**
- **Point crates handle game progression**

## 📊 Dice Probabilities

Uses authentic craps probabilities from `Constants.py`:
- **2, 12**: 1/36 (2.78%)
- **3, 11**: 2/36 (5.56%) 
- **4, 10**: 3/36 (8.33%)
- **5, 9**: 4/36 (11.11%)
- **6, 8**: 5/36 (13.89%)
- **7**: 6/36 (16.67%)

## 🎉 Multiple Systems

You can run multiple craps systems simultaneously:
- `Diamond10` (10 diamonds)
- `Emerald5` (5 emeralds)
- `Gold_Ingot25` (25 gold ingots)
- `Netherite_Ingot1` (1 netherite ingot)

Each system is completely independent with unique crate names.

## 📝 Notes

- Item types should use Minecraft naming (e.g., `gold_ingot`, not `gold ingot`)
- Win/loss amounts can be any positive integer
- System automatically handles item capitalization for display items
- Generated crates don't appear in GUI (matches existing craps behavior)
- All crates use proper dice roll probabilities for authentic gameplay