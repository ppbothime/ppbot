from image_upload import ImageTweet
from utilities import *
import cv2
import random
import os.path

import requests

from auth import *

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/health')
def health():
    tweet()
    return '200 OK'

@app.route('/auth')
def auth():
    getGoogleAuth()
    return '200 OK'

def ping():

    try:
        r = requests.head("https://oshi.onrender.com")
        print(r.status_code)

    except requests.ConnectionError:
        print("failed to connect")

def tweet():
    
	file = getRandomFile()

	if(file['extension'] == 'mkv'):
		# Load the video file
		video_path = file['title']
		print(video_path)
		cap = cv2.VideoCapture(video_path)

		# Get the total number of frames in the video
		total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

		# Generate a random frame number
		random_frame = random.randint(0, total_frames)

		# Set the video frame position to the random frame
		cap.set(cv2.CAP_PROP_POS_FRAMES, random_frame)

		# Read the frame
		ret, frame = cap.read()

		# Check if the frame variable is not empty
		if ret:
			# Extract the video file name and timestamp
			video_name = os.path.splitext(os.path.basename(video_path))[0]
			timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) // 1000
			timestamp = int(timestamp)
			timestamp_str = "{:02d}h{:02d}m{:02d}s".format(timestamp//3600, (timestamp//60)%60, timestamp%60)
			
			# Construct the output file name
			frame_name = f"{video_name} - {timestamp_str}.png"
			
			# Save the frame as a PNG file
			cv2.imwrite(frame_name, frame)
			print(f"Random frame {random_frame} saved as {frame_name}")
		else:
			print("Error: Failed to read frame from the video file.")

		# Release the video capture object
		cap.release()
		os.remove(video_path)

	imageTweet = ImageTweet(frame_name)
	imageTweet.tweet()
	
if __name__ == '__main__':
    app.run()
