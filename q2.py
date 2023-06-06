def get_file_type(extension_type, file_list):
    extension_type_pairs = dict(pair.split(",") for pair in extension_type.split(";"))
    file_type_dict = {}

    for file_name in file_list:
        file_extension = file_name.split(".")[-1]
        file_type = extension_type_pairs.get(file_extension, "unknown")
        file_type_dict[file_name] = file_type

    return file_type_dict

# ("xls,spreadsheet;xlsx,spreadsheet;jpg,image", ["abc.jpg","xyz.xls", "text.csv", "123"])
extension_type = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
file_list = ["abc.jpg","xyz.xls", "text.csv", "123"]

file_types = get_file_type(extension_type, file_list)
print(file_types)