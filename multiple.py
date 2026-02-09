# multiple inheritance

class camera:
    def __init__(self, camera_quality):
        self.camera_quality = camera_quality
    def display_camera_details(self):
        print(f"Camera quality: {self.camera_quality}")    

class MusicPlayer:
    def __init__(self, sound_quality):
        self.sound_quality = sound_quality
    def display_music_details(self):
        print(f"Sound quality: {self.sound_quality}")

class Smartphone(camera, MusicPlayer):
    def __init__(self, camera_quality, sound_quality):
        camera.__init__(self, camera_quality)
        MusicPlayer.__init__(self, sound_quality)
    def display_smartphone_details(self):
        self.display_camera_details()
        self.display_music_details()

obj = Smartphone("12MP", "High")
obj.display_smartphone_details()                        