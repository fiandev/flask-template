import os
from flask import request
from werkzeug.utils import secure_filename
from application.constants.paths import PROGRAM_PATH
from system.lib.File import File

class BaseController:
    DEFAULT_STORAGE_PATH = f"{PROGRAM_PATH}/storage/"

    def __init__(self):
        """
        Constructor for BaseController.

        This method sets the following properties:
        - self.current_url: The current URL of the request.
        - self.previous_url: The previous URL of the request or None if it
            doesn't exist.
        - self.method: The HTTP method of the request.
        """
        self.current_url = request.url
        self.previous_url = request.referrer or None
        self.method = request.method
    
    def handle_file_upload(self, options = None):
        """
        Handles file upload to the server.

        Parameters
        ----------
        options : dict
            Additional options for the method.

        Returns
        -------
        list
            A list of File objects for each saved file.
        """
        saved_files = []

        try:
            for field_name, file in request.files.items():
                if file and (file.filename):
                    filename = secure_filename(file.filename)
                
                file.save(os.path.join(self.DEFAULT_STORAGE_PATH, filename))
                saved_files.append(File(file))
            return saved_files
        except:
            return []