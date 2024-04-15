#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_bytes - a function
 * @p: input
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	long int size_;
	int i;
	char *_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &_str, &size_);

	printf("  size: %li\n", size_);
	printf("  trying string: %s\n", _str);
	if (size_ < 10)
		printf("  first %li bytes:", size_ + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= size_ && i < 10; i++)
		printf(" %02hhx", _str[i]);
	printf("\n");
}
/**
 * print_python_list - a function
 * @p: input
 * Return: input
 */
void print_python_list(PyObject *p)
{
	long int size_ = PyList_Size(p);
	int i;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size_);
	printf("[*] Allocated = %li\n", list->allocated);
	for (i = 0; i < size_; i++)
	{
		type = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[i]);
	}
}
