import os
import sys

def Counttool(filePath):
    try:
        byteCount = os.path.getsize(filePath)
        print(f"Number of bytes in the provided file: {byteCount}")
    except OSError as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != '-c':
        print("Usage Error: Counttool -c <filepath>")
        sys.exit(1)

    filePath = sys.argv[2]
    
    if not(os.path.isfile(filePath)):
        print("File has not been found in this path")
        sys.exit(1)
    Counttool(filePath)