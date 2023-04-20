from flask import Flask, Response, request
import json
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017,
        serverSelectionTimeoutMS=1000
    )
    db = mongo.food
    mongo.server_info()  # Excepción desencadenada si no se puede conectar a la BD
except:
    print("ERROR - No se pudo conectar a la BD")


##############################
@app.route("/users", methods=["GET"])
def get_some_users():
    try:
        data = list(db.users.find())
        for user in data:
            user["_id"] = str(user["_id"])
        return Response(
            response=json.dumps(data),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "No se pueden leer usuarios"}),
            status=500,
            mimetype="application/json"
        )


##############################
@app.route("/users", methods=["POST"])
def create_user():
    try:
        user = {
            "name": request.form["name"],
            "lastName": request.form["lastName"]
        }
        dbResponse = db.users.insert_one(user)
        print(dbResponse.inserted_id)
        # for attr in dir(dbResponse):
        #     print(attr)
        return Response(
            response=json.dumps(
                {"message": "Usuario Creado",
                 "id": f"{dbResponse.inserted_id}"
                 }),
            status=200,
            mimetype="application/json"
        )

    except Exception as ex:
        print("***********")
        print(ex)
        print("***********")
    ##############################


@app.route("/users/<id>", methods=["PATCH"])
def update_user(id):
    try:
        dbResponse = db.users.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"name": request.form["name"]}},
            # {"$set":{"lastName":request.form["lastName"]}},
            # upsert=True
        )
        # for attr in dir(dbResponse):
        #     print(f"**********{attr}**********")
        if dbResponse.modified_count == 1:
            return Response(
                response=json.dumps(
                    {"message": "Usuario actualizado"}),
                status=200,
                mimetype="application/json"
            )
        else:
            return Response(
                response=json.dumps(
                    {"message": "No es necesario actualizar"}),
                status=200,
                mimetype="application/json"
            )

    except Exception as ex:
        print("*********************")
        print(ex)
        print("*********************")
        return Response(
            response=json.dumps(
                {"message": "Perdón, no se puede actualizar el usuario"}),
            status=500,
            mimetype="application/json"
        )


##############################
@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    try:
        dbResponse = db.users.delete_one({"_id": ObjectId(id)})
        if dbResponse.deleted_count == 1:
            return Response(
                response=json.dumps(
                    {"message": "Usuario eliminado", "id": f"{id}"}),
                status=200,
                mimetype="application/json"
            )
        else:
            return Response(
                response=json.dumps(
                    {"message": "Usuario no encontrado", "id": f"{id}"}),
                status=200,
                mimetype="application/json"
            )
        # for attr in dir(dbResponse):
        #     print(f"******{attr}********")
    except Exception as ex:
        print("*********************")
        print(ex)
        print("*********************")
        return Response(
            response=json.dumps(
                {"message": "Perdón, no se puede eliminar el usuario"}),
            status=500,
            mimetype="application/json"
        )


##############################
if __name__ == "__main__":
    app.run(port=5000, debug=True)
