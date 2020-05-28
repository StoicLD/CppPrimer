# 第二章 变量和基本类型 

## 练习2.1

类型 int、long、long long 和 short 的区别是什么？无符号类型和带符号类型的区别是什么？float 和 double的区别是什么？

## 练习2.2

计算按揭贷款时，对于利率、本金和付款分别应选择何种数据类型？说明你的理由。

## 练习2.3

读程序写结果。

```cpp
unsigned u = 10, u2 = 42;
std::cout << u2 - u << std::endl;
std::cout << u - u2 << std::endl;
int i = 10, i2 = 42;
std::cout << i2 - i << std::endl;
std::cout << i - i2 << std::endl;
std::cout << i - u << std::endl;
std::cout << u - i << std::endl;
```

## 练习2.4

编写程序检查你的估计是否正确，如果不正确，请仔细研读本节直到弄明白问题所在。

## 练习2.5

指出下述字面值的数据类型并说明每一组内几种字面值的区别：

```
(a) 'a', L'a', "a", L"a"
(b) 10, 10u, 10L, 10uL, 012, 0xC
(c) 3.14, 3.14f, 3.14L
(d) 10, 10u, 10., 10e-2
```

## 练习2.6

下面两组定义是否有区别，如果有，请叙述之：

```cpp
int month = 9, day = 7;
int month = 09, day = 07;
```

## 练习2.7

下述字面值表示何种含义？它们各自的数据类型是什么？

```cpp
(a) "Who goes with F\145rgus?\012"
(b) 3.14e1L
(c) 1024f
(d) 3.14L
```

## 练习2.8

请利用转义序列编写一段程序，要求先输出 2M，然后转到新一行。修改程序使其先输出 2，然后输出制表符，再输出 M，最后转到新一行。

## 练习2.9

解释下列定义的含义，对于非法的定义，请说明错在何处并将其改正。

- (a) std::cin >> int input_value;
- (b) int i = { 3.14 };
- (c) double salary = wage = 9999.99;
- (d) int i = 3.14;

## 练习2.10

下列变量的初值分别是什么？

```cpp
std::string global_str;
int global_int;
int main()
{
    int local_int;
    std::string local_str;
}
```

## 练习2.11

指出下面的语句是声明还是定义：

- (a) extern int ix = 1024;
- (b) int iy;
- (c) extern int iz;

## 练习2.12

请指出下面的名字中哪些是非法的？

- (a) int double = 3.14;
- (b) int _;
- (c) int catch-22;
- (d) int 1_or_2 = 1;
- (e) double Double = 3.14;

## 练习2.13

下面程序中`j`的值是多少？

```cpp
int i = 42;
int main()
{
    int i = 100;
    int j = i;
}
```

## 练习2.14

下面的程序合法吗？如果合法，它将输出什么？

```cpp
int i = 100, sum = 0;
for (int i = 0; i != 10; ++i)
    sum += i;
std::cout << i << " " << sum << std::endl;
```

## 练习2.15

下面的哪个定义是不合法的？为什么？

- (a) int ival = 1.01;
- (b) int &rval1 = 1.01;
- (c) int &rval2 = ival;
- (d) int &rval3;

## 练习2.16

考察下面的所有赋值然后回答：哪些赋值是不合法的？为什么？哪些赋值是合法的？它们执行了哪些操作？

```cpp
int i = 0, &r1 = i; 
double d = 0, &r2 = d;
```

- (a) r2 = 3.14159;
- (b) r2 = r1;
- (c) i = r2;
- (d) r1 = d;

## 练习2.17

执行下面的代码段将输出什么结果？

```cpp
int i, &ri = i;
i = 5; ri = 10;
std::cout << i << " " << ri << std::endl;
```

## 练习2.18

编写代码分别改变指针的值以及指针所指对象的值。

## 练习2.19

说明指针和引用的主要区别

## 练习2.20

请叙述下面这段代码的作用。

```cpp
int i = 42;
int *p1 = &i; 
*p1 = *p1 * *p1;
```

## 练习2.21

请解释下述定义。在这些定义中有非法的吗？如果有，为什么？

`int i = 0;`

- (a) double* dp = &i;
- (b) int *ip = i;
- (c) int *p = &i;

## 练习2.22

假设 p 是一个 int 型指针，请说明下述代码的含义。

```cpp
if (p) // ...
if (*p) // ...
```

## 练习2.23

给定指针 p，你能知道它是否指向了一个合法的对象吗？如果能，叙述判断的思路；如果不能，也请说明原因。

## 练习2.24

在下面这段代码中为什么 p 合法而 lp 非法？

```cpp
int i = 42;
void *p = &i;
long *lp = &i;
```

## 练习2.25

说明下列变量的类型和值。

```cpp
(a) int* ip, i, &r = i;
(b) int i, *ip = 0;
(c) int* ip, ip2;
```

## 练习2.26

下面哪些语句是合法的？如果不合法，请说明为什么？

## 练习2.27

下面的哪些初始化是合法的？请说明原因。

## 练习2.28

说明下面的这些定义是什么意思，挑出其中不合法的。

## 练习2.29

假设已有上一个练习中定义的那些变量，则下面的哪些语句是合法的？请说明原因。

## 练习2.30

对于下面的这些语句，请说明对象被声明成了顶层const还是底层const？

```cpp
const int v2 = 0; int v1 = v2;
int *p1 = &v1, &r1 = v1;
const int *p2 = &v2, *const p3 = &i, &r2 = v2;
```

## 练习2.31

假设已有上一个练习中所做的那些声明，则下面的哪些语句是合法的？请说明顶层const和底层const在每个例子中有何体现。

## 练习2.32

下面的代码是否合法？如果非法，请设法将其修改正确。

```cpp
int null = 0, *p = null;
```

## 练习2.33

利用本节定义的变量，判断下列语句的运行结果。

## 练习2.34

基于上一个练习中的变量和语句编写一段程序，输出赋值前后变量的内容，你刚才的推断正确吗？如果不对，请反复研读本节的示例直到你明白错在何处为止。

## 练习2.35

判断下列定义推断出的类型是什么，然后编写程序进行验证。

```cpp
const int i = 42;
auto j = i; const auto &k = i; auto *p = &i; 
const auto j2 = i, &k2 = i;
```

## 练习2.36

关于下面的代码，请指出每一个变量的类型以及程序结束时它们各自的值。

```cpp
int a = 3, b = 4;
decltype(a) c = a;
decltype((b)) d = a;
++c;
++d;
```

## 练习2.37

赋值是会产生引用的一类典型表达式，引用的类型就是左值的类型。也就是说，如果 i 是 int，则表达式 i=x 的类型是 int&。根据这一特点，请指出下面的代码中每一个变量的类型和值。

```cpp
int a = 3, b = 4;
decltype(a) c = a;
decltype(a = b) d = a;
```

## 练习2.38

说明由decltype 指定类型和由auto指定类型有何区别。请举一个例子，decltype指定的类型与auto指定的类型一样；再举一个例子，decltype指定的类型与auto指定的类型不一样。

## 练习2.39

编译下面的程序观察其运行结果，注意，如果忘记写类定义体后面的分号会发生什么情况？记录下相关的信息，以后可能会有用。

```cpp
struct Foo { /* 此处为空  */ } // 注意：没有分号
int main()
{
    return 0;
}。
```

## 练习2.40

根据自己的理解写出 Sales_data 类，最好与书中的例子有所区别。

```cpp
struct Sale_data
{
    std::string bookNo;
    std::string bookName;
    unsigned units_sold = 0;
    double revenue = 0.0;
    double price = 0.0;
    //...
}
```

## 练习2.41

使用你自己的Sale_data类重写1.5.1节（第20页）、1.5.2节（第21页）和1.6节（第22页）的练习。眼下先把Sales_data类的定义和main函数放在一个文件里。

```cpp
// 1.5.1

#include <iostream>
#include <string>

struct Sale_data
{
    std::string bookNo;
    unsigned units_sold = 0;
    double revenue = 0.0;
};

int main()
{
    Sale_data book;
    double price;
    std::cin >> book.bookNo >> book.units_sold >> price;
    book.revenue = book.units_sold * price;
    std::cout << book.bookNo << " " << book.units_sold << " " << book.revenue << " " << price;

    return 0;
}

```

```cpp
// 1.5.2

#include <iostream>
#include <string>

struct Sale_data
{
    std::string bookNo;
    unsigned units_sold = 0;
    double revenue = 0.0;
};

int main()
{
    Sale_data book1, book2;
    double price1, price2;
    std::cin >> book1.bookNo >> book1.units_sold >> price1;
    std::cin >> book2.bookNo >> book2.units_sold >> price2;
    book1.revenue = book1.units_sold * price1;
    book2.revenue = book2.units_sold * price2;

    if (book1.bookNo == book2.bookNo)
    {
        unsigned totalCnt = book1.units_sold + book2.units_sold;
        double totalRevenue = book1.revenue + book2.revenue;
        std::cout << book1.bookNo << " " << totalCnt << " " << totalRevenue << " ";
        if (totalCnt != 0)
            std::cout << totalRevenue / totalCnt << std::endl;
        else
            std::cout << "(no sales)" << std::endl;
        return 0;
    }
    else
    {
        std::cerr << "Data must refer to same ISBN" << std::endl;
        return -1;  // indicate failure
    }
}

```

```cpp
// 1.6

#include <iostream>
#include <string>

struct Sale_data
{
    std::string bookNo;
    unsigned units_sold = 0;
    double revenue = 0.0;
};

int main()
{
    Sale_data total;
    double totalPrice;
    if (std::cin >> total.bookNo >> total.units_sold >> totalPrice)
    {
        total.revenue = total.units_sold * totalPrice;

        Sale_data trans;
        double transPrice;
        while (std::cin >> trans.bookNo >> trans.units_sold >> transPrice)
        {
            trans.revenue = trans.units_sold * transPrice;

            if (total.bookNo == trans.bookNo)
            {
                total.units_sold += trans.units_sold;
                total.revenue += trans.revenue;
            }
            else
            {
                std::cout << total.bookNo << " " << total.units_sold << " " << total.revenue << " ";
                if (total.units_sold != 0)
                    std::cout << total.revenue / total.units_sold << std::endl;
                else
                    std::cout << "(no sales)" << std::endl;

                total.bookNo = trans.bookNo;
                total.units_sold = trans.units_sold;
                total.revenue = trans.revenue;
            }
        }

        std::cout << total.bookNo << " " << total.units_sold << " " << total.revenue << " ";
        if (total.units_sold != 0)
            std::cout << total.revenue / total.units_sold << std::endl;
        else
            std::cout << "(no sales)" << std::endl;

        return 0;
    }
    else
    {
        std::cerr << "No data?!" << std::endl;
        return -1;  // indicate failure
    }
}
```

## 练习2.42

根据你自己的理解重写一个Sales_data.h头文件，并以此为基础重做2.6.2节（第67页）的练习。



