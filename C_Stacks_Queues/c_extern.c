// Using extern is only for relevance when the program you are building consists of muiltiple source files linked together. The header
// is included by the one source file that defines the variable and by all the source files that reference the variable. For each
// program, one source fles defines the variable. Similary, one header file should declare the variable.

#include "c_extern.h"
#include "c_extern2.h"

int global_variable = 70;

int increment(void) { return global_variable++; }
