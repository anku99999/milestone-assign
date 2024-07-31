def read_file(file_name):
    try:
        with open(file_name,"r") as file:
            return file.read()
    except FileNotFoundError:
        return "file not found"

def write_file(file_name,data):
    with open(file_name,"w") as file:
        return file.write(data)

def append_file(file_name,data):
    with open(file_name,"a") as file:
        return file.append(data)
    


    

        