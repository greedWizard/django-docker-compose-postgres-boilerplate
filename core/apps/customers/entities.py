from dataclasses import dataclass
from datetime import datetime


@dataclass
class CustomerEntity:
    phone: str
    created_at: datetime
