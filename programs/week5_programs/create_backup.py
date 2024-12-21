import sys
import shutil

def create_backup(file_name):
    backup_name = file_name + "_backup"

    try:
        shutil.copy(file_name, backup_name)
        print(f"Backup of '{file_name}' created as '{backup_name}'.")
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_backup.py <filename>")
    else:
        create_backup(sys.argv[1])
