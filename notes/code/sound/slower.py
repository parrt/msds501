import soundfile as sf    # Use this package
import sounddevice as sd  # and this one

kiss, samplerate = sf.read('Kiss.aiff')  # load Kiss.aiff into kiss variable
sd.play(kiss, samplerate*.8)             # play the music at 80% speed
sd.wait()                                # wait until music finishes before exiting
