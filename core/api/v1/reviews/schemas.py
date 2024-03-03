from datetime import datetime

from pydantic import BaseModel

from core.apps.products.entities.reviews import Review as ReviewEntity


class ReviewInSchema(BaseModel):
    rating: int
    text: str

    def to_entity(self):
        return ReviewEntity(text=self.text, rating=self.rating)


class CreateReviewSchema(BaseModel):
    product_id: int
    cusotmer_token: str
    review: ReviewInSchema


class ReviewOutSchema(ReviewInSchema):
    id: int  # noqa
    created_at: datetime
    updated_at: datetime | None

    @classmethod
    def from_entity(cls, review: ReviewEntity) -> 'ReviewOutSchema':
        return cls(
            id=review.id,
            text=review.text,
            rating=review.rating,
            created_at=review.created_at,
            updated_at=review.updated_at,
        )
