from flask import Flask, request

app = Flask(__name__)


@app.route('/PrimeNumber')
def alku_luku():
    args = request.args
    number = int(args.get("number"))
    prime = 0

    if number > 1:
        for i in range(2, number):

            if number % i == 0:
                prime = False
                break
        else:
            prime = True

    vastaus = {
        "Number": number,
        "IsPrime": prime

    }
    return str(vastaus)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port= 3000)