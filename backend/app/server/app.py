from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.server.database import init_db

from app.server.models.users import (UserCreate, UserRead, UserUpdate, User, 
                                     auth_backend_google, auth_backend,
                                     current_active_user, fastapi_users,
                                     google_oauth_client,
)
from app.server.routes.customers import router as RouterCustomers
from app.server.routes.projects import router as RouterProjects
from app.server.routes.timeframes import router as RouterTimeFrames
from app.server.routes.attendances import router as RouterAttendances


#from app.server.routes.employees import router as RouterEmployee
#from app.server.routes.product_review import router as RouterReviews

from app.server.configs import Configs

origins = [
    "*"
]


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(
#     fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
# )
# app.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix="/auth",
#     tags=["auth"],
# )
# app.include_router(
#     fastapi_users.get_reset_password_router(),
#     prefix="/auth",
#     tags=["auth"],
# )
# app.include_router(
#     fastapi_users.get_verify_router(UserRead),
#     prefix="/auth",
#     tags=["auth"],
# )
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
app.include_router(
    fastapi_users.get_oauth_router(
            oauth_client=google_oauth_client,
            backend=auth_backend_google,
            state_secret=Configs.SECRET_KEY,
            redirect_url=Configs.GOOGLE_CALLBACK_URL,
            associate_by_email=True),
    prefix="/auth/google",
    tags=["auth"],
)

@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


app.include_router(RouterCustomers, tags=["Customers"], prefix="/customers")
app.include_router(RouterProjects, tags=["Projects"], prefix="/projects")
app.include_router(RouterTimeFrames, tags=["TimeFrames"], prefix="/timeframes")
app.include_router(RouterAttendances, tags=["Attendances"], prefix="/attendances")



#app.include_router(RouterEmployee, tags=["Employee"], prefix="/employees")
#app.include_router(RouterReviews, tags=["Product Reviews"], prefix="/reviews")


@app.on_event("startup")
async def start_db():
    await init_db()


