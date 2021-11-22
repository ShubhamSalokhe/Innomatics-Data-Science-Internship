from flask import Flask, render_template ,request
import re


######################################
app = Flask(__name__)


#####################################

@app.route('/')
def home_get():
    return render_template("index.html")

@app.route('/',methods = ['POST'])
def home_post():
    string_ = request.form.get("in_1")
    regex = request.form.get("in_2")
    if string_ =="":
        return render_template("index.html",empty ="Fill with string")
    elif regex =="":
        return render_template("index.html",empty ="Fill with Regular Expression")

    else:
        lst = re.findall(regex, string_)
        length = len(lst)
        Matches = ("We have found {} Matches".format(length))
        return render_template("index.html",data= lst, match = Matches, string_show = string_, regex_show = regex) 





#####################################3
if __name__ == "__main__":
    app.run(debug=True)