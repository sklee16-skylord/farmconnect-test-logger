from flask import Flask, request

app = Flask(__name__)
@app.route("/")
def home():
    return "FarmConnect Logger is running!"


@app.route("/log", methods=["GET", "POST"])
def log():
    print("===== NEW REQUEST RECEIVED =====")
    print("Method:", request.method)
    print("Query Params:", request.args.to_dict())
    print("Form Data:", request.form.to_dict())
    print("Headers:", dict(request.headers))
    print("Raw Body:", request.get_data(as_text=True))
    print("================================")
    return "logged", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

