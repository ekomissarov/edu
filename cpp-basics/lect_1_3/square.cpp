int square(int value)
{
    return value * value;
}

// g++ -c square.cpp
//objdump -d square.o
/*

func1.o:     формат файла elf64-x86-64


Дизассемблирование раздела .text:

0000000000000000 <_Z6squarei>:
   0:	55                   	push   %rbp
   1:	48 89 e5             	mov    %rsp,%rbp
   4:	89 7d fc             	mov    %edi,-0x4(%rbp)
   7:	8b 45 fc             	mov    -0x4(%rbp),%eax
   a:	0f af 45 fc          	imul   -0x4(%rbp),%eax
   e:	5d                   	pop    %rbp
   f:	c3                   	retq
----------------------------------------------------------
mangling name: _Z6square

*/

//c++filt _Z6squarei