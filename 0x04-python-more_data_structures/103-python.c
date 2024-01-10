#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
void print_python_bytes(PyObject *p)
{
long int len;
int i;
char *trying_str = NULL;
printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}
PyBytes_AsStringAndSize(p, &trying_str, &len);
printf("  size: %li\n", len);
printf("  trying string: %s\n", trying_str);
if (len < 10)
printf("  first %li bytes:", len + 1);
else
printf("  first 10 bytes:");
for (i = 0; i <= len && i < 10; i++)
printf(" %02hhx", trying_str[i]);
printf("\n");
}
void print_python_list(PyObject *p)
{
long int len = PyList_Size(p);
int i;
PyListObject *list = (PyListObject *)p;
const char *type;
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %li\n", len);
printf("[*] Allocated = %li\n", list->allocated);
for (i = 0; i < len; i++)
{
type = (list->ob_item[i])->ob_type->tp_name;
printf("Element %i: %s\n", i, type);
if (!strcmp(type, "bytes"))
print_python_bytes(list->ob_item[i]);
}
}
