from flask import Flask

app = Flask(__name__)

@app.route('/color')
def color():
    return f"Sevimli rangim qora"

@app.route('/food')
def food():
    return f"Sevimli ovqatim osh"

@app.route('/hobby')
def hobby():
    return f"Hobbiyim futbol"
 
    
if __name__ == '__main__':
    app.run(debug=True)
