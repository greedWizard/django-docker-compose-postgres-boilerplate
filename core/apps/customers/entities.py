from dataclasses import dataclass
from datetime import datetime


@dataclass
class Customer:
    phone: str
    created_at: datetime
