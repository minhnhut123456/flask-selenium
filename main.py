# main.py

from flask import Flask, send_file
from selenium import webdriver

app = Flask(__name__)

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Remote(
    command_executor='http://chrome-driver:4444/wd/hub',
    options=options
)

@app.route("/")
def hello_world():
    driver.get("https://www.google.com/")
    driver.save_screenshot("spooky.png")
    return send_file("spooky.png")
