This repo contains examples from [article in our blog](http://steelkiwi.com/blog/practical-application-singleton-design-pattern/).

As it is written in the book “Design Patterns:  Elements of Reusable Object-Oriented Software” by Gang of Four:

> The singleton pattern is a design pattern that is used to ensure that a class can only have one concurrent instance. Whenever additional objects of a singleton class are required, the previously created, single instance is provided.

Although you can use singletons in the form of ordinary classes in Django applications, let’s take a look at the implementation of a singleton as a model which allows you to save the internal state of the singleton in the database. In our singleton design pattern example, we will show how to implement some project settings in such a way that they can be changed in the admin panel and can be used in templates.

## License
```
Copyright © 2017 SteelKiwi, http://steelkiwi.com

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
