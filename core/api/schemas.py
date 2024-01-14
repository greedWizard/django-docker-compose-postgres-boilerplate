from pydantic import BaseModel


class PingResponseSchema(BaseModel):
    result: bool
