
import zipfile

# ========= file path ========
file_path = "./myfiles/images/new.zip"



# ========= get filename and extension ==========
def get_file_info(file_path):
    file_name = file_path.rpartition('/')[-1]
    file_extension = file_name.rpartition('.')[-1]
    file_info_list = [file_name, file_extension]
    return file_info_list

print(get_file_info(file_path))