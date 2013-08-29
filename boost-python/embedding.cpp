// Building:
// g++ -I /usr/local/Cellar/python/2.7.3/Frameworks/Python.framework/Versions/2.7/include/python2.7 -lpython2.7 embedding.cpp
// Run:
// ./a.out

#include <Python.h>

int main(int argc, char *argv[])
{
  Py_Initialize();
  PyRun_SimpleString("from time import time,ctime\n"
                     "print 'Today is',ctime(time())\n");
  Py_Finalize();

  return 0;
}
