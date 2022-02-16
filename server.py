from bottle import route, run, template, get, post, request, response, redirect
import sqlite3

connection = sqlite3.connect("shopping_list.db")

@route('/list')
def get_list():
    global connection
    cursor = connection.cursor()
    items = cursor.execute("select id, description from list")
    items = list(items)
    shopping_list = [{"id":item[0], "desc":item[1]} for item in items]
    return template('shopping_list.tpl', shopping_list=shopping_list)

@get("/add")
def get_add():
    return template('add_item.tpl')

@post("/add")
def post_add():
    description = request.forms.get("description")
    print(f"post was called. description={description}")
    global connection
    cursor = connection.cursor()
    items = cursor.execute(f"insert into list (description) values ('{description}')")
    connection.commit()
    redirect("/list")

@route("/delete/<id>")
def get_delete(id):
    global connection
    cursor = connection.cursor()
    items = cursor.execute(f"delete from list where id={id}")
    connection.commit()
    redirect("/list")

@route("/edit/<id>")
def get_edit(id):
    global connection
    cursor = connection.cursor()
    items = cursor.execute(f"select description from list where id={id}")
    items = list(items)
    if len(items) != 1:
        redirect("/list")
    description = items[0][0]
    print(description)
    return template('edit_item.tpl', id=id, description=description)

@post("/edit/<id>")
def post_edit(id):
    description = request.forms.get("description")
    global connection
    cursor = connection.cursor()
    items = cursor.execute(f"update list set description='{description}' where id={id}")
    connection.commit()
    redirect("/list")

run(host='localhost', port=8080)