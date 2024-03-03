from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from core.apps.customers.entities import Customer as CustomerEntity
from core.apps.products.entities.products import Product as ProductEntity
from core.apps.products.entities.reviews import Review as ReviewEntity
from core.apps.products.exceptions.reviews import ReviewInvalidRating
from core.apps.products.models.reviews import Review as ReviewModel


class BaseReviewService(ABC):
    @abstractmethod
    def save_review(
        self,
        customer: CustomerEntity,
        product: ProductEntity,
        review: ReviewEntity,
    ) -> ReviewEntity:
        ...


class ORMReviewService(BaseReviewService):
    def save_review(
        self,
        customer: CustomerEntity,
        product: ProductEntity,
        review: ReviewEntity,
    ) -> ReviewEntity:
        review_dto: ReviewModel = ReviewModel.from_entity(
            review=review,
            product=product,
            customer=customer,
        )
        review_dto.save()

        return review_dto.to_entity()


class BaseReviewValidatorService(ABC):
    def validate(
        self,
        review: ReviewEntity,
        customer: CustomerEntity | None = None,
        product: ProductEntity | None = None,
    ):
        ...


class ReviewRatingValidatorService(BaseReviewValidatorService):
    def validate(
        self,
        review: ReviewEntity,
        *args,
        **kwargs,
    ):
        # TODO: константы
        if not (1 <= review.rating <= 5):
            raise ReviewInvalidRating(rating=review.rating)


@dataclass
class ComposedReviewValidatorService(BaseReviewValidatorService):
    validators: list[BaseReviewValidatorService]

    def validate(
        self,
        review: ReviewEntity,
        customer: CustomerEntity | None = None,
        product: ProductEntity | None = None,
    ):
        for validator in self.validators:
            validator.validate(review=review, customer=customer, product=product)