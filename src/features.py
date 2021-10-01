import zipfile
from tabulate import tabulate


def show_children_files_info(archive_file: zipfile.ZipFile):
    children_file_info = {"file": [], "size": [], 'is Folder': [], 'compress type': [], 'compress size': []}
    for file in archive_file.filelist:
        name = file.filename
        size = file.file_size
        children_file_info['file'].append(name)
        children_file_info['size'].append(str(size) + " byte")
        children_file_info['is Folder'].append(file.is_dir())
        children_file_info['compress type'].append(file.compress_type)
        children_file_info['compress size'].append(file.compress_size)
    print(tabulate(children_file_info, headers='keys', tablefmt='fancy_outline',
                   showindex=range(1, len(archive_file.filelist) + 1)))


def show_base_file_info(archive_file: zipfile.ZipFile):
    directory_count = 0
    for file in archive_file.filelist:
        if file.is_dir():
            directory_count += 1
        else:
            print("{} creation date : last modified on {}/{}/{} at {}:{}:{}".format(
                file.filename.rpartition('/')[-1], *file.date_time))
    print("filename : ", archive_file.filename)
    print("number of children files : ", len(archive_file.filelist))
    print("children folders : ", directory_count)


def get_files_with_extension(archive_file: zipfile.ZipFile, extension: str):
    search_result = []
    for file in archive_file.filelist:
        actual_file_name = str(file.filename.rpartition('/')[-1])
        if actual_file_name.rpartition('.')[-1].lower() == extension:
            search_result.append(actual_file_name)
    return search_result


def show_results(archive_file: zipfile.ZipFile, search_query):
    query_text = search_query
    file_type_string = str(query_text.rpartition('.')[-1].lower())
    print("searching result with input ( {} )".format(search_query))
    search_results = get_files_with_extension(archive_file=archive_file, extension=file_type_string)
    count_search_result = len(search_results)
    # search_result_table = {}
    try:
        # ================ If results are folder ===============
        if search_results[0] == '':
            search_results = []
            file_type_string = 'folders'
            search_result_table = {"{} {} found".format(count_search_result, file_type_string): search_results}

        # ================ If results are files =============
        else:
            search_result_table = {"{} {} files found".format(count_search_result, file_type_string): search_results}
        print(tabulate(search_result_table, headers='keys', tablefmt='fancy_outline', missingval='N/A'))

    except IndexError:
        # ================== If no results found ==================
        search_result_table = {"{} {} files found".format(count_search_result, file_type_string): search_results}
        print(tabulate(search_result_table, headers='keys', tablefmt='fancy_outline'))


def extract_all_files(archive_file: zipfile.ZipFile):
    extract_directory = str(archive_file.filename.rpartition('.')[0])
    archive_file.extractall(extract_directory)
    print("all files extracted successfully :)")
    print("go to -> '{}' to get you files".format(extract_directory))
