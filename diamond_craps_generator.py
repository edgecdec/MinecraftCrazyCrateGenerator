#!/usr/bin/env python3
"""
Diamond Craps Generator Script
Generates CSV files for a craps game that pays out diamonds instead of money.
Win payout: 10 diamonds
Loss/Re-roll payout: 0 diamonds
"""

import os
import csv
from Constants import TwoDiceRollChances

class DiamondCrapsGenerator:
    def __init__(self, win_payout=10, loss_payout=0):
        self.win_payout = win_payout
        self.loss_payout = loss_payout
        self.base_dir = f"CrateCSVs/Craps/Diamond{win_payout}"
        self.crate_prefix = f"CrapsDiamond{win_payout}Crate"
        
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
    
    def create_directory(self):
        """Create the directory structure for diamond craps files"""
        os.makedirs(self.base_dir, exist_ok=True)
        print(f"Created directory: {self.base_dir}")
    
    def get_win_command(self):
        """Get the command for winning (giving diamonds)"""
        return f"give %player% diamond {self.win_payout}"
    
    def get_loss_command(self):
        """Get the command for losing (giving nothing)"""
        return f"give %player% diamond {self.loss_payout}"
    
    def get_reroll_command(self, target_number):
        """Get the command for re-rolling with a specific target"""
        return f"give %player% diamond {self.loss_payout}, crates give physical {self.crate_prefix}-{target_number} 1 %player%"
    
    def create_first_roll_csv(self):
        """Create the first roll CSV file"""
        filename = os.path.join(self.base_dir, f"{self.crate_prefix}-FirstRoll.csv")
        
        # CSV header
        header = [
            "DisplayName", "DisplayItem", "DisplayAmount", "Lore", "MaxRange", 
            "Chance", "PercentChance", "Items", "Amounts", "Commands", 
            "TimesToExecuteCommands", "Messages"
        ]
        
        rows = []
        
        for roll in range(2, 13):
            chance = self.roll_chances[roll]
            percent = round((chance / TwoDiceRollChances.TOTAL) * 100, 2)
            
            if roll in [7, 11]:  # Natural wins
                display_name = f"&a&l{roll}!!! YOU WON!"
                display_item = "DIAMOND"
                command = self.get_win_command()
                message = "&7You won!"
            elif roll in [2, 3, 12]:  # Craps (immediate loss)
                display_name = f"&a&l{roll}!!! YOU LOSE!"
                display_item = "BONE"
                command = self.get_loss_command()
                message = "&7You lost!"
            else:  # Point numbers (4, 5, 6, 8, 9, 10) - re-roll
                display_name = f"&a&l{roll}!!! RE-ROLL!"
                display_item = "TRIPWIRE_HOOK"
                command = self.get_reroll_command(roll)
                message = "&7Re-Roll!"
            
            row = [
                display_name,
                display_item,
                "1",  # DisplayAmount
                f"ROLL {roll}",  # Lore
                "",  # MaxRange (will be calculated later)
                str(chance),  # Chance
                str(percent),  # PercentChance
                "AIR",  # Items
                "1",  # Amounts
                command,  # Commands
                "1",  # TimesToExecuteCommands
                message  # Messages
            ]
            rows.append(row)
        
        # Write to CSV
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
        
        rows = []
        
        for roll in range(2, 13):
            chance = self.roll_chances[roll]
            percent = round((chance / TwoDiceRollChances.TOTAL) * 100, 2)
            
            if roll == point_number:  # Hit the point - WIN!
                display_name = f"&a&l{roll}!!! YOU WON!"
                display_item = "DIAMOND"
                command = self.get_win_command()
                message = "&7You won!"
            elif roll == 7:  # Seven out - LOSE!
                display_name = f"&a&l{roll}!!! YOU LOSE!"
                display_item = "BONE"
                command = self.get_loss_command()
                message = "&7You lost!"
            else:  # Any other number - re-roll with same point
                display_name = f"&a&l{roll}!!! RE-ROLL!"
                display_item = "TRIPWIRE_HOOK"
                command = self.get_reroll_command(point_number)
                message = "&7Re-Roll!"
            
            row = [
                display_name,
                display_item,
                "1",  # DisplayAmount
                f"ROLL {roll}",  # Lore
                "",  # MaxRange (will be calculated later)
                str(chance),  # Chance
                str(percent),  # PercentChance
                "AIR",  # Items
                "1",  # Amounts
                command,  # Commands
                "1",  # TimesToExecuteCommands
                message  # Messages
            ]
            rows.append(row)
        
        # Write to CSV
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows(rows)
        
        print(f"Created: {filename}")
    
    def generate_all_files(self):
        """Generate all CSV files for the diamond craps game"""
        print("Generating Diamond Craps CSV files...")
        print(f"Win payout: {self.win_payout} diamonds")
        print(f"Loss payout: {self.loss_payout} diamonds")
        print()
        
        # Create directory
        self.create_directory()
        
        # Create first roll file
        self.create_first_roll_csv()
        
        # Create point roll files (4, 5, 6, 8, 9, 10)
        point_numbers = [4, 5, 6, 8, 9, 10]
        for point in point_numbers:
            self.create_point_roll_csv(point)
        
        print()
        print("All Diamond Craps CSV files generated successfully!")
        print(f"Files created in: {self.base_dir}")

def main():
    """Main function to run the diamond craps generator"""
    print("=== Diamond Craps Generator ===")
    print("This script generates CSV files for a craps game that pays out diamonds.")
    print()
    
    # Create generator with specified payouts
    generator = DiamondCrapsGenerator(win_payout=10, loss_payout=0)
    
    # Generate all files
    generator.generate_all_files()
    
    print()
    print("How to use:")
    print(f"1. Add a crate entry to your main CSV with CrapsAmount set to 'Diamond{generator.win_payout}'")
    print("2. The crate system will automatically use these CSV files")
    print("3. Players will receive diamonds instead of money for wins!")

if __name__ == "__main__":
    main()