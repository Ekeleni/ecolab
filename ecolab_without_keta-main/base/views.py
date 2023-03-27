from flask import Flask, render_template, request, redirect, url_for
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    return render_template('./index.html')


@app.route('/registration', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        user = [form.username.data, form.email.data,
                    form.password.data]
        return redirect(url_for('auth'))
    return render_template('register.html', form=form)

@app.route('/login', methods = ['GET', 'POST'])
def auth():
    form = LoginForm(request.form)
    user = [form.username.data, form.password.data]
    return render_template('log_page.html', title = 'Sign In', form = form)


app.run(host="0.0.0.0")