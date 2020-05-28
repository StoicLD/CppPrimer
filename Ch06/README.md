# 第六章 函数

## 练习6.1

实参和形参的区别的什么？

## 练习6.2

请指出下列函数哪个有错误，为什么？应该如何修改这些错误呢？

```cpp
(a) int f() {
         string s;
         // ...
         return s;
   }
(b) f2(int i) { /* ... */ }
(c) int calc(int v1, int v1) { /* ... */ }
(d) double square (double x)  return x * x; 
```

## 练习6.3

编写你自己的`fact`函数，上机检查是否正确。注：阶乘。

## 练习6.4

编写一个与用户交互的函数，要求用户输入一个数字，计算生成该数字的阶乘。在main函数中调用该函数。

```cpp
#include <iostream>
#include <string>

int fact(int i)
{
    return i > 1 ? i * fact(i - 1) : 1;
}

void interactive_fact()
{
    std::string const prompt = "Enter a number within [1, 13) :\n";
    std::string const out_of_range = "Out of range, please try again.\n";
    for (int i; std::cout << prompt, std::cin >> i; )
    {
        if (i < 1 || i > 12)
        {
            std::cout << out_of_range; 
            continue;
        }
        std::cout << fact(i) << std::endl;
    }
}

int main()
{
    interactive_fact();
    return 0;
}
```

## 练习6.5

编写一个函数输出其实参的绝对值。

```cpp
#include <iostream>

int abs(int i)
{
   return i > 0 ? i : -i;
}

int main()
{
   std::cout << abs(-5) << std::endl;
   return 0;
}
```

## 练习6.6

说明形参、局部变量以及局部静态变量的区别。编写一个函数，同时达到这三种形式。

## 练习6.7

编写一个函数，当它第一次被调用时返回0，以后每次被调用返回值加1。

## 练习6.8

编写一个名为Chapter6.h 的头文件，令其包含6.1节练习中的函数声明。

## 练习6.9 : fact.cc | factMain.cc

编写你自己的fact.cc 和factMain.cc ，这两个文件都应该包含上一小节的练习中编写的 Chapter6.h 头文件。通过这些文件，理解你的编译器是如何支持分离式编译的。

## 练习6.10

编写一个函数，使用指针形参交换两个整数的值。
在代码中调用该函数并输出交换后的结果，以此验证函数的正确性。

## 练习6.11

编写并验证你自己的reset函数，使其作用于引用类型的参数。注：reset即置0。

## 练习6.12

改写6.2.1节练习中的程序，使其引用而非指针交换两个整数的值。你觉得哪种方法更易于使用呢？为什么？

```cpp
#include <iostream>
#include <string>


void swap(int& lhs, int& rhs)
{
    int temp = lhs;
    lhs = rhs;
    rhs = temp;
}

int main()
{
    for (int left, right; std::cout << "Please Enter:\n", std::cin >> left >> right; )
    {
        swap(left, right);
        std::cout << left << " " << right << std::endl;
    }

    return 0;
}
```

很明显引用更好用。

## 练习6.13

假设`T`是某种类型的名字，说明以下两个函数声明的区别：
一个是`void f(T)`, 另一个是`void f(&T)`。

## 练习6.14

举一个形参应该是引用类型的例子，再举一个形参不能是引用类型的例子。

## 练习6.15

说明`find_char`函数中的三个形参为什么是现在的类型，特别说明为什么`s`是常量引用而`occurs`是普通引用？
为什么`s`和`occurs`是引用类型而`c`不是？
如果令`s`是普通引用会发生什么情况？
如果令`occurs`是常量引用会发生什么情况？

## 练习6.16

下面的这个函数虽然合法，但是不算特别有用。指出它的局限性并设法改善。

```cpp
bool is_empty(string& s) { return s.empty(); }
```

## 练习6.17

编写一个函数，判断`string`对象中是否含有大写字母。
编写另一个函数，把`string`对象全部改写成小写形式。
在这两个函数中你使用的形参类型相同吗？为什么？

## 练习6.18

为下面的函数编写函数声明，从给定的名字中推测函数具备的功能。

- (a) 名为`compare`的函数，返回布尔值，两个参数都是`matrix`类的引用。
- (b) 名为`change_val`的函数，返回`vector`的迭代器，有两个参数：一个是`int`，另一个是`vector`的迭代器。

## 练习6.19

假定有如下声明，判断哪个调用合法、哪个调用不合法。对于不合法的函数调用，说明原因。

```cpp
double calc(double);
int count(const string &, char);
int sum(vector<int>::iterator, vector<int>::iterator, int);
vector<int> vec(10);
(a) calc(23.4, 55.1);
(b) count("abcda",'a');
(c) calc(66);
(d) sum(vec.begin(), vec.end(), 3.8);
```

## 练习6.20

引用形参什么时候应该是常量引用？如果形参应该是常量引用，而我们将其设为了普通引用，会发生什么情况？

## 练习6.21

编写一个函数，令其接受两个参数：一个是`int`型的数，另一个是`int`指针。
函数比较`int`的值和指针所指的值，返回较大的那个。
在该函数中指针的类型应该是什么？

## 练习6.22

编写一个函数，令其交换两个`int`指针。

## 练习6.23

参考本节介绍的几个`print`函数，根据理解编写你自己的版本。
依次调用每个函数使其输入下面定义的`i`和`j`:

```cpp
int i = 0, j[2] = { 0, 1 };
```

## 练习6.24

描述下面这个函数的行为。如果代码中存在问题，请指出并改正。

```cpp
void print(const int ia[10])
{
	for (size_t i = 0; i != 10; ++i)
		cout << ia[i] << endl;
}
```

## 练习6.25

编写一个`main`函数，令其接受两个实参。把实参的内容连接成一个`string`对象并输出出来。

## 练习6.26

编写一个程序，使其接受本节所示的选项；输出传递给`main`函数的实参内容。

## 练习6.27

编写一个函数，它的参数是`initializer_list`类型的对象，函数的功能是计算列表中所有元素的和。

## 练习6.28

在`error_msg`函数的第二个版本中包含`ErrCode`类型的参数，其中循环内的`elem`是什么类型？

## 练习6.29

在范围`for`循环中使用`initializer_list`对象时，应该将循环控制变量声明成引用类型吗？为什么？

## 练习6.30

编译第200页的`str_subrange`函数，看看你的编译器是如何处理函数中的错误的。

## 练习6.31

什么情况下返回的引用无效？什么情况下返回常量的引用无效？

## 练习6.32

下面的函数合法吗？如果合法，说明其功能；如果不合法，修改其中的错误并解释原因。

```cpp
int &get(int *array, int index) { return array[index]; }
int main()
{
    int ia[10];
    for (int i = 0; i != 10; ++i)
        get(ia, i) = i;
}
```

## 练习6.33

编写一个递归函数，输出`vector`对象的内容。

## 练习6.34

如果`factorial`函数的停止条件如下所示，将发生什么？

```cpp
if (val != 0)
```

## 练习6.35

在调用`factorial`函数时，为什么我们传入的值是`val-1`而非`val--`？

## 练习6.36

编写一个函数声明，使其返回数组的引用并且该数组包含10个`string`对象。
不用使用尾置返回类型、`decltype`或者类型别名。

## 练习6.37

为上一题的函数再写三个声明，一个使用类型别名，另一个使用尾置返回类型，最后一个使用`decltype`关键字。
你觉得哪种形式最好？为什么？

## 练习6.38

修改`arrPtr`函数，使其返回数组的引用。

## 练习6.39

说明在下面的每组声明中第二条语句是何含义。
如果有非法的声明，请指出来。

```cpp
(a) int calc(int, int);
	int calc(const int, const int);
(b) int get();
	double get();
(c) int *reset(int *);
	double *reset(double *);
```

## 练习6.40

下面的哪个声明是错误的？为什么？

```cpp
(a) int ff(int a, int b = 0, int c = 0);
(b) char *init(int ht = 24, int wd, char bckgrnd);	
```

## 练习6.41

下面的哪个调用是非法的？为什么？哪个调用虽然合法但显然与程序员的初衷不符？为什么？

```cpp
char *init(int ht, int wd = 80, char bckgrnd = ' ');
(a) init();
(b) init(24,10);
(c) init(14,'*');
```

## 练习6.42

给`make_plural`函数的第二个形参赋予默认实参's', 利用新版本的函数输出单词success和failure的单数和复数形式。

## 练习6.43

你会把下面的哪个声明和定义放在头文件中？哪个放在源文件中？为什么？

```cpp
(a) inline bool eq(const BigInt&, const BigInt&) {...}
(b) void putValues(int *arr, int size);
```

## 练习6.44

将6.2.2节的`isShorter`函数改写成内联函数。

## 练习6.45

回顾在前面的练习中你编写的那些函数，它们应该是内联函数吗？
如果是，将它们改写成内联函数；如果不是，说明原因。

## 练习6.46

能把`isShorter`函数定义成`constexpr`函数吗？
如果能，将它改写成`constxpre`函数；如果不能，说明原因。

## 练习6.47

改写6.3.2节练习中使用递归输出`vector`内容的程序，使其有条件地输出与执行过程有关的信息。
例如，每次调用时输出`vector`对象的大小。
分别在打开和关闭调试器的情况下编译并执行这个程序。

## 练习6.48

说明下面这个循环的含义，它对assert的使用合理吗？

```cpp
string s;
while (cin >> s && s != sought) { } //空函数体
assert(cin);
```

## 练习6.49

什么是候选函数？什么是可行函数？

## 练习6.50

已知有第217页对函数`f`的声明，对于下面的每一个调用列出可行函数。
其中哪个函数是最佳匹配？
如果调用不合法，是因为没有可匹配的函数还是因为调用具有二义性？

```cpp
(a) f(2.56, 42)
(b) f(42)
(c) f(42, 0)
(d) f(2.56, 3.14)
```

## 练习6.51

编写函数`f`的4版本，令其各输出一条可以区分的消息。
验证上一个练习的答案，如果你的回答错了，反复研究本节内容直到你弄清自己错在何处。

## 练习6.52

已知有如下声明：

```cpp
void manip(int ,int);
double dobj;
```

请指出下列调用中每个类型转换的等级。

```cpp
(a) manip('a', 'z');
(b) manip(55.4, dobj);
```

## 练习6.53

说明下列每组声明中的第二条语句会产生什么影响，并指出哪些不合法（如果有的话）。


```cpp
(a) int calc(int&, int&); 
	int calc(const int&, const int&); 
(b) int calc(char*, char*);
	int calc(const char*, const char*);
(c) int calc(char*, char*);
	int calc(char* const, char* const);
```

## 练习6.54

编写函数的声明，令其接受两个`int`形参并返回类型也是`int`；然后声明一个`vector`对象，令其元素是指向该函数的指针。

## 练习6.55

编写4个函数，分别对两个`int`值执行加、减、乘、除运算；在上一题创建的`vector`对象中保存指向这些函数的指针。

## 练习6.56

调用上述`vector`对象中的每个元素并输出结果。

