import time
import zipfile
#import rarfile
from unrar import rarfile
import multiprocessing

# 数字：0、1、2、3、4、5、6、7、8、9
#
# 字母：a、b、c、d、e、f、g、h、i、j、k、l、m、n、o、p、q、r、s、t、u、v、w、x、y、z、A、B、C、D、E、F、G、H、I、J、K、L、M、N、O、P、Q、R、S、T、U、V、W、X、Y、Z
#
# 标点符号：!、@、#、$、%、^、&、*、(、)、-、_、+、=、{、}、[、]、|、\、;、:、'、"、,、.、/、<、>、?
#
# 其他：空格、换行符、制表符等。
import itertools

password = ""
chars = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+=-[]{}\|,.<>;:/?"
length = 1
#wod2

def brutefoce(zfile):
    try:
        myzip = zipfile.ZipFile(zfile)
    except FileExistsError:
        print("你传入的zip文件不存在")
        return
    global length
    while True:
        password = itertools.product(chars, repeat=length)
        total = len(chars) ** length
        for i, passwd in enumerate(password):
            passwd = ''.join(passwd)
            try:
                myzip.extractall(pwd=passwd.encode("utf-8"))
                print('密码破解', passwd)
                return
            except Exception as e:
                print('密码破解失败', e)
                print('密码破解失败', passwd)
            if i == total - 1:
                length += 1
                break


zfile = "your-path"

#brutefoce(zfile)
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
    # pool = multiprocessing.Pool()
    for pwd in range(0,1000):
        # print("密码破解", pwd)
        # pool.apply_async(extract_zip1, args=(pwd, rar_file))
        try:
            pwdstr = str(pwd)
            rar_file.extractall(pwd=pwdstr)
            print("密码破解", pwd)
            return
        except Exception as e:
            print("An exception occurred:", e)
            print("密码破解失败", pwd)
        # pool.apply_async(extract_zip, args=(pwd, zip_file))
    # pool.close()
    # pool.join()

def bruteforce2(rar_file):
    pool = multiprocessing.Pool()
    for pwd in range(0,1000):
        print("密码破解1", pwd)
        last = pool.apply_async(extract_zip2, args=(pwd, rar_file))
        if len(pool._cache) > 500:
            print("waiting for cache to clear...")
            last.wait()
    print("waiting for pool.close1()...")
    pool.close()
    print("waiting for pool.close()...")
    pool.join()
    print("waiting for pool.join()...")

def bruteforce3(rar_file):
    # pool = multiprocessing.Pool()
    # for pwd in range(0, 1000):
    #     print("密码破解1", pwd)
    #     last = pool.apply_async(extract_zip2, args=(pwd, rar_file))
    #     if len(pool._cache) > 500:
    #         print("waiting for cache to clear...")
    #         last.wait()
    # print("waiting for pool.close1()...")
    # pool.close()
    # print("waiting for pool.close()...")
    # pool.join()
    # print("waiting for pool.join()...")
    pool = multiprocessing.Pool()
    global length
    startProgram = False
    while True:
        password = itertools.product(chars, repeat=length)
        total = len(chars) ** length
        for i, passwd in enumerate(password):
            passwd = ''.join(passwd)
            if(passwd == "uqqq"):
                startProgram = True
            if(passwd == "iqqq"):
                return
            if(not str(passwd).isdecimal() and startProgram):#wod2
                print("密码破解1", passwd)
                last = pool.apply_async(extract_zip2, args=(passwd, rar_file))
            if len(pool._cache) > 1000:
                print("waiting for cache to clear...")
                last.wait()
            if i == total - 1:
                length += 1
                break
    print("waiting for pool.close1()...")
    pool.close()
    print("waiting for pool.close()...")
    pool.join()
    print("waiting for pool.join()...")

def extract_zip2(pwd, rar_file):
    # print("extract_zip", pwd)
    try:
        rar_file.extractall(pwd=str(pwd))
        print("uqqq密码破解", pwd)
        return pwd
    except Exception as e:
        #print("An exception occurred:", e)
        print("uqqq密码破解失败", pwd)
        return pwd
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
            start_time = time.time()
            #bruteforce1(rar_file)#52秒
            #bruteforce2(rar_file)#20秒左右
            bruteforce3(rar_file)
            end_time = time.time()
            run_time = end_time - start_time
            print(run_time)
        except Exception as e:
            print("报错1", e)
        finally:
            rar_file.close()
    except Exception as e:
        print("报错", e)
        print("你的文件不存在")
        return


if __name__ == "__main__":
    main()
