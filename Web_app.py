from flask import Flask, render_template, url_for
from Weather import weatherAPI, weather_type_img
from Forms import addressForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'

@app.route('/', methods = ['GET', 'POST'])
def page():
	dates = weatherAPI.build_weathers('Pilar, Buenos Aires, Argentina')
	form = addressForm()
	if form.validate_on_submit():
		dates = weatherAPI.build_weathers(form.address.data)
	return render_template("page.html", dates= dates, form = form, weather_img = weather_type_img)

if __name__ == '__main__':
	app.run(debug=True)
