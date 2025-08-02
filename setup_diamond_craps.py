#!/usr/bin/env python3
"""
Setup Diamond Craps Crate
This script adds the CrapsAmount column to the main CSV and creates a sample diamond craps crate entry.
"""

import csv
import os
from datetime import datetime

def backup_csv(filename):
    """Create a backup of the CSV file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{filename}.backup_{timestamp}"
    
    with open(filename, 'r', encoding='utf-8') as original:
        with open(backup_name, 'w', encoding='utf-8') as backup:
            backup.write(original.read())
    
    print(f"Created backup: {backup_name}")
    return backup_name

def add_craps_column_to_csv():
    """Add CrapsAmount column to the main CSV file if it doesn't exist"""
    csv_file = "IMLCrateInfo - Crates.csv"
    
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found!")
        return False
    
    # Create backup
    backup_csv(csv_file)
    
    # Read the current CSV
    rows = []
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    if not rows:
        print("Error: CSV file is empty!")
        return False
    
    # Check if CrapsAmount column already exists
    header = rows[0]
    if 'CrapsAmount' in header:
        print("CrapsAmount column already exists!")
        return True
    
    # Add CrapsAmount column to header
    header.append('CrapsAmount')
    
    # Add empty CrapsAmount values to existing rows
    for i in range(1, len(rows)):
        rows[i].append('')  # Empty value for existing crates
    
    # Write back to CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    print("Added CrapsAmount column to the main CSV file!")
    return True

def add_diamond_craps_crate():
    """Add a sample diamond craps crate entry to the main CSV"""
    csv_file = "IMLCrateInfo - Crates.csv"
    
    # Diamond craps crate configuration
    diamond_craps_entry = [
        "CrapsDiamondCrate-FirstRoll",  # RewardSheetName
        "QuickCrate",                   # CrateType
        "&b&lDiamond Craps Crate",     # CrateName
        "&b&lDiamond Craps Crate",     # Preview-Name
        "0",                           # StartingKeys
        "1",                           # Max-Mass-Open (1 for craps)
        "TRUE",                        # InGUI
        "15",                          # Slot
        "TRUE",                        # OpeningBroadCast
        "%prefix%&6&l%player%&r &7is rolling the dice in a &b&lDiamond Craps Crate&7!",  # BroadCast
        "DIAMOND",                     # Item
        "TRUE",                        # Glowing
        "&b&lDiamond Craps Crate",     # Name
        "&7Roll the dice and win diamonds!\\n&7Natural 7 or 11 wins instantly!\\n&7Snake eyes (2), 3, or 12 loses!\\n&7Other numbers become your point!\\n&7You have &6%Keys% keys &7to open this crate with.\\n&7&l(&e&l!&7&l) Right click to view rewards.",  # Lore
        "TRUE",                        # Preview.Toggle
        "6",                           # Preview.ChestLines
        "TRUE",                        # Preview.Glass.Toggle
        "",                            # Preview.Glass.Name
        "LIGHT_BLUE_STAINED_GLASS_PANE",  # Preview.Glass.Item
        "&b&lDiamond Craps Crate &c&lKey",  # PhysicalKeyName
        "&7A Diamond Craps Key\\n&7Roll the dice for diamonds!",  # PhysicalKeyLore
        "TRIPWIRE_HOOK",               # PhysicalKeyItem
        "TRUE",                        # PhysicalKeyGlowing
        "TRUE",                        # HologramToggle
        "1.5",                         # HologramHeight
        "&b&lDiamond Craps Crate\\n&7Roll for Diamonds!",  # HologramMessage
        "Diamond"                      # CrapsAmount
    ]
    
    # Read current CSV
    rows = []
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Add the new crate entry
    rows.append(diamond_craps_entry)
    
    # Write back to CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    print("Added Diamond Craps Crate entry to the main CSV!")

def main():
    """Main function"""
    print("=== Diamond Craps Setup ===")
    print("This script will set up the diamond craps crate system.")
    print()
    
    # Step 1: Add CrapsAmount column
    print("Step 1: Adding CrapsAmount column to main CSV...")
    if not add_craps_column_to_csv():
        print("Failed to add CrapsAmount column!")
        return
    
    # Step 2: Add diamond craps crate entry
    print("\\nStep 2: Adding Diamond Craps Crate entry...")
    add_diamond_craps_crate()
    
    print("\\n=== Setup Complete! ===")
    print("Your diamond craps crate system is now ready!")
    print()
    print("What was created:")
    print("1. Diamond craps CSV files in CrateCSVs/Craps/Diamond/")
    print("2. CrapsAmount column added to main CSV")
    print("3. Diamond Craps Crate entry added to main CSV")
    print()
    print("How it works:")
    print("- Players roll dice and can win 10 diamonds")
    print("- Natural 7 or 11 = instant win")
    print("- Snake eyes (2), 3, or 12 = instant loss")
    print("- Other numbers (4,5,6,8,9,10) become 'point' numbers")
    print("- Player must roll their point again before rolling a 7 to win")
    print()
    print("To generate the actual crate files, run: python3 CrateGenerator.py")

if __name__ == "__main__":
    main()