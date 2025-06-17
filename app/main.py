import shutil
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from bson import ObjectId
from datetime import datetime
from app.models import video_collection
from app.tasks import process_video
from app.config import VIDEO_DIR, THUMBNAIL_DIR

app = FastAPI()

VIDEO_DIR.mkdir(exist_ok=True)
THUMBNAIL_DIR.mkdir(exist_ok=True)

@app.post("/upload-video/")
def upload_video(file: UploadFile = File(...)):
    file_path = VIDEO_DIR / file.filename
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    doc = {
        "filename": file.filename,
        "upload_time": datetime.utcnow().isoformat(),
        "status": "pending"
    }
    result = video_collection.insert_one(doc)
    video_id = str(result.inserted_id)
    process_video.delay(video_id)
    return {"video_id": video_id}

@app.get("/video-status/{video_id}")
def get_status(video_id: str):
    doc = video_collection.find_one({"_id": ObjectId(video_id)})
    if not doc:
        return JSONResponse(status_code=404, content={"error": "Video not found"})
    return {"status": doc["status"]}

@app.get("/video-metadata/{video_id}")
def get_metadata(video_id: str):
    doc = video_collection.find_one({"_id": ObjectId(video_id)})
    if not doc:
        return JSONResponse(status_code=404, content={"error": "Video not found"})
    return doc

@app.get("/thumbnails/{filename}")
def get_thumbnail(filename: str):
    file_path = THUMBNAIL_DIR / filename
    return FileResponse(file_path)
