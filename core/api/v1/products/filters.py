from ninja import Schema


class ProductFilters(Schema):
    search: str | None = None
