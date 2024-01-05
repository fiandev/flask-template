from application.core import app
from application.controllers.WelcomeController import WelcomeController
from application.controllers.api.ExampleApiController import ExampleApiController

# web route example
@app.route("/")
def Home ():
    return WelcomeController.index()

# api route example
@app.route("/api/test")
def ApiTest ():
    return ExampleApiController.index()