# About

https://realpython.com/introduction-to-mongodb-and-python/

## Setup 

Install MongoDB:

```
brew tap mongodb/brew
brew install mongodb-community@5.0
```

run/stop as a service

```
brew services start mongodb-community@5.0
brew services stop mongodb-community@5.0
```

connect:

```
mongosh
```

create a new db

```
use rptutorials
show dbs
db
```

create a collection (table) using dot notation

```
db.tutorial
```

document (table row)

When you’re building a MongoDB database application, probably your most important decision is about the structure of documents. In other words, you’ll have to decide which fields and values your documents will have.

insert a document:

```
db.tutorial.insertOne(
{
    "title": "Reading and Writing CSV Files in Python",
    "author": "Jon",
    "contributors": [
        "Aldren",
        "Geir Arne",
        "Joanna",
        "Jason"
    ],
    "url": "https://realpython.com/python-csv/"
}
)

db.tutorial.insertOne(
{
"title": "Python 3's f-Strings: An Improved String Formatting Syntax",
"author": "Joanna",
"contributors": [
         "Adriana",
        "David",
         "Dan",
        "Jim",
         "Pavel"
    ],
     "url": "https://realpython.com/python-f-strings/"
}
)
```

find
```
db.tutorial.find()
db.tutorial.find({author: "Joanna"})
```
