# importing Flask and other modules
from flask import Flask, request, render_template 
import functions

# Flask constructor
app = Flask('__name__', template_folder = r'C:\Users\James\Desktop\Project') 

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def getSummonerName():
   if request.method == "POST":
      # getting input with name = fname in HTML form
      summonerName = request.form.get("sname")
      return functions.levelCheck(summonerName)
   return render_template("index.html")

if __name__=='__main__':
   app.debug = True
   app.run()
