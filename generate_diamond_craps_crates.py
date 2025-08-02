#!/usr/bin/env python3
"""
Generate Diamond Craps Crate YAML Files
This script generates all the individual diamond craps crate YAML files for the point numbers.
"""

import os
import yaml
from TemplateClasses import Crate
from Util import convert_csv_to_dict

def create_diamond_craps_crate_entry(reward_sheet_name, crate_name):
    """Create a crate entry dictionary for diamond craps crates"""
    return {
        'RewardSheetName': reward_sheet_name,
        'CrateType': 'QuickCrate',
        'CrateName': crate_name,
        'Preview-Name': crate_name,
        'StartingKeys': '0',
        'Max-Mass-Open': '1',
        'InGUI': 'FALSE',  # Point crates shouldn't appear in GUI
        'Slot': '14',
        'OpeningBroadCast': 'TRUE',
        'BroadCast': f'%prefix%&6&l%player%&r &7is rolling the dice in a {crate_name}&7!',
        'Item': 'DIAMOND',
        'Glowing': 'TRUE',
        'Name': crate_name,
        'Lore': '&7Rolling for your point!\\n&7You have &6%Keys% keys &7to open this crate with.\\n&7&l(&e&l!&7&l) Right click to view rewards.',
        'Preview.Toggle': 'TRUE',
        'Preview.ChestLines': '6',
        'Preview.Glass.Toggle': 'TRUE',
        'Preview.Glass.Name': '',
        'Preview.Glass.Item': 'LIGHT_BLUE_STAINED_GLASS_PANE',
        'PhysicalKeyName': f'{crate_name} &c&lKey',
        'PhysicalKeyLore': f'&7A {crate_name} Key\\n&7Roll for your point!',
        'PhysicalKeyItem': 'TRIPWIRE_HOOK',
        'PhysicalKeyGlowing': 'TRUE',
        'HologramToggle': 'TRUE',
        'HologramHeight': '1.5',
        'HologramMessage': f'{crate_name}\\n&7Roll for your point!',
        'CrapsAmount': 'Diamond'
    }

def generate_diamond_point_crates():
    """Generate YAML files for all diamond craps point crates"""
    point_numbers = [4, 5, 6, 8, 9, 10]
    output_dir = "Crates/Craps/Diamond"
    
    # Create the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    print("Generating Diamond Craps Point Crate YAML files...")
    
    for point in point_numbers:
        reward_sheet_name = f"CrapsDiamondCrate-{point}"
        crate_name = f"&b&lDiamond Craps Crate-{point}"
        
        # Create crate entry
        crate_info = create_diamond_craps_crate_entry(reward_sheet_name, crate_name)
        
        # Create Crate object
        crate_obj = Crate.Crate(crate_info)
        
        # Generate filename in the proper craps directory structure
        filename = f"{output_dir}/CrapsDiamondCrate-{point}.yml"
        
        # Write YAML file
        with open(filename, "w") as outfile:
            yaml.dump(crate_obj.dict, outfile, sort_keys=False)
        
        print(f"Created: {filename}")
    
    print("\\nAll Diamond Craps Point Crate YAML files generated successfully!")

def move_main_crate():
    """Move the main diamond craps crate to the proper directory"""
    old_path = "Crates/&lDiamondCrapsCrate.yml"
    new_dir = "Crates/Craps/Diamond"
    new_path = f"{new_dir}/CrapsDiamondCrate-FirstRoll.yml"
    
    # Create directory if it doesn't exist
    os.makedirs(new_dir, exist_ok=True)
    
    if os.path.exists(old_path):
        # Move and rename the file
        os.rename(old_path, new_path)
        print(f"Moved: {old_path} -> {new_path}")
    else:
        print(f"Main crate file not found at: {old_path}")

def cleanup_old_files():
    """Remove old diamond craps files from the wrong location"""
    old_files = [
        "Crates/DiamondCrapsCrate-4.yml",
        "Crates/DiamondCrapsCrate-5.yml", 
        "Crates/DiamondCrapsCrate-6.yml",
        "Crates/DiamondCrapsCrate-8.yml",
        "Crates/DiamondCrapsCrate-9.yml",
        "Crates/DiamondCrapsCrate-10.yml"
    ]
    
    print("\\nCleaning up old files from wrong location...")
    for file_path in old_files:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Removed: {file_path}")

def main():
    """Main function"""
    print("=== Diamond Craps Point Crates Generator ===")
    print("This script generates YAML files for diamond craps point crates.")
    print("Files will be organized in the proper Crates/Craps/Diamond/ directory.")
    print()
    
    # Move main crate to proper location
    move_main_crate()
    
    # Generate point crates in proper location
    generate_diamond_point_crates()
    
    # Clean up old files
    cleanup_old_files()
    
    print()
    print("Complete diamond craps system files (properly organized):")
    print("1. Crates/Craps/Diamond/CrapsDiamondCrate-FirstRoll.yml - Main first roll crate")
    print("2. Crates/Craps/Diamond/CrapsDiamondCrate-4.yml - Point 4 crate")
    print("3. Crates/Craps/Diamond/CrapsDiamondCrate-5.yml - Point 5 crate")
    print("4. Crates/Craps/Diamond/CrapsDiamondCrate-6.yml - Point 6 crate")
    print("5. Crates/Craps/Diamond/CrapsDiamondCrate-8.yml - Point 8 crate")
    print("6. Crates/Craps/Diamond/CrapsDiamondCrate-9.yml - Point 9 crate")
    print("7. Crates/Craps/Diamond/CrapsDiamondCrate-10.yml - Point 10 crate")
    print()
    print("Your diamond craps system is now properly organized!")
    print("All files follow the same structure as other craps crates.")

if __name__ == "__main__":
    main()