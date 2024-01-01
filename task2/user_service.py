from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound
from task2.user_model import UserDTO

class UserService:
    def __init__(self, async_session: AsyncSession):
        self.async_session = async_session

    async def get(self, user_id: int) -> UserDTO:
        async with self.async_session() as session:
            try:
                user = await session.execute(
                    self._get_query().where(User.id == user_id)
                )
                return UserDTO(**user.scalars().first())
            except NoResultFound:
                return None

    async def add(self, user: UserDTO) -> UserDTO:
        async with self.async_session() as session:
            new_user = User(**user.dict())
            session.add(new_user)
            await session.commit()
            return UserDTO(**new_user.__dict__)

    def _get_query(self):
        return self.async_session.query(User)
