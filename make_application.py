import json
import os
import platform
import subprocess
import sys
import PyInstaller.__main__


DEFAULT_CONFIG = {
    "version": 2,
    "app_file": "app.py",
    "app_path": "dist/app.app",
    "github_url": f"https://github.com/Daniel-Wilcox/SimpleApplication",
}


def _read_json(filepath: str) -> dict:
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return {}
    return data


def _write_config(config_path: str, data: dict):
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def _get_executable_path():
    app_name = "app"
    root_dir = os.path.dirname(os.path.abspath(__file__))
    dist_path = os.path.join(root_dir, "dist", app_name)

    match platform.system():
        case "Windows":
            executable_name = f"{app_name}.exe"
        case _:
            executable_name = f"{app_name}"

    executable_path = os.path.join(dist_path, executable_name)

    return executable_path


def launch_executable():
    exec_path = _get_executable_path()

    if os.path.exists(exec_path):
        print(f"Launching application from {exec_path}...")
        subprocess.run([exec_path])  # Run the executable
    else:
        print(f"Executable not found at {exec_path}")

    return exec_path


def main():

    root_path = os.path.dirname(__file__)
    config_path = os.path.join(root_path, "config.json")

    if not os.path.exists(config_path):
        config_data = DEFAULT_CONFIG
        _write_config(config_path, DEFAULT_CONFIG)
        print(f"1. {config_data = }")

    else:
        config_data = _read_json(config_path)
        print(f"2. {config_data = }")

    # Pyinstaller
    PyInstaller.__main__.run(["app.py", "--onedir", "--windowed", "-y"])

    launch_executable()


if __name__ == "__main__":
    main()
