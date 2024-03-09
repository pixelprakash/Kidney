from fastapi import FastAPI, File, UploadFile, Form, Request, Response, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil
import fnmatch
import os
from pathlib import Path
from main import maincode

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

path1 = Path.cwd()
originalimagepath = path1
copyimagepath = os.path.join(path1, 'static', 'uploads', 'displayimages')
pattern = "output.png"


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("das.html", {"request": request})


@app.get("/docto", response_class=HTMLResponse)
async def docto(request: Request):
    return templates.TemplateResponse("docto.html", {"request": request})


@app.get("/doct", response_class=HTMLResponse)
async def doct(request: Request):
    return templates.TemplateResponse("doct.html", {"request": request})


@app.get("/abou", response_class=HTMLResponse)
async def abou(request: Request):
    return templates.TemplateResponse("abou.html", {"request": request})


@app.get("/index", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/diseases", response_class=HTMLResponse)
async def diseases(request: Request):
    return templates.TemplateResponse("diseases.html", {"request": request})


@app.post("/")
async def upload_image(request: Request, file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")
    
    filename = file.filename
    if not allowed_file(filename):
        raise HTTPException(status_code=400, detail="Allowed image types are - png, jpg, jpeg, gif")
    
    contents = await file.read()
    filesavedpath = os.path.join(UPLOAD_FOLDER, filename)
    with open(filesavedpath, "wb") as f:
        f.write(contents)
    
    maincode(filesavedpath)
    
    src_files = os.listdir(originalimagepath)
    for filename in src_files:
        if fnmatch.fnmatch(filename, pattern):
            full_file_name = os.path.join(originalimagepath, filename)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, copyimagepath)
    
    outputsavedpath = os.path.join(app.config['UPLOAD_FOLDER'], 'displayimages', 'output.png')
    return templates.TemplateResponse("index.html", {"request": request, "filenames": outputsavedpath})


@app.get("/display/{filename}", response_class=HTMLResponse)
async def display_image(filename: str):
    return {"filename": filename}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
