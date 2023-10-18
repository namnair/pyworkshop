
from flask import Flask, render_template
import requests
#import random
app = Flask(__name__)

#random_no=random.randint(0,9)

response=requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_blog=response.json()
#print(response[0]["title"])
#for post in response:
 #   print(post["title"])
     #t=response[0]["title"]
    # s=response[0]["subtitle"]


@app.route("/")
def ok():
    return render_template("index.html",posts=all_blog)

@app.route("/bye/<name>")
def say_bye(name):
  #  return render_template("post.html")
  return f"Hey {name}"

@app.route("/blog/<int:id>")
def read(id):
   return render_template("post.html", title=all_blog[id]['title'],body=all_blog[id]['body'])

if __name__=="__main__":
    app.run(debug=True)