from .time_helper import now

def read_audio(request):
    filename = f"temp/{str(now())}"
    file = request.files["audio"]
    file.save(f"{filename}.pcm")
    return filename