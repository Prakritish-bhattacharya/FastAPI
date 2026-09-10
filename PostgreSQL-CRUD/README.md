# 🎯 Important Interview Questions

## What is SQLAlchemy?

SQLAlchemy is a Python SQL toolkit and ORM that allows Python applications to interact with relational databases using Python objects and SQL.

## What is an ORM?

ORM (Object-Relational Mapping) maps Python classes/objects to database tables/rows.
```text
Python Class  →  Database Table
Python Object →  Database Row
Attribute     →  Column
```
## What is create_engine()?

It creates the SQLAlchemy engine used to communicate with the database.

```python
Base.metadata.create_all(bind=engine)
```

It tells SQLAlchemy:

>"Look at all models registered with Base and create their tables in the database if they don't already exist."