from app import PyFrameApp

app = PyFrameApp()

@app.route("/home")
def home(request, response):
    response.text = "Hello from the home page"

@app.route("/about")
def about(request, response):
    response.text = "Hello from the about page"