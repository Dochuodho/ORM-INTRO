import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE users (
    id INT PRIMARY KEY,
    official_name VARCHAR(100)
    username VARCHAR(50)
    
    );


    """
)

cursor.execute(
    """
    CREATE TABLE posts (
    id INT PRIMARY KEY,
    caption VARCHAR(200),
    photo_url VARCHAR(20)
    );

    """

)

conn.commit()

#create user
class User:
    def __init__(self, id, official_name, username):
        self.id = id
        self.official_name = official_name
        self.username = username

class Post:
    def __init__(self, id, caption, photo_url):
        self.id = id
        self.caption = caption
        self.photo_url = photo_url

def create_user(user):
        cursor.execute("INSERT INTO users(id, official_name, username) VALUES (?, ?,?)")
        cursor.commit()

def get_users():
     cursor.execute("SELECT * FROM users")
     rows = cursor.fetchall()
     for i in rows:
          id,off_name, username = i
          userObj = {
               "id" :id,
               "officialName":off_name,
               "username": username

          }
          return userObj

#create POSTS
def create_post(post):
     cursor.execute("INSERT INTO posts (caption, photo_url) VALUES (?,?)")
     cursor.commit() 

def get_posts():
     cursor.execute("SELECT * FROM posts")
     rows = cursor.fetchall()
     return [Post(*rows) for row in rows]


if __name__ == "__main__":
     #user1 = User(1, "Derrick","Ochuodho")
     #create_user(user1)

     users = get_users()
     print(users.get("off_name"))

     
    
          