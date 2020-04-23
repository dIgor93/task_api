import uvicorn

from app.api.handlers import app

if __name__ == '__main__':
    uvicorn.run(app)