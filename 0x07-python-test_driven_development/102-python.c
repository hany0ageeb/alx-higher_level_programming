#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <locale.h>

/**
 * print_data - print data
 * @data: pointer to data
 * @length: length
 * @kind: kind
 */
void print_data(void *data, Py_ssize_t length, int kind)
{
	printf("  value: ");
	for (Py_ssize_t i = 0; i < length; ++i)
	{
		printf("%lc", PyUnicode_READ(kind, data, i));
	}
	printf("\n");
}
/**
 * print_python_string -  function that prints Python strings.
 * @p: python string
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	void *data = NULL;

	printf("[.] string object info\n");
	if (p == NULL || strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
	}
	else
	{
		length = PyUnicode_GET_LENGTH(p);
		if (PyUnicode_IS_ASCII(p))
		{
			printf("  type: %s\n", "compact ascii");
		}
		else if (PyUnicode_IS_COMPACT(p))
		{
			printf("  type: %s\n", "compact unicode object");
		}
		else if (PyUnicode_IS_COMPACT_ASCII(p))
		{
			printf("  type: %s\n", "compact ascii");
		}
		printf("  length: %lu\n", length);
		setlocale(LC_ALL, "");
		data = PyUnicode_DATA(p);
		print_data(data, length, PyUnicode_KIND(p));
	}
}
