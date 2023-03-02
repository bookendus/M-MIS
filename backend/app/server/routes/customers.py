from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException

from app.server.models.customers import Customer, UpdateCustomer


router = APIRouter()

@router.post("/", response_description="고객 정보를 저장함")
async def add_customer_data(customer: Customer) -> dict:
    await customer.create()
    return {"message": "Customer added successfully"}

@router.get("/{id}", response_description="고객 정보를 조회함")
async def get_customer_record(id: PydanticObjectId) -> Customer:
    record = await Customer.get(id)
    return record


@router.get("/", response_description="고객 목록을 조회함")
async def get_customers() -> List[Customer]:
    records = await Customer.find_all().to_list()
    return records

@router.put("/{id}", response_description="고객 정보를 갱신함")
async def update_customer_data(id: PydanticObjectId, req: UpdateCustomer) -> Customer:
    req = {k: v for k, v in req.dict().items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in req.items()
    }}

    record = await Customer.get(id)
    if not record:
        raise HTTPException(
            status_code=404,
            detail="Customer record not found!"
        )

    await record.update(update_query)
    return record

@router.delete("/{id}", response_description="고객정보를 삭제함")
async def delete_customer_data(id: PydanticObjectId) -> dict:
    record = await Customer.get(id)

    if not record:
        raise HTTPException(
            status_code=404,
            detail="Customer record not found!"
        )

    await record.delete()
    return {
        "message": "Customer deleted successfully"
    }