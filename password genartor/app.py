from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)


def algo_1(b):
    a = [
        "A", "B", "C", "D", "E", "F", "G", 
        "H", "I", "J", "K", "L", "M", "N", 
        "O", "P", "Q", "R", "S", "T", "U", 
        "V", "W", "X", "Y", "Z"
    ]
    
   # b=input()
    output=""
    for i in b :
        I=i.upper()
        if I in a:
            pos=a.index(I)
            if pos==len(a)-1:
                pos=0
            else:
                pos+=1
        output=output+a[pos]
    output=output.lower()
    output=output[0].upper()+output[1:]
    return output

@app.route("/",methods=["GET","POST"])

def main():
	if request.method=="GET":
   		return render_template("index.html")
	elif request.method=="POST":
		a=request.form["0"]
		b=request.form["1"]
		c=algo_1(a)
		c=c+'@'+b
		return render_template("2.html",l=c)

#app.debug=True
app.run()