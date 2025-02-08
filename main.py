from flask import Flask, request, jsonify
from graphene import ObjectType, String, Int, Field, List, Mutation, Schema

## In-memory data storage
users = []

## Type class
class UserType(ObjectType):
    id = Int()
    name = String()
    email = String()

## Query class to fetch users
class Query(ObjectType):
    all_users = List(UserType)
    user_by_id = Field(UserType, id=Int(required=True))

    def resolve_all_users(root, info):
        return users

    def resolve_user_by_id(root, info, id):
        return next((user for user in users if user["id"] == id), None)

## Mutation to add a new user
class AddUser(Mutation):
    class Arguments:
        name = String(required=True)
        email = String(required=True)

    user = Field(UserType)

    def mutate(root, info, name, email):
        new_user = {
            "id": len(users) + 1,
            "name": name,
            "email": email
        }
        users.append(new_user)
        return AddUser(user=new_user)

## Mutation class
class Mutation(ObjectType):
    add_user = AddUser.Field()

## Create schema
schema = Schema(query=Query, mutation=Mutation)

app = Flask(__name__)

@app.route("/graphql", methods=["POST"])
def graphql():
    data = request.get_json()
    result = schema.execute(data.get("query"), variables=data.get("variables"))
    return jsonify(result.data)

if __name__ == "__main__":
    app.run(debug=True)
