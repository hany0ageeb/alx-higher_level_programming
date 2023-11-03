#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: a pointer to PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;
	PyListObject *lst;

	if (PyList_CheckExact(p))
	{
		size = PyList_Size(p);
		printf("[*] Size of the Python List = %lu\n", size);
		lst = (PyListObject *)p;
		printf("[*] Allocated = %lu\n", lst->allocated);
		for (i = 0; i < size; ++i)
		{
			item = PyList_GetItem(p, i);
			printf("Element %lu: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
}
