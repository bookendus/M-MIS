from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException

from app.server.models.employees import Employee


router = APIRouter()

@router.get("/{id}", response_description="직원 정보를 조회함")
async def get_employee_record(id: PydanticObjectId) -> Employee:
    record = await Employee.get(id)
    return record


@router.get("/", response_description="직원 목록을 조회함")
async def get_employee() -> List[Employee]:
    records = await Employee.find_all().to_list()
    return records
