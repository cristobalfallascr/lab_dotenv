import os
from dotenv import load_dotenv, dotenv_values

from flask import Flask
from flask_cors import CORS

load_dotenv()

print(os.getenv("TEST1"))
print(os.getenv("TEST_2"))

app = Flask(__name__)
CORS(app)

app.get("/")(lambda: f"Hello World! {os.getenv("TEST1")} and now also {os.getenv("TEST_2")}...." )