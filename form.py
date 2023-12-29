# importing Flask and other modules
from flask import Flask, request, render_template, redirect, url_for
import functions
import os

user = os.environ.get('USERNAME')

# Flask constructor
app = Flask('__name__', template_folder = rf'C:\Users\{user}\Desktop\Project') 
summonerName = ""

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def getSummonerName():
   if request.method == "POST":
      # getting input with name = fname in HTML form
      summonerName = request.form.get("sname")
      return redirect(url_for('tellingSummonerStats', summonerName=summonerName))
   return render_template("index.html")

# A decorator used to tell the application
# which URL is associated function
@app.route('/stats', methods =["GET", "POST"])
def tellingSummonerStats():
   summonerName = request.args.get('summonerName')
   levelCheck = functions.levelCheck(summonerName)
   return render_template("summonerStats.html", levelCheck = levelCheck)

if __name__=='__main__':
   app.debug = True
   app.run()