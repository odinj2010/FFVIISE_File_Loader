# Final Fantasy VII Steam Edition - Direct File Loader (`d3d11.dll`)

A lightweight, portable, and high-performance mod loader for the **Final Fantasy VII Steam Edition** (and compatible PC releases). 

This utility allows modders and players to load unpacked, custom "loose" files (like textures, models, movies, music, and database files) directly from a `mods/` directory, completely bypassing the need to repack `.lgp` archives or modify game installation files.

---

## Features

*   **Zero-Repack Workflow**: Place your raw files directly on disk. The loader hooks the game's file operations to redirect them instantly.
*   **LGP Archive Overrides**: Easily override any asset file inside LGP archives (e.g. textures, models, map scripts) without modifying the original archive.
*   **Full File Overrides**: Redirect entire game directories or standalone files (like `scene.bin`, movies, music, or layouts).
*   **Native Compatibility**: Acts as a proxy for the system `d3d11.dll`, forwarding all graphics commands directly to DirectX 11 for perfect game performance and compatibility with Steam overlays and launchers.
*   **Diagnostic Logging**: Automatically outputs a log (`mods_loader_log.txt`) in the game directory to verify which files are being successfully redirected.

---

## Installation

1.  Download and extract the contents of **`FFVIISE_File_Loader.zip`**.
2.  Navigate to your Final Fantasy VII Steam installation folder (where `FFVII.exe` and `FFVII_LAUNCHER.exe` are located). The default path is usually:
    `C:\Program Files (x86)\Steam\steamapps\common\FINAL FANTASY VII Steam Edition\`
3.  Drag and drop all extracted files (`d3d11.dll`, `FFVIISE_File_Loader_README.md`, and the empty `mods` folder) directly into this folder.

---

## How to Organize Your Mods

Place your custom files inside the newly created `mods/` directory. 

Any file path loaded by the game under the original data directory can be overridden by mirroring the structure inside the `mods/` directory.

### 1. Overriding Standalone / Loose Game Files
**Rule of Thumb**: Any file originally located under the game's `ff7/workingdir/data/` folder can be overridden by placing a modified copy in the `mods/` folder, mirroring the path structure.

**Examples:**
*   **Scene Database**:
    Original: `.../ff7/workingdir/data/lang-en/battle/scene.bin`
    Override: `.../mods/lang-en/battle/scene.bin`
*   **Game Movies**:
    Original: `.../ff7/workingdir/data/movies/opening.bik`
    Override: `.../mods/movies/opening.bik`
*   **Audio Files**:
    Original: `.../ff7/workingdir/data/music_ogg/01_prelude.ogg`
    Override: `.../mods/music_ogg/01_prelude.ogg`

---

### 2. Overriding Files inside LGP Archives
To override a specific file packed inside an `.lgp` archive, create a folder in your `mods/` directory named after the LGP archive (without the `.lgp` extension) and place your loose file inside it.

**Examples:**
*   **Models / Textures inside `char.lgp`**:
    To override `aaab.rsd` inside `ff7/workingdir/data/char.lgp`, place it at:
    `.../mods/char/aaab.rsd`
*   **Field Scripts inside `field.lgp`**:
    To override `mds7_w.dat` inside `ff7/workingdir/data/field.lgp`, place it at:
    `.../mods/field/mds7_w.dat`
*   **Menu Assets inside `menu.lgp`**:
    To override `window.tex` inside `ff7/workingdir/data/menu.lgp`, place it at:
    `.../mods/menu/window.tex`

---

## Verifying Redirections (Troubleshooting)

When you launch the game, the loader automatically creates a file named **`mods_loader_log.txt`** in your game directory. You can open this text file to verify the status:

1.  **Successful Initialization**:
    ```text
    [Loader] Initializing hooks...
    [Loader] Hooks initialized. fopen: 00007FFC09FE5C00, _wfopen: 00007FFC09FDDFA0
    ```
2.  **File Redirection Confirmation**:
    When the game successfully overrides an asset, it will log the path redirection:
    ```text
    [Loader] Redirecting fopen: D:\Games\FF7\ff7\workingdir\data\movies\opening.bik -> D:\Games\FF7\mods\movies\opening.bik
    ```

### Common Issues:
*   **No log file is created**: Double check that `d3d11.dll` is placed in the same folder as the game's main executable. Also ensure you are running the 64-bit version of the game.
*   **The game crashes or restarts immediately**: Make sure you have installed the correct 64-bit compiled DLL. Running a 32-bit DLL in a 64-bit game environment will cause loading errors.

---

## Compiling From Source (For Developers)

If you wish to compile the DLL yourself:

1.  Open the **x64 Native Tools Command Prompt for VS**.
2.  Navigate to the source directory.
3.  Run the python build script:
    ```cmd
    python compile.py
    ```
4.  The compiled `d3d11.dll` will be outputted directly to the directory.
