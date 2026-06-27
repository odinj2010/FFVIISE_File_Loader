# FFVIISE Mod Loader - v1.1.0 Release Notes

A major upgrade focused on asset conflict resolution, load order customization, and developer ease of use.

## 🚀 Key Features & Changes

### 📁 Multi-Mod Subfolders & Prioritized Load Order
* **Mod Isolation:** Mods no longer need to be merged into a single flat directory. Each mod now lives in its own subdirectory inside the `mods/` folder (e.g., `mods/TextureMod/`, `mods/TranslateMod/`), preventing file conflicts.
* **Priority Loader (`load_order.txt`):** Added a load priority list. Mod folders listed at the top of `mods/load_order.txt` have the highest priority and will override matching assets in folders below them.
* **Auto-Discovery & Appending:** 
  * If `load_order.txt` is missing, it will auto-create and populate it with all discovered folders alphabetically.
  * When you add a new mod directory later, the loader automatically detects it and appends it to the bottom of `load_order.txt` (lowest priority) so your custom load order is never broken.

### 🖼️ Configurable Splash Screens
* **SplashScreens Option:** Added a configurable key in `mods_loader.ini` to customize the game's startup screens (`dotemu-logo.png`, `finelogo.png`, `press_start.png`):
  * `custom`: Always loads the custom splash screens embedded directly inside the DLL (ignores the mods folder).
  * `default`: Checks your active mods folder for replacements first, falling back to original game splash screens if none are found.

### 📝 Auto-Clearing Logs
* **Session Logging:** The log file (`mods_loader_log.txt`) is now truncated/cleared on every fresh game startup. It will no longer grow indefinitely, keeping logs clean and relevant for your current session.

### 🛠️ Interactive Developer Tool (`run.bat`)
* **Dual-Option Menu:** Refactored the helper script into an interactive menu. Launching it now prompts you to choose between:
  1. Compiling the mod loader `d3d11.dll` (includes embedding assets compiled via `rc.exe` and `resources.res`).
  2. Pushing all changes directly to GitHub with a custom or default commit message.
