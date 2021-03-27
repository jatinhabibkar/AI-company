## AI-company

## tested on linux ubuntu 20.10 x86_64 Python version 3.8

## ener in project by this commands
` cd project `

I have useded nosql database mongodb as it is schema less and as images contain more then one object it is easy to store all name and coordinate in the same document location without join Operation
## install mongo also assuming know how to install mongo on linux
`sudo apt-get install -y mongodb-org`

## start mongo
`sudo systemctl start mongod`



## create virual env
`python3 -m venv venv`

## activate 
`source venv/bin/activate`

## install dependences
`pip3 install -r req.txt`

## run the app
`python3 app.py`

## app running on 
`http://localhost:5000/`
