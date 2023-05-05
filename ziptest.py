import zipfile
#import rarfile
from unrar import rarfile
import multiprocessing


def extract_zip(pwd, zip_file):
    print("extract_zip", pwd)
    try:
        zip_file.extractall(pwd=pwd.encode("utf-8"))
        print("密码破解", pwd)
        return pwd
    except Exception as e:
        print("密码破解失败", pwd)

def extract_zip1(pwd, rar_file):
    # print("extract_zip", pwd)
    try:
        rar_file.extractall(pwd=str(pwd))
        print("密码破解", pwd)
        return pwd
    except Exception as e:
        # print("An exception occurred:", e)
        print("密码破解失败", pwd)

def bruteforce(zip_file):
    # pool = multiprocessing.Pool()
    for pwd in range(0,9999999999):
        # print("密码破解", pwd)
        try:
            zip_file.extractall(pwd=bytes(str(pwd), 'utf-8'))
            print("密码破解", pwd)
            return
        except Exception as e:
            print("An exception occurred:", e)
            print("密码破解失败", pwd)
        # pool.apply_async(extract_zip, args=(pwd, zip_file))
    # pool.close()
    # pool.join()

def bruteforce1(rar_file):
    pool = multiprocessing.Pool()
    for pwd in range(46299,999999999999999):
        # print("密码破解", pwd)
        # pool.apply_async(extract_zip1, args=(pwd, rar_file))
        try:
            rar_file.extractall(pwd=str(pwd))
            print("密码破解", pwd)
            return
        except Exception as e:
        #     print("An exception occurred:", e)
            print("密码破解失败", pwd)
        # pool.apply_async(extract_zip, args=(pwd, zip_file))
    pool.close()
    pool.join()


def pwdGen(pwdListPath):
    with open(pwdListPath, 'r', encoding="latin-1") as f:
        for line in f:
            yield line.strip()


def main():
    myzip = "./test1.zip"
    myrar = "./test1.rar"
    pwd_list_path = "./0-9.8位纯数密码.txt"
    try:
        #zip_file = zipfile.ZipFile(myzip)
        rar_file = rarfile.RarFile(myrar)
        try:
            # pwd_gen = pwdGen(pwd_list_path)
            #bruteforce(zip_file)
            bruteforce1(rar_file)
        finally:
            zip_file.close()
    except FileExistsError:
        print("你的文件不存在")
        return


if __name__ == "__main__":
    main()
