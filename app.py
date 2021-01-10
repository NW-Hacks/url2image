from flask import Flask,request,jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_query_string():
    data = request.args.getlist('key')[0]
    print(data)
    import base64
    from PIL import Image
    from io import BytesIO

    im = Image.open(BytesIO(base64.b64decode(data)))
    im.save('image.png', 'PNG')
    return data



if __name__ == '__main__':
    app.run(debug=True)


