/*Static and Dynamic libraries. When a C Program is compiled, the compiler genarates object code. Then invokes the linker. One of the 
functions of the linker is to make code of library functions. (eg printf(), scanf() ) available to your program. A linker can accomplish
this task in two ways, by copying the code of a library function to your object code or making some arrangements so that the complete 
code of the library functions is not copied but made available at run time*/

// Static Linking and Static Libraries

/*This is the result of the linker making copy of all used library funtions to the executable file. Static linking creates a larger bi
nary files and need more space on disk and main memory. Examples of static libraries which are statically linked are, .a(files in linux),
.lib(files in windows)*/

// Steps in creating a static library for UNIX or UNIX like OS

#include <stdio.h>
#include "dynamic.h"

void fun(void)
{
printf("fun() called from a static library");
}

// We first create a the above file then compile. Then create a header file. <filename.h>

// After compiling create a static library. This step is to bundle multiple object files in one static library. The command used is
// ar rcs <filename.a> <filename.o> The output of this step is static library. Now after this our static library is ready to use. We can
// copy <filename.a> somewhere else to use it. Let us create a driver program.
