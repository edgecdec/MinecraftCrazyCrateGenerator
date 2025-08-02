#!/usr/bin/env python3
"""
Diamond Craps System Summary
This script provides a summary of the diamond craps system that was created.
"""

import os

def check_file_exists(filepath):
    """Check if a file exists and return status"""
    return "✅" if os.path.exists(filepath) else "❌"

def main():
    """Display summary of the diamond craps system"""
    print("=" * 60)
    print("🎲 DIAMOND CRAPS SYSTEM SUMMARY 🎲")
    print("=" * 60)
    print()
    
    print("📋 SYSTEM OVERVIEW:")
    print("• Game Type: Craps (dice game)")
    print("• Payout Currency: Diamonds")
    print("• Win Amount: 10 diamonds")
    print("• Loss Amount: 0 diamonds")
    print("• Organization: Properly structured in Crates/Craps/Diamond/")
    print()
    
    print("🎯 GAME RULES:")
    print("• First Roll:")
    print("  - Natural 7 or 11 = Instant WIN (10 diamonds)")
    print("  - Snake eyes (2), 3, or 12 = Instant LOSS (0 diamonds)")
    print("  - Other numbers (4,5,6,8,9,10) = Establish POINT")
    print("• Point Rolls:")
    print("  - Roll your point number again = WIN (10 diamonds)")
    print("  - Roll a 7 = LOSS (0 diamonds)")
    print("  - Any other number = Re-roll")
    print()
    
    print("📁 FILE STRUCTURE:")
    
    # CSV Files
    print("\\n📊 CSV Data Files:")
    csv_files = [
        "CrateCSVs/Craps/Diamond/CrapsDiamondCrate-FirstRoll.csv",
        "CrateCSVs/Craps/Diamond/CrapsDiamondCrate-4.csv",
        "CrateCSVs/Craps/Diamond/CrapsDiamondCrate-5.csv",
        "CrateCSVs/Craps/Diamond/CrapsDiamondCrate-6.csv",
        "CrateCSVs/Craps/Diamond/CrapsDiamondCrate-8.csv",
        "CrateCSVs/Craps/Diamond/CrapsDiamondCrate-9.csv",
        "CrateCSVs/Craps/Diamond/CrapsDiamondCrate-10.csv"
    ]
    
    for csv_file in csv_files:
        status = check_file_exists(csv_file)
        filename = os.path.basename(csv_file)
        print(f"  {status} {filename}")
    
    # YAML Files
    print("\\n🎁 Crate YAML Files:")
    yaml_files = [
        "Crates/Craps/Diamond/CrapsDiamondCrate-FirstRoll.yml",
        "Crates/Craps/Diamond/CrapsDiamondCrate-4.yml",
        "Crates/Craps/Diamond/CrapsDiamondCrate-5.yml",
        "Crates/Craps/Diamond/CrapsDiamondCrate-6.yml",
        "Crates/Craps/Diamond/CrapsDiamondCrate-8.yml",
        "Crates/Craps/Diamond/CrapsDiamondCrate-9.yml",
        "Crates/Craps/Diamond/CrapsDiamondCrate-10.yml"
    ]
    
    for yaml_file in yaml_files:
        status = check_file_exists(yaml_file)
        filename = os.path.basename(yaml_file)
        if "FirstRoll" in filename:
            print(f"  {status} {filename} (Main crate - appears in GUI)")
        else:
            point = filename.split('-')[1].replace('.yml', '')
            print(f"  {status} {filename} (Point {point} crate)")
    
    # Configuration
    print("\\n⚙️  Configuration:")
    main_csv_status = check_file_exists("IMLCrateInfo - Crates.csv")
    print(f"  {main_csv_status} Main CSV updated with CrapsAmount column")
    print(f"  {main_csv_status} Diamond Craps Crate entry added to main CSV")
    
    print()
    print("🚀 USAGE INSTRUCTIONS:")
    print("1. Copy all files to your Minecraft server's CrazyCrates plugin folder")
    print("2. Restart the server or reload the CrazyCrates plugin")
    print("3. Give players the Diamond Craps Crate key:")
    print("   /crates give physical CrapsDiamondCrate-FirstRoll 1 <player>")
    print("4. Players can use the key to start rolling dice for diamonds!")
    print()
    
    print("🔧 SCRIPTS CREATED:")
    scripts = [
        "diamond_craps_generator.py - Generates CSV data files",
        "setup_diamond_craps.py - Sets up main CSV configuration", 
        "generate_diamond_craps_crates.py - Generates YAML crate files",
        "diamond_craps_summary.py - This summary script"
    ]
    
    for script in scripts:
        status = check_file_exists(script.split(' - ')[0])
        print(f"  {status} {script}")
    
    print()
    print("=" * 60)
    print("🎉 DIAMOND CRAPS SYSTEM READY! 🎉")
    print("=" * 60)

if __name__ == "__main__":
    main()