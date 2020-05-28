## 练习9.1

> 对于下面的程序任务，`vector`、`deque`和`list`哪种容器最为适合？解释你的选择的理由。如果没有哪一种容器优于其他容器，也请解释理由。

* (a) 读取固定数量的单词，将它们按字典序插入到容器中。我们将在下一章中看到，关联容器更适合这个问题。
* (b) 读取未知数量的单词，总是将单词插入到末尾。删除操作在头部进行。
* (c) 从一个文件读取未知数量的整数。将这些数排序，然后将它们打印到标准输出。

## 练习9.2

> 定义一个`list`对象，其元素类型是`int`的`deque`。

## 练习9.3

> 构成迭代器范围的迭代器有何限制？

## 练习9.4

> 编写函数，接受一对指向`vector<int>`的迭代器和一个`int`值。在两个迭代器指定的范围中查找给定的值，返回一个布尔值来指出是否找到。

## 练习9.5

> 重写上一题的函数，返回一个迭代器指向找到的元素。注意，程序必须处理未找到给定值的情况。

## 练习9.6

> 下面的程序有何错误？你应该如何修改它？

```cpp
list<int> lst1;
list<int>::iterator iter1 = lst1.begin(),
					iter2 = lst1.end();
while (iter1 < iter2) /* ... */
```

解:

修改成如下：

```cpp
while (iter1 != iter2)
```

## 练习9.7

> 为了索引`int`的`vector`中的元素，应该使用什么类型？

解:

```cpp
vector<int>::size_type
```

## 练习9.8

> 为了读取`string`的`list`中的元素，应该使用什么类型？如果写入`list`，又应该使用什么类型？

解:

```cpp
list<string>::const_iterator // 读
list<string>::iterator // 写
```

## 练习9.9

> `begin`和`cbegin`两个函数有什么不同？

解:

`begin` 返回的是普通迭代器，`cbegin` 返回的是常量迭代器。

## 练习9.10

> 下面4个对象分别是什么类型？

```cpp
vector<int> v1;
const vector<int> v2;
auto it1 = v1.begin(), it2 = v2.begin();
auto it3 = v1.cbegin(), it4 = v2.cbegin();
```

解:

`it1` 是 `vector<int>::iterator`

`it2`，`it3` 和 `it4` 是 `vector<int>::const_iterator`


## 练习9.11

> 对6种创建和初始化`vector`对象的方法，每一种都给出一个实例。解释每个`vector`包含什么值。

## 练习9.12

> 对于接受一个容器创建其拷贝的构造函数，和接受两个迭代器创建拷贝的构造函数，解释它们的不同。

## 练习9.13

> 如何从一个`list<int>`初始化一个`vector<double>`？从一个`vector<int>`又该如何创建？编写代码验证你的答案。

## 练习9.14

> 编写程序，将一个`list`中的`char *`指针元素赋值给一个`vector`中的`string`。

## 练习9.15

> 编写程序，判定两个`vector<int>`是否相等。

## 练习9.16

> 重写上一题的程序，比较一个list<int>中的元素和一个vector<int>中的元素。

## 练习9.17

> 假定`c1`和`c2`是两个容器，下面的比较操作有何限制？

## 练习9.18

> 编写程序，从标准输入读取`string`序列，存入一个`deque`中。编写一个循环，用迭代器打印`deque`中的元素。

## 练习9.19

> 重写上一题的程序，用`list`替代`deque`。列出程序要做出哪些改变。

## 练习9.20

> 编写程序，从一个`list<int>`拷贝元素到两个`deque`中。值为偶数的所有元素都拷贝到一个`deque`中，而奇数值元素都拷贝到另一个`deque`中。

## 练习9.21

> 如果我们将第308页中使用`insert`返回值将元素添加到`list`中的循环程序改写为将元素插入到`vector`中，分析循环将如何工作。

## 练习9.22

> 假定`iv`是一个`int`的`vector`，下面的程序存在什么错误？你将如何修改？

## 练习9.23

> 在本节第一个程序中，若`c.size()` 为1，则`val`、`val2`、`val3`和`val4`的值会是什么？

## 练习9.24

> 编写程序，分别使用`at`、下标运算符、`front` 和 `begin` 提取一个`vector`中的第一个元素。在一个空`vector`上测试你的程序。

## 练习9.25

> 对于第312页中删除一个范围内的元素的程序，如果 `elem1` 与 `elem2` 相等会发生什么？如果 `elem2` 是尾后迭代器，或者 `elem1` 和 `elem2` 皆为尾后迭代器，又会发生什么？

## 练习9.26

> 使用下面代码定义的`ia`，将`ia`拷贝到一个`vector`和一个`list`中。是用单迭代器版本的`erase`从`list`中删除奇数元素，从`vector`中删除偶数元素。

```cpp
int ia[] = { 0, 1, 1, 2, 3, 5, 8, 13, 21, 55, 89 };
```

## 练习9.27

> 编写程序，查找并删除`forward_list<int>`中的奇数元素。

## 练习9.28

> 编写函数，接受一个`forward_list<string>`和两个`string`共三个参数。函数应在链表中查找第一个`string`，并将第二个`string`插入到紧接着第一个`string`之后的位置。若第一个`string`未在链表中，则将第二个`string`插入到链表末尾。

```cpp
void find_and_insert(forward_list<string>& flst, const string& s1, const string& s2)
{
	auto prev = flst.before_begin();
	auto curr = flst.begin();
	while (curr != flst.end())
	{
		if (*curr == s1)
		{
			flst.insert_after(curr, s2);
			return;
	    }
	    prev = curr;
	    ++curr;
    }
    flst.insert_after(prev, s2);
}
```

## 练习9.29

> 假定`vec`包含25个元素，那么`vec.resize(100)`会做什么？如果接下来调用`vec.resize(10)`会做什么？

## 练习9.30

> 接受单个参数的`resize`版本对元素类型有什么限制（如果有的话）？

## 练习9.31

> 第316页中删除偶数值元素并复制奇数值元素的程序不能用于`list`或`forward_list`。为什么？修改程序，使之也能用于这些类型。

## 练习9.32

> 在第316页的程序中，向下面语句这样调用`insert`是否合法？如果不合法，为什么？

```cpp
iter = vi.insert(iter, *iter++);
```

## 练习9.33

> 在本节最后一个例子中，如果不将`insert`的结果赋予`begin`，将会发生什么？编写程序，去掉此赋值语句，验证你的答案。

## 练习9.34

> 假定`vi`是一个保存`int`的容器，其中有偶数值也有奇数值，分析下面循环的行为，然后编写程序验证你的分析是否正确。

```cpp
iter = vi.begin();
while (iter != vi.end())
	if (*iter % 2)
		iter = vi.insert(iter, *iter);
	++iter;
```

## 练习9.35

> 解释一个`vector`的`capacity`和`size`有何区别。

## 练习9.36

> 一个容器的`capacity`可能小于它的`size`吗？

## 练习9.37

> 为什么`list`或`array`没有`capacity`成员函数？

## 练习9.38

> 编写程序，探究在你的标准实现中，`vector`是如何增长的。

## 练习9.39

> 解释下面程序片段做了什么：

```cpp
vector<string> svec;
svec.reserve(1024);
string word;
while (cin >> word)
	svec.push_back(word);
svec.resize(svec.size() + svec.size() / 2);
```

## 练习9.40

> 如果上一题的程序读入了256个词，在`resize`之后容器的`capacity`可能是多少？如果读入了512个、1000个、或1048个呢？

## 练习9.41

> 编写程序，从一个`vector<char>`初始化一个`string`。

## 练习9.42

> 假定你希望每次读取一个字符存入一个`string`中，而且知道最少需要读取100个字符，应该如何提高程序的性能？

## 练习9.43

> 编写一个函数，接受三个`string`参数是`s`、`oldVal` 和`newVal`。使用迭代器及`insert`和`erase`函数将`s`中所有`oldVal`替换为`newVal`。测试你的程序，用它替换通用的简写形式，如，将"tho"替换为"though",将"thru"替换为"through"。

## 练习9.44

> 重写上一题的函数，这次使用一个下标和`replace`。

## 练习9.45

> 编写一个函数，接受一个表示名字的`string`参数和两个分别表示前缀（如"Mr."或"Mrs."）和后缀（如"Jr."或"III"）的字符串。使用迭代器及`insert`和`append`函数将前缀和后缀添加到给定的名字中，将生成的新`string`返回。

## 练习9.46

> 重写上一题的函数，这次使用位置和长度来管理`string`，并只使用`insert`。

## 练习9.47

> 编写程序，首先查找`string`"ab2c3d7R4E6"中每个数字字符，然后查找其中每个字母字符。编写两个版本的程序，第一个要使用`find_first_of`，第二个要使用`find_first_not_of`。

## 练习9.48

> 假定`name`和`numbers`的定义如325页所示，`numbers.find(name)`返回什么？

## 练习9.49

> 如果一个字母延伸到中线之上，如d或f，则称其有上出头部分（`ascender`）。如果一个字母延伸到中线之下，如p或g，则称其有下出头部分（`descender`）。编写程序，读入一个单词文件，输出最长的既不包含上出头部分，也不包含下出头部分的单词。

## 练习9.50

> 编写程序处理一个`vector<string>`，其元素都表示整型值。计算`vector`中所有元素之和。修改程序，使之计算表示浮点值的`string`之和。

## 练习9.51

> 设计一个类，它有三个`unsigned`成员，分别表示年、月和日。为其编写构造函数，接受一个表示日期的`string`参数。你的构造函数应该能处理不同的数据格式，如January 1,1900、1/1/1990、Jan 1 1900 等。

## 练习9.52

> 使用`stack`处理括号化的表达式。当你看到一个左括号，将其记录下来。当你在一个左括号之后看到一个右括号，从`stack`中`pop`对象，直至遇到左括号，将左括号也一起弹出栈。然后将一个值（括号内的运算结果）`push`到栈中，表示一个括号化的（子）表达式已经处理完毕，被其运算结果所替代。

