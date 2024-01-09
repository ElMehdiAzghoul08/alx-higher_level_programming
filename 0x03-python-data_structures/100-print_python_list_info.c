#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *item;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->alloc_slots;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; ++i)
	{
		printf("Element %d: ", alloc);

		item = PyList_GetItem(p, i);
		printf("%s\n", i, Py_TYPE(item)->tp_name);
	}
}
