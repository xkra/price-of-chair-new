import os
from flask import Flask, render_template
from views.alerts import alert_blueprint
from views.users import user_blueprint
from views.stores import store_blueprint


app = Flask(__name__)
app.secret_key = 'lskfjhawnr7ze435t453g45g45g4g45g45hdfghdfghdfjj56hwoiwfhj98wf9'
app.config.update(
	ADMIN=os.environ.get('ADMIN')
)

@app.route('/')
def home():
	return render_template('home.html')

app.register_blueprint(alert_blueprint, url_prefix="/alerts")
app.register_blueprint(store_blueprint, url_prefix="/stores")
app.register_blueprint(user_blueprint, url_prefix="/users")


if __name__ == '__main__':
	app.run(debug=True)