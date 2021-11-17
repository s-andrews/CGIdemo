#!/usr/bin/env python3

# Load the cgi library so we can read URL parameters
import cgi

# Use cgi tracebacks so we get sensible error reports
# in the browser if anything goes wrong
import cgitb 
cgitb.enable()

# Import the mysql connector
import mysql.connector

# Set up the jinja2 HTML template system so that we can separate the
# HTML into template files and just keep code and logic in the CGI
# script
from jinja2 import Environment, FileSystemLoader, select_autoescape

def main():

    # Create the jinja2 environment so we can find templates
    global env
    env = Environment(
        loader = FileSystemLoader("../templates"),
        autoescape=select_autoescape()
    )


    # Create the database connection
    global db
    db = mysql.connector.connect(
        host="localhost",
        user="cgiuser",
        database="CGItest"
    )

    # Read the URL parameters
    form = cgi.FieldStorage()

    if "page" not in form:
        show_landing_page()

    elif form["page"].value == "dynamic":
        show_dynamic_page(form["name"].value)

    elif form["page"].value == "database":
        name = ""
        if "name" in form:
            name = form["name"].value
        show_database_page(name)


def show_database_page(query_name):
    cursor = db.cursor()

    if query_name:
        cursor.execute("SELECT first_name, last_name, phone FROM person WHERE first_name=%s",(query_name,))
    
    else:
        cursor.execute("SELECT first_name, last_name, phone FROM person")


    people_data = cursor.fetchall()

    template = env.get_template("database.html")

    print(template.render(name=query_name, people=people_data))


def show_dynamic_page(name_from_form):
    template = env.get_template("name.html")
    print(template.render(name=name_from_form))

def show_landing_page():
    # The route for the initial page
    template = env.get_template("index.html")
    print(template.render())





if __name__ == "__main__":
    main()