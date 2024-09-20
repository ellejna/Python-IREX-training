from fastapi import FastAPI
from projeck1 import Developer, Project

app = FastAPI()

@app.post("/developers/")
async def create_developer(developer: Developer):
    return {"message": "Developer created successfully",
            "developer": developer}

@app.post("/project/")
async def create_project(project: Project):
    return {"message": "Developer created successfully",
            "project": project}

@app.get("/projects/")
async def get_projects():
    developer = Developer(name="Dren")
    sample_project = Project(name="Sample Project",
                             description="This is a project sample",
                             language=["Python", "C++", "Java"],
                             lead_developer=developer)
    return {"projects": {sample_project}}