from flask import Flask, render_template, jsonify  # Imorting the flask framework and returns json object and one renders HTMl object .
import requests # Importing the request package for script
from api_key import key  # Importing the API key value from the key file.
app = Flask(__name__)   #Here we are creating the flask app import the flask.

searchtext_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"  #API url for text search taken from API google developers guide object type is json
detailstext_url = "https://maps.googleapis.com/maps/api/place/details/json"   # API url for place details taken from API google developers guide


@app.route("/", methods=["GET"])  # here we are using the GET mothod to fetch details and used app.route
def retreive(): # Funtion defined
    return render_template('search_page.html')  # the route on the render_template returns the search page

@app.route("/sendRequest/<string:query>")  # The send request will take in the query
def results(query):
    print(query)   # test
    # here we create a payload object where keys and values of the data is being sent over.
    # same way we create a request object
    search_payload = {"key":key, "query": query} # at payload the mandatory parameters are key = api key and query i.e a text string on which search needs to be performed.
    search_request = requests.get(searchtext_url, params=search_payload) # we are sending it to search url and params value is the value in search payload . This will give output as response
    search_json = search_request.json()  # This will convert the above returned value in the Json format.
    print(search_json)  # test print
    place_id = search_json["results"][0]["place_id"]  #  For the URL to search in the JSON extracted we take the oth index of result and in that the place_id

# The same things are performed for the second API url .
    details_payload = {"key":key, "placeid":place_id}
    details_response = requests.get(detailstext_url, params=details_payload)
    details_json = details_response.json()

    print(details_json)
    url = details_json["result"]["url"]  # The url is returned from the JSOn
    print(url)
    return jsonify({'result': url})


if __name__ == "__main__":  # THis commands says that start the webserver
    app.run(debug=True)
