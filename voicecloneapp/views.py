from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from gtts import gTTS
import os
import uuid

def home(request):
    return render(request, 'voicecloneapp/home.html')

def generate_speech(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if not text:
            return HttpResponse("No text provided", status=400)

        filename = f"speech_{uuid.uuid4().hex}.mp3"
        filepath = os.path.join('media', filename)

        tts = gTTS(text)
        tts.save(filepath)

        return render(request, 'voicecloneapp/home.html', {
            'audio_file': filename,
            'text': text,
        })
    return HttpResponse("Invalid request", status=405)
