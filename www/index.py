#!/usr/bin/env python3

# Load the cgi library so we can read URL parameters
import cgi

# Use cgi tracebacks so we get sensible error reports
# in the browser if anything goes wrong
import cgitb 
cgitb.enable()

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

    # Read the URL parameters
    form = cgi.FieldStorage()

    if "page" not in form:
        show_landing_page()

    elif form["page"].value == "dynamic":
        show_dynamic_page(form["name"].value)


def show_dynamic_page(name_from_form):
    template = env.get_template("name.html")
    print(template.render(name=name_from_form))

def show_landing_page():
    # The route for the initial page
    template = env.get_template("index.html")
    print(template.render())





if __name__ == "__main__":
    main()