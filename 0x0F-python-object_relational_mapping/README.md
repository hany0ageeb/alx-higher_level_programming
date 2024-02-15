# 0x0F. Python - Object-relational mapping

## Background Context

In this project, you will link two amazing worlds: Databases and Python!
In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.
In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).
The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.
Without ORM:
```python
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
	print(row)
cur.close()
conn.close()
```
With an ORM:
```python
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)
session = Session(engine)
for state in session.query(State).order_by(State.id).all():# HERE: no SQL query, only objects!
	print("{}: {}".format(state.id, state.name))
session.close()
```
## Resources

- [Object-relational mappers](https://intranet.alxswe.com/rltoken/a8DUOWhXpNX3TEwgyT-U8A)
- [mysqlclient/MySQLdb documentation] (https://intranet.alxswe.com/rltoken/JtFaKjnqxudr6Hi05Us1Lw)
- [MySQLdb tutorial](https://intranet.alxswe.com/rltoken/TdUSYFNGbXJG1WjCEoq5FA)
- [SQLAlchemy tutorial](https://intranet.alxswe.com/rltoken/YyL5hsscviNH04XGW-XpfA)
- [SQLAlchemy](https://intranet.alxswe.com/rltoken/j9azWF2Db_2rNolTxOF3SA)
- [mysqlclient/MySQLdb](https://intranet.alxswe.com/rltoken/0zLhY9KqKjn-zmdb7X598Q)
- [Introduction to SQLAlchemy](https://intranet.alxswe.com/rltoken/pw50Bl1Bj84wksxm018dwA)
- [Flask SQLAlchemy](https://intranet.alxswe.com/rltoken/B-xIdMtGvpus8vHxAIRrPg)
- [10 common stumbling blocks for SQLAlchemy newbies](https://intranet.alxswe.com/rltoken/deIzPMrfK8Ixqm-AboFHWg)
- [Python SQLAlchemy Cheatsheet](https://intranet.alxswe.com/rltoken/dZfUNK3lJicGMK5PU0bE7Q)
- [https://intranet.alxswe.com/rltoken/dZfUNK3lJicGMK5PU0bE7Q](https://intranet.alxswe.com/rltoken/hNxBKC8lHge5XjsRO8ksHQ)
- [SQLAlchemy ORM Tutorial for Python Developers](https://intranet.alxswe.com/rltoken/hNxBKC8lHge5XjsRO8ksHQ)
- [SQLAlchemy Tutorial](https://intranet.alxswe.com/rltoken/5G_R2NmQRFqiZb84qxYERQ)
- [Python Virtual Environments: A primer](https://intranet.alxswe.com/rltoken/OXle6kXpmD88D0WbgbTWqg)
