from application.utilities.response import api_response_error, api_response_success

class ExampleApiController:
    @staticmethod
    def index ():
        try:
            return api_response_success({
              "message": "success",
              "data": {
                "name": "fian",
                "hobbies": ["anime", "coding", "music"]
              }
            })
        except Exception as err:
            return api_response_error(str(err))