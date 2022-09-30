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
    os.system('b2.exe variant=release address-model=64 link=static,shared')

    os.environ["BOOST_ROOT"] = BOOST_DIR

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
    LIBTIFF_REPO = "https://gitlab.com/libtiff/libtiff.git"
    LIBTIFF_DIR = dir_path + "/ext/libtiff"
    LIBTIFF_BUILD_DIR = LIBTIFF_DIR + "/build"
    LIBTIFF_INSTALL_DIR = dir_path + "/ext/dist"
    print("libtiff will be installed to " + LIBTIFF_INSTALL_DIR)

    if not os.path.isdir(LIBTIFF_DIR):
        os.system("git clone " + LIBTIFF_REPO + " " + LIBTIFF_DIR)
    os.chdir(LIBTIFF_DIR)

    os.system("git checkout " + LIBTIFF_VERSION + " --force")
    if not os.path.isdir(LIBTIFF_BUILD_DIR):
        os.mkdir(LIBTIFF_BUILD_DIR)

    os.system("cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=" + LIBTIFF_INSTALL_DIR + "..")
    os.system("cmake --build . --target install")

    os.environ["LIBTIFF_ROOT"] = LIBTIFF_INSTALL_DIR

def build_openexr():
    OPENEXR_VERSION = "v2.4.1"
    OPENEXR_REPO = "https://github.com/AcademySoftwareFoundation/openexr.git"
    OPENEXR_DIR = dir_path + "/ext/openexr"
    OPENEXR_BUILD_DIR = OPENEXR_DIR + "/build"
    OPENEXR_INSTALL_DIR = dir_path + "/ext/dist"
    print("openexr will be installed to " + OPENEXR_INSTALL_DIR)

    if not os.path.isdir(OPENEXR_DIR):
        os.system("git clone " + OPENEXR_REPO + " " + OPENEXR_DIR)
    os.chdir(OPENEXR_DIR)

    os.system("git checkout " + OPENEXR_VERSION + " --force")
    if not os.path.isdir(OPENEXR_BUILD_DIR):
        os.mkdir(OPENEXR_BUILD_DIR)

    os.system("cmake -DCMAKE_BUILD_TYPE=Release -DILMBASE_PACKAGE_PREFIX=" + OPENEXR_INSTALL_DIR + " -DOPENEXR_BUILD_UTILS=0 -DOPENEXR_BUILD_TESTS=0 -DOPENEXR_BUILD_PYTHON_LIBS=0 -DCMAKE_INSTALL_PREFIX=" + OPENEXR_INSTALL_DIR + "..")
    os.system("cmake --build . --config Release --target install")

    os.environ["ILMBASE_ROOT"] = OPENEXR_INSTALL_DIR
    os.environ["OPENEXR_ROOT"] = OPENEXR_INSTALL_DIR
    os.environ["ILMBASE_LIBRARY_DIR"] = OPENEXR_INSTALL_DIR + "/lib"
    os.environ["OPENEXR_LIBRARY_DIR"] = OPENEXR_INSTALL_DIR + "/lib"

def build_libjpeg_turbo():
    LIBJPEG_TURBO_VERSION = "2.0.5"
    LIBJPEG_TURBO_REPO = "https://github.com/libjpeg-turbo/libjpeg-turbo.git"
    LIBJPEG_TURBO_DIR = dir_path + "/ext/libjpeg-turbo"
    LIBJPEG_TURBO_BUILD_DIR = LIBJPEG_TURBO_DIR + "/build"
    LIBJPEG_TURBO_INSTALL_DIR = dir_path + "/ext/dist"

    if not os.path.isdir(LIBJPEG_TURBO_DIR):
        os.system("git clone " + LIBJPEG_TURBO_REPO + " " + LIBJPEG_TURBO_DIR)
    os.chdir(LIBJPEG_TURBO_DIR)

    os.system("git checkout " + LIBJPEG_TURBO_VERSION + " --force")
    if not os.path.isdir(LIBJPEG_TURBO_BUILD_DIR):
        os.mkdir(LIBJPEG_TURBO_BUILD_DIR)

    os.system("cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=" + LIBJPEG_TURBO_INSTALL_DIR + "..")
    os.system("cmake --build . --config Release --target install")

    os.environ["JPEGTurbo_ROOT"] = LIBJPEG_TURBO_INSTALL_DIR

def build_pybind11():
    PYBIND11_VERSION = "v2.8.1"
    PYBIND11_REPO = "https://github.com/pybind/pybind11.git"
    PYBIND11_DIR = dir_path + "/ext/pybind11"
    PYBIND11_BUILD_DIR = PYBIND11_DIR + "/build"
    PYBIND11_INSTALL_DIR = dir_path + "/ext/dist"

    if not os.path.isdir(PYBIND11_DIR):
        os.system("git clone " + PYBIND11_REPO + " " + PYBIND11_DIR)
    os.chdir(PYBIND11_DIR)

    os.system("git checkout " + PYBIND11_VERSION + " --force")
    if not os.path.isdir(PYBIND11_BUILD_DIR):
        os.mkdir(PYBIND11_BUILD_DIR)

    os.system("cmake -DPYBIND11_TEST=OFF -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=" + PYBIND11_INSTALL_DIR + "..")
    os.system("cmake --build . --config Release --target install")

    os.environ["pybind11_ROOT"] = PYBIND11_INSTALL_DIR

def build_oiio():
    OIIO_DIR = dir_path
    # OIIO_BUILD_DIR = OIIO_DIR + "/build"
    OIIO_INSTALL_DIR = dir_path + "/dist"

    os.chdir(OIIO_DIR)

    os.system("cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=" + OIIO_INSTALL_DIR + "..")
    # os.system("cmake --build . --config Release --target install")

build_boost()
# build_zlib()
# build_tiff()
# build_openexr()
# build_libjpeg_turbo()
# build_pybind11()

# build_oiio()