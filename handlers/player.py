import wave
import pyaudio

# no?
def audioStream(path: str):
    audio = pyaudio.PyAudio()
    wf = wave.open(path, 'rb')
    stream = audio.open(
        format=audio.get_format_from_width(wf.getsampwidth()),
        channels=2,
        rate=wf.getframerate(),
        output=True
    )

    try:
        while True:
            data = wf.readframes(4096)
            stream.write(data)
        
    except KeyboardInterrupt:
        pass

    stream.close()
    audio.terminate()