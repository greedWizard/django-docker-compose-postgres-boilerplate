from dataclasses import dataclass

from httpx import Client


@dataclass
class ElasticClient:
    http_client: Client

    def upsert_index(self, index: str, document_id: int | str, document: dict):
        response = self.http_client.post(
            f'{index}/_update/{document_id}', json={
                'doc': document,
                'doc_as_upsert': True,
            },
        )

        response.raise_for_status()
