from typing import Annotated

from fastapi import Depends

from app.unit import Unit

unitDepend = Annotated[Unit, Depends(Unit)]
