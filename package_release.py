import os
import zipfile
import shutil

def package_release():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_dir = os.path.dirname(project_dir)
    
    zip_name = "FFVIISE_File_Loader.zip"
    releases_dir = os.path.join(workspace_dir, "Releases")
    os.makedirs(releases_dir, exist_ok=True)
    zip_path = os.path.join(releases_dir, zip_name)
    
    dll_source = os.path.join(project_dir, "d3d11.dll")
    readme_source = os.path.join(project_dir, "FFVIISE_File_Loader_README.md")
    
    if not os.path.exists(dll_source):
        print(f"Error: {dll_source} not found! Please compile the DLL first using compile.py.")
        return False
        
    print(f"Packaging release into {zip_name}...")
    
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # 1. Add DLL to zip root
            zipf.write(dll_source, "d3d11.dll")
            print("Added d3d11.dll")
            
            # 2. Add README to zip root
            if os.path.exists(readme_source):
                zipf.write(readme_source, "FFVIISE_File_Loader_README.md")
                print("Added FFVIISE_File_Loader_README.md")
            else:
                print("Warning: FFVIISE_File_Loader_README.md not found, skipping.")
                
            # 3. Create empty mods folder entry
            # To add an empty folder in a zip file, append a path ending with '/'
            zipf.writestr("mods/", "")
            print("Added empty mods/ directory")
            
        print(f"\nSuccessfully created release zip: {zip_path}")
        return True
    except Exception as e:
        print(f"Failed to create zip: {e}")
        return False

if __name__ == "__main__":
    package_release()
