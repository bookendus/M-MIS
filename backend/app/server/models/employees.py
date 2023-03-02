from datetime import datetime
from enum import Enum

from beanie import Document
from pydantic import BaseModel, Field
from typing import Optional

class EmployStatus(str, Enum):
    normal = '상주'
    offside = '비상주'
    leave = '퇴사'

class Employee(Document):
    employeeCode: str
    employeeName: str
    employeeNo: int
    employstatus: EmployStatus = Field(None, alias='Status')
    recordDate: datetime = datetime.now()

    class Settings:
        name = "Employee"

    class Config:
        schema_extra = {
            "example": {
                "employeeCode": "EM10000",
                "employeeName": "박재완",
                "employeeNo": 1,
                "employstatus": "상주",
                "recordDate": datetime.now()
            }
        }
