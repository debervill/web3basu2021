from flask import render_template, Flask, request, redirect
from flask.templating import render_template
import app_config

app = Flask(__name__)
app.config.from_object(app_config)


@app.route('/', methods=['GET', 'POST'])
def index():

	if request.method == "POST":
		user_email= request.form.get('semail1')
		user_name = request.form.get('fname')
		user_famila = request.form.get('ffamilia')
		
		print(user_email)
		print(user_name)
		print(user_famila)

		return redirect(request.url)
	
	return render_template('index.html')

@app.route('/form')
def gb():
	return render_template('2.html')



if __name__ == '__main__':
	app.jinja_env.auto_reload = True
	app.run(debug=True, host='0.0.0.0', port='1234')