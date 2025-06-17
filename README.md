# 🎬 Clipo AI Backend

A FastAPI-based video upload and processing backend using MongoDB, Celery, Redis, and FFmpeg.

## 📦 Tech Stack

- **FastAPI** (async API server)
- **MongoDB** via `pymongo` (sync)
- **Celery** + **Redis** (background processing)
- **FFmpeg** (video processing)
- **Python 3.9+**

---

## 🚀 Features

- Upload and store video files
- Background job to extract video metadata and generate thumbnail
- View job status and final metadata

---

## 🖥️ Local Setup Instructions

### ✅ Prerequisites

Make sure the following are installed:

- Python 3.9+
- pip
- MongoDB
- Redis
- FFmpeg

---

### 📁 Clone the Repo

```bash
git clone https://github.com/kishoretocs/CLIPO
cd clipo-ai-backend


🧪 Create & Activate Virtual Environment

python3 -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
📦 Install Dependencies

pip install -r requirements.txt
🛠️ Create Required Directories

mkdir -p videos thumbnails
🧱 Starting Services
Open separate terminals for each service.

1️⃣ Start MongoDB
If MongoDB is installed as a service:


sudo systemctl start mongod
Or run manually:


mongod --dbpath ~/data/db
2️⃣ Start Redis

redis-server
3️⃣ Start FastAPI Server
In your project folder with virtualenv activated:


uvicorn app.main:app --reload
Visit: http://localhost:8000/docs

4️⃣ Start Celery Worker
In a new terminal:

source venv/bin/activate
celery -A app.celery_worker.app worker --loglevel=info
🧪 API Endpoints
📤 POST /upload-video/
Upload a video file via multipart/form-data.

📊 GET /video-status/{id}
Check the processing status of a video (pending, processing, done).

📋 GET /video-metadata/{id}
Get full metadata after processing:

{
  "filename": "example.mp4",
  "upload_time": "2025-06-14T10:00:00",
  "status": "done",
  "duration": "00:02:45",
  "thumbnail_url": "http://localhost:8000/thumbnails/example.jpg"
}
🧾 Project Structure

CLIPO/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── tasks.py
│   ├── celery_worker.py
│   ├── config.py
│   └── utils.py
├── videos/
├── thumbnails/
├── env/
├── requirements.txt
└── README.md
🐞 Troubleshooting
Issue	Solution
MongoDB not running	sudo systemctl start mongod
Redis connection error	Ensure redis-server is running
Celery not picking jobs	Make sure Redis & MongoDB are up
Thumbnail not showing	Check thumbnails/ folder permissions

✅ Local storage

👤 Author

```
