#define PY_SSIZE_T_CLEAN
#include <Python.h>
void print_python_float(PyObject *p)
{
	PyFloatObject *float_obj = NULL;
	printf("[.] float object info\n");
	if (PyFloat_CheckExact(p))
	{
		float_obj = (PyFloatObject *)p;
		printf("  value: %.17g\n", float_obj->ob_fval);
	}
	else
	{
		printf("  [ERROR] Invalid Float Object\n");
	}
}
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, end, index;
	PyBytesObject *bytes_obj = NULL;

	printf("[.] bytes object info\n");
	if (PyBytes_CheckExact(p))
	{
		bytes_obj = (PyBytesObject *)p;
		size = PyBytes_Size(p);
		printf("  size: %lu\n", size);
		printf("  trying string: %s\n", bytes_obj->ob_sval);
		if (size > 10)
			end = 10;
		else
			end = size + 1;
		printf("  first %lu bytes: ", end);
		for (index = 0; index < end; index++)
		{
			if (index < end - 1)
				printf("%02x ", bytes_obj->ob_sval[index]);
			else
				printf("%02x\n", bytes_obj->ob_sval[index]);
		}
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}
void print_python_list(__attribute__((unused))PyObject *p)
{
	PyListObject *list = NULL;
	PyObject *item = NULL;
	Py_ssize_t index, size;

	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		list = (PyListObject *)p;
		size = ((PyVarObject *)p)->ob_size;
		printf("[*] Size of the Python List = %lu\n", size);
		printf("[*] Allocated = %lu\n", list->allocated);
		for (index = 0; index < size; ++index)
		{
			item = list->ob_item[index];
			printf("Element %lu: %s\n", index, item->ob_type->tp_name);
			if (strcmp(item->ob_type->tp_name, "bytes") == 0)
				print_python_bytes(item);
			else if (strcmp(item->ob_type->tp_name, "str") == 0)
				print_python_bytes(item);
			else if (strcmp(item->ob_type->tp_name, "float") == 0)
				print_python_float(item);
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
	}
}
