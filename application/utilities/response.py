from flask import jsonify

def response_json(data, **kwargs):
    """
    Generate a json response with the given data and optional parameters.

    The following optional parameters are supported:

    - code: The HTTP status code to return. Defaults to 200.
    - status: A string indicating the status of the response. Defaults to "success".

    All other keyword arguments are merged into the response template.

    The function returns a flask.Response object.

    :param data: The data to include in the response
    :param kwargs: Additional keyword arguments to include in the response
    :return: A flask.Response object
    """
    response_template = {
        "code": kwargs.get("code", 200),
        "status": kwargs.get("status", "success"),
        "data": data,
    }
    response_template.update(kwargs)
    return jsonify(response_template)

def api_response_error(message, code=500):
    """
    Generate an error response with the given message and optional HTTP status code.

    :param message: The error message to include in the response
    :param code: The HTTP status code to return. Defaults to 500.
    :return: A flask.Response object
    """
    return response_json(message=message, code=code, status="failed")

def api_response_success(data, **kwargs):
    """
    Generate a successful response with the given data and optional parameters.

    The following optional parameters are supported:

    - code: The HTTP status code to return. Defaults to 200.
    - status: A string indicating the status of the response. Defaults to "success".

    All other keyword arguments are merged into the response template.

    The function returns a flask.Response object.

    :param data: The data to include in the response
    :param kwargs: Additional keyword arguments to include in the response
    :return: A flask.Response object
    """
    return response_json(data, code=kwargs.get("code", 200), status=kwargs.get("status", "success"), **kwargs)
