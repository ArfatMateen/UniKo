from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        user_email = request.form["email"]

        with open('emails.txt', 'a+') as file:
            file.seek(0)
            emails = file.readlines()

            for email in emails:
                if email == f"{user_email}\n":
                    return "ERROR! This email is already in the list."

            file.write(f"{user_email}\n")
            return "You signed up for newsletter successfully."
    else:
        return render_template("index.html")

@app.route("/index_schedule.html")
def index_schedule():
    return render_template("index_schedule.html")

if __name__ == "__main__":
    app.run(debug=True)
