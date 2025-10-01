import json

from app.database import LocalSession, initial_db
from app.models.user import User
from app.models.post import Post
from app.models.comment import Comment

initial_db()

def insert_users():
    with open('demo/users.json') as jsonfile:
        data = json.load(jsonfile)

    users = []
    for item in data:
        user = User(
            first_name=item['first_name'],
            last_name=item['last_name'],
            username=item['username'],
            gender=item['gender'],
            phone=item['phone']
        )

        users.append(user)

    db = LocalSession()
    db.bulk_save_objects(users)
    db.commit()


def insert_posts():
    with open('demo/posts.json') as jsonfile:
        data = json.load(jsonfile)

    posts = []
    for item in data:
        post = Post(
            title=item['title'],
            description=item['description'],
            author_id=item['author_id']
        )

        posts.append(post)

    db = LocalSession()
    db.bulk_save_objects(posts)
    db.commit()


def insert_comments():
    with open('demo/comments.json') as jsonfile:
        data = json.load(jsonfile)

    comments = []
    for item in data:
        comment = Comment(
            text=item['text'],
            user_id=item['author_id'],
            post_id=item['post_id']
        )

        if comment.text is None:
            print(comment)

        comments.append(comment)

    db = LocalSession()
    db.bulk_save_objects(comments)
    db.commit()

insert_comments()

