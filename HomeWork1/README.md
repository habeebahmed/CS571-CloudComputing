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