from beanie import init_beanie
import motor.motor_asyncio

from app.server.models.product_review import ProductReview
from app.server.models.users import User


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://root:1234@localhost:27017/"
    )

    await init_beanie(database=client.mydb, document_models=[User, ProductReview]) 