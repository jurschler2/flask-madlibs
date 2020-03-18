from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

debug = DebugToolbarExtension(app)


@app.route("/madlibs")
def index():
    """This function creates the madlib template specified by the python
        Story class"""

    return render_template("base.html", word_list=stories.story.prompts)


@app.route("/story")
def create_story():
    """This function generates the story using the inputs passed by the 
        user into the form"""

    created_story = stories.story.generate(request.args)

    return render_template("story.html", created_story=created_story)
