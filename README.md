# AirBnB_clone

Welcome to the AirBnB clone project!

## Description:

The goal of the project is to deploy on our server a simple copy of the AirBnB website.

we won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, we will have a complete web application composed by:

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## The console

we will create our data model, manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file).
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” 
and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end 
and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

The console will be a tool to validate this storage engine

![Image](image.png)
