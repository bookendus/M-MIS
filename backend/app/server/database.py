from beanie import init_beanie
import motor.motor_asyncio

from app.server.configs import Configs

from app.server.models.users import User
from app.server.models.customers import Customer
from app.server.models.projects import Project
from app.server.models.timeframes import TimeFrame
from app.server.models.attendances import Attendance

#from app.server.models.product_review import ProductReview
#from app.server.models.employees import Employee


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        Configs.DB_URL
    )
    database = client[Configs.DB_DATABASE]
    await init_beanie(database=database, document_models=[User, Customer, Project, TimeFrame, Attendance ]) 