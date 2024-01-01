import unittest
from task2.user_service import UserService
from task2.user_model import UserDTO

class AsyncSessionMock:
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass

    async def query(self, model):
        return self

    async def execute(self, query):
        return {
            'id': 1,
            'username': 'test_user',
            'email': 'test@example.com'
        }

class TestUserService(unittest.TestCase):
    async def test_get_user_by_id(self):
        async_session_mock = AsyncSessionMock()
        user_service = UserService(async_session_mock)
        
        result = await user_service.get(1)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.username, 'test_user')
        self.assertEqual(result.email, 'test@example.com')

    async def test_add_user(self):
        async_session_mock = AsyncSessionMock()
        user_service = UserService(async_session_mock)
        
        new_user = UserDTO(id=1, username='new_user', email='new@example.com')
        result = await user_service.add(new_user)
        self.assertEqual(result.id, new_user.id)
        self.assertEqual(result.username, new_user.username)
        self.assertEqual(result.email, new_user.email)

if __name__ == '__main__':
    unittest.main()
