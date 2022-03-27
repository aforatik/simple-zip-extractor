# ========== Imports ===========
from utils import *

# =============== Useful variables ============


available_operations = '''========  Operations  ======== :
    1) Extract all
    2) Selective extract
    3) Search files with extension name
    4) List all file information within this archive
    5) Count all file types
    6) Count Specific file types
    7) Extract specific file types
    8) Exit
    \n'''


# =========== Useful functions =============

def titleText(title: str, width: int, fill_char: str = ' ', gap_between: int = 0):
    print(title.center(len(title) + gap_between * 2, " ").center(len(title) + (gap_between + width) * 2, fill_char))


def no_use():
    print("Functionality not added...")


# =========== Enter file path ========

file_path = input("enter a zip file path : ")

file_path = file_path.strip(" ")

if file_path == "":
    print("File path can't be empty!!")
else:
    try:
        archive_file = zipfile.ZipFile(file_path)
    except Exception as file_e:
        print(f"Error! {file_e.args[1]}")
    else:
        file_actual_name = archive_file.filename.rpartition('/')[-1]

        titleText("basic file information", 10, "=", gap_between=2)

        # 1) Extract all (available)
        # 2) Selective extract
        # 3) Search files with extension name (available)
        # 4) List all file information within this archive (available)
        # 5) Count all file types
        # 6) Count Specific file types
        # 7) Extract specific file types
        # 8) Exit

        show_base_file_basic_info(archive_file=archive_file)

        while True:
            print(available_operations)
            operation = input(">> ").strip()

            # ======= Extract all files =======
            if operation == '1':
                print("\n[NOTE: keep empty to extract at current directory]\n")
                output_folder = input('provide output directory name : ')
                extract_all_files(archive_file=archive_file, output_directory=output_folder)
                print('\n')
                input("....continue....".center(50))
            # ======= Selective extract ========
            elif operation == '2':
                no_use()
                print('\n')
                input("....continue....".center(50))

            # ========== Search files with extension name ===========
            elif operation == '3':
                print("\n[NOTE: keep empty or put space to search folders]\n")
                query = input("enter extension name : ")
                show_search_results(archive_file=archive_file, search_query=query)
                print('\n')
                input("....continue....".center(50))

            # List all file information within this archive
            elif operation == '4':
                show_children_files_info(archive_file=archive_file)
                print('\n')
                input("....continue....".center(50))

            # Count all file types
            elif operation == '5':
                no_use()
                print('\n')
                input("....continue....".center(50))
            elif operation == '6':
                no_use()
                print('\n')
                input("....continue....".center(50))
            elif operation == '7':
                no_use()
                print('\n')
                input("....continue....".center(50))
            elif operation == '8':
                exit(0)
            else:
                print("please enter number between 1-8\n")
