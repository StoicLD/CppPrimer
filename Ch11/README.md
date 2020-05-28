# 第十一章 关联容器

## 练习11.1

> 描述`map`和`vector`的不同。

## 练习11.2

> 分别给出最适合使用`list`、`vector`、`deque`、`map`以及`set`的例子。

## 练习11.3

> 编写你自己的单词计数程序。

## 练习11.4

> 扩展你的程序，忽略大小写和标点。例如，"example."、"example,"和"Example"应该递增相同的计数器。

## 练习11.5

> 解释`map`和`set`的区别。你如何选择使用哪个？

## 练习11.6

> 解释`set`和`list`的区别。你如何选择使用哪个？

`set` 是有序不重复集合，底层实现是红黑树，而 `list` 是无序可重复集合，底层实现是链表。

## 练习11.7

> 定义一个`map`，关键字是家庭的姓，值是一个`vector`，保存家中孩子（们）的名。编写代码，实现添加新的家庭以及向已有家庭中添加新的孩子。

## 练习11.8

> 编写一个程序，在一个`vector`而不是一个`set`中保存不重复的单词。使用`set`的优点是什么？

## 练习11.9

> 定义一个`map`，将单词与一个行号的`list`关联，`list`中保存的是单词所出现的行号。

## 练习11.10

> 可以定义一个`vector<int>::iterator` 到 `int` 的`map`吗？`list<int>::iterator` 到 `int` 的`map`呢？对于两种情况，如果不能，解释为什么。

## 练习11.11

> 不使用`decltype` 重新定义 `bookstore`。

## 练习11.12

> 编写程序，读入`string`和`int`的序列，将每个`string`和`int`存入一个`pair` 中，`pair`保存在一个`vector`中。

## 练习11.13

> 在上一题的程序中，至少有三种创建`pair`的方法。编写此程序的三个版本，分别采用不同的方法创建`pair`。解释你认为哪种形式最易于编写和理解，为什么？

## 练习11.14

> 扩展你在11.2.1节练习中编写的孩子姓达到名的`map`，添加一个`pair`的`vector`，保存孩子的名和生日。

## 练习11.15

> 对一个`int`到`vector<int>的map`，其`mapped_type`、`key_type`和 `value_type`分别是什么？

## 练习11.16

> 使用一个`map`迭代器编写一个表达式，将一个值赋予一个元素。

## 练习11.17

> 假定`c`是一个`string`的`multiset`，`v` 是一个`string` 的`vector`，解释下面的调用。指出每个调用是否合法：

```cpp
copy(v.begin(), v.end(), inserter(c, c.end()));
copy(v.begin(), v.end(), back_inserter(c));
copy(c.begin(), c.end(), inserter(v, v.end()));
copy(c.begin(), c.end(), back_inserter(v));
```

## 练习11.18

> 写出第382页循环中`map_it` 的类型，不要使用`auto` 或 `decltype`。

## 练习11.19

> 定义一个变量，通过对11.2.2节中的名为 `bookstore` 的`multiset` 调用`begin()`来初始化这个变量。写出变量的类型，不要使用`auto` 或 `decltype`。

## 练习11.20

> 重写11.1节练习的单词计数程序，使用`insert`代替下标操作。你认为哪个程序更容易编写和阅读？解释原因。

## 练习11.21

> 假定`word_count`是一个`string`到`size_t`的`map`，`word`是一个`string`，解释下面循环的作用：

```cpp
while (cin >> word)
	++word_count.insert({word, 0}).first->second;
```

## 练习11.22

> 给定一个`map<string, vector<int>>`，对此容器的插入一个元素的`insert`版本，写出其参数类型和返回类型。

```cpp
std::pair<std::string, std::vector<int>>    // 参数类型
std::pair<std::map<std::string, std::vector<int>>::iterator, bool> // 返回类型
```

## 练习11.23

> 11.2.1节练习中的`map` 以孩子的姓为关键字，保存他们的名的`vector`，用`multimap` 重写此`map`。

## 练习11.24

> 下面的程序完成什么功能？

```cpp
map<int, int> m;
m[0] = 1;
```

## 练习11.25

> 对比下面的程序与上一题程序

```cpp
vector<int> v;
v[0] = 1;
```

## 练习11.26

> 可以用什么类型来对一个`map`进行下标操作？下标运算符返回的类型是什么？请给出一个具体例子——即，定义一个`map`，然后写出一个可以用来对`map`进行下标操作的类型以及下标运算符将会返会的类型。

## 练习11.27

> 对于什么问题你会使用`count`来解决？什么时候你又会选择`find`呢？

## 练习11.28

> 对一个`string`到`int`的`vector`的`map`，定义并初始化一个变量来保存在其上调用`find`所返回的结果。

## 练习11.29

> 如果给定的关键字不在容器中，`upper_bound`、`lower_bound` 和 `equal_range` 分别会返回什么？

## 练习11.30

> 对于本节最后一个程序中的输出表达式，解释运算对象`pos.first->second`的含义。

## 练习11.31

> 编写程序，定义一个作者及其作品的`multimap`。使用`find`在`multimap`中查找一个元素并用`erase`删除它。确保你的程序在元素不在`map` 中时也能正常运行。

## 练习11.32

> 使用上一题定义的`multimap`编写一个程序，按字典序打印作者列表和他们的作品。

## 练习11.33

> 实现你自己版本的单词转换程序。

## 练习11.34

> 如果你将`transform` 函数中的`find`替换为下标运算符，会发生什么情况？

## 练习11.35

> 在`buildMap`中，如果进行如下改写，会有什么效果？

```cpp
trans_map[key] = value.substr(1);
//改为
trans_map.insert({key, value.substr(1)});
```

## 练习11.36

> 我们的程序并没检查输入文件的合法性。特别是，它假定转换规则文件中的规则都是有意义的。如果文件中的某一行包含一个关键字、一个空格，然后就结束了，会发生什么？预测程序的行为并进行验证，再与你的程序进行比较。

## 练习11.37

> 一个无序容器与其有序版本相比有何优势？有序版本有何优势？

无序容器拥有更好的性能，有序容器使得元素始终有序。

## 练习11.38

> 用 `unordered_map` 重写单词计数程序和单词转换程序。

