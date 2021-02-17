from src.db.core import *

# Query to retrieve data from table
def sql_get(table_name=""):
    sql_query = f"SELECT * FROM {table_name}"
    return get_data(sql_query)


# Query to add data to the database
def sql_add(table_name="", mydict={}):
    columns = ", ".join(mydict.keys())
    values = ", ".join("'" + str(x).replace("/", "_") + "'" for x in mydict.values())
    sql_query = "INSERT INTO %s ( %s ) VALUES ( %s )" % (table_name, columns, values)
    return sql_query


# Query to update data in the database
def sql_update(table_name="", mydict={}):
    columns = ", ".join(mydict.keys())
    values = ", ".join("'" + str(x).replace("/", "_") + "'" for x in mydict.values())
    sql_query = "REPLACE INTO %s ( %s ) VALUES ( %s )" % (table_name, columns, values)
    return sql_query


# Query to delete data in the database
def sql_delete(table_name="", id=""):
    sql_query = "DELETE FROM %s WHERE id = %s" % (table_name, id)
    return sql_query