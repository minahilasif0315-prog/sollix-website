from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "sollix-secret-key"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/values')
def values():
    return render_template('values.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':

        name = request.form.get('name')
        company = request.form.get('company')
        email = request.form.get('email')
        phone = request.form.get('phone')
        service = request.form.get('service')
        message = request.form.get('message')

        print("\n------------------------------")
        print("NEW SOLLIX INQUIRY")
        print("------------------------------")
        print("Name:", name)
        print("Company:", company)
        print("Email:", email)
        print("Phone:", phone)
        print("Service:", service)
        print("Message:", message)
        print("------------------------------\n")

        flash(
            "Thank you. Your inquiry has been submitted successfully.",
            "success"
        )

        return redirect(url_for('contact'))

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)