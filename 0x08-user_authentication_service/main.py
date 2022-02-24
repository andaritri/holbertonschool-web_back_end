#!/usr/bin/env python3
"""
Main file
"""
# from user import User

# print(User.__tablename__)

# for column in User.__table__.columns:
#     print("{}: {}".format(column, column.type))
#####################################################
# from db import DB
# from user import User

# my_db = DB()

# user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
# print(user_1.id)

# user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
# print(user_2.id)
#####################################################
# from db import DB
# from user import User

# from sqlalchemy.exc import InvalidRequestError
# from sqlalchemy.orm.exc import NoResultFound


# my_db = DB()

# email = 'test@test.com'
# hashed_password = "hashedPwd"

# user = my_db.add_user(email, hashed_password)
# print(user.id)

# try:
#     my_db.update_user(user.id, hashed_password='NewPwd')
#     print("Password updated")
# except ValueError:
#     print("Error")

##################################################
from auth import _hash_password

print(_hash_password("Hello Holberton"))
