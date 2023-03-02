from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException

from app.server.models.projects import Project, UpdateProject

router = APIRouter()

@router.post("/", response_description="프로젝트 정보를 저장함")
async def add_project_data(project: Project) -> dict:
    await project.create()
    return {"message": "Project added successfully"}

@router.get("/{id}", response_description="프로젝트 정보를 조회함")
async def get_project_record(id: PydanticObjectId) -> Project:
    record = await Project.get(id)
    return record

@router.get("/", response_description="프로젝트 목록을 조회함")
async def get_projects() -> List[Project]:
    records = await Project.find_all().to_list()
    return records

@router.put("/{id}", response_description="프로젝트 정보를 갱신함")
async def update_project_data(id: PydanticObjectId, req: UpdateProject) -> Project:
    req = {k: v for k, v in req.dict().items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in req.items()
    }}

    record = await Project.get(id)
    if not record:
        raise HTTPException(
            status_code=404,
            detail="Project record not found!"
        )

    await record.update(update_query)
    return record

@router.delete("/{id}", response_description="프로젝트 정보를 삭제함")
async def delete_project_data(id: PydanticObjectId) -> dict:
    record = await Project.get(id)

    if not record:
        raise HTTPException(
            status_code=404,
            detail="Project record not found!"
        )

    await record.delete()
    return {
        "message": "Project deleted successfully"
    }