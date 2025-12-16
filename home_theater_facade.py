from subsystems.dvd_player import DVDPlayer
from subsystems.projector import Projector
from subsystems.sound_system import SoundSystem

class HomeTheaterFacade:
    def __init__(self):
        self.dvd = DVDPlayer()
        self.projector = Projector()
        self.sound = SoundSystem()

    def watch_movie(self, movie):
        print("\nStarting movie...")
        self.projector.on()
        self.sound.on()
        self.sound.set_volume(10)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("\nShutting down movie theater...")
        self.dvd.off()
        self.sound.off()
        self.projector.off()
