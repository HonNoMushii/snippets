import os
import subprocess
import shutil


def format_python_files(directory):
    """Recursively formats all Python files in a given directory using Black."""

    # Try to find the full path to `black`
    black_path = shutil.which("black")

    if black_path is None:
        print("❌ Error: Black is not installed or not found in PATH.")
        return

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):  # Check if it's a Python file
                file_path = os.path.join(root, file)
                print(f"🖤 Formatting: {file_path}")
                subprocess.run(
                    [black_path, file_path], check=True
                )  # Run Black Formatter


if __name__ == "__main__":
    directory = input("📂 Enter the directory path to format: ")
    if os.path.isdir(directory):
        format_python_files(directory)
        print("✅ Formatting complete!")
    else:
        print("❌ Invalid directory. Please provide a valid path.")
