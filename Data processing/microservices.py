# Microservices is an architectural style and pattern that structures an application as a collection of coherent services
# Are a way to organize complex software system
# Microservices are deployed independently and communicate through messages

# Using Flask

from flask import Flask

app = Flask(__name__)

@app.get('/')
def index():
    return "Hello from flask microservice"

if __name__ == '__main__':
    app.run(port=5000, debug=True)