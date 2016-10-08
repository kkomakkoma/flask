#include <Python.h>

#include <iostream>									// for standard I/O
#include <string>										// for strings

#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/imgcodecs.hpp>

static PyObject *Err;

static PyObject *
detectionC_detectionVideo(PyObject *self, PyObject *args)
{

				using namespace std;
				using namespace cv;

				const char *uploadpath;
				const char *filename;

				if(!PyArg_ParseTuple(args, "ss", &uploadpath, &filename))
								return NULL;
	

				const string sourcepath = string(uploadpath) + "/" + string(filename);
				const string renamepath = string(uploadpath) + "/Detection_" + string(filename);
				const string outputpath = renamepath + ".avi";

				VideoCapture inputVideo(sourcepath);


				return Py_BuildValue("sssss", uploadpath, filename, sourcepath.c_str(), renamepath.c_str(), outputpath.c_str());
}

static PyMethodDef DetectionMethods[] = {
				{"detectionVideo", detectionC_detectionVideo, METH_VARARGS,
							"Detection Video"},
				{NULL, NULL, 0, NULL}					// end of array
};

PyMODINIT_FUNC
initdetectionC(void){
				PyObject *m;

				m = Py_InitModule("detectionC",DetectionMethods);
				if (m == NULL)
								return;

				Err = PyErr_NewException("detectionC.error", NULL, NULL);
				Py_INCREF(Err);
				PyModule_AddObject(m, "error", Err);
}


