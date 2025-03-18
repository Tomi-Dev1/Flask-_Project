from flask import Flask, render_template, request
import os
#Flask helps us build a simple website.
# render_template is used to show HTML pages.
# request allows us to handle things like file uploads.
# os helps us manage files and folders.
app = Flask(__name__)
#This creates our web app and makes it ready to run.
# Define the uploads folder path
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
#We tell Flask that all uploaded music files should be saved in a folder called "static/uploads".
# Create the uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
# If the "uploads" folder does not exist, this creates it.
# This is like creating a drawer before putting files inside
@app.route("/")  
def home():
    return render_template("index.html")
#When someone visits the homepage, they see "index.html"
@app.route("/games")  
def games():
    return render_template("games.html")
#When someone visits /games, they see "games.html".
@app.route("/music", methods=["GET", "POST"])
def music():
    if request.method == "POST":
        file = request.files["musicFile"]
        if file:
            filename = file.filename  # Get the filename
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)  # Save path
            file.save(filepath)  # Save file
            # Ensure the path is correctly used in HTML and it will Return only "uploads/filename.mp3"
            return render_template("music.html", music_file=f"uploads/{filename}")
    return render_template("music.html", music_file=None)
# If the user just visits the page, it shows "music.html".
# If the user uploads a music file:
# The file is saved inside "static/uploads".
# The page updates and shows the uploaded music.
#then you can play the music file.
@app.route("/videos")  
def videos():
    return render_template("videos.html")
# When someone visits /videos, they see "videos.html".
# This page will play a list of videos .
if __name__ == "__main__":
    app.run(debug=True)
# This starts the Flask website when you run the file.
# debug=True helps find errors easily.

