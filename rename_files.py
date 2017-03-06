import os
def rename_files():

    # get file name
    file_list = os.listdir(r"D:\prank")
    print(file_list)

    #rename file name
    saved_path = os.getcwd()
    print("current working directory is" + saved_path)
    os.chdir(r"D:\prank")
    for file_name in file_list:
        print("old name-" + file_name)
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print("new name-" + file_name)

    os.chdir(saved_path)
rename_files()
