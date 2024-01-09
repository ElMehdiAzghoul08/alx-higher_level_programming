#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	int size, allocated_slots, i;
	PyObject *item;

	size = PyList_Size(p);
	allocated_slots = ((PyListObject *)p)->allocated_slots;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated_slots);

	for (i = 0; i < size; ++i)
	{
		printf("Element %d: ", allocated_slots);

		item = PyList_GetItem(p, i);
		printf("%s\n", i, Py_TYPE(item)->tp_name);
	}
}
