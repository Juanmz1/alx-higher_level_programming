#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - Print information about python
 * @p: PyObject
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	PyObject *items;
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size, alloca;
	int i = 0;

	if Pylist_CheckExact(p)
	{
		size = PyList_SIZE(p);
		alloca = list->allocated;
		
		printf("[*]size of python list: %li\n", size);
		printf("[*]numberv allocated: %li\n", alloca);
		
		for (i = 0; i < size; i++)
		{
			items = PyList_GetItem(p, i);
			printf("Element with index: %d: %s\n", i, Py_TYPE(items)->tp_name);
		}
	}
}
