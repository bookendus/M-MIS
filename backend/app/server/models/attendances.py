from datetime import datetime
from enum import Enum
from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel


from app.server.models.users import User

class TypdOfCredit(str, Enum):
    dayOff = "연차/반차"
    businessTrip = "출장"    

class ApprovalCredit(BaseModel):
    typeOfCredit: TypdOfCredit
    timeCredit: int
    approvalDoc: str


class Attendance(Document):
    attUser: Link[User]
    attDate: datetime
    timeCredit: Optional[int]
    timeOfArriving : Optional[datetime]
    timeOfLeaving : Optional[datetime]
    timeOfHomeStart: Optional[datetime]
    timeOfHomeEnd: Optional[datetime]
    otherCredit: Optional[List[ApprovalCredit]]
    date: datetime = datetime.now()

    class Settings:
        name = "Attendance"

    class Config:
        schema_extra = {
            "example": {
                "attUser": "63fc658baa02417be4600e28",
                "attDate": datetime(2023,1,1),
                "timeCredit": 3,
                "timeOfArriving": datetime.now(),
                "timeOfLeaving": datetime.now(),
                "timeOfHomeStart": datetime.now(),
                "timeOfHomeEnd": datetime.now(),
                "otherCredit": [
                    {
                        "typeOfCredit": TypdOfCredit.businessTrip,
                        "timeCredit": 2,
                        "approvalDoc": "결제1"
                    },
                    {
                        "typeOfCredit": TypdOfCredit.dayOff,
                        "timeCredit": 3,
                        "approvalDoc": "결제2"
                    }
                ],
                "date": datetime.now()
            }
        }
class UpdateAttendance(BaseModel):
    # attUser: Link[User]
    # attDate: datetime
    timeCredit: Optional[int]
    timeOfArriving : Optional[datetime]
    timeOfLeaving : Optional[datetime]
    timeOfHomeStart: Optional[datetime]
    timeOfHomeEnd: Optional[datetime]
    otherCredit: Optional[List[ApprovalCredit]]
    date: datetime = datetime.now()
    class Config:
        schema_extra = {
            "example": {
                "attUser": "63fc658baa02417be4600e28",
                "attDate": datetime(2023,1,1),
                "timeCredit": 3,
                "timeOfArriving": datetime.now(),
                "timeOfLeaving": datetime.now(),
                "timeOfHomeStart": datetime.now(),
                "timeOfHomeEnd": datetime.now(),
                "otherCredit": [
                    {
                        "typeOfCredit": TypdOfCredit.businessTrip,
                        "timeCredit": 2,
                        "approvalDoc": "결제1"
                    },
                    {
                        "typeOfCredit": TypdOfCredit.dayOff,
                        "timeCredit": 3,
                        "approvalDoc": "결제2"
                    }
                ],
                "date": datetime.now()
            }
        }