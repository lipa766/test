""" Frontend of internal DevOps Project for adding animal and their names """
import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()

templates = Jinja2Templates(directory="templates")

backend_url: str = "http://localhost:5001/"
logs: list = []


@app.get("/")
def get_method(request: Request, get_animals: str = Form):
    """ Get method for loading frontend and display animals with logs """
    if get_animals:
        logs.append("[FRONTEND] Getting animals from backend")
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "log": logs, "animals": requests.get(url=backend_url).json()}
    )


@app.post("/")
def post_method(request: Request, name: str = Form(''), animal: str = Form('')):
    """ Post method for adding animals from as well as adding logs and load frontend """
    if not animal or not name:
        logs.append("[FRONTEND] Both animal and name are required")
    else:
        payload = {'name': name, 'kind': animal}
        response = requests.post(backend_url, json=payload)
        logs.append(f"[FRONTEND] Adding Name: {name} Animal: {animal} to database")
        logs.append(f'[BACKEND] {response.text}')
    return templates.TemplateResponse("index.html", {"request": request, "log": logs})


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host='0.0.0.0',
        reload=True,
        port=5010
    )
