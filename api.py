from fastapi import FastAPI, File, UploadFile, Form
from ai_processing import detect_droplets
from PIL import Image
from io import BytesIO

app = FastAPI()

@app.post("/droplet-stats/")
async def get_image_stats(pixel_ratio: float = Form(...), 
                       file: UploadFile = File(...)):
    
    contents = await file.read()
    image = Image.open(BytesIO(contents))
    diameter, diameters_stats, volume, volumes_stats = detect_droplets(image, image.size, pixel_ratio)

    return {
        "diameters" : diameter, 
        "diameters_stats" : diameters_stats,
        "volume" : volume,
        "volumes_stats" : volumes_stats
    }

@app.post("/droplet-boxes/")
async def get_image_boxes(pixel_ratio: float = Form(...), 
                       unit: str = Form(...), 
                       file: UploadFile = File(...)):

    return {"a":"a"}

@app.post("/droplet-stats-and-boxes/")
async def get_image_stats_and_boxes(pixel_ratio: float = Form(...), 
                       unit: str = Form(...), 
                       file: UploadFile = File(...)):

    return {"a":"a"}

@app.get("/")
def read_root():
    return {"Hello": "World"}