import os


#  set environment variable
os.environ["password"] = "12345"

# get environment variable
# method 1
env = os.getenv("password")
print(env)

# method 1
env1 = os.environ.get("password")
print(env1)