from flask import Flask, render_template, request
from bot import chatWithGPT
from waitress import serve
import textwrap

app = Flask(__name__) # defines flask app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/handlePrompt')
def handlePrompt():
    query = request.form.get('query')

    reponse = ""

    reponse = chatWithGPT(query)

    #reponse = "INVALID API KEY!"
    return render_template(
        "botResponse.html",
        help_desk_text = textwrap.fill(reponse, width=200)
    )



if __name__ == "__main__":
    # host="0.0.0.0" for local machine
    serve(app,host="0.0.0.0", port=8000)