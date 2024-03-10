import json
from typing import Callable

from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.urls import (
    resolve,
    Resolver404,
)

import elasticapm


class ElasticApmMiddleware:
    """Middleware для создания отдельных транзакций.

    Также добавляет тело ответа в apm

    """

    def __init__(self, get_response: Callable):
        self.get_response = get_response
        self._client = elasticapm.get_client()

    def __call__(self, request: HttpRequest) -> HttpResponse:
        transaction_name = self._create_transaction_name(request)
        self._start_new_transaction(transaction_name)
        response = self.get_response(request)
        self._set_response_body_for_apm(response)
        return response

    def _start_new_transaction(self, transaction_name: str) -> None:
        elasticapm.instrument()
        self._client.begin_transaction("request")
        elasticapm.set_transaction_name(transaction_name)

    def _set_response_body_for_apm(self, response: HttpResponse) -> None:
        try:
            response_body_unicode = response.content.decode("utf-8")
            response_body = json.loads(response_body_unicode)
        except json.JSONDecodeError:
            response_body = response.content
        except AttributeError:
            # TODO: Сделать нормально для WhiteNois'а через streaming_content
            response_body = ""
        elasticapm.set_context(data={"response_body": response_body})

    def _create_transaction_name(self, request: HttpRequest) -> str:
        try:
            current_url = resolve(request.path_info).route
        except Resolver404:
            current_url = request.path

        return f"{request.method} {current_url}"
