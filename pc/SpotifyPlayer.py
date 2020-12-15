import time
from MusicPlaybackState import MusicPlaybackState
from MusicVisualizer import MusicVisualizer

class SpotifyPlayer:
    spotify = None
    visualizer = None

    def __init__(self, spotify, visualizer):
        self.spotify = spotify
        self.visualizer = visualizer

    def startCurrentSongVisualization(self):
        track = self.spotify.current_playback()
        if track is None:
            return "No track playing right now"
        analysis = self.spotify.audio_analysis(track["item"]["id"])
        start = time.time()
        track = self.spotify.current_playback()
        time_offset = track["progress_ms"] / 1000 + (time.time() - start) / 2
        self.visualizer.endVisualization()
        self.visualizer.startVisualization(MusicPlaybackState(analysis, time_offset, MusicVisualizer(self.visualizer.leds), self.endCallback).callback)

    def endCallback(self):
        self.startCurrentSongVisualization()