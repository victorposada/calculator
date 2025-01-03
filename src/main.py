from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database.tools import writeCalculations, getCurrentTotal

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )

@app.get("/calculate/")
async def read_item(n1: int = 2, n2: int = 3, operation: str = "add"):
    writeCalculations(n1, n2, operation)
    result = getCurrentTotal()
    return {"Hello": result}


@app.get("/", response_class=HTMLResponse)
async def calculate(request: Request, n1: int = 0, n2: int = 0, operation: str = "add"):
    clientIp = request.client.host
    writeCalculations(n1, n2, operation, clientIp)
    result = getCurrentTotal()  
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "n1": n1, "n2": n2, "operation": operation, "result": result}
    )