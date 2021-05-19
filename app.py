from flask import Flask, render_template, request, redirect, url_for
from flask.wrappers import Response
from locations import Locations
from forms import AddLocationForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_PROJECT"

visit = Locations()
categories = {
    "recommended": "Recommended",
    "tovisit": "Places To Go",
    "visited": "Visited!!!",
}

UP_ACTION = "\u2197"
DEL_ACTION = "X"


@app.route("/<category>", methods=["GET", "POST"])
def locations(category):

    # locations is list of Location class genereated by Locations by loading data in csv
    locations = visit.get_list_by_category(category)
    if request.method == "POST":
        [(name, action)] = request.form.items()
        if action == UP_ACTION:
            visit.moveup(name)
        elif action == DEL_ACTION:
            visit.delete(name)
        return redirect(
            url_for(
                "locations",
                category=category,
            )
        )
    return render_template(
        "locations.html",
        category=category,
        categories=categories,
        locations=locations,
        add_location=AddLocationForm(),
    )


@app.route("/add_location", methods=["POST"])
def add_location():
    ## Validate and collect the form data

    if True:
        name = None
        description = None
        category = None
        visit.add(name, description, category)

    ## Redirect to locations route function
    return ""


@app.route("/")
def index():

    ## Redirect to locations route function
    return ""
