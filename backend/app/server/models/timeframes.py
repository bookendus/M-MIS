from datetime import date, datetime

from beanie import Document
from pydantic import BaseModel
from typing import Optional


class TimeFrame(Document):
    TFCode: str
    TFCodeName: str
    weeks: int
    startDate: datetime
    endDate: datetime
    workDay: str
    recordDate: datetime = datetime.now()

    class Settings:
        name = "TimeFrame"

    class Config:
        schema_extra = {
            "example": {
                "TFCode": "TF2301",
                "TFCodeName": "1/52 Week (2023/01/01 ~ 2023/01/07)",
                "weeks": 1,
                "startDate": datetime(2023,1,1),
                "endDate": datetime(2023,1,7),
                "workDay": "HEEEEEH",
                "date": datetime.now()
            }
        }
