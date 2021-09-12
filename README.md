# Employee API

Please do following steps to execute the project.

Prerequisites 
- python3.6
- mysql (database)

Project deployment process-
- Navigate into the project directory by cd binmilepoc
- Create a virtual environment by doing command
- python3.6 -m venv dj-venv
- source ./dj-venv/bin/activate
- pip3 install -r requirement.txt (Install all dependencies)

You need to Create an user into mysql and a database and add basic info of database into .env file
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306


then do
- python3.6 manage.py makemigrations
- python3.6 manage.py migrate
- python3.6 manage.py runserver 8000

use the url to get API info
http://127.0.0.1:8000/docs/

We need to create at-least on department before creating employee, use following to create

curl --location --request POST 'http://127.0.0.1:8000/api/v1/department/' \
--header 'Content-Type: application/json' \
--data-raw '{"name":"Technology"}'

To create Employee
curl --location --request POST 'http://127.0.0.1:8000/api/v1/employee/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name":"Vijay",
    "last_name": "Pal",
    "gender": "M",
    "job_title":"SSE",
    "department":1,
    "salary":20000
    }'
