from flask import Flask, render_template, url_for

app = Flask(__name__)

posts= [
    {
        'author': 'João Henrique Cordeiro',
        'title': 'Blog Post 1',
        'content': 'First Blog Post',
        'data_posted': 'April 1, 2025'
    },

    {
        'author': 'Geovana Remes Gomes Araujo',
        'title': 'Blog Post 2',
        'content': 'Second Blog Post',
        'data_posted': 'April 2, 2025'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
@app.route("/about")
def about():
    return render_template('about.html', title = 'About')


if __name__ == '__main__':
    app.run(debug=True)

