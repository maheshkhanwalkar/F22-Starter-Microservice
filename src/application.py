import os

from flask import Flask, Response, request
from datetime import datetime
import json
from columbia_student_resource import ColumbiaStudentResource
from flask_cors import CORS, cross_origin

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')

CORS(app)


@app.get("/api/health")
@cross_origin()
def get_health():
    t = str(datetime.now())
    msg = {
        "name": "F22-Starter-Microservice",
        "health": "Good",
        "at time": t
    }

    # DFF TODO Explain status codes, content type, ... ...
    result = Response(json.dumps(msg), status=200, content_type="application/json")
    # result.headers.add('Access-Control-Allow-Origin', '*')
    # result.headers.add("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")

    return result


@app.route("/api/students/<uni>", methods=["GET"])
@cross_origin()
def get_student_by_uni(uni):

    result = ColumbiaStudentResource.get_by_key(uni)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    # rsp.headers.add('Access-Control-Allow-Origin', '*')
    # rsp.headers.add("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
    return rsp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)

