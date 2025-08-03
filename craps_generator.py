#!/usr/bin/env python3
"""
Generalized Craps Generator
Generates CSV and YAML files for a craps game that pays out any item and count.
Supports any Minecraft item type and any win/loss amounts.
"""

import os
import csv
import yaml
from Constants import TwoDiceRollChances
from TemplateClasses import Crate

class CrapsGenerator:
    def __init__(self, item_type="diamond", win_count=10, loss_count=0):
        """
        Initialize the craps generator
        
        Args:
            item_type (str): Minecraft item type (e.g., "diamond", "emerald", "gold_ingot")
            win_count (int): Number of items to give for wins
            loss_count (int): Number of items to give for losses
        """
        self.item_type = item_type.lower()
        self.win_count = win_count
        self.loss_count = loss_count
        
        # Create folder name and crate prefix
        self.folder_name = f"{item_type.title()}{win_count}"
        self.base_dir = f"CrateCSVs/Craps/{self.folder_name}"
        self.crate_prefix = f"Craps{self.folder_name}Crate"
        self.yaml_dir = f"Crates/Craps/{self.folder_name}"
        
        # Dice roll probabilities (out of 36 total combinations)
        self.roll_chances = {
            2: TwoDiceRollChances.TWO,
            3: TwoDiceRollChances.THREE,
            4: TwoDiceRollChances.FOUR,
            5: TwoDiceRollChances.FIVE,
            6: TwoDiceRollChances.SIX,
            7: TwoDiceRollChances.SEVEN,
            8: TwoDiceRollChances.EIGHT,
            9: TwoDiceRollChances.NINE,
            10: TwoDiceRollChances.TEN,
            11: TwoDiceRollChances.ELEVEN,
            12: TwoDiceRollChances.TWELVE
        }
    
    def get_win_command(self):
        """Get the command for winning"""
        if self.win_count > 0:
            return f"give %player% {self.item_type} {self.win_count}"
        else:
            return ""  # No command if giving 0 items
    
    def get_loss_command(self):
        """Get the command for losing"""
        if self.loss_count > 0:
            return f"give %player% {self.item_type} {self.loss_count}"
        else:
            return ""  # No command if giving 0 items
    
    def get_reroll_command(self, target_number):
        """Get the command for re-rolling with a specific target"""
        commands = []
        if self.loss_count > 0:
            commands.append(f"give %player% {self.item_type} {self.loss_count}")
        commands.append(f"crates give physical {self.crate_prefix}-{target_number} 1 %player%")
        return ", ".join(commands)
    
    def create_first_roll_csv(self):
        """Create the first roll CSV file"""
        filename = os.path.join(self.base_dir, f"{self.crate_prefix}-FirstRoll.csv")
        
        # CSV header
        header = [
            "DisplayName", "DisplayItem", "DisplayAmount", "Lore", "MaxRange", 
            "Chance", "PercentChance", "Items", "Amounts", "Commands", 
            "TimesToExecuteCommands", "Messages"
        ]
        
        # Create rows for each possible dice roll
        rows = []
        for roll in range(2, 13):
            chance = self.roll_chances[roll]
            percent = round((chance / 36) * 100, 2)
            
            if roll in [7, 11]:  # Natural wins
                display_name = f"<green><bold>{roll}!!! YOU WON!"
                display_item = self.item_type.upper()
                command = self.get_win_command()
                message = "<gray>You won!"
            elif roll in [2, 3, 12]:  # Craps (losses)
                display_name = f"<green><bold>{roll}!!! YOU LOSE!"
                display_item = "BONE"
                command = self.get_loss_command()
                message = "<gray>You lost!"
            else:  # Point numbers (4, 5, 6, 8, 9, 10)
                display_name = f"<green><bold>{roll}!!! RE-ROLL!"
                display_item = "TRIPWIRE_HOOK"
                command = self.get_reroll_command(roll)
                message = "<gray>Re-Roll!"
            
            row = [
                display_name, display_item, "1", f"ROLL {roll}", "", 
                str(chance), str(percent), "AIR", "1", command, "1", message
            ]
            rows.append(row)
        
        # Write CSV file
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows(rows)
        
        print(f"Created: {filename}")
    
    def create_point_roll_csv(self, point_number):
        """Create a CSV file for rolling when a point is established"""
        filename = os.path.join(self.base_dir, f"{self.crate_prefix}-{point_number}.csv")
        
        # CSV header
        header = [
            "DisplayName", "DisplayItem", "DisplayAmount", "Lore", "MaxRange", 
            "Chance", "PercentChance", "Items", "Amounts", "Commands", 
            "TimesToExecuteCommands", "Messages"
        ]
        
        # Create rows for each possible dice roll
        rows = []
        for roll in range(2, 13):
            chance = self.roll_chances[roll]
            percent = round((chance / 36) * 100, 2)
            
            if roll == point_number:  # Hit the point - WIN!
                display_name = f"<green><bold>{roll}!!! YOU WON!"
                display_item = self.item_type.upper()
                command = self.get_win_command()
                message = "<gray>You won!"
            elif roll == 7:  # Seven out - LOSE!
                display_name = f"<green><bold>{roll}!!! YOU LOSE!"
                display_item = "BONE"
                command = self.get_loss_command()
                message = "<gray>You lost!"
            else:  # Any other number - re-roll
                display_name = f"<green><bold>{roll}!!! RE-ROLL!"
                display_item = "TRIPWIRE_HOOK"
                command = self.get_reroll_command(point_number)
                message = "<gray>Re-Roll!"
            
            row = [
                display_name, display_item, "1", f"ROLL {roll}", "", 
                str(chance), str(percent), "AIR", "1", command, "1", message
            ]
            rows.append(row)
        
        # Write CSV file
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows(rows)
        
        print(f"Created: {filename}")
    
    def create_crate_yaml_entry(self, reward_sheet_name, crate_name, is_main_crate=False):
        """Create a crate entry dictionary for YAML generation"""
        return {
            'RewardSheetName': reward_sheet_name,
            'CrateType': 'QuickCrate',
            'CrateName': crate_name,
            'Preview-Name': crate_name,
            'StartingKeys': '0',
            'Max-Mass-Open': '1',
            'InGUI': 'FALSE',  # Craps crates don't appear in GUI
            'Slot': '14',
            'OpeningBroadCast': 'TRUE',
            'BroadCast': f'%prefix%<gold><bold>%player%<reset> <gray>is rolling the dice in a {crate_name}<gray>!',
            'Item': self.item_type.upper(),
            'Glowing': 'TRUE',
            'Name': crate_name,
            'Lore': f'<gray>Rolling for {self.item_type}!\\n<gray>You have <gold>%Keys% keys <gray>to open this crate with.\\n<gray><bold>(<yellow><bold>!<gray><bold>) Right click to view rewards.',
            'Preview.Toggle': 'TRUE',
            'Preview.ChestLines': '6',
            'Preview.Glass.Toggle': 'TRUE',
            'Preview.Glass.Name': '',
            'Preview.Glass.Item': 'LIGHT_BLUE_STAINED_GLASS_PANE',
            'PhysicalKeyName': f'{crate_name} <red><bold>Key',
            'PhysicalKeyLore': f'<gray>A {crate_name} Key\\n<gray>Roll for {self.item_type}!',
            'PhysicalKeyItem': 'TRIPWIRE_HOOK',
            'PhysicalKeyGlowing': 'TRUE',
            'HologramToggle': 'TRUE',
            'HologramHeight': '1.5',
            'HologramMessage': f'{crate_name}\\n<gray>Roll for {self.item_type.title()}!',
            'CrapsAmount': self.folder_name
        }
    
    def generate_yaml_files(self):
        """Generate YAML files for all craps crates"""
        # Create the YAML directory if it doesn't exist
        os.makedirs(self.yaml_dir, exist_ok=True)
        
        print(f"Generating {self.folder_name} Craps Crate YAML files...")
        print(f"YAML output directory: {self.yaml_dir}")
        print()
        
        # Generate FirstRoll crate (main crate)
        print("Creating FirstRoll crate (main crate)...")
        reward_sheet_name = f"{self.crate_prefix}-FirstRoll"
        crate_name = f"<aqua><bold>{self.item_type.title()} {self.win_count} Craps Crate"
        
        # Create crate entry with special lore for main crate
        crate_info = self.create_crate_yaml_entry(reward_sheet_name, crate_name, is_main_crate=True)
        crate_info['Lore'] = f'<gray>Roll the dice and win {self.win_count} {self.item_type}!\\n<gray>Natural 7 or 11 wins instantly!\\n<gray>Snake eyes (2), 3, or 12 loses!\\n<gray>Other numbers become your point!\\n<gray>You have <gold>%Keys% keys <gray>to open this crate with.\\n<gray><bold>(<yellow><bold>!<gray><bold>) Right click to view rewards.'
        
        # Create Crate object
        crate_obj = Crate.Crate(crate_info)
        
        # Generate filename
        filename = f"{self.yaml_dir}/{self.crate_prefix}-FirstRoll.yml"
        
        # Write YAML file
        with open(filename, "w") as outfile:
            yaml.dump(crate_obj.dict, outfile, sort_keys=False)
        
        print(f"Created: {filename}")
        
        # Generate point crates (4, 5, 6, 8, 9, 10)
        print("\\nCreating point crates...")
        point_numbers = [4, 5, 6, 8, 9, 10]
        
        for point in point_numbers:
            reward_sheet_name = f"{self.crate_prefix}-{point}"
            crate_name = f"<aqua><bold>{self.item_type.title()} {self.win_count} Craps Crate-{point}"
            
            # Create crate entry
            crate_info = self.create_crate_yaml_entry(reward_sheet_name, crate_name)
            
            # Create Crate object
            crate_obj = Crate.Crate(crate_info)
            
            # Generate filename
            filename = f"{self.yaml_dir}/{self.crate_prefix}-{point}.yml"
            
            # Write YAML file
            with open(filename, "w") as outfile:
                yaml.dump(crate_obj.dict, outfile, sort_keys=False)
            
            print(f"Created: {filename}")
        
        print("\\nAll Craps Crate YAML files generated successfully!")
    
    def generate_all_files(self):
        """Generate both CSV and YAML files for the complete craps system"""
        print(f"=== {self.folder_name} Craps Generator ===")
        print(f"Item: {self.item_type}")
        print(f"Win payout: {self.win_count} {self.item_type}")
        print(f"Loss payout: {self.loss_count} {self.item_type}")
        print()
        
        # Create directories
        os.makedirs(self.base_dir, exist_ok=True)
        os.makedirs(self.yaml_dir, exist_ok=True)
        
        print("Generating CSV files...")
        
        # Generate first roll CSV
        self.create_first_roll_csv()
        
        # Generate point roll CSVs
        point_numbers = [4, 5, 6, 8, 9, 10]
        for point in point_numbers:
            self.create_point_roll_csv(point)
        
        print(f"\\nCSV files created in: {self.base_dir}")
        print()
        
        # Generate YAML files
        self.generate_yaml_files()
        
        print(f"\\nYAML files created in: {self.yaml_dir}")
        print()
        print("🎉 Complete craps system generated successfully!")
        print()
        print("How to use:")
        print(f"1. Players get keys for: {self.crate_prefix}-FirstRoll")
        print(f"2. Win: {self.win_count} {self.item_type}")
        print(f"3. Loss: {self.loss_count} {self.item_type}")

def main():
    """Main function with interactive prompts"""
    print("=" * 60)
    print("🎲 GENERALIZED CRAPS GENERATOR 🎲")
    print("=" * 60)
    print()
    print("This script creates a complete craps system for any Minecraft item.")
    print("Examples: diamonds, emeralds, gold_ingots, netherite_ingots, etc.")
    print()
    
    # Get item type
    item_type = input("Enter item type (e.g., diamond, emerald, gold_ingot): ").strip()
    if not item_type:
        item_type = "diamond"
        print(f"Using default: {item_type}")
    
    # Get win count
    try:
        win_count = int(input(f"Enter win amount (number of {item_type} for wins): ").strip() or "10")
    except ValueError:
        win_count = 10
        print(f"Using default: {win_count}")
    
    # Get loss count
    try:
        loss_count = int(input(f"Enter loss amount (number of {item_type} for losses, usually 0): ").strip() or "0")
    except ValueError:
        loss_count = 0
        print(f"Using default: {loss_count}")
    
    print()
    print(f"Creating {item_type.title()}{win_count} craps system...")
    print(f"Win: {win_count} {item_type}")
    print(f"Loss: {loss_count} {item_type}")
    print()
    
    # Generate the system
    generator = CrapsGenerator(item_type, win_count, loss_count)
    generator.generate_all_files()

if __name__ == "__main__":
    main()