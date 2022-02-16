from bottle import route, run, template, get, post, request, redirect
import sqlite3
from models import List, Person

@route('/list')
def get_list():
    shopping_list = [item for item in List.select().order_by(List.person)]
    return template('shopping_list.tpl', shopping_list=shopping_list)

@get("/add")
def get_add():
    return template('add_item.tpl')

@post("/add")
def post_add():
    description = request.forms.get("description")
    person_name = request.forms.get("person")
    # create person associated with this item
    new_person, _ = Person.get_or_create(name=person_name)
    List.create(description=description, person=new_person) # create new item and immediently save.
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