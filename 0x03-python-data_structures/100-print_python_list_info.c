#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - a function
 * @p: input
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int size_e, allocated_slots, i;
	PyObject *item;

	size_e = PyList_Size(p);
	allocated_slots = ((PyListObject *)p)->allocated_slots;

	printf("[*] Size of the Python List = %ld\n", size_e);
	printf("[*] Allocated = %ld\n", allocated_slots);

	for (i = 0; i < size_e; ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
