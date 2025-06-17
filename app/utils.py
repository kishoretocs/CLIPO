import subprocess
from app.config import VIDEO_DIR,THUMBNAIL_DIR


def extract_duration(video_path:str):
    cmd=[
        "ffprobe","-v","error",
        "-show_entries","format-duration",
        "-of","default-noprint_wrappers=1:nokey-1",video_path
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
    duration =float(result.stdout.strip())
    minutes = int(duration//60)
    seconds = int(duration % 60)
    return f"{minutes:02}:{seconds:02}"

def generate_thumbnail(video_path:str, thumbnail_path:str,duration:float):
    timestamp = duration*0.01
    cmd = [
        "ffmpeg","-y","-ss",str(timestamp),"-i",video_path,
        "-vframes","1","-q:v","2",thumbnail_path
    ]
    subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)