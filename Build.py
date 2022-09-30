import platform
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description='Build OpenImageIO')
    parser.add_argument('--target', default="VS2022", help='the target to build(VS2022, VS2019, XCode)')
    args = parser.parse_args()
     
    systemName = platform.system()
    print("Building On " + systemName + " System")

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("Current Path is " + dir_path)

    boost_path = dir_path + "/ext/boost"

    if not os.path.isdir(dir_path + '/build/'):
        os.mkdir(dir_path + '/build/')

    os.chdir(dir_path + "/build")
    if systemName == "Windows":
        if args.target == "VS2022":
            os.system('cmake -DBOOST_ROOT=' + boost_path + ' -G "Visual Studio 17 2022" -A x64 ../')
        else:
            os.system('cmake -G "Visual Studio 16 2019" -A x64 ../')
    elif systemName == "Darwin":
        os.system('cmake -G "Xcode" ../')

if __name__ == '__main__':
    main()