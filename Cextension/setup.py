from distutils.core import setup, Extension
import subprocess
import os

os.environ["CC"]="gcc"
os.environ["CXX"]="g++"

detectionC_mod = Extension('detectionC',
                           sources = ['detectionC.cpp'],
                           include_dirs = ['/usr/local/include'],
                           library_dirs = ['/usr/local/lib'])

detectionC_mod.extra_compile_args = ['-ggdb',
                                     subprocess.check_output(['pkg-config','--cflags','opencv']),
                                     subprocess.check_output(['pkg-config','--libs','opencv']),
                                    ];

setup(name = "detectionC",
      version = "1.0",
      description = "OpenCV Video Face Detection Module",
      ext_modules = [detectionC_mod],
)
