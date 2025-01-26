# GraphQL API 

## **API Endpoint**
The API will be available at:  
`http://127.0.0.1:5000/graphql`

You can use this endpoint with tools like **Postman** or **cURL** to perform GraphQL queries and mutations.

---

## **Examples**

### **1. Fetching All Users**

#### **Request Body**
```json
{
  "query": "{ allUsers { id name email } }"
}
```
The expected output should be:
```json
{
  "data": {
    "allUsers": []
  }
}
```

#### **Example**
Adding a User (Mutation)
```json
{
  "query": "mutation($name: String!, $email: String!) { addUser(name: $name, email: $email) { user { id name email } } }",
  "variables": {
    "name": "User",
    "email": "user@example.com"
  }
}
```
Expected Output should be:
```json
{
  "data": {
    "addUser": {
      "user": {
        "id": 1,
        "name": "User",
        "email": "user@example.com"
      }
    }
  }
}
```

