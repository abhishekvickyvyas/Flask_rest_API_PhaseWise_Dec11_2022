from flask import Flask, request , jsonify
from flask_restful import Api, Resource 

app = Flask(__name__)
api = Api( app)


class Add(Resource):
    def post(self):
        postData =  request.get_json()
        x = postData["x"]
        y = postData["y"]
        x = int(x)
        y = int(y)
        ret =  x + y
        ret_map = {

            "Message": ret,
            "Status Code": 200

        } 
        return jsonify(ret_map)
    pass

class Subtract(Resource):
    pass


class Multiply(Resource):
    pass

class Divide(Resource):
    pass

api.add_resource(Add, "/add")



@app.route("/hello_world")
def hello_world():
    return "Hello World!!"




if __name__ == "__main__":
    app.run(debug= True)

