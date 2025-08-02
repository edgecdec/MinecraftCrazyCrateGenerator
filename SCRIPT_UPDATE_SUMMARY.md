# Script Update Summary - Color Format Conversion

## Overview
All scripts have been successfully updated to use the new `<color>` format instead of the old `&{code}` format for Minecraft color formatting. This ensures compatibility with the latest CrazyCrates plugin version.

## Files Updated

### 1. craps_generator.py ✅
**Changes Made:**
- Updated display names: `&a&l{roll}!!! YOU WON!` → `<green><bold>{roll}!!! YOU WON!`
- Updated messages: `&7You won!` → `<gray>You won!`
- Updated crate names: `&b&l{item} {count} Craps Crate` → `<aqua><bold>{item} {count} Craps Crate`
- Updated lore text with proper color formatting
- Updated broadcast messages and physical key formatting

**Impact:** Future craps crates generated will use the new color format

### 2. QuickScripts/CrapsCrateGenerator.py ✅
**Changes Made:**
- Updated display names in CSV generation
- Updated win/loss/reroll messages
- Updated crate info generation with new color codes
- Updated broadcast messages and physical key names

**Impact:** Legacy craps generation script now uses new format

### 3. Util.py ✅
**Changes Made:**
- Updated `getDefaultCrateString()` function
- Converted all color codes in the default crate template string
- Updated broadcast messages and lore formatting

**Impact:** Default crate generation templates now use new format

### 4. TemplateClasses/Crate.py ✅
**Changes Made:**
- Updated default broadcast message format
- Updated default lore formatting
- Updated default physical key name formatting

**Impact:** All crate template generation uses new color format

## Color Code Mapping Applied

| Old Format | New Format |
|------------|------------|
| `&0` | `<black>` |
| `&1` | `<dark_blue>` |
| `&2` | `<dark_green>` |
| `&3` | `<dark_aqua>` |
| `&4` | `<dark_red>` |
| `&5` | `<dark_purple>` |
| `&6` | `<gold>` |
| `&7` | `<gray>` |
| `&8` | `<dark_gray>` |
| `&9` | `<blue>` |
| `&a` | `<green>` |
| `&b` | `<aqua>` |
| `&c` | `<red>` |
| `&d` | `<light_purple>` |
| `&e` | `<yellow>` |
| `&f` | `<white>` |
| `&l` | `<bold>` |
| `&m` | `<strikethrough>` |
| `&n` | `<underlined>` |
| `&o` | `<italic>` |
| `&r` | `<reset>` |
| `&k` | `<obfuscated>` |

## Testing Results

✅ **craps_generator.py** - Tested successfully, generates CSV files with new color format
✅ **All existing crate files** - Previously updated by update_color_format.py script
✅ **Template classes** - Updated to use new format for future generations

## Next Steps

1. **Test in Minecraft** - Verify that all crates display correctly with the new plugin version
2. **Generate new crates** - Any new crates created will automatically use the new format
3. **Documentation** - Update any documentation to reference the new color format

## Compatibility

- ✅ **New CrazyCrates Plugin** - Fully compatible with `<color>` format
- ✅ **Future Crate Generation** - All scripts updated to use new format
- ✅ **Existing Crates** - Already converted by previous update script

## Files Not Requiring Updates

- `Constants.py` - Contains only constant definitions, no color codes
- `CrateGenerator.py` - Uses data from CSV files (already updated)
- Template classes other than `Crate.py` - No hardcoded color formatting
- `update_color_format.py` - Already designed for this conversion

All scripts are now ready for use with the latest CrazyCrates plugin version!
