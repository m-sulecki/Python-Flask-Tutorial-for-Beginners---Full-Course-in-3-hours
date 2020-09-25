from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default = 'N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post ' + str(self.id)


all_posts = [
    # {
    #     'title': 'Post 1',
    #     'content': 'This is the content of post 1.'
    # },

    #  {
    #     'title': 'Post 2',
    #     'content': 'This is the content of post 2.',
    #     'author': 'Aaron',
    # },

    #  {
    #     'title': 'Post 3',
    #     'content': 'This is the content of post 3.'
    # },
]

@app.route('/')
def index():
    # return "<h1>Home Page</h1>"
    return render_template('index.html')

@app.route('/posts', methods=['GET', 'POST'])
def posts():

    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        new_post = BlogPost(title=post_title, content=post_title, author='Aaron')
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
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