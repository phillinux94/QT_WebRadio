# Copyright Philippe Labbe 2019
#!/usr/bin/python3

import vlc
import time

class Radio:

    def __init__(self):

        self.instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
        self.player = self.instance.media_player_new()

    def setRadioFg(self):

        url = 'http://radiofg.impek.com/fg'
        media = self.instance.media_new(url)
        self.player.set_media(media)

        self.player.stop()

        self.player.play()

    def setRadioNRJ(self):
        
        url = 'http://cdn.nrjaudio.fm/audio1/fr/30001/mp3_128.mp3?origine=fluxradios'
        media = self.instance.media_new(url)
        self.player.set_media(media)

        self.player.stop()
        self.player.play()
    
    def setRadioCherieFM(self):
        url = 'http://cdn.nrjaudio.fm/audio1/fr/30201/mp3_128.mp3?origine=fluxradios'
        media = self.instance.media_new(url)
        self.player.set_media(media)

        self.player.stop()
        self.player.play()
    
    def setRadioVoltage(self):
        url = 'http://start-voltage.ice.infomaniak.ch/start-voltage-high.mp3'
        media = self.instance.media_new(url)
        self.player.set_media(media)

        self.player.stop()
        self.player.play()

    def setRadioRFM(self):
        url = 'http://rfm-live-mp3-128.scdn.arkena.com/rfm.mp3'
        media = self.instance.media_new(url)
        self.player.set_media(media)

        self.player.stop()
        self.player.play()
    
    def setPlayRadio(self):

        self.player.play()
    
    def setPauseRadio(self):

        self.player.pause()

    def setStopRadio(self):

        self.player.stop()

    def setVolumeRadio(self, volume):

        self.player.audio_set_volume(volume)

    

