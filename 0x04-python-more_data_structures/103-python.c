#define PY_SSIZE_T_CLEAN
#include <Python.h>
/**
 * print_python_list - print python list
 * @p: python object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = NULL;
	PyObject *item = NULL;
	Py_ssize_t index, size;

	if (PyList_CheckExact(p))
	{
		list = (PyListObject *)p;
		size = ((PyVarObject *)p)->ob_size;
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %lu\n", size);
		printf("[*] Allocated = %lu\n", list->allocated);
		for (index = 0; index < size; ++index)
		{
			item = list->ob_item[index];
			printf("Element %lu: %s\n", index, item->ob_type->tp_name);
		}
	}
}
/**
 * print_python_bytes - print python bytes
 * @p: python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, end, index;
	PyBytesObject *bytes_obj = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (PyBytes_CheckExact(p))
	{
		size = PyBytes_Size(p);
		printf("  size: %lu\n", size);
		printf("  trying string: %s\n", bytes_obj->ob_sval);
		if (size > 10)
			end = 10;
		else
			end = size + 1;
		printf("first %lu bytes: ", end);
		for (index = 0; index < end; index++)
		{
			printf("%x ", bytes_obj->ob_sval[index]);
		}
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}
