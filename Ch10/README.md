# 第十章 泛型算法

## 练习10.1

> 头文件`algorithm`中定义了一个名为`count`的函数，它类似`find`， 接受一对迭代器和一个值作为参数。`count`返回给定值在序列中出现的次数。编写程序，读取`int`序列存入`vector`中，打印有多少个元素的值等于给定值。

## 练习10.2

> 重做上一题，但读取 `string` 序列存入 `list` 中。

## 练习10.3

> 用 `accumulate`求一个 `vector<int>` 中元素之和。

## 练习10.4

> 假定 `v` 是一个`vector<double>`，那么调用 `accumulate(v.cbegin(),v.cend(),0)` 有何错误（如果存在的话）？

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

int main()
{
    // Exercise 10.3
    std::vector<int> v = { 1, 2, 3, 4 };
    std::cout << "ex 10.03: " << std::accumulate(v.cbegin(), v.cend(), 0) << std::endl;

    // Exercise 10.4
    std::vector<double> vd = { 1.1, 0.5, 3.3 };
    std::cout   << "ex 10.04: "
                << std::accumulate(vd.cbegin(), vd.cend(), 0)
                << std::endl;                        //   ^<-- note here.
    // @attention
    //
    // The ouput is 4 rather than 4.9 as expected.
    // The reason is std::accumulate is a template function. The third parameter is _Tp __init
    // When "0" , an integer, had been specified here, the compiler deduced _Tp as
    // interger.As a result , when the following statments were being excuted :
    //  for (; __first != __last; ++__first)
    //	__init = __init + *__first;
    //  return __init;
    // all calculation would be converted to integer.

    return 0;
}
```

结果会是 `int` 类型。

## 练习10.5

> 在本节对名册（`roster`）调用`equal`的例子中，如果两个名册中保存的都是C风格字符串而不是`string`，会发生什么？

C风格字符串是用指向字符的指针表示的，因此会比较两个指针的值（地址），而不会比较这两个字符串的内容。

## 练习10.6

> 编写程序，使用 `fill_n` 将一个序列中的 `int` 值都设置为0。

## 练习10.7

> 下面程序是否有错误？如果有，请改正：

```cpp
(a) vector<int> vec; list<int> lst; int i;
	while (cin >> i)
		lst.push_back(i);
	copy(lst.cbegin(), lst.cend(), vec.begin());
(b) vector<int> vec;
	vec.reserve(10);
	fill_n(vec.begin(), 10, 0);
```

## 练习10.8

> 本节提到过，标准库算法不会改变它们所操作的容器的大小。为什么使用 `back_inserter`不会使这一断言失效？

`back_inserter` 是插入迭代器，在 `iterator.h` 头文件中，不是标准库的算法。

## 练习10.9

> 实现你自己的`elimDups`。分别在读取输入后、调用`unique`后以及调用`erase`后打印`vector`的内容。

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

// print containers like vector, deque, list, etc.
template<typename Sequence>
auto println(Sequence const& seq) -> std::ostream&
{
    for (auto const& elem : seq) 
        std::cout << elem << " ";
    return std::cout << std::endl;
}

auto eliminate_duplicates(std::vector<std::string> &vs) -> std::vector<std::string>&
{
    std::sort(vs.begin(), vs.end());
    println(vs);

    auto new_end = std::unique(vs.begin(), vs.end());
    println(vs);

    vs.erase(new_end, vs.end());
    return vs;
}

int main()
{
    std::vector<std::string> vs{ "a", "v", "a", "s", "v", "a", "a" };
    println(vs);
    println(eliminate_duplicates(vs));

    return 0;
}
```

## 练习10.10

> 你认为算法不改变容器大小的原因是什么？

## 练习10.11

> 编写程序，使用 `stable_sort` 和 `isShorter` 将传递给你的 `elimDups` 版本的 `vector` 排序。打印 `vector`的内容，验证你的程序的正确性。

## 练习10.12

> 编写名为 `compareIsbn` 的函数，比较两个 `Sales_data` 对象的`isbn()` 成员。使用这个函数排序一个保存 `Sales_data` 对象的 `vector`。

## 练习10.13

> 标准库定义了名为 `partition` 的算法，它接受一个谓词，对容器内容进行划分，使得谓词为`true` 的值会排在容器的前半部分，而使得谓词为 `false` 的值会排在后半部分。算法返回一个迭代器，指向最后一个使谓词为 `true` 的元素之后的位置。编写函数，接受一个 `string`，返回一个 `bool` 值，指出 `string` 是否有5个或更多字符。使用此函数划分 `words`。打印出长度大于等于5的元素。

## 练习10.14

> 编写一个`lambda`，接受两个`int`，返回它们的和。

```cpp
auto f = [](int i, int j) { return i + j; };
```

## 练习10.15

> 编写一个 `lambda` ，捕获它所在函数的 `int`，并接受一个 `int`参数。`lambda` 应该返回捕获的 `int` 和 `int` 参数的和。

## 练习10.16

> 使用 `lambda` 编写你自己版本的 `biggies`。

## 练习10.17

> 重写10.3.1节练习10.12的程序，在对`sort`的调用中使用 `lambda` 来代替函数 `compareIsbn`。

## 练习10.18

> 重写 `biggies`，用 `partition` 代替 `find_if`。我们在10.3.1节练习10.13中介绍了 `partition` 算法。

## 练习10.19

> 用 `stable_partition` 重写前一题的程序，与 `stable_sort` 类似，在划分后的序列中维持原有元素的顺序。

## 练习10.20

> 标准库定义了一个名为 `count_if` 的算法。类似 `find_if`，此函数接受一对迭代器，表示一个输入范围，还接受一个谓词，会对输入范围中每个元素执行。`count_if`返回一个计数值，表示谓词有多少次为真。使用`count_if`重写我们程序中统计有多少单词长度超过6的部分。

## 练习10.21

> 编写一个 `lambda`，捕获一个局部 `int` 变量，并递减变量值，直至它变为0。一旦变量变为0，再调用`lambda`应该不再递减变量。`lambda`应该返回一个`bool`值，指出捕获的变量是否为0。

## 练习10.22

> 重写统计长度小于等于6的单词数量的程序，使用函数代替`lambda`。

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>

using std::string;
using namespace std::placeholders;

bool isLesserThanOrEqualTo6(const string &s, string::size_type sz)
{
    return s.size() <= sz;
}

int main()
{
    std::vector<string> authors{ "Mooophy", "pezy", "Queequeg90", "shbling", "evan617" };
    std::cout << count_if(authors.cbegin(), authors.cend(), bind(isLesserThanOrEqualTo6, _1, 6));
}
```

## 练习10.23

> `bind` 接受几个参数？

假设被绑定的函数接受 `n` 个参数，那么`bind` 接受`n + 1`个参数。

## 练习10.24

> 给定一个`string`，使用 `bind` 和 `check_size` 在一个 `int` 的`vector` 中查找第一个大于`string`长度的值。

## 练习10.25

> 在10.3.2节的练习中，编写了一个使用`partition` 的`biggies`版本。使用 `check_size` 和 `bind` 重写此函数。

## 练习10.26

> 解释三种插入迭代器的不同之处。

## 练习10.27

> 除了 `unique` 之外，标准库还定义了名为 `unique_copy` 的函数，它接受第三个迭代器，表示拷贝不重复元素的目的位置。编写一个程序，使用 `unique_copy`将一个`vector`中不重复的元素拷贝到一个初始化为空的`list`中。

## 练习10.28

> 一个`vector` 中保存 1 到 9，将其拷贝到三个其他容器中。分别使用`inserter`、`back_inserter` 和 `front_inserter` 将元素添加到三个容器中。对每种 `inserter`，估计输出序列是怎样的，运行程序验证你的估计是否正确。

## 练习10.29

> 编写程序，使用流迭代器读取一个文本文件，存入一个`vector`中的`string`里。

## 练习10.30

> 使用流迭代器、`sort` 和 `copy` 从标准输入读取一个整数序列，将其排序，并将结果写到标准输出。

## 练习10.31

> 修改前一题的程序，使其只打印不重复的元素。你的程序应该使用 `unique_copy`。

## 练习10.32

> 重写1.6节中的书店程序，使用一个`vector`保存交易记录，使用不同算法完成处理。使用 `sort` 和10.3.1节中的 `compareIsbn` 函数来排序交易记录，然后使用 `find` 和 `accumulate` 求和。

## 练习10.33

> 编写程序，接受三个参数：一个输入文件和两个输出文件的文件名。输入文件保存的应该是整数。使用 `istream_iterator` 读取输入文件。使用 `ostream_iterator` 将奇数写入第一个输入文件，每个值后面都跟一个空格。将偶数写入第二个输出文件，每个值都独占一行。

## 练习10.34

> 使用 `reverse_iterator` 逆序打印一个`vector`。

## 练习10.35

> 使用普通迭代器逆序打印一个`vector`。

## 练习10.36

> 使用 `find` 在一个 `int` 的`list` 中查找最后一个值为0的元素。

## 练习10.37

> 给定一个包含10 个元素的`vector`，将位置3到7之间的元素按逆序拷贝到一个`list`中。

## 练习10.38

> 列出5个迭代器类别，以及每类迭代器所支持的操作。

* 输入迭代器 : `==`,`!=`,`++`,`*`,`->`
* 输出迭代器 : `++`,`*`
* 前向迭代器 : `==`,`!=`,`++`,`*`,`->`
* 双向迭代器 : `==`,`!=`,`++`,`--`,`*`,`->`
* 随机访问迭代器 : `==`,`!=`,`<`,`<=`,`>`,`>=`,`++`,`--`,`+`,`+=`,`-`,`-=`,`*`,`->`,`iter[n]`==`*(iter[n])`

## 练习10.39

> `list` 上的迭代器属于哪类？`vector`呢？

* `list` 上的迭代器是 **双向迭代器**
* `vector` 上的迭代器是 **随机访问迭代器**

## 练习10.40

> 你认为 `copy` 要求哪类迭代器？`reverse` 和 `unique` 呢？

* `copy` 需要两个**输入迭代器**，一个**输出迭代器**
* `reverse` 需要**双向迭代器**
* `unique`需要**随机访问迭代器**

## 练习10.41

> 仅根据算法和参数的名字，描述下面每个标准库算法执行什么操作：

```cpp
replace(beg, end, old_val, new_val);
replace_if(beg, end, pred, new_val);
replace_copy(beg, end, dest, old_val, new_val);
replace_copy_if(beg, end, dest, pred, new_val);
```

## 练习10.42

> 使用 `list` 代替 `vector` 重新实现10.2.3节中的去除重复单词的程序。

