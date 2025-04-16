from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Define configuration
UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"mp3", "wav", "ogg"}  # Allowed audio formats
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create the uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function to check allowed extensions
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/games")
def games():
    return render_template("games.html")

@app.route("/music", methods=["GET", "POST"])
def music():
    if request.method == "POST":
        # Check if a file was uploaded
        if "musicFile" not in request.files:
            return render_template("music.html", error="No file selected!", music_file=None)
        
        file = request.files["musicFile"]

        # Check if the uploaded file is valid
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  # Secure filename to prevent malicious input
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            
            # Save the uploaded file
            file.save(filepath)
            
            # Return only "uploads/filename.mp3" for rendering
            return render_template("music.html", music_file=f"uploads/{filename}")
        else:
            return render_template("music.html", error="Invalid file type! Please upload an audio file.", music_file=None)
    
    return render_template("music.html", music_file=None)

@app.route("/videos")
def videos():
    return render_template("videos.html")

if __name__ == "__main__":
    app.run(debug=True)

#Flask helps us build a simple website.
# render_template is used to show HTML pages.
# request allows us to handle things like file uploads.
# os helps us manage files and folders.

#This creates our web app and makes it ready to run.
# Define the uploads folder path

#We tell Flask that all uploaded music files should be saved in a folder called "static/uploads".
# Create the uploads folder if it doesn't exist

# If the "uploads" folder does not exist, this creates it.
# This is like creating a drawer before putting files inside

#When someone visits the homepage, they see "index.html"

#When someone visits /games, they see "games.html".

            # Ensure the path is correctly used in HTML and it will Return only "uploads/filename.mp3"
           
# If the user just visits the page, it shows "music.html".
# If the user uploads a music file:
# The file is saved inside "static/uploads".
# The page updates and shows the uploaded music.
#then you can play the music file.

# When someone visits /videos, they see "videos.html".
# This page will play a list of videos .

# This starts the Flask website when you run the file.
# debug=True helps find errors easily.

