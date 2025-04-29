#!/usr/bin/env python3

import sqlite3
import sys
import os
import platform

# List of potential database locations
DEFAULT_DB_PATHS = [
    "./node-data.db",
]
DEFAULT_DB_PATHS_windows = [
    r"./node-data.db",
    r"./base-sepolia/node-data.db",
    r"./polygon-amoy/node-data.db",
    r"C:\WINDOWS\system32\config\systemprofile\AppData\Local\MASQ\base-sepolia\node-data.db",
    r"C:\WINDOWS\system32\config\systemprofile\AppData\Local\MASQ\polygon-amoy\node-data.db",
]
DEFAULT_DB_PATHS_macos = [
    "./node-data.db",
    "./base-sepolia/node-data.db",
    "./polygon-amoy/node-data.db",
    "~/Library/Application Support/MASQ/base-sepolia/node-data.db",
    "~/Library/Application Support/MASQ/polygon-amoy/node-data.db",
]
DEFAULT_DB_PATHS_linux = [
    "./node-data.db",
    "./base-sepolia/node-data.db",
    "./polygon-amoy/node-data.db",
    "~/snap/masq/x1/.local/share/MASQ/base-sepolia/node-data.db",
    "~/snap/masq/x1/.local/share/MASQ/polygon-amoy/node-data.db",
]

current_os = platform.system()
if current_os == "Windows":
    active_default_paths = DEFAULT_DB_PATHS_windows
elif current_os == "Darwin":
    active_default_paths = DEFAULT_DB_PATHS_macos
elif current_os == "Linux":
    active_default_paths = DEFAULT_DB_PATHS_linux
else:
    print(f"Warning: Unsupported operating system '{current_os}'. Using default paths.")
    active_default_paths = ["./node-data.db"] # Fallback

def empty_pending_payable(db_path):
    if not os.path.isfile(db_path):
        print(f"Database file '{db_path}' does not exist or is not accessible.")
        return False

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        print(f"\n*** WARNING ***")
        print(f"You are about to clear the 'pending_payable' table in the database:")
        print(f"  {db_path}")
        confirm = input("Are you absolutely sure you want to proceed? (y/n): ").lower()

        if confirm == 'y':
            cursor.execute("DELETE FROM pending_payable;")
            conn.commit()
            print(f"\nTable 'pending_payable' has been emptied successfully in '{db_path}'.")
            return True
        else:
            print("\nOperation cancelled by user.")
            return False

    except sqlite3.Error as e:
        print(f"An error occurred while processing '{db_path}': {e}")
        return False
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    processed_any = False
    if len(sys.argv) > 1:
        db_path = sys.argv[1]
        print(f"Processing specified database: {db_path}")
        if empty_pending_payable(db_path):
            processed_any = True
    else:
        print(f"No database path provided. Checking default locations:")
        found_any = False
        for path_template in active_default_paths:
            path = os.path.expanduser(path_template) # Expand ~
            print(f"- Checking '{path}' (from template '{path_template}')...")
            if os.path.isfile(path):
                found_any = True
                print(f" ✅ Found. Attempting to empty 'pending_payable'...")
                if empty_pending_payable(path):
                    processed_any = True
            else:
                print(f"  Not found or not accessible.")
        if not found_any:
            print("\nNo database files found in the default locations.")
        if processed_any:
            print("\n✅ Successfully reset 'pending_payable' in database.")
        else:
            print("\n❌ No databases found or 'pending_payable' reset failed.")
        if platform.system() == "Windows":
            print("\nPress Enter to continue...")
            os.system("pause")