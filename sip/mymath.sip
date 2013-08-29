// Define the SIP wrapper to the word library.

%Module MyMath

class MyMath {

%TypeHeaderCode
#include "mymath.h"
%End

public:
    int Add(int a, int b);
    int Minus(int a, int b);
};