# 第七章 类

## 练习7.1

使用2.6.1节定义的`Sales_data`类为1.6节的交易处理程序编写一个新版本。

## 练习7.2

曾在2.6.2节的练习中编写了一个`Sales_data`类，请向这个类添加`combine`函数和`isbn`成员。

## 练习7.3

修改7.1.1节的交易处理程序，令其使用这些成员。

## 练习7.4

编写一个名为`Person`的类，使其表示人员的姓名和地址。使用`string`对象存放这些元素，接下来的练习将不断充实这个类的其他特征。

## 练习7.5

在你的`Person`类中提供一些操作使其能够返回姓名和地址。
这些函数是否应该是`const`的呢？解释原因。

## 练习7.6

对于函数`add`、`read`和`print`，定义你自己的版本。

## 练习7.7

使用这些新函数重写7.1.2节练习中的程序。

```cpp
int main()
{
    Sales_data total;
    if (read(std::cin, total))
    {
        Sales_data trans;
        while (read(std::cin, trans)) {
            if (total.isbn() == trans.isbn())
                total.combine(trans);
            else {
                print(std::cout, total) << std::endl;
                total = trans;
            }
        }
        print(std::cout, total) << std::endl;
    }
    else
    {
        std::cerr << "No data?!" << std::endl;
        return -1;
    }
    
    return 0;
}
```

## 练习7.8

为什么`read`函数将其`Sales_data`参数定义成普通的引用，而`print`函数将其参数定义成常量引用？

## 练习7.9

对于7.1.2节练习中代码，添加读取和打印`Person`对象的操作。

## 练习7.10

在下面这条`if`语句中，条件部分的作用是什么？

```cpp
if (read(read(cin, data1), data2)) //等价read(std::cin, data1);read(std::cin, data2);
```

## 练习7.11 : 

在你的`Sales_data`类中添加构造函数，
然后编写一段程序令其用到每个构造函数。

## 练习7.12

把只接受一个`istream`作为参数的构造函数移到类的内部。

## 练习7.13

使用`istream`构造函数重写第229页的程序。

## 练习7.14

编写一个构造函数，令其用我们提供的类内初始值显式地初始化成员。

```cpp
Sales_data() : units_sold(0) , revenue(0) { }
```

## 练习7.15

为你的`Person`类添加正确的构造函数。

## 练习7.16

在类的定义中对于访问说明符出现的位置和次数有限定吗？
如果有，是什么？什么样的成员应该定义在`public`说明符之后？
什么样的成员应该定义在`private`说明符之后？

## 练习7.17

使用`class`和`struct`时有区别吗？如果有，是什么？

## 练习7.18

封装是何含义？它有什么用处？

## 练习7.19

在你的`Person`类中，你将把哪些成员声明成`public`的？
哪些声明成`private`的？
解释你这样做的原因。

构造函数、`getName()`、`getAddress()`函数将设为`public`。
`name`和 `address` 将设为`private`。
函数是暴露给外部的接口，因此要设为`public`；
而数据则应该隐藏让外部不可见。

## 练习7.20

友元在什么时候有用？请分别举出使用友元的利弊。

## 练习7.21

修改你的`Sales_data`类使其隐藏实现的细节。
你之前编写的关于`Sales_data`操作的程序应该继续使用，借助类的新定义重新编译该程序，确保其正常工作。

## 练习7.22

修改你的`Person`类使其隐藏实现的细节。

## 练习7.23

编写你自己的`Screen`类型。

## 练习7.25

`Screen`能安全地依赖于拷贝和赋值操作的默认版本吗？
如果能，为什么？如果不能？为什么？

## 练习7.26

将`Sales_data::avg_price`定义成内联函数。

## 练习7.27 

给你自己的`Screen`类添加`move`、`set` 和`display`函数，通过执行下面的代码检验你的类是否正确。

```cpp
Screen myScreen(5, 5, 'X');
myScreen.move(4, 0).set('#').display(cout);
cout << "\n";
myScreen.display(cout);
cout << "\n";
```

## 练习7.28

如果`move`、`set`和`display`函数的返回类型不是`Screen&` 而是`Screen`，则在上一个练习中将会发生什么？

## 练习7.29

修改你的`Screen`类，令`move`、`set`和`display`函数返回`Screen`并检查程序的运行结果，在上一个练习中你的推测正确吗？

## 练习7.30

通过`this`指针使用成员的做法虽然合法，但是有点多余。讨论显示使用指针访问成员的优缺点。

## 练习7.31

定义一对类`X`和`Y`，其中`X`包含一个指向`Y`的指针，而`Y`包含一个类型为`X`的对象。

## 练习7.32

定义你自己的`Screen`和`Window_mgr`，其中`clear`是`Window_mgr`的成员，是`Screen`的友元。

## 练习7.33

如果我们给`Screen`添加一个如下所示的`size`成员将发生什么情况？如果出现了问题，请尝试修改它。

```cpp
pos Screen::size() const
{
    return height * width;
}
```

##  练习7.34

如果我们把第256页`Screen`类的`pos`的`typedef`放在类的最后一行会发生什么情况？

## 练习7.35

解释下面代码的含义，说明其中的`Type`和`initVal`分别使用了哪个定义。如果代码存在错误，尝试修改它。

```cpp
typedef string Type;
Type initVal(); 
class Exercise {
public:
    typedef double Type;
    Type setVal(Type);
    Type initVal(); 
private:
    int val;
};
Type Exercise::setVal(Type parm) { 
    val = parm + initVal();     
    return val;
}
```

## 练习7.36

下面的初始值是错误的，请找出问题所在并尝试修改它。

```cpp
struct X {
	X (int i, int j): base(i), rem(base % j) {}
	int rem, base;
};
```

## 练习7.37

使用本节提供的`Sales_data`类，确定初始化下面的变量时分别使用了哪个构造函数，然后罗列出每个对象所有的数据成员的值。

## 练习7.38

有些情况下我们希望提供`cin`作为接受`istream&`参数的构造函数的默认实参，请声明这样的构造函数。

## 练习7.39

如果接受`string`的构造函数和接受`istream&`的构造函数都使用默认实参，这种行为合法吗？如果不，为什么？

## 练习7.40

从下面的抽象概念中选择一个（或者你自己指定一个），思考这样的类需要哪些数据成员，提供一组合理的构造函数并阐明这样做的原因。

```
(a) Book
(b) Data
(c) Employee
(d) Vehicle
(e) Object
(f) Tree
```

## 练习7.41

使用委托构造函数重新编写你的`Sales_data`类，给每个构造函数体添加一条语句，令其一旦执行就打印一条信息。用各种可能的方式分别创建`Sales_data`对象，认真研究每次输出的信息直到你确实理解了委托构造函数的执行顺序。

## 练习7.42

对于你在练习7.40中编写的类，确定哪些构造函数可以使用委托。如果可以的话，编写委托构造函数。如果不可以，从抽象概念列表中重新选择一个你认为可以使用委托构造函数的，为挑选出的这个概念编写类定义。

## 练习7.43

假定有一个名为`NoDefault`的类，它有一个接受`int`的构造函数，但是没有默认构造函数。定义类`C`，`C`有一个 `NoDefault`类型的成员，定义`C`的默认构造函数。

```cpp
class NoDefault {
public:
    NoDefault(int i) { }
};

class C {
public:
    C() : def(0) { } 
private:
    NoDefault def;
};
```

## 练习7.44

下面这条声明合法吗？如果不，为什么？

```cpp
vector<NoDefault> vec(10);//vec初始化有10个元素
```

## 练习7.45

如果在上一个练习中定义的vector的元素类型是C，则声明合法吗？为什么？

合法。因为`C`有默认构造函数。

## 练习7.46

下面哪些论断是不正确的？为什么？

- (a) 一个类必须至少提供一个构造函数。
- (b) 默认构造函数是参数列表为空的构造函数。
- (c) 如果对于类来说不存在有意义的默认值，则类不应该提供默认构造函数。
- (d) 如果类没有定义默认构造函数，则编译器将为其生成一个并把每个数据成员初始化成相应类型的默认值。

## 练习7.47

说明接受一个`string`参数的`Sales_data`构造函数是否应该是`explicit`的，并解释这样做的优缺点。

## 练习7.48

假定`Sales_data`的构造函数不是`explicit`的，则下述定义将执行什么样的操作？

## 练习7.49

对于`combine`函数的三种不同声明，当我们调用`i.combine(s)`时分别发生什么情况？其中`i`是一个`Sales_data`，而` s`是一个`string`对象。

## 练习7.50

确定在你的`Person`类中是否有一些构造函数应该是`explicit` 的。

## 练习7.51

`vector`将其单参数的构造函数定义成`explicit`的，而`string`则不是，你觉得原因何在？

假如我们有一个这样的函数：

```cpp
int getSize(const std::vector<int>&);
```

如果`vector`没有将单参数构造函数定义成`explicit`的，我们就可以这样调用：

```cpp
getSize(34);
```

很明显这样调用会让人困惑，函数实际上会初始化一个拥有34个元素的`vecto`r的临时量，然后返回34。但是这样没有任何意义。而`string`则不同，`string`的单参数构造函数的参数是`const char *`，因此凡是在需要用到`string`的地方都可以用` const char *`来代替（字面值就是`const char *`）。如：

```cpp
void print(std::string);
print("hello world");
```

## 练习7.52

使用2.6.1节的 `Sales_data` 类，解释下面的初始化过程。如果存在问题，尝试修改它。

```cpp
Sales_data item = {"987-0590353403", 25, 15.99};
```

## 练习7.53

定义你自己的`Debug`。

## 练习7.54

`Debug`中以 `set_` 开头的成员应该被声明成`constexpr` 吗？如果不，为什么？

## 练习7.55

7.5.5节的`Data`类是字面值常量类吗？请解释原因。

## 练习7.56

什么是类的静态成员？它有何优点？静态成员与普通成员有何区别？

## 练习7.57

编写你自己的`Account`类。

## 练习7.58

下面的静态数据成员的声明和定义有错误吗？请解释原因。

```cpp
//example.h
class Example {
public:
	static double rate = 6.5;
	static const int vecSize = 20;
	static vector<double> vec(vecSize);
};

//example.c
#include "example.h"
double Example::rate;
vector<double> Example::vec;
```

