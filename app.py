from database import Database
from models.post import Post

Database.initialize()

posts = Post.from_blog(123)

for post in posts:
    print(post)

