from flask import Flask

app = Flask(__name__)
PORT = 3001

@app.route("/")
def hello_world():
  return {"message": "Hello, world!"}, 200

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port=PORT)
