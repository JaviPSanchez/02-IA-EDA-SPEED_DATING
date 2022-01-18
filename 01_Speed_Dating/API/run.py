from flask import Flask, request, json, jsonify, render_template
import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly
import plotly.express as px

print('Loading server app...')
app = Flask(__name__)
print('Done!')
print()




@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True, port=4000)