from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException

from app.server.models.timeframes import TimeFrame


router = APIRouter()

@router.get("/{id}", response_description="Time Frame 정보를 조회함")
async def get_TFCode_record(id: PydanticObjectId) -> TimeFrame:
    record = await TimeFrame.get(id)
    return record


@router.get("/", response_description="Time Frame 목록을 조회함")
async def get_TFCodes() -> List[TimeFrame]:
    records = await TimeFrame.find_all().to_list()
    return records

@router.post("/", response_description="Time Frame 정보를 저장함")
async def add_TFCode_data(timeFrame: TimeFrame) -> dict:
    await timeFrame.create()
    return {"message": "TimeFrame added successfully"}