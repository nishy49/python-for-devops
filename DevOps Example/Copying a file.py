import shutil
def copy_file(source,destination):
    try:
        shutil.copy(source,destination)#Copy file fromsource
        print(f"File copied from {source} to {destination}")
    except FileNotFoundError:
        print("Error:source file not found") #Handle case when source file does not exists
    except PermissionError:
        print("Error:Permission denied")#Handle permission denied
    except Exception as e:
        print(f"Unexpected error:{e}")#Handles other exceptions
    finally:
        print("Copy operation completed")
copy_file("example.txt","backup.txt")