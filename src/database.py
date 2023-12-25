from datetime import datetime
from enum import unique
from flask_sqlalchemy import SQLAlchemy
import string
import random

db = SQLAlchemy()

class User(db.Model):
    id=db.column(db.Integer, primary_key=True)
    username= db.column(db.String(80), unique=True, nullable=False)
    email= db.column(db.String(150), unique=True, nullable=False)
    password= db.column(db.Text(), nullable=False)
    created_at = db.column(db.DateTime, default=datetime.now())
    update_at = db.column(db.DateTime, onupdate=datetime.now())
    bookmarks = db.relationship('Bookmark', backref="user")

    def __repr__(self) -> str:
        return 'User>>> {self.username}'
    

class Bookmark(db.Model):
      id=db.column(db.Integer, primary_key=True)
      body= db.column(db.Text, nullable=True)
      url= db.column(db.Text,  nullable=False)
      short_url = db.column(db.String(3), nullable=True)
      visits= db.column(db.Tnteger, default=0)
      user_id = db.column(db.Integer, db.ForeingKey('user.id'))
      created_at = db.column(db.DateTime, default=datetime.now())
      update_at = db.column(db.DateTime, onupdate=datetime.now())      
      
      def generate_short_caracters(self):
          characters = string.digits+string.ascii_letters
          picked_chars = ''.join(random.choices(characters, k=3))
          
          if link:
              self.generate_short_caracters()
          else:
              return picked_chars
      
      def __init__(self, **kwargs):
          super().__init__(**kwargs)
          
          self.short_url = self.generate_short_caracters()
      
      def __repr__(self) -> str:
         return 'Bookmark>>> {self.url}'