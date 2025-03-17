import shutil

def mov_file(source,destination):
    try:
        shutil.move(source,destination)#Move file from source todestination
        print(f"File moved from {source} to {destination}")
    except FileNotFoundError:
        print("Error :Source file not found ")#Handle case when source file oes notexists
    except PermissionError:
        print("Error: Permission denied.")  # Handle permission issues
    except Exception as e:
        print(f"Unexpected error: {e}")  # Handle any other errors
    finally:
        print("Move operation completed.")  # Always executes
mov_file("backup.txt","FileCopy/backup.txt")