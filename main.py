import uvicorn
from app import get_app
from app.controller.prediction_controller import prediction_router
from fastapi.templating import Jinja2Templates
from fastapi import Request
import os
from pathlib import Path

project_path = Path(__file__).parent
template_path = os.path.join(project_path, "templates")
templates = Jinja2Templates(directory=template_path)
app = get_app()


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


app.include_router(prediction_router, prefix="/predict")

# if __name__ == "__main__":
#     app.include_router(prediction_router, prefix="/predict")
#     uvicorn.run(app, host="localhost", port=8000)
