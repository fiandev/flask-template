import os
import mimetypes
from datetime import datetime
from werkzeug.datastructures import FileStorage

class File:
    def __init__(self, file):
        """
        Initializes a File object.

        Parameters
        ----------
        file : FileStorage or str
            The file to be processed. Can be a Flask FileStorage object for 
            files uploaded through a web request or a string representing 
            the path to a file stored on disk.

        Raises
        ------
        ValueError
            If the file is neither a valid path nor a FileStorage object.

        Attributes
        ----------
        file_storage : FileStorage or None
            The FileStorage object if the file is from a Flask request, 
            otherwise None.
        filename : str
            The name of the file.
        mime_type : str
            The MIME type of the file.
        size_bytes : int
            The size of the file in bytes.
        extension : str
            The file extension.
        created_at : str or None
            The creation time of the file if stored, otherwise None.
        modified_at : str or None
            The last modified time of the file if stored, otherwise None.
        """
        
        if isinstance(file, FileStorage):
            # If the file is from Flask request (FileStorage)
            self.file_storage = file
            self.filename = file.filename
            self.mime_type = file.mimetype or self._guess_mime_type(self.filename)
            self.size_bytes = self._get_size_from_filestorage(file)
            self.extension = os.path.splitext(self.filename)[1].lower()
            self.created_at = None  # Cannot get creation time from memory
            self.modified_at = None
        elif isinstance(file, str) and os.path.isfile(file):
            # If the file is already stored
            self.file_storage = None
            self.filename = os.path.basename(file)
            self.mime_type = self._guess_mime_type(file)
            self.size_bytes = os.path.getsize(file)
            self.extension = os.path.splitext(file)[1].lower()
            self.created_at = self._get_creation_time(file)
            self.modified_at = self._get_modification_time(file)
        else:
            raise ValueError("File must be a valid path or a FileStorage object.")

    def _guess_mime_type(self, filename):
        """Detects MIME type based on file extension."""
        mime_type, _ = mimetypes.guess_type(filename)
        return mime_type or "Unknown"

    def _get_size_from_filestorage(self, file_storage):
        """Calculates file size without saving it to disk."""
        file_storage.stream.seek(0, os.SEEK_END)
        size = file_storage.stream.tell()
        file_storage.stream.seek(0)  # Reset position to the beginning
        return size

    def _get_creation_time(self, file_path):
        """Gets file creation time (only for stored files)."""
        timestamp = os.path.getctime(file_path)
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    def _get_modification_time(self, file_path):
        """Gets file last modification time (only for stored files)."""
        timestamp = os.path.getmtime(file_path)
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    def get_metadata(self):
        """Returns file metadata as a dictionary."""
        return {
            "filename": self.filename,
            "size_bytes": self.size_bytes,
            "mime_type": self.mime_type,
            "extension": self.extension,
            "created_at": self.created_at,
            "modified_at": self.modified_at
        }