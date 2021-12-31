## AI-company

## tested on linux ubuntu Python3

I have used sqllite3 database for storing data Django-rest for server side and react for front-end

## api documentations
[Api documentation link](https://documenter.getpostman.com/view/5938078/UVJZpJwa)

# docker installed
## docker 
`docker-compose up --build` 
## App running on 
http://localhost:3000/

# docker not installed
## backend
`cd backend`<br>
`python3 -m venv venv`<br>
`source venv/bin/activate`<br>
`pip install -r requirements.txt`<br>
`python manage.py makemigrations`<br>
`python manage.py migrate`<br>
`python manage.py runserver`<br>
`server running on http://localhost:8000/`
#### or copy paste this 
`cd backend \`<br>
`&& python3 -m venv venv \`<br>
`&& source venv/bin/activate \`<br>
`&& pip install -r requirements.txt \`<br>
`&& python manage.py makemigrations \`<br>
`&& python manage.py migrate \`<br>
`&& python manage.py runserver \ `<br>


#### server running on http://localhost:8000/

## Run the React app
`cd backend/client/ \`<br>
`&& npm install -g serve \`<br>
`&& npm run prod`

## App running on 
http://localhost:3000/


# Website
#### Index page to upload file 
![index_page](./images/index.png)

#### Filter data by dates and report creation
![filter_page](./images/sort.png)
