import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    site_packages_dir = ""
    file_name = "wanda_automation_env.pth"

    for path in sys.path:
        if 'site-packages' in path:
            site_packages_dir = path
    if site_packages_dir:
        path = os.path.join(site_packages_dir, file_name)
    else:
        print("Set automation environment failed: Cannot find site-packages folder in system path.")
        exit(0)

    if len(sys.argv) < 2:
        print("usage: python3.5 configuration.py [options ...]")
        print("\r")
        print("Options:")
        print("    install : Setup wanda automation test project.")
        print("    uninstall : Uninstall wanda automation test project.")
        print("\r")
        print("If you experience permissions issues, please use the root user.")
    elif sys.argv[1] == "install":
        fp = open(path, 'a')
        fp.write(BASE_DIR)
        fp.close
        print("Set automation environment success.")
    elif sys.argv[1] == "uninstall":
        cmd = "rm " + path
        os.system(cmd)
        print("Cleanup automation environment success.")
    else:
        exit(0)
