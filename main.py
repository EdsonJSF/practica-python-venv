from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,4]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
      <h1>Hola mundo desde FasAPI y HTMLResponse<h1/>
      <hr/>
    """

def run():
    print("edson")

if __name__ == '__main__':
    run()