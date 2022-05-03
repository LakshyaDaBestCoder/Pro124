from flask import Flask,jsonify, request

app = Flask(__name__)

tasks ={
    "data":[    
        {
            'Contact': "9987644456",
            'Name': "Raju",
            'done': False,
            'id': 1
        },
        {
            'Contact': "9676543222",
            'Name': "Rahul",
            'done': False,
            'id': 2
        }
    ]
}

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "The request is Unsuccessful!:("
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['Name'],
        'contact': request.json.get('Contact', ""),
        'done': False
    }
    tasks.append(contact)
    return jsonify({
        "status":"success",
        "message": "The request is Successful!:)"
    })

if (__name__ == "__main__"):
    app.run(debug=True)