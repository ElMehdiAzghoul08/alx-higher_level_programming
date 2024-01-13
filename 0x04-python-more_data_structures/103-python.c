#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - a function
 * @p: input
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size_, i;
	char *str_;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size_ = PyBytes_Size(p);
	str_ = PyBytes_AsString(p);

	printf("  size: %ld\n", size_);
	printf("  trying string: %s\n", str_);

	printf("  first 10 bytes: ");
	for (i = 0; i < size_ && i < 10; ++i)
	{
		printf("%02x", (unsigned char)str_[i]);
		if (i < size_ - 1 && i < 9)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_list - a function
 * @p: input
 * Return: input
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size_, i;
	PyObject *item_;

	printf("[*] Python list info\n");

	size_ = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size_);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size_; ++i)
	{
		item_ = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item_)->tp_name);

		if (PyBytes_Check(item_))
			print_python_bytes(item_);
	}
}
