# flask-rest
This is a template for a REST API using Flask


## Creating the database
```bash
flask db init

flask db migrate -m "book table"
```
This will create the database and generate the scripts. To apply the changes to the database run:

```bash
flask db upgrade
```
