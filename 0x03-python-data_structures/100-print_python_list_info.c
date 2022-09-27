#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - function, prints some basic info about python list
 * @p: PyObject
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int j;
	PyObject *v;
	PyListObject *list;
	Py_ssize_t len;

	if (PyList_Check(p))
		list = (PyListObject *)(p);

	len = PyList_Size(p);

	printf("[*] Size of the Python List = %zu\n", len);
	printf("[*] Allocated = %zu\n", list->allocated);

	for (j = 0; j < len; j++)
	{
	  v = PyList_GET_ITEM(p, j);
	printf("Element %d: %s\n", j, (v->ob_type)->tp_name);
	}
}
