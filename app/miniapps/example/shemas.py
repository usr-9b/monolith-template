from app.shemas import BaseShema


class ExampleShema(BaseShema):
    id: int
    name: str


class ExampleCreate(BaseShema):
    name: str


class ExampleGet(BaseShema):
    id: int
