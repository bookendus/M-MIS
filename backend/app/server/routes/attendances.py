from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException

from app.server.models.attendances import Attendance, UpdateAttendance


router = APIRouter()

@router.post("/", response_description="근태 정보를 저장함")
async def add_attendance_data(attendance: Attendance) -> dict:
    await attendance.create()
    return {"message": "Attendance added successfully"}

@router.get("/{id}", response_description="근태 정보를 조회함")
async def get_attendance_record(id: PydanticObjectId) -> Attendance:
    record = await Attendance.get(id)
    return record


@router.get("/", response_description="근태 목록을 조회함")
async def get_attendances() -> List[Attendance]:
    records = await Attendance.find_all().to_list()
    return records

@router.put("/{id}", response_description="근태 정보를 갱신함")
async def update_attendance_data(id: PydanticObjectId, req: UpdateAttendance) -> Attendance:
    req = {k: v for k, v in req.dict().items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in req.items()
    }}

    record = await Attendance.get(id)
    if not record:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found!"
        )

    await record.update(update_query)
    return record

@router.delete("/{id}", response_description="근태 정보를 삭제함")
async def delete_attendance_data(id: PydanticObjectId) -> dict:
    record = await Attendance.get(id)

    if not record:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found!"
        )

    await record.delete()
    return {
        "message": "Attendance deleted successfully"
    }