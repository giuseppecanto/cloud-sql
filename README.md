# Cloud SQL

Cloud SQL is a fully-managed database service that makes it easy to set up, maintain, manage, and administer your relational databases on Google Cloud Platform.

## **How to connect**

To connect to Cloud SQL there are several available options:

- From local environment for testing purposes
- From _App Engine_, _Cloud Run_, and more.

## **Local Enviroment**

The local environment can be configured using a local Cloud SQL Proxy.

In short:

1. Install the [Cloud SDK](https://cloud.google.com/sdk/docs)
2. Install and launch the [Cloud SQL Proxy](https://cloud.google.com/sql/docs/mysql/quickstart-proxy-test).
3. Connect using a language-specific solution:
   - Python, pymysql and TCP
