from typing import Type
from app.database import session_maker
from app.miniapps.example.repository import Repository as ExampleRepository


class Unit:
    example: Type[ExampleRepository]

    def __init__(self):
        self.maker = session_maker

    async def __aenter__(self):
        self.session = self.maker()

        self.example = ExampleRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
