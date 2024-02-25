from dataclasses import dataclass


@dataclass(frozen=True)
class ProductFilters:
    search: str | None = None
