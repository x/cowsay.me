import os
import pyfortune
import cowsay
from flask import Flask


app = Flask(__name__)


@app.route('/')
def says():
    # fortune -s | cowsay
    s = cowsay.cowsay(pyfortune.Chooser().choose()[1]).rstrip() + '\n'
    return s, 200, {'Content-Type': 'text/plain; charset=UTF-8'}


def main():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)


if __name__ == '__main__':
    main()
