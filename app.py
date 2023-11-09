from flask import Flask, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.secret_key = "mysecretkey"

blueprint = make_google_blueprint(
    client_id="302964484250-657mgtu5o1s81hlk4ll2kjj6k0kcaith.apps.googleusercontent.com",
    client_secret="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",
    scope=["profile", "email"],
)

app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/")
def index():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email = resp.json()["email"]
    return f"Logged in as {email}"

if __name__ == "__main__":
    app.run(debug=True)
