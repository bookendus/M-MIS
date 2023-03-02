from datetime import datetime

from beanie import Document
from pydantic import BaseModel
from typing import Optional


class Customer(Document):
    customerCode: str
    customerName: str
    typeOfCustomer: str
    date: datetime = datetime.now()

    class Settings:
        name = "Customer"

    class Config:
        schema_extra = {
            "example": {
                "customerCode": "OR999",
                "customerName": "전사공통",
                "typeOfCustomer": "내부조직",
                "date": datetime.now()
            }
        }
class UpdateCustomer(BaseModel):
    customerCode: Optional[str]
    customerName: Optional[str]
    typeOfCustomer: Optional[str]
    date: Optional[datetime]

    class Config:
        schema_extra = {
            "example": {
                "customerCode": "OR999",
                "customerName": "전사공통적용",
                "typeOfCustomer": "내부조직",
                "date": datetime.now()
            }
        }