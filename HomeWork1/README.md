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


<img width="1169" alt="image" src="https://user-images.githubusercontent.com/36078669/216456045-6f564e6a-e6ec-4986-abf0-32a0619aaebc.png">
    
<img width="1247" alt="image" src="https://user-images.githubusercontent.com/36078669/216456311-0da0eecb-e0c1-4155-a149-876611616371.png">

<img width="1026" alt="image" src="https://user-images.githubusercontent.com/36078669/216456365-1b68ad10-184f-4f69-b48e-90f755632b88.png">


<img width="563" alt="image" src="https://user-images.githubusercontent.com/36078669/216456556-a0fd1de6-0650-4f65-b700-e5a2fd63cc42.png">

 

