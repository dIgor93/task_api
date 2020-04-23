from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.test_resources import TestResources

app = FastAPI()
app.state.res = TestResources()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/health')
async def health():
    return {"status": "Ok"}


@app.get('/projects')
async def projects():
    res = await app.state.res.get_projects()
    return res


@app.get('/resources/{project_id}/tasks/{group}')
async def get_tasks(project_id, group):
    res = await app.state.res.get_tasks(project_id, group)
    return res


@app.get('/resources/{project_id}/requirements/{group}')
async def get_tasks(project_id, group):
    res = await app.state.res.get_requirements(project_id, group)
    return res


@app.get('/resources/{project_id}/command/{group}')
async def get_tasks(project_id, group):
    res = await app.state.res.get_command(project_id, group)
    return res


@app.get('/resources/{project_id}/statistic/{group}')
async def get_stat(project_id, group):
    res = await app.state.res.get_plot_data(project_id, group)
    return res



