from pymongo import MongoClient

try:
    # redis = redis.Redis(
    #     host='localhost',
    #     port='6379',
    #     charset='utf-8',
    #     decode_responses=True
    # )

    mongo = MongoClient(
        host ="localhost",
        port=27017,
        serverSelectionTimeoutMS = 1000
    )
    db = mongo["MongodbPokemon"]
    print(mongo.server_info())


    print("Connexion établie")
    mydict = { "name": "John", "address": "Highway 37" }
    mycol = db["Collection_Pokemon"]
    # x = mycol.insert_one(mydict)

except:
    print("ERREUR-Impossibe de se connecter à la BDD")
