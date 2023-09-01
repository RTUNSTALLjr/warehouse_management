from flask import render_template
from flask_app import app

@app.route("/")
def admin_home():
    return render_template("/admin/site_admin.html")