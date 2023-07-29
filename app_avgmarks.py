# simple Flask application
from flask import Flask, render_template, request, url_for, redirect

# create flask application
app = Flask(__name__)  # call entry point
@app.route('/')   # route() assign various url
def home():
    return "welcome to home page"  

@app.route('/index')   # route() assign various url
def index():
    return render_template('index.html')   # use html template to execute
    # render_template takes all html file from templates folder
@app.route('/welcome')   # route() assign various url
def welcome():
    return "<h2>Welcome to Flask tutorail page!<h2/>"    # may use html tags <h1>, <p>,.. so on

# A simple use case: return marks which is given in url
@app.route('/success/<int:mark>')
def success(mark):
    return "Got Pass and the mark is: "+str(mark)   # str - return string by default

@app.route('/fail/<int:mark>')
def fail(mark):
    return "Got fail and the mark is: "+str(mark)   # str - return string by default

@app.route('/calculate', methods=["GET", "POST"])     # methods: GET and POST are getting url and submitting the from
def calculate():
    if request.method == "GET":
        return render_template('calculate.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        physics = float(request.form['physics'])

        avg = int((maths+science+physics)/3)
        return render_template('result.html', result=avg)   # result is displaying in another page through result.html
        # return render_template('calculate.html', result=avg)  # result is displaying in the same page
        # Use render_template for the same url page 
        
        """
        # if-else condition wrriten on html page 
        if avg>=50:   # calling different url based on condition
            return redirect(url_for("success",mark=avg))
            # Use redirect to use/redirect for another url page
        else:
            return redirect(url_for("fail",mark=avg))
        """

if __name__ == "__main__":
    app.run(debug = True)   # run() is a Flask method
    # debug = True only in development phase not in production
    # debug : reload the app when see any changes
    