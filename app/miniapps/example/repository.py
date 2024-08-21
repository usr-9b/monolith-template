from app.miniapps.example.models import ExampleModel
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession


class Repository:
    model = ExampleModel

    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert(self, data: dict):
        stmt = insert(self.model).values(**data).returning(self.model)
        res = await self.session.execute(stmt)

        return res.scalar_one()

    async def select(self, id: int):
        stmt = select(self.model).where(self.model.id == id)
        res = await self.session.execute(stmt)

        return res.scalar_one_or_none()

    async def delete(self, id: int):
        res = await self.select(id)
        if res is not None:
            await self.session.delete(res)
