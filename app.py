from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/quotes", methods=["GET"])
def get_quotes():
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes_list = []
    for quote_block in soup.find_all("div", class_="quote"):
        text = quote_block.find("span", class_="text").get_text()
        author = quote_block.find("small", class_="author").get_text()
        quotes_list.append({"text": text, "author": author})

    return jsonify(quotes_list)

if __name__ == "__main__":
    # 0.0.0.0 makes the server accessible from your LAN (for Flutter app)
    app.run(debug=True, host="0.0.0.0", port=5000)
