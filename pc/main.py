from flask import Flask, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

from update import VisualizationState, startUpdater, endUpdater
from patterns import sectionCallback, barCallback, beatCallback, tatumCallback, segmentCallback, genericCallback

sp  = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-read-playback-state", redirect_uri='http://127.0.0.1:5001'))
vs  = VisualizationState("/dev/ttyUSB0", 180, sectionCallback, barCallback, beatCallback, tatumCallback, segmentCallback, genericCallback)
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1><a href=/test>Test</a></h1><br>" \
        "<h1><a href=/start>Start</a></h1>"

@app.route('/start')
def start():
    global vs
    track = sp.current_playback()
    if track is None:
        return "No track playing right now"
    analysis = sp.audio_analysis(track["item"]["id"])
    start = time.time()
    track = sp.current_playback()
    endUpdater()
    print((time.time() - start) * 0.6)
    startUpdater(vs, analysis, track["progress_ms"] / 1000 + (time.time() - start) * 0.6)
    return redirect("/")