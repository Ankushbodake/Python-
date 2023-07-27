from flask import Flask
app=Flask(__name__)

@app.route('/')
def hellow_word():
    return ' hellow,word!'

if __name__==__main__:
    app.run(debug=True)