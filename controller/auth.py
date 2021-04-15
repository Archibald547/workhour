from fastapi import APIRouter
from fastapi_login import LoginManager
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException

SECRET = "super-secret-key"
manager = LoginManager(SECRET, '/login')

DB = {
    'users': {
        'johndoe@mail.com': {
            'name': 'John Doe',
            'password': 'hunter2'
        }
    }
}

def query_user(user_id: str):
    """
    Get a user from the db
    :param user_id: E-Mail of the user
    :return: None or the user object
    """
    return DB['users'].get(user_id)

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


@router.post('/login')
def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password

    user = query_user(email)
    if not user:
        # you can return any response or error of your choice
        raise InvalidCredentialsException
    elif password != user['password']:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data={'sub': email}
    )
    return {'token': access_token}

@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]
