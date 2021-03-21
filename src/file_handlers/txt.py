def load_data_intxt(file_path, file_info):
    try:
        with open(file_path, "r") as pr:
            for item in pr.readlines():
                file_info.append(item.rstrip())
    except Exception as e:
        print("The following error has occurred: " + str(e))
    return file_info


def save_data_intxt(file_path, file_info):
    try:
        with open(file_path, "w") as pr:
            for item in file_info:
                pr.write("{}\n".format(item))
    except Exception as e:
        print("The following error has occurred: " + str(e))
    return file_info