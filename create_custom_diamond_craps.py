#!/usr/bin/env python3
"""
Custom Diamond Craps Creator
This script allows you to create diamond craps crates with different payout amounts.
"""

import os
import sys
from diamond_craps_generator import DiamondCrapsGenerator

def create_custom_diamond_craps(win_amount, loss_amount=0, folder_name=None):
    """Create a custom diamond craps system with specified payouts"""
    
    if folder_name is None:
        folder_name = f"Diamond{win_amount}"
    
    print(f"Creating Diamond Craps system:")
    print(f"  Win payout: {win_amount} diamonds")
    print(f"  Loss payout: {loss_amount} diamonds")
    print(f"  Folder: CrateCSVs/Craps/{folder_name}")
    print()
    
    # Create custom generator
    generator = DiamondCrapsGenerator(win_payout=win_amount, loss_payout=loss_amount)
    
    # Update the base directory
    generator.base_dir = f"CrateCSVs/Craps/{folder_name}"
    
    # Generate all files
    generator.generate_all_files()
    
    print()
    print("📋 To use this system:")
    print(f"1. Add a crate entry to your main CSV with CrapsAmount set to '{folder_name}'")
    print("2. Update the RewardSheetName to match your desired crate names")
    print("3. Run the crate generator to create YAML files")
    
    return folder_name

def show_examples():
    """Show examples of different diamond amounts"""
    print("💎 DIAMOND CRAPS PAYOUT EXAMPLES:")
    print()
    
    examples = [
        (1, 0, "Single diamond for casual players"),
        (5, 0, "Small reward for beginners"), 
        (25, 0, "Medium reward for regular players"),
        (50, 0, "High reward for VIP players"),
        (100, 0, "Jackpot level for special events"),
        (10, 1, "Win 10, lose 1 (consolation prize)"),
        (20, 5, "Win 20, lose 5 (partial refund)")
    ]
    
    for win, loss, description in examples:
        print(f"  {win:3d} win / {loss:2d} loss - {description}")
    
    print()

def main():
    """Main function"""
    print("=" * 60)
    print("🎲 CUSTOM DIAMOND CRAPS CREATOR 🎲")
    print("=" * 60)
    print()
    
    show_examples()
    
    if len(sys.argv) >= 2:
        # Command line usage
        try:
            win_amount = int(sys.argv[1])
            loss_amount = int(sys.argv[2]) if len(sys.argv) >= 3 else 0
            folder_name = sys.argv[3] if len(sys.argv) >= 4 else None
            
            create_custom_diamond_craps(win_amount, loss_amount, folder_name)
            
        except ValueError:
            print("❌ Error: Please provide valid numbers for win and loss amounts")
            print("Usage: python3 create_custom_diamond_craps.py <win_amount> [loss_amount] [folder_name]")
            
    else:
        # Interactive mode
        print("🎯 INTERACTIVE MODE:")
        print("Enter the diamond amounts you want for your craps game.")
        print()
        
        try:
            win_amount = int(input("💎 Diamonds for WINNING: "))
            loss_amount = int(input("💔 Diamonds for LOSING (usually 0): ") or "0")
            
            folder_name = input(f"📁 Folder name (press Enter for 'Diamond{win_amount}'): ").strip()
            if not folder_name:
                folder_name = None
                
            print()
            create_custom_diamond_craps(win_amount, loss_amount, folder_name)
            
        except ValueError:
            print("❌ Error: Please enter valid numbers")
        except KeyboardInterrupt:
            print("\\n\\n👋 Cancelled by user")

if __name__ == "__main__":
    main()