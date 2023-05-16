#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - Print information about python
 * @p: PyObject
 * Return: nothing
 */
void print_python_list_info(PyObject *p);
{
	PyObject *items;
	PyListObject *list = (PyListObject *)p;
	int size, alloca, i;

	size = Py_SIZE(p);
	alloca = list->allocated;

	printf("size of python list: %d\n", size);
	printf("numberv allocated: %d\n", alloca);

	for (i = 0; i < size; i++)
	{
		items = PyList_getItem(p, i);
		printf("Element with index: %d: %s\n", i, Py_TYPE(items)->tp_name);
	}
}
