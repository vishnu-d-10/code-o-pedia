from flask import Flask, render_template

app = Flask(__name__)

# Sample blog posts (you can replace these with your own data)
posts = [
    {
        'title': 'Art Exhibit 1',
        'content': 'This is the first art exhibit I want to share.',
        'date_posted': 'August 26, 2023'
    },
    {
        'title': 'Art Exhibit 2',
        'content': 'The second art exhibit is now live!',
        'date_posted': 'August 27, 2023'
    }
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
