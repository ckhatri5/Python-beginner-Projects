import os

def list_all_files_and_directories(path):
    try:
        for root, dirs, files in os.walk(path):
            print(f"Directory: {root}")
            for dir_name in dirs:
                print(f"  Subdirectory: {os.path.join(root, dir_name)}")
            for file_name in files:
                print(f"  File: {os.path.join(root, file_name)}")
    except FileNotFoundError:
        print(f"The path '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")

if __name__ == "__main__":
    path_to_check = input("Enter the directory path to list: ")
    list_all_files_and_directories(path_to_check)
