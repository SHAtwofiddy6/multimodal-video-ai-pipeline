pip install pyannote.audio git+https://github.com/openai/whisper.git

# audio/audio_processor.py
from pyannote.audio import Pipeline as PyannotePipeline
import whisper

pyannote = PyannotePipeline.from_pretrained("pyannote/speaker-diarization")
whisper_model = whisper.load_model("large")

def diarize_audio(audio_path):
    diarization = pyannote(audio_path)
    segments = []
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        segments.append({'start': turn.start, 'end': turn.end, 'speaker': speaker})
    return segments

def transcribe_audio(audio_path):
    result = whisper_model.transcribe(audio_path)
    return result['text']
