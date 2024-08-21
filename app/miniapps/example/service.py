from app.exceptions import ObjectNotFound
from app.miniapps.example.shemas import ExampleCreate, ExampleShema
from app.unit import Unit
from app.miniapps.example.models import ExampleModel


class Serivce:
    async def get(self, unit: Unit, id: int) -> ExampleShema:
        async with unit:
            example: ExampleModel = await unit.example.select(id=id)
            if example is None:
                raise ObjectNotFound
            return example.to_read_model()

    async def create(self, unit: Unit, data: ExampleCreate) -> ExampleShema:
        async with unit:
            example: ExampleModel = await unit.example.insert(data=data.model_dump())
            await unit.commit()

            return example.to_read_model()
