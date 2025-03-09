from flask import render_template
from system.core.BaseController import BaseController

class WelcomeController (BaseController):
    def __init__(self):
        """
        Constructor.
        
        Calls BaseController constructor.
        """
        super().__init__()
    
    @staticmethod
    def index ():
        return render_template("welcome.html")