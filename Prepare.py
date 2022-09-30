import os
import wget
import zipfile

dir_path = os.path.dirname(os.path.realpath(__file__))
print("Current Path is " + dir_path)

def build_boost():
    print("Start Building BOOST")
    BOOST_URL = "https://boostorg.jfrog.io/artifactory/main/release/1.78.0/source/boost_1_78_0.zip"
    BOOST_ZIP_FILE = dir_path + "/ext/boost_1_78_0.zip"
    BOOST_DIR = dir_path + "/ext/boost"
    
    if not os.path.isdir(BOOST_DIR):
        if not os.path.isfile(BOOST_ZIP_FILE):
            wget.download(BOOST_URL, out=dir_path + "/ext/")
            print("Downloaded " + BOOST_ZIP_FILE)
        
        with zipfile.ZipFile(BOOST_ZIP_FILE, 'r') as zip_ref:
            zip_ref.extractall(dir_path + "/ext")
            os.rename(dir_path + "/ext/boost_1_78_0", BOOST_DIR)

    os.chdir(dir_path + "/ext/boost")
    os.system('bootstrap.bat')
    os.system('b2.exe')

def build_zlib():
    ZLIB_VERSION = "v1.2.11"
    ZLIB_REPO = "https://github.com/madler/zlib.git"
    ZLIB_DIR = dir_path + "/ext/zlib"
    ZLIB_BUILD_DIR = ZLIB_DIR + "/build"
    ZLIB_INSTALL_DIR = dir_path + "/ext/dist"
    print("zlib will be installed to " + ZLIB_INSTALL_DIR)

    os.system("git clone " + ZLIB_REPO + " " + ZLIB_DIR)
    os.chdir(ZLIB_DIR)
    os.system("git checkout " + ZLIB_VERSION + " --force")
    os.mkdir(ZLIB_BUILD_DIR)

    os.system("cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=" + ZLIB_INSTALL_DIR + "..")
    os.system("cmake --build . --config Release --target install")

def build_tiff():
    LIBTIFF_VERSION= "v4.3.0"
    # LIBTIFF_REPO =

# build_boost()
# build_zlib()