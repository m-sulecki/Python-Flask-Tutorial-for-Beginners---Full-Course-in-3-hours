from flask import Flask, render_template

app = Flask(__name__)

all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is the content of post 1.'
    },

     {
        'title': 'Post 2',
        'content': 'This is the content of post 2.',
        'author': 'Aaron',
    },

     {
        'title': 'Post 3',
        'content': 'This is the content of post 3.'
    },
]

@app.route('/')
def index():
    # return "<h1>Home Page</h1>"
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)

@app.route('/')
@app.route('/home/users/<string:name>/posts/<int:id>')
def hello(name, id):
    return f"Helllo {name}! Your id is: {str(id)}"

@app.route('/onlyget', methods=['GET'])
def get_req():
    return 'You can only get this webpage.'

if __name__ == "__main__":
    app.run(debug=True)