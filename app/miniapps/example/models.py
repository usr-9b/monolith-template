from app.database import Base
from app.miniapps.example.shemas import ExampleShema
from sqlalchemy.orm import Mapped, mapped_column


class ExampleModel(Base):
    __tablename__ = "examples"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    def to_read_model(self) -> ExampleShema:
        return ExampleShema.model_validate(self)
