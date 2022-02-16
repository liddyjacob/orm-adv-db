from bottle import route, run, template, get, post, request, response, redirect
import sqlite3
from models import List

connection = sqlite3.connect("shopping_list.db")

@route('/list')
def get_list():
    shopping_list = [item for item in List.select()]
    return template('shopping_list.tpl', shopping_list=shopping_list)

@get("/add")
def get_add():
    return template('add_item.tpl')

@post("/add")
def post_add():
    description = request.forms.get("description")
    List.create(description=description) # create new item and immediently save.
    # alternative - List.create(description=description) 
    redirect("/list")

@route("/delete/<id>")
def get_delete(id):
    List.get(List.id==id).delete_instance()
    redirect("/list")

@route("/edit/<id>")
def get_edit(id):
    item = List.get(List.id==id)
    return template('edit_item.tpl', id=id, description=item.description)

@post("/edit/<id>")
def post_edit(id):
    description = request.forms.get("description")
    item = List.get(List.id==id)
    item.description = description
    item.save()
    redirect("/list")

run(host='localhost', port=8080)