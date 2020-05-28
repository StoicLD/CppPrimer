## 练习16.1

> 给出实例化的定义。

## 练习16.2

> 编写并测试你自己版本的 `compare` 函数。

## 练习16.3

> 对两个 `Sales_data` 对象调用你的 `compare` 函数，观察编译器在实例化过程中如何处理错误。

## 练习16.4

> 编写行为类似标准库 `find` 算法的模版。函数需要两个模版类型参数，一个表示函数的迭代器参数，另一个表示值的类型。使用你的函数在一个 `vector<int>` 和一个`list<string>`中查找给定值。


## 练习16.5

> 为6.2.4节中的`print`函数编写模版版本，它接受一个数组的引用，能处理任意大小、任意元素类型的数组。

## 练习16.6

> 你认为接受一个数组实参的标准库函数 `begin` 和 `end` 是如何工作的？定义你自己版本的 `begin` 和 `end`。

## 练习16.7

> 编写一个 `constexpr` 模版，返回给定数组的大小。

## 练习16.8

> 在第97页的“关键概念”中，我们注意到，C++程序员喜欢使用 `!=` 而不喜欢 `<` 。解释这个习惯的原因。

## 练习16.9

> 什么是函数模版，什么是类模版？

## 练习16.10

> 当一个类模版被实例化时，会发生什么？

## 练习16.11

> 下面 `List` 的定义是错误的。应如何修改它？

```cpp
template <typename elemType> class ListItem;
template <typename elemType> class List {
public:
	List<elemType>();
	List<elemType>(const List<elemType> &);
	List<elemType>& operator=(const List<elemType> &);
	~List();
	void insert(ListItem *ptr, elemType value);
private:
	ListItem *front, *end;
};
```

## 练习16.12

> 编写你自己版本的 `Blob` 和 `BlobPtr` 模版，包含书中未定义的多个`const`成员。

## 练习16.13

> 解释你为 `BlobPtr` 的相等和关系运算符选择哪种类型的友好关系？

## 练习16.14

> 编写 `Screen` 类模版，用非类型参数定义 `Screen` 的高和宽。


## 练习16.15

> 为你的 `Screen` 模版实现输入和输出运算符。`Screen` 类需要哪些友元（如果需要的话）来令输入和输出运算符正确工作？解释每个友元声明（如果有的话）为什么是必要的。

## 练习16.16

> 将 `StrVec` 类重写为模版，命名为 `Vec`。

## 练习16.17

> 声明为 `typename` 的类型参数和声明为 `class` 的类型参数有什么不同（如果有的话）？什么时候必须使用`typename`？

## 练习16.18

> 解释下面每个函数模版声明并指出它们是否非法。更正你发现的每个错误。

```cpp
(a) template <typename T, U, typename V> void f1(T, U, V);
(b) template <typename T> T f2(int &T);
(c) inline template <typename T> T foo(T, unsigned int *);
(d) template <typename T> f4(T, T);
(e) typedef char Ctype;
	template <typename Ctype> Ctype f5(Ctype a);
```

## 练习16.19

> 编写函数，接受一个容器的引用，打印容器中的元素。使用容器的 `size_type` 和 `size`成员来控制打印元素的循环。

## 练习16.20

> 重写上一题的函数，使用`begin` 和 `end` 返回的迭代器来控制循环。

## 练习16.21

> 编写你自己的 `DebugDelete` 版本。

## 练习16.22

> 修改12.3节中你的 `TextQuery` 程序，令 `shared_ptr` 成员使用 `DebugDelete` 作为它们的删除器。

## 练习16.23

> 预测在你的查询主程序中何时会执行调用运算符。如果你的预测和实际不符，确认你理解了原因。

## 练习16.24

> 为你的 `Blob` 模版添加一个构造函数，它接受两个迭代器。

## 练习16.25

> 解释下面这些声明的含义。

```cpp
extern template class vector<string>;
template class vector<Sales_data>;
```

## 练习16.26

> 假设 `NoDefault` 是一个没有默认构造函数的类，我们可以显式实例化 `vector<NoDefualt>`吗？如果不可以，解释为什么。

## 练习16.27

> 对下面每条带标签的语句，解释发生了什么样的实例化（如果有的话）。如果一个模版被实例化，解释为什么;如果未实例化，解释为什么没有。

```cpp
template <typename T> class Stack {	};
void f1(Stack<char>); 		//(a)
class Exercise {
	Stack<double> &rds;		//(b)
	Stack<int> si;			//(c)
};
int main() {
	Stack<char> *sc;		//(d)
	f1(*sc);				//(e)
	int iObj = sizeof(Stack<string>);	//(f)
}
```

## 练习16.28

> 编写你自己版本的 `shared_ptr` 和 `unique_ptr`。

## 练习16.29

> 修改你的 `Blob` 类，用你自己的 `shared_ptr` 代替标准库中的版本。

## 练习16.30

> 重新运行你的一些程序，验证你的 `shared_ptr` 类和修改后的 `Blob` 类。（注意：实现 `weak_ptr` 类型超出了本书范围，因此你不能将`BlobPtr`类与你修改后的`Blob`一起使用。）

## 练习16.31

> 如果我们将 `DebugDelete` 与 `unique_ptr` 一起使用，解释编译器将删除器处理为内联形式的可能方式。

## 练习16.32

> 在模版实参推断过程中发生了什么？

## 练习16.33

> 指出在模版实参推断过程中允许对函数实参进行的两种类型转换。

## 练习16.34

> 对下面的代码解释每个调用是否合法。如果合法，`T` 的类型是什么？如果不合法，为什么？

```cpp
template <class T> int compare(const T&, const T&);
(a) compare("hi", "world");
(b) compare("bye", "dad");
```

## 练习16.35

> 下面调用中哪些是错误的（如果有的话）？如果调用合法，`T` 的类型是什么？如果调用不合法，问题何在？

```cpp
template <typename T> T calc(T, int);
tempalte <typename T> T fcn(T, T);
double d; float f; char c;
(a) calc(c, 'c'); 
(b) calc(d, f);
(c) fcn(c, 'c');
(d) fcn(d, f);
```

## 练习16.36

> 进行下面的调用会发生什么：

```cpp
template <typename T> f1(T, T);
template <typename T1, typename T2) f2(T1, T2);
int i = 0, j = 42, *p1 = &i, *p2 = &j;
const int *cp1 = &i, *cp2 = &j;
(a) f1(p1, p2);
(b) f2(p1, p2);
(c) f1(cp1, cp2);
(d) f2(cp1, cp2);
(e) f1(p1, cp1);
(f) f2(p1, cp1);
```

## 练习16.37

> 标准库 `max` 函数有两个参数，它返回实参中的较大者。此函数有一个模版类型参数。你能在调用 `max` 时传递给它一个 `int` 和一个 `double` 吗？如果可以，如何做？如果不可以，为什么？

## 练习16.38

> 当我们调用 `make_shared` 时，必须提供一个显示模版实参。解释为什么需要显式模版实参以及它是如果使用的。

## 练习16.39

> 对16.1.1节 中的原始版本的 `compare` 函数，使用一个显式模版实参，使得可以向函数传递两个字符串字面量。

## 练习16.40

> 下面的函数是否合法？如果不合法，为什么？如果合法，对可以传递的实参类型有什么限制（如果有的话）？返回类型是什么？

```cpp
template <typename It>
auto fcn3(It beg, It end) -> decltype(*beg + 0)
{
	//处理序列
	return *beg;
}
```

## 练习16.41

> 编写一个新的 `sum` 版本，它返回类型保证足够大，足以容纳加法结果。

## 练习16.42

> 对下面每个调用，确定 `T` 和 `val` 的类型：

```cpp
template <typename T> void g(T&& val);
int i = 0; const int ci = i;
(a) g(i);
(b) g(ci);
(c) g(i * ci);
```

## 练习16.43

> 使用上一题定义的函数，如果我们调用`g(i = ci)`,`g` 的模版参数将是什么？

## 练习16.44

> 使用与第一题中相同的三个调用，如果 `g` 的函数参数声明为 `T`（而不是`T&&`），确定T的类型。如果`g`的函数参数是 `const T&`呢？

## 练习16.45

> 如果下面的模版，如果我们对一个像42这样的字面常量调用`g`，解释会发生什么？如果我们对一个`int` 类型的变量调用`g` 呢？

```cpp
template <typename T> void g(T&& val) { vector<T> v; }
```

## 练习16.46

> 解释下面的循环，它来自13.5节中的 `StrVec::reallocate`:

```cpp
for (size_t i = 0; i != size(); ++i)
	alloc.construct(dest++, std::move(*elem++));
```

## 练习16.47

> 编写你自己版本的翻转函数，通过调用接受左值和右值引用参数的函数来测试它。

## 练习16.48

> 编写你自己版本的 `debug_rep` 函数。

## 练习16.49

> 解释下面每个调用会发生什么：

```cpp
template <typename T> void f(T);
template <typename T> void f(const T*);
template <typename T> void g(T);
template <typename T> void g(T*);
int i = 42, *p = &i;
const int ci = 0, *p2 = &ci;
g(42); g(p); g(ci); g(p2);
f(42); f(p); f(ci); f(p2);
```

## 练习16.50

> 定义上一个练习中的函数，令它们打印一条身份信息。运行该练习中的代码。如果函数调用的行为与你预期不符，确定你理解了原因。

## 练习16.51

> 调用本节中的每个 `foo`，确定 `sizeof...(Args)` 和 `sizeof...(rest)`分别返回什么。

## 练习16.52

> 编写一个程序验证上一题的答案。

## 练习16.53

> 编写你自己版本的 `print` 函数，并打印一个、两个及五个实参来测试它，要打印的每个实参都应有不同的类型。 

## 练习16.54

> 如果我们对一个没 `<<` 运算符的类型调用 `print`，会发生什么？

## 练习16.55

> 如果我们的可变参数版本 `print` 的定义之后声明非可变参数版本，解释可变参数的版本会如何执行。

## 练习16.56

> 编写并测试可变参数版本的 `errorMsg`。

## 练习16.57

> 比较你的可变参数版本的 `errorMsg` 和6.2.6节中的 `error_msg`函数。两种方法的优点和缺点各是什么？

## 练习16.58

> 为你的 `StrVec` 类及你为16.1.2节练习中编写的 `Vec` 类添加 `emplace_back` 函数。

## 练习16.59

> 假定 `s` 是一个 `string`，解释调用 `svec.emplace_back(s)`会发生什么。

## 练习16.60

> 解释 `make_shared` 是如何工作的。

## 练习16.61

> 定义你自己版本的 `make_shared`。

## 练习16.62

> 定义你自己版本的 `hash<Sales_data>`, 并定义一个 `Sales_data` 对象的 `unorder_multise`。将多条交易记录保存到容器中，并打印其内容。

## 练习16.63

> 定义一个函数模版，统计一个给定值在一个`vecor`中出现的次数。测试你的函数，分别传递给它一个`double`的`vector`，一个`int`的`vector`以及一个`string`的`vector`。

## 练习16.64

> 为上一题的模版编写特例化版本来处理`vector<const char*>`。编写程序使用这个特例化版本。

## 练习16.65

> 在16.3节中我们定义了两个重载的 `debug_rep` 版本，一个接受 `const char*` 参数，另一个接受 `char *` 参数。将这两个函数重写为特例化版本。

## 练习16.66

> 重载`debug_rep` 函数与特例化它相比，有何优点和缺点？

## 练习16.67

> 定义特例化版本会影响 `debug_rep` 的函数匹配吗？如果不影响，为什么？

