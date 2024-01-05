# flask template

![GitHub contributors](https://img.shields.io/github/contributors/fiandev/flask-template)
![GitHub License](https://img.shields.io/github/license/fiandev/flask-template)
![PyPI - Version](https://img.shields.io/pypi/v/Flask)

folder structure for python flask

------------------

## how to usage
To run your flask application, just follow the steps below

### using development mode
To run the application in development mode, just write the following command line

```shell
flask run --debug
```

or if you are having problems after you have run the above command, you can try the following steps

#### edit the entry file
the entry file for this project is `main.py` file.
please change the contents of the file as below

```python
if __name__ == "__main__":
    app.run(debug=True)
```

### using production mode
To run the application in development mode, just write the following command line

```shell
flask run
```

or if you are having problems after you have run the above command, you can try the following steps

#### edit the entry file
the entry file for this project is `main.py` file.
please change the contents of the file as below

```python
if __name__ == "__main__":
    app.run(debug=False)
```

------------------

> built with ♥️ by fiandev
