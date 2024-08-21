from fastapi import APIRouter
from app.depends import unitDepend
from app.miniapps.example.shemas import (
    ExampleCreate,
    ExampleGet,
    ExampleShema,
)
from app.miniapps.example.service import Serivce

router = APIRouter(prefix="/example", tags=["example"])


@router.post("/get")
async def get_example(
    id: ExampleGet,
    unit: unitDepend,
) -> ExampleShema:
    return await Serivce().get(unit, id.id)


@router.put("/create")
async def create_example(
    example: ExampleCreate,
    unit: unitDepend,
) -> ExampleShema:
    return await Serivce().create(unit, example)
