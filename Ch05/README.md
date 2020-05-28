# 第五章 语句

## 练习5.1

什么是空语句？什么时候会用到空语句？

## 练习5.2

什么是块？什么时候会用到块？

## 练习5.3

使用逗号运算符重写1.4.1节的`while`循环，使它不再需要块，观察改写之后的代码可读性提高了还是降低了。

```cpp
while (val <= 10)
    sum += val, ++val;
```

代码的可读性反而降低了。

## 练习5.4

说明下列例子的含义，如果存在问题，试着修改它。

```cpp
(a) while (string::iterator iter != s.end()) { /* . . . */ }

(b) while (bool status = find(word)) { /* . . . */ }
		if (!status) { /* . . . */ }
```

## 练习5.5

写一段自己的程序，使用`if else`语句实现把数字转换为字母成绩的要求。

```cpp
#include <iostream>
#include <vector>
#include <string>
using std::vector; using std::string; using std::cout; using std::endl; using std::cin;

int main()
{
    vector<string> scores = { "F", "D", "C", "B", "A", "A++" };
    for (int g; cin >> g;)
    {
        string letter;
        if (g < 60)
        {
            letter = scores[0];
        }
        else
        {
            letter = scores[(g - 50) / 10];
            if (g != 100)
                letter += g % 10 > 7 ? "+" : g % 10 < 3 ? "-" : "";
        }
        cout << letter << endl;
    }

    return 0;
}
```

## 练习5.6

改写上一题的程序，使用条件运算符代替`if else`语句。

```cpp
#include <iostream>
#include <vector>
#include <string>
using std::vector; using std::string; using std::cout; using std::endl; using std::cin;

int main()
{
    vector<string> scores = { "F", "D", "C", "B", "A", "A++" };

    int grade = 0;
    while (cin >> grade)
    {
        string lettergrade = grade < 60 ? scores[0] : scores[(grade - 50) / 10];
        lettergrade += (grade == 100 || grade < 60) ? "" : (grade % 10 > 7) ? "+" : (grade % 10 < 3) ? "-" : "";
        cout << lettergrade << endl;
    }

    return 0;
}
```

## 练习5.7

改写下列代码段中的错误。

```cpp
(a) if (ival1 != ival2) 
		ival1 = ival2
    else 
    	ival1 = ival2 = 0;
(b) if (ival < minval) 
		minval = ival;
    	occurs = 1;
(c) if (int ival = get_value())
    	cout << "ival = " << ival << endl;
    if (!ival)
    	cout << "ival = 0\n";
(d) if (ival = 0)
    	ival = get_value();
```

## 练习5.8

什么是“悬垂else”？C++语言是如何处理else子句的？

## 练习5.9

编写一段程序，使用一系列`if`语句统计从`cin`读入的文本中有多少元音字母。

## 练习5.10

我们之前实现的统计元音字母的程序存在一个问题：如果元音字母以大写形式出现，不会被统计在内。编写一段程序，既统计元音字母的小写形式，也统计元音字母的大写形式，也就是说，新程序遇到'a'和'A'都应该递增`aCnt`的值，以此类推。

## 练习5.11

修改统计元音字母的程序，使其也能统计空格、制表符、和换行符的数量。

## 练习5.12

修改统计元音字母的程序，使其能统计含以下两个字符的字符序列的数量：`ff`、`fl`和`fi`。

## 练习5.13

下面显示的每个程序都含有一个常见的编码错误，指出错误在哪里，然后修改它们。

```cpp
(a) unsigned aCnt = 0, eCnt = 0, iouCnt = 0;
    char ch = next_text();
    switch (ch) {
        case 'a': aCnt++;
        case 'e': eCnt++;
        default: iouCnt++;
    }
(b) unsigned index = some_value();
    switch (index) {
        case 1:
            int ix = get_value();
            ivec[ ix ] = index;
            break;
        default:
            ix = ivec.size()-1;
            ivec[ ix ] = index;
    }
(c) unsigned evenCnt = 0, oddCnt = 0;
    int digit = get_num() % 10;
    switch (digit) {
        case 1, 3, 5, 7, 9:
            oddcnt++;
            break;
        case 2, 4, 6, 8, 10:
            evencnt++;
            break;
    }
(d) unsigned ival=512, jval=1024, kval=4096;
    unsigned bufsize;
    unsigned swt = get_bufCnt();
    switch(swt) {
        case ival:
            bufsize = ival * sizeof(int);
            break;
        case jval:
            bufsize = jval * sizeof(int);
            break;
        case kval:
            bufsize = kval * sizeof(int);
            break;
    }
```

## 练习5.14

编写一段程序，从标准输入中读取若干`string`对象并查找连续重复出现的单词，所谓连续重复出现的意思是：一个单词后面紧跟着这个单词本身。要求记录连续重复出现的最大次数以及对应的单词。如果这样的单词存在，输出重复出现的最大次数；如果不存在，输出一条信息说明任何单词都没有连续出现过。
例如：如果输入是：

```
how now now now brown cow cow
```

那么输出应该表明单词now连续出现了3次。

## 练习5.15

说明下列循环的含义并改正其中的错误。

```cpp
(a) for (int ix = 0; ix != sz; ++ix) { /* ... */ }
    if (ix != sz)
    	// . . .
(b) int ix;
    for (ix != sz; ++ix) { /* ... */ }
(c) for (int ix = 0; ix != sz; ++ix, ++sz) { /*...*/ }
```

## 练习5.16

`while`循环特别适用于那种条件不变、反复执行操作的情况，例如，当未达到文件末尾时不断读取下一个值。
`for`循环更像是在按步骤迭代，它的索引值在某个范围内一次变化。根据每种循环的习惯各自编写一段程序，然后分别用另一种循环改写。
如果只能使用一种循环，你倾向于哪种？为什么？

## 练习5.17

假设有两个包含整数的`vector`对象，编写一段程序，检验其中一个`vector`对象是否是另一个的前缀。
为了实现这一目标，对于两个不等长的`vector`对象，只需挑出长度较短的那个，把它的所有元素和另一个`vector`对象比较即可。
例如，如果两个`vector`对象的元素分别是0、1、1、2 和 0、1、1、2、3、5、8，则程序的返回结果为真。

## 练习5.18

说明下列循环的含义并改正其中的错误。

```cpp
(a) do { // 应该添加花括号
        int v1, v2;
        cout << "Please enter two numbers to sum:" ;
        if (cin >> v1 >> v2)
            cout << "Sum is: " << v1 + v2 << endl;
    }while (cin);
(b) int ival;
    do {
        // . . .
    } while (ival = get_response()); // 应该将ival 定义在循环外
(c) int ival = get_response();
    do {
        ival = get_response();
    } while (ival); // 应该将ival 定义在循环外
```

## 练习5.19

编写一段程序，使用`do while`循环重复地执行下述任务：
首先提示用户输入两个`string`对象，然后挑出较短的那个并输出它。

## 练习5.20

编写一段程序，从标准输入中读取`string`对象的序列直到连续出现两个相同的单词或者所有的单词都读完为止。
使用`while`循环一次读取一个单词，当一个单词连续出现两次时使用`break`语句终止循环。
输出连续重复出现的单词，或者输出一个消息说明没有任何单词是连续重复出现的。

## 练习5.21

修改5.5.1节练习题的程序，使其找到的重复单词必须以大写字母开头。

## 练习5.22

本节的最后一个例子跳回到`begin`，其实使用循环能更好的完成该任务，重写这段代码，注意不再使用`goto`语句。

```cpp
// 向后跳过一个带初始化的变量定义是合法的
begin:
    int sz = get_size();
    if (sz <= 0) {
        goto begin;
    }
```

## 练习5.23

编写一段程序，从标准输入读取两个整数，输出第一个数除以第二个数的结果。

## 练习5.24

修改你的程序，使得当第二个数是0时抛出异常。先不要设定`catch`子句，运行程序并真的为除数输入0，看看会发生什么？

## 练习5.25

修改上一题的程序，使用`try`语句块去捕获异常。`catch`子句应该为用户输出一条提示信息，询问其是否输入新数并重新执行`try`语句块的内容。

