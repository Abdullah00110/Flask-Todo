from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Practice():
    return render_template('index.html')

    # return 'hello World'


@app.route('/products')
def products():
    return 'This is prod'


if __name__ == '__main__':
    app.run(debug=True , port=8000)
        