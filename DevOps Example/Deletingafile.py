import os
def delete_file(filename):
    try:
        if os.path.exists(filename): #Check if file exists
            os.remove(filename)#Delete the file
            print(f"{filename} deleted successfully")
        else:
            print("Error:file not found")
    except Exception as e:
        print(f"Error:{e}")
    finally:
        print("Delete Operation completed")

delete_file("oldfile.txt")