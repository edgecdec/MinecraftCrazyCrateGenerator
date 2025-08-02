#!/usr/bin/env python3
"""
Cleanup Diamond Craps Files
This script removes old/test diamond craps files and keeps only the main Diamond10 system.
"""

import os
import shutil

def remove_directory(path):
    """Remove a directory and all its contents"""
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"✅ Removed: {path}")
    else:
        print(f"⚠️  Not found: {path}")

def remove_file(path):
    """Remove a single file"""
    if os.path.exists(path):
        os.remove(path)
        print(f"✅ Removed: {path}")
    else:
        print(f"⚠️  Not found: {path}")

def main():
    """Main cleanup function"""
    print("=== Diamond Craps Cleanup ===")
    print("Removing old and test diamond craps files...")
    print()
    
    # Remove old Diamond folder (without number)
    print("🗑️  Removing old Diamond folder (old naming convention):")
    remove_directory("CrateCSVs/Craps/Diamond")
    remove_directory("Crates/Craps/Diamond")
    
    print()
    
    # Remove test folders
    print("🗑️  Removing test Diamond folders:")
    remove_directory("CrateCSVs/Craps/Diamond25")
    remove_directory("CrateCSVs/Craps/Diamond50")
    
    print()
    
    # List what we're keeping
    print("✅ Keeping main Diamond10 system:")
    if os.path.exists("CrateCSVs/Craps/Diamond10"):
        print("  ✅ CrateCSVs/Craps/Diamond10/ (CSV data files)")
    else:
        print("  ❌ CrateCSVs/Craps/Diamond10/ (MISSING!)")
    
    if os.path.exists("Crates/&lDiamond10CrapsCrate.yml"):
        print("  ✅ Crates/&lDiamond10CrapsCrate.yml (Main crate file)")
    else:
        print("  ❌ Crates/&lDiamond10CrapsCrate.yml (MISSING!)")
    
    print()
    
    # Show final directory structure
    print("📁 Final Craps directory structure:")
    if os.path.exists("CrateCSVs/Craps"):
        for item in sorted(os.listdir("CrateCSVs/Craps")):
            item_path = os.path.join("CrateCSVs/Craps", item)
            if os.path.isdir(item_path):
                print(f"  📂 {item}")
    
    print()
    print("🎉 Cleanup complete!")
    print("Ready for git commit with clean Diamond10 craps system.")

if __name__ == "__main__":
    main()