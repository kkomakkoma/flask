from distutils.core import setup, Extension

detectionC_mod = Extension('detectionC',
        sources = ['detectionC.cpp'])

setup(name = "detectionC",
        version = "1.0",
        description = "OpenCV Video Face Detection Module",
        ext_modules = [detectionC_mod],
)
