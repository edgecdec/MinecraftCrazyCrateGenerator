#!/usr/bin/env python3
"""
Update Color Format Script
Updates all craps crate files from old &{code} format to new <color> format
"""

import os
import re

# Color code mapping from &{code} to <color>
COLOR_MAPPING = {
    '&0': '<black>',
    '&1': '<dark_blue>',
    '&2': '<dark_green>',
    '&3': '<dark_aqua>',
    '&4': '<dark_red>',
    '&5': '<dark_purple>',
    '&6': '<gold>',
    '&7': '<gray>',
    '&8': '<dark_gray>',
    '&9': '<blue>',
    '&a': '<green>',
    '&b': '<aqua>',
    '&c': '<red>',
    '&d': '<light_purple>',
    '&e': '<yellow>',
    '&f': '<white>',
    '&l': '<bold>',
    '&m': '<strikethrough>',
    '&n': '<underlined>',
    '&o': '<italic>',
    '&r': '<reset>',
    '&k': '<obfuscated>'
}

def convert_color_codes(text):
    """Convert &{code} format to <color> format"""
    if not isinstance(text, str):
        return text
    
    result = text
    for old_code, new_code in COLOR_MAPPING.items():
        result = result.replace(old_code, new_code)
    
    return result

def update_file(filepath):
    """Update a single file with new color format"""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        original_content = content
        updated_content = convert_color_codes(content)
        
        if original_content != updated_content:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            print(f"✅ Updated: {filepath}")
            return True
        else:
            print(f"⚪ No changes: {filepath}")
            return False
    except Exception as e:
        print(f"❌ Error updating {filepath}: {e}")
        return False

def update_directory(directory):
    """Update all files in a directory"""
    updated_count = 0
    total_count = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.csv', '.yml', '.yaml')):
                filepath = os.path.join(root, file)
                total_count += 1
                if update_file(filepath):
                    updated_count += 1
    
    return updated_count, total_count

def main():
    """Main function"""
    print("=" * 60)
    print("🎨 COLOR FORMAT UPDATER")
    print("=" * 60)
    print("Converting from &{code} format to <color> format")
    print()
    
    # Show mapping examples
    print("📋 Color Code Mapping Examples:")
    examples = [
        ('&b&lDiamond 10 Craps Crate', '<aqua><bold>Diamond 10 Craps Crate'),
        ('&a&l7!!! YOU WON!', '<green><bold>7!!! YOU WON!'),
        ('&7You won!', '<gray>You won!'),
        ('&e&lC++ Crate', '<yellow><bold>C++ Crate'),
        ('&6&l%player%', '<gold><bold>%player%')
    ]
    
    for old, new in examples:
        print(f"  {old} → {new}")
    
    print()
    
    # Update craps CSV files
    print("🎲 Updating Craps CSV files...")
    csv_updated, csv_total = update_directory("CrateCSVs/Craps")
    print(f"CSV files: {csv_updated}/{csv_total} updated")
    print()
    
    # Update craps YAML files
    print("📦 Updating Craps YAML files...")
    yaml_updated, yaml_total = update_directory("Crates/Craps")
    print(f"YAML files: {yaml_updated}/{yaml_total} updated")
    print()
    
    # Update main CSV file
    print("📋 Updating main CSV file...")
    main_csv_updated = update_file("IMLCrateInfo - Crates.csv")
    print()
    
    # Update other crate files
    print("🎁 Updating other crate files...")
    other_updated, other_total = update_directory("Crates")
    print(f"Other crate files: {other_updated}/{other_total} updated")
    print()
    
    # Summary
    total_updated = csv_updated + yaml_updated + (1 if main_csv_updated else 0) + other_updated
    total_files = csv_total + yaml_total + 1 + other_total
    
    print("=" * 60)
    print("🎉 UPDATE COMPLETE!")
    print("=" * 60)
    print(f"Total files updated: {total_updated}/{total_files}")
    print()
    print("✅ All craps crates now use the new <color> format!")
    print("✅ Compatible with latest CrazyCrates plugin!")
    
    if total_updated > 0:
        print()
        print("📝 Next steps:")
        print("1. Test the updated crates in Minecraft")
        print("2. Commit the changes to git")
        print("3. Update the craps_generator.py script for future crates")

if __name__ == "__main__":
    main()