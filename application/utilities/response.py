from flask import jsonify

def response_json (data):
    return jsonify(data)

def api_response_error (message, code = 500):
    return response_json({
      "code": code,
      "status": "failed",
      "message": message,
    })

def api_response_success (data, status = "success", code = 200, otherStateData = {}):
    response_template = {
      "code": code,
      "status": status,
      "data": data,
    }
    
    for key in otherStateData:
        response_template[key] = otherStateData[key]
    
    return response_json(response_template)