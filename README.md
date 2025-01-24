Directions to use:

The API will be available at http://127.0.0.1:5000/graphql

You can use this with postman or curl 

Ex:- Fetching all the users (Request Body)
{
  "query": "{ allUsers { id name email } }"
}

The expected output should be:
{
  "data": {
    "allUsers": []
  }
}
