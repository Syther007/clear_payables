# MASQNode DB Reset Tool (`clear_payables.py`)

## Description

This is a simple script designed to clear the `pending_payable` table within a MASQNode SQLite database file (`masq_node.db`). Its primary purpose is to help resolve specific payment bugs by resetting this table.

## Prerequisites

- **If running the script directly:** Python 3
- **If using the compiled executable:** No specific prerequisites are needed, as it's self-contained.

## Usage

1.  **Compile the script** (if you haven't already) using the instructions below.
2.  **Run the executable in one of two ways:**
    *   **Specify Path:** Provide the full path to your `masq_node.db` file as a command-line argument. This tells the script exactly which database to clear.
        *   *Mac/Linux:* `./clear_payables /path/to/your/masq_node.db`
        *   *Windows:* `.\clear_payables.exe C:\path\to\your\masq_node.db`
    *   **Auto-Search:** Run the executable without any arguments. The script will automatically search through a list of default MASQNode installation directories for the `masq_node.db` file and clear the first one it finds.
        *   *Mac/Linux:* `./clear_payables`
        *   *Windows:* `.\clear_payables.exe`
3.  **Confirmation:** Regardless of the method used, the script will display the path of the database it intends to modify and ask for your confirmation before proceeding to clear the `pending_payable` table.


# Examples

**(Assuming the compiled executable is in the `dist` directory)**

**Mac/Linux:**

*   Specify the database path:
    ```bash
    ./clear_payables /Users/youruser/Library/Application\ Support/MASQ/base-sepolia/node-data.db
    ```
*   Auto-search default locations:
    ```bash
    ./clear_payables
    ```

**Windows:**

*   Specify the database path:
    ```powershell
    .\clear_payables.exe "C:\WINDOWS\system32\config\systemprofile\AppData\Local\MASQ\base-sepolia\node-data.db"
    ```
*   Auto-search default locations:
    ```powershell
    .\clear_payables.exe
    ```

## Compile to Bin using pyinstaller

### Install pyinstaller
```
pip3 install pyinstaller
```



## PyInstaller Common Flags

| Flag               | What it does                                        |
|:-------------------|:----------------------------------------------------|
| `--onefile`         | Create a single executable.                        |
| `--noconsole`       | (Windows only) Hide console window for GUI apps.    |
| `--icon=myicon.ico` | Add an icon to the binary (Windows, Mac).            |
| `--clean`           | Clean temporary build files before building.        |



```
pyinstaller --onefile clear_payables.py


# The compiled executable will be in the 'dist' directory:
# dist/clear_payables    # (Linux/Mac)
# dist/clear_payables.exe # (Windows)
```


### mac OS install command
```
pyinstaller --onefile clear_payables.py 
```

### Windows OS install command
```
pyinstaller.exe --onefile clear_payables.py

# C:\Users\cyther\AppData\Roaming\Python\Python313\Scripts\pyinstaller.exe --onefile --noconsole clear_payables.py
```