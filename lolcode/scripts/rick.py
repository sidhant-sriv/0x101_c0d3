# This is some bullshit code that you are writing at 2 am because you are a garbage person.
import os
from flask import Flask,redirect
app = Flask(__name__)
# This is the stupidest fucking idea, why are you doing this shit
@app.route('/')
def hello():
    return redirect("https://youtu.be/dQw4w9WgXcQ",code=302)
if __name__=='__main__':
    #fucking port 5000 normie
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port)
#Remember to add flask environment and do flask run, don't forget like the idiot you are

