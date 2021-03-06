###### 0301 Classes, Instances, Type, Methods and Attributes
```
* Class: a blueprint for an instance
* Instance: a constructed object of the class
* Type: indicates the class the instance belongs to
* Attribute: any object value: object.attribute
* Method: a "callable attribute" defined in the class (function)

Instance Methods and Attributes

* A "car" can be seen as a class of object
* The car class provides the blueprint for a car object
* Each instance of a car does the same things (methods)
* But, each car instance has its own state (attributes)

An object's interface

* An object's interface is made up of its methods
* Methods are like "buttons" that operate the object
* Methods often change an instance's state (its data)
* A method's often complex implementation is hidden behind the interface
```

###### 0302 Defining a Class; Constructing an Instance
```
Review: class
    * Classes are "instance factories"
    * Classes define an "instance blueprint"
Counstruct an instance or object of the class
    * Instances know to which class they belong ("type")
    * Instances can access variables degined in the class
```

###### 0303 Instance Methods
```
* Instance methods are variables defines in the class
* They are accessed through the instance: instance.method()
* When called through the instance, the instance is automatically passed as 1st argument to the method. 
* Because of this automatic passing of the instance, instance methods are known as "bound" menthods, i.e. bound to the instance upon which it is called

Points to Understanding Classes
    * A method on an instance passes instance as the first argument of the method (named self in the method)
```

###### 0304 Instance Attributes ("state")
```
What is an object?
    * An object is a unit of data (having one or more attributes), of a particular class or type, with associated functionality (methods).

* We have seen that an instance can access variables defined in the class
* An instance can also get and set values in itself
* Because these values change according to what happens to the object, we call these values state
* Instance data takes the form of instance attribute values, set and accessed through object.attribute syntax

* Instances have their own data, instance attributes.
```

###### 0305 Encapsulation
```
* Encapsulation: the first of the three pillars of OOP
* Encapsulation refers to the safe storage of data (as attirbutes) in an instance
* Data should be accessed only through instance methods
* Data should be validated as correct (depending on the requirements set in class methods)
* Data should be safe from changes by external processes

Breaking Encapsulation
    * Although normally set in a setter method, instance attribute values can be set anywhere
    * Encapsulation in Python is a voluntary restriction
    * Python does not implement data hiding, as does other languages
```

###### 0306 The __init__ constructor
```
* __init__ is a keyword variable: it must be named init
* it is a method automatically called when a new instance is constructed
* If it is not present, it is not called
* The self argument is the first appearance of the instance
* __init__ offers the opportunity to initialize attributes in the instance at the time of construction 
```

###### 0307 Class Attributes
```
* Attributes / variables in the class are accessible through the instance
* Instance attributes are also accessible by the instance
* When we use the syntax object.attribute, we're asking Python to look up  the attribute:
    * First in the instance
    * Then in the class
* Method calls through the instance follow this lookup
```

###### 0308 Working with Class and Instance Data
```
* No slides 
* Working File: 0308_class_instance_data.py
```

###### 0404 Inheriting the Constructor
```
* __init__ is like any other method; it can be inherited
* If a class does not have an __init__ constructor, Python will check its parent class to see if it can find one
* As soon as it finds one, Python calls it and stops looking
* We can use the super() function to call methods in the parent class
* We may want to initialize in the parent as well as our own class
```

###### 0405 Multiple Inheritance
```
* Any class can inherit from multiple classes
* Python normally uses a "depth-first" order when searching inheriting classes
* But when two classes inherit from the same class, Python eliminates the first mention of that class from the mro (method resolution order)
* The above applies to "new style" classes (inheriting from object)
```

###### 0406 Decorators; Class and Static Methods
```
* A class method takes the class (not instance) as argument and works with the class object
* A static method requires no argument and does not work with the class or instance (but it still belongs in the class code)
* A decorator is a processor that modifies a function
* @classmethod and @staticmethod modify the default binding that instance methods provide
```

###### 0407 Abstract Base Classes
```
* An abstract class is a kind of "model" for other classes to be defined. It is not designed to contruct instances, but can be subclassed by regular classes. 
* Abstract classes can define an interface, or methods that must be implemented by its subclasses
* The python abc module enables the creation of abstract base classes
* For information, see the abc module and related docs
```

###### 0408 Inheritance Examples
```
* When working in a child class we can choose to implement parent class methods in different ways
    * Inherit: simply use the parent class' defined method
    * Override/overload: provide child's own version of a method
    * Extend: do work in addition to that in parent's method
    * Provide: implement abstract method that parent requires
```

###### 0409 Composition vs. Inheritance
```
* Inheritance can be brittle (a change may require changes elsewhere)
* Decoupled code is classes, functions, etc. that work independently and don't depend on one another
* As long as the interface is maintained, interaction between classes will work
* Not checking or requiring particular types is polymorphic and Pythonic
```

###### 0501 Implementing Python's Core Syntax
```
* Our classes can respond to core syntax features
    * Operators like +, -, *, /
    * Operators like in
    * Built-in functions line len() and str()
    * looping
    * Subscripts and slices
* Core syntax features translate to "magic" method calls
* http://www.rafekettler.com/magicmethods.html

* Core syntax resolutions:
    * 'abc' in var  = var.__contains__('abc')
    * var == 'abc'  = var.__eq__('abc')
    * var[1]        = var.__getitem__(1)
    * var[1:3]      = var.__getslice__(1, 3)
    * len(var)      = var.__len__()
    * print var     = var.__repr__()
```

###### 0502 Subclassing Built-Ins
```
Inheriting From Built-Ins
    * Python lets our classes inhering from built-in classes
    * An inheriting (child) class of a built-in shared all the same attributes (including methods) of the built-in
    * We can take advantage of core built-in functionality, but customize selected operations
    * Built-in behavior is familiar to all Python developers - this can make use of our inheriting class easy to learn
```
