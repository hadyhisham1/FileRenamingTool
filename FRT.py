import os
def main():
    path = input('Enter Folder Path : ')
    kword = input('Enter KeyWord : ')
    for count, filename in enumerate(os.listdir(path)):
        dst = f"{kword} {str(count+1)}.txt"
        src =f"{path}/{filename}"
        dst =f"{path}/{dst}"
        os.rename(src, dst)
main()
