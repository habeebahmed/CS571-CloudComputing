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
<img width="639" alt="image" src="https://user-images.githubusercontent.com/36078669/216307212-12c62f70-d4a7-4a93-9fb5-3a25ee56c884.png">


http://localhost:5000/zipcode/ca/dublin
<img width="480" alt="image" src="https://user-images.githubusercontent.com/36078669/216307328-e770b8d0-43c4-4c39-bc1e-ad2ce78658bc.png">

# Terminal logs:
<img width="1159" alt="image" src="https://user-images.githubusercontent.com/36078669/216307727-308bc273-3601-4fca-b3fb-6e4e42253ad8.png">


# Limitation
Need to specify state acronym for the api to work
