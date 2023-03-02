from datetime import datetime
from typing import Optional, List
from enum import Enum

from beanie import Document, Link
from pydantic import BaseModel, Field

from app.server.models.customers import Customer
from app.server.models.users import User

class ProjectStatus(str, Enum):
    alive = "Alive"
    stop = "Stop"
    end = "End"
    delayed = "Delayed"

class UaRole(str, Enum):
    pm = "PM"
    business = "사업"
    plan = "기획"
    design = "디자인"
    appfe = "앱개발"
    webfe = "웹프론트개발"
    backend = "백엔드개발"
    qa = "QA"

class UserAttendance(Document):
    uaUser: Link[User]
    uaRole: UaRole
    uaStartDate: Optional[datetime] = None
    uaEndDate: Optional[datetime] = None
    recordDate: datetime = datetime.now()


class Project(Document):
    projectCode: str
    projectName: str
    projectCustomer: Link[Customer]
    projectPM: Link[User]
    projectUsers: List[Link[User]]
    projectStartDate: Optional[datetime] = None
    projectEndDate: Optional[datetime] = None
    actualEndDate: Optional[datetime] = None
    projectStatus: ProjectStatus #= Field(None, alias="Status")
    projectRemark: str
    projectAttendances: Optional[List[UserAttendance]]
    recordDate: datetime = datetime.now()

    class Settings:
        name = "Project"

    class Config:
        schema_extra = {
            "example": {
                "projectCode": "PJ-OR999-A01",
                "projectName": "2023 전사교육",
                "projectCustomer" : "63fc2e50ed67382c9a72fd06",
                "projectPM": "63fc658baa02417be4600e28",
                "projectUsers": [
                    "63fc658baa02417be4600e28",
                    "63fc658baa02417be4600e28",
                ],
                "projectStartDate": datetime.now(),
                "projectStatus": ProjectStatus.alive,
                "projectRemark": "전사공통",
                "projectAttendances": [ { 
                    "uaUser": "63fc658baa02417be4600e28",
                    "uaRole": UaRole.pm,
                    "uaStartDate": datetime.now(),
                    "uaEndDate": datetime.now(),
                    "recordDate": datetime.now()
                } ],
                "recordDate": datetime.now()
            }
        }
class UpdateProject(BaseModel):
    projectCode: Optional[str]
    projectName: Optional[str]
    projectCustomer: Optional[Customer]
    projectPM: Optional[User]
    projectStartDate: Optional[datetime]
    projectEndDate: Optional[datetime]
    actualEndDate: Optional[datetime]
    projectStatus: Optional[str]
    projectRemark: Optional[str]
    projectAttendances: Optional[List[UserAttendance]]
    recordDate: Optional[datetime]

    class Config:
        schema_extra = {
            "example": {
                "projectCode": "PJ-OR999-A01",
                "projectName": "2023년 전사교육",
                "projectCustomer" : "63fc2e50ed67382c9a72fd06",
                "projectPM": "a",
                "projectStartDate": datetime.now(),
                "projectEndDate": datetime.now(),
                "projectStatus": "alive",
                "projectRemark": "전사공통",
                "projectAttendances": [ { 
                    "uaUser": "63fc658baa02417be4600e28",
                    "uaRole": UaRole.pm,
                    "uaStartDate": datetime.now(),
                    "uaEndDate": datetime.now(),
                    "recordDate": datetime.now()
                } ],                
                "recordDate": datetime.now()
            }
        }