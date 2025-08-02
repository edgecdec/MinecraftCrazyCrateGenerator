#!/usr/bin/env python3
"""
Update Diamond Craps CSV Entry
This script updates the main CSV to use the new diamond amount naming convention.
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

def update_diamond_craps_entry(diamond_amount=10):
    """Update the diamond craps entry in the main CSV"""
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
    
    # Find and update the diamond craps entry
    updated = False
    for i, row in enumerate(rows):
        if len(row) > 0 and 'Diamond Craps Crate' in str(row):
            # Update the entry with new naming convention
            new_reward_sheet_name = f"CrapsDiamond{diamond_amount}Crate-FirstRoll"
            new_craps_amount = f"Diamond{diamond_amount}"
            new_crate_name = f"&b&lDiamond {diamond_amount} Craps Crate"
            new_name = f"&b&lDiamond {diamond_amount} Craps Crate"
            new_lore = f"&7Roll the dice and win {diamond_amount} diamonds!\\\\n&7Natural 7 or 11 wins instantly!\\\\n&7Snake eyes (2), 3, or 12 loses!\\\\n&7Other numbers become your point!\\\\n&7You have &6%Keys% keys &7to open this crate with.\\\\n&7&l(&e&l!&7&l) Right click to view rewards."
            new_broadcast = f"%prefix%&6&l%player%&r &7is rolling the dice in a &b&lDiamond {diamond_amount} Craps Crate&7!"
            new_physical_key_name = f"&b&lDiamond {diamond_amount} Craps Crate &c&lKey"
            new_physical_key_lore = f"&7A Diamond {diamond_amount} Craps Key\\\\n&7Roll the dice for {diamond_amount} diamonds!"
            new_hologram_message = f"&b&lDiamond {diamond_amount} Craps Crate\\\\n&7Roll for {diamond_amount} Diamonds!"
            
            # Update the row
            row[0] = new_reward_sheet_name  # RewardSheetName
            row[2] = new_crate_name         # CrateName
            row[3] = new_crate_name         # Preview-Name
            row[9] = new_broadcast          # BroadCast
            row[12] = new_name              # Name
            row[13] = new_lore              # Lore
            row[19] = new_physical_key_name # PhysicalKeyName
            row[20] = new_physical_key_lore # PhysicalKeyLore
            row[25] = new_hologram_message  # HologramMessage
            row[26] = new_craps_amount      # CrapsAmount
            
            updated = True
            print(f"Updated Diamond Craps Crate entry for {diamond_amount} diamonds")
            break
    
    if not updated:
        print("Diamond Craps Crate entry not found in CSV!")
        return False
    
    # Write back to CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    print("Main CSV updated successfully!")
    return True

def main():
    """Main function"""
    print("=== Diamond Craps CSV Updater ===")
    print("This script updates the main CSV to use the new diamond amount naming.")
    print()
    
    diamond_amount = input("Enter diamond amount for the main crate (default: 10): ").strip()
    if not diamond_amount:
        diamond_amount = 10
    else:
        try:
            diamond_amount = int(diamond_amount)
        except ValueError:
            print("Invalid number, using default of 10")
            diamond_amount = 10
    
    print(f"Updating for {diamond_amount} diamonds...")
    print()
    
    if update_diamond_craps_entry(diamond_amount):
        print()
        print("✅ Update complete!")
        print(f"Your main CSV now references the Diamond{diamond_amount} craps system.")
        print()
        print("Next steps:")
        print(f"1. Make sure you have CSV files in CrateCSVs/Craps/Diamond{diamond_amount}/")
        print("2. Run: python3 CrateGenerator.py")
        print("3. Your crate will be ready to use!")
    else:
        print("❌ Update failed!")

if __name__ == "__main__":
    main()