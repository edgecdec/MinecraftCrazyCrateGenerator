#!/usr/bin/env python3
"""
Cleanup Old Scripts
This script removes all the old diamond-specific scripts now that we have a generalized craps generator.
"""

import os

def remove_file(filepath):
    """Remove a file if it exists"""
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"✅ Removed: {filepath}")
    else:
        print(f"⚠️  Not found: {filepath}")

def remove_directory(dirpath):
    """Remove a directory if it exists"""
    if os.path.exists(dirpath):
        import shutil
        shutil.rmtree(dirpath)
        print(f"✅ Removed directory: {dirpath}")
    else:
        print(f"⚠️  Directory not found: {dirpath}")

def main():
    """Main cleanup function"""
    print("=== Cleanup Old Diamond-Specific Scripts ===")
    print("Removing old scripts now that we have a generalized craps generator...")
    print()
    
    # List of old scripts to remove
    old_scripts = [
        "cleanup_diamond_craps.py",
        "create_custom_diamond_craps.py", 
        "diamond_craps_generator.py",
        "diamond_craps_summary.py",
        "generate_diamond_craps_crates.py",
        "generate_diamond10_craps_crates.py",
        "remove_diamond_csv_entry.py",
        "setup_diamond_craps.py",
        "update_diamond_craps_csv.py"
    ]
    
    print("🗑️  Removing old diamond-specific scripts:")
    for script in old_scripts:
        remove_file(script)
    
    print()
    
    # Remove test emerald system (created for testing)
    print("🗑️  Removing test emerald system:")
    remove_directory("CrateCSVs/Craps/Emerald5")
    remove_directory("Crates/Craps/Emerald5")
    
    print()
    
    # Show what we're keeping
    print("✅ Keeping:")
    print("  ✅ craps_generator.py (NEW generalized script)")
    print("  ✅ CrateCSVs/Craps/Diamond10/ (Working diamond system)")
    print("  ✅ Crates/Craps/Diamond10/ (Working diamond YAML files)")
    print("  ✅ cleanup_old_scripts.py (This cleanup script)")
    
    print()
    print("🎉 Cleanup complete!")
    print()
    print("📋 How to use the new generalized system:")
    print("  python3 craps_generator.py")
    print()
    print("Examples:")
    print("  • Diamond craps: item=diamond, win=10, loss=0")
    print("  • Emerald craps: item=emerald, win=5, loss=1") 
    print("  • Gold craps: item=gold_ingot, win=20, loss=0")
    print("  • Netherite craps: item=netherite_ingot, win=1, loss=0")

if __name__ == "__main__":
    main()