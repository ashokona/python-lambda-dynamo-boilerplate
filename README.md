## Setup & Deploy
node version 16 to install serverless package.
## Setup & Deploy

```bash
npm install -g serverless
```
In order to deploy the endpoint simply run

```bash
serverless deploy
```

#Test api's

Create User
```bash
curl -X POST https://<uniqueid>.execute-api.us-east-1.amazonaws.com/create --data '{ "name": "ashok k", email: "ashokona47@gmail.com", address: "Hyderabad, India" }' -H "Content-Type: application/json"
```
List users
```bash
curl https://<uniqueid>.execute-api.us-east-1.amazonaws.com/user
```

Fetch one user
```bash
curl https://<uniqueid>.execute-api.us-east-1.amazonaws.com/user/<id>
```

Update user
```bash
curl -X PUT https://<uniqueid>.execute-api.us-east-1.amazonaws.com/user/<id> --data '{ "address": "Hyderabad, India."}' -H "Content-Type: application/json"
```

delete user
```bash
curl -X DELETE https://<uniqueid>.execute-api.us-east-1.amazonaws.com/user/<id>
```# python-lambda-dynamo-boilerplate
