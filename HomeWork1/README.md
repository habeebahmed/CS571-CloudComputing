## Microservice Weather Stats using Python(Flask)

# Steps to run
1. Install the following packages 
    $ pip install requests flask
2. Run the ServerTwo before running the first server
    $ python3 ServerTwo.py
3. Run the ServerOne
    $ python3 ServerOne.py

# Test
Use the following api to test based on city name and state name
http://localhost:5000/zipcode/<state short form>/<city name>

examples:
http://localhost:5000/zipcode/ca/fremont

http://localhost:5000/zipcode/ca/dublin

# Limitation
Need to specify state acronym for the api to work


# Docker build and deploy
## Server Two
- $ cd ServiceWeather
- $ docker build -t flask-app2:latest .
- $ docker run -d -p 9000:9000 flask-app2

## Server One
- $ cd ServiceZipCode

- `Make sure to replace the Internal IP of Server Two container in ServerOne at line 16, for me it was "172.17.0.4"`
- $ docker build -t flask-app:latest .
- $ docker run -d -p 5000:5000 flask-app