from celery import Celery
from app.models import video_collection
from app.utils import extract_duration,generate_thumbnail
from app.config import REDIS_BROKER,VIDEO_DIR,THUMBNAIL_DIR

app = Celery("tasks",broker=REDIS_BROKER)

@app.task
def process_video(video_id:str):
    doc = video_collection.find_one({"id":video_id})
    if not doc:
        return
    
    video_path = VIDEO_DIR / doc['filename']
    duration_str = extract_duration(str(video_path))
    duration_seconds = sum(x * int(t) for x,t in zip([60,1],duration_str.split(":")))

    thumbnail_filename = f"{video_path.stem}.jpg"
    thumbnail_path = THUMBNAIL_DIR/ thumbnail_filename
    generate_thumbnail(str(video_path), str(thumbnail_path),duration_seconds)
    video_collection.update_one(
            {"_id": video_id},
            {"$set": {
                "duration": duration_str,
                "thumbnail_url": f"http://localhost:8000/thumbnails/{thumbnail_filename}",
                "status": "done"
            }}
        )