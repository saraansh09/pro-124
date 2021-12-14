from flask import Flask, json,jsonify,request

app = Flask(__name__)
List = [
    {
        "id" : 1,
        "name" :u"Raju",
        "contact":u"9382020492",
        "done":False
    },
     {
        "id" : 2,
        "name" :u"Rajiv",
        "contact":u"9382049502",
        "done":False
    }
    ]

@app.route("/add-data",methods = ["POST"])
def add_task ():
  if not request.json:
      return jsonify({
          "status" : "error",
          "message" : "please provide data!"
      },400)

  contact = {
    'id' : tasks[-1]['id'] + 1,
    'Name' : request.json['name'],
    'Contact' : request.json.get('contact',""),
    'done' : False
    }
  List.append(contact)
  return jsonify({
        "status" : "success",
        "message" : "contact added successfully!"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : "List"
    })

if (__name__ == "__main__"):
    app.run(debug = True)

