from dataclasses import dataclass
from datetime import datetime


@dataclass
class Product:
    id: int  # noqa
    title: str
    description: str
    created_at: datetime
    updated_at: datetime
