from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from app.controllers import UserController  # Import the UserController
from app.schemas.quiz.schema import User as UserSchema, UserOut, UserIn  # Import the UserSchema
from typing import List
from core.factory import Factory

user_router = APIRouter()

# Secret key to sign and verify JWT tokens (replace this with a secure secret key)
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme), controller: UserController = Depends(Factory().get_user_controller)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = controller.get_by_username(username)
    if user is None:
        raise credentials_exception
    return user

@user_router.post("/login", response_model=dict)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), controller: UserController = Depends(Factory().get_user_controller)):
    user = await controller.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token_data = {"sub": user.username}
    access_token = create_jwt_token(token_data)

    return {"access_token": access_token, "token_type": "bearer"}

def create_jwt_token(data: dict):
    to_encode = data.copy()
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@user_router.get("/", response_model=List[UserOut])
async def get_all_users(controller: UserController = Depends(Factory().get_user_controller)):  # Use the UserController
    return await controller.repository.get_all()

@user_router.get("/{id}", response_model=UserOut)
async def get_user(id: int, controller: UserController = Depends(Factory().get_user_controller)):  # Use the UserController
    user = await controller.get_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.post("/", response_model=UserOut)
async def create_user(user: UserIn, controller: UserController = Depends(Factory().get_user_controller)):  # Use the UserController
    return await controller.add(user)

@user_router.put("/{id}", response_model=UserOut)
async def update_user(id: int, user: UserIn, controller: UserController = Depends(Factory().get_user_controller)):  # Use the UserController
    return await controller.update(id, user)

@user_router.delete("/{id}")
async def delete_user(id: int, controller: UserController = Depends(Factory().get_user_controller)):  # Use the UserController
    await controller.delete(id)
    return {"message": "User deleted successfully"}
