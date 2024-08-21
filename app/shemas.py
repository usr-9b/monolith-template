import json
from pydantic import BaseModel


class BaseShema(BaseModel):
    class Config:
        from_attributes = True

    def serializable(self) -> dict:
        return json.loads(self.model_dump_json())
