import vlc
import pafy
import time

def play_video(duration, url):

    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url

    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()

    end = time.time() + duration

    while True:
        if time.time() > end:
            player.stop()