from flask import Flask

app = Flask(__name__)
fp =open('log.html', encoding='utf8')
html = fp.read()
fp.close()
@app.route('/report')
def report():
    return html

if __name__ == '__main__':
    app.run(debug=True)