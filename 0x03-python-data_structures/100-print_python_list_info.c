#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - a function
 * @p: input
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated_slots, i;
	PyObject *item;

	size = PyList_Size(p);
	allocated_slots = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated_slots);

	for (i = 0; i < size; ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
