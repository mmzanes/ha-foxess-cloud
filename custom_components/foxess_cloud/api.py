"""Thin async client for the FoxESS Cloud Open API."""
from __future__ import annotations

import hashlib
import time
from typing import Any

import aiohttp

from .const import BASE_URL, DEVICE_LIST_PATH, REAL_QUERY_PATH


class FoxEssCloudError(Exception):
    """Raised when the FoxESS Cloud API returns an error."""


class FoxEssCloudClient:
    """Client for the FoxESS Cloud Open API (token-based auth)."""

    def __init__(self, session: aiohttp.ClientSession, api_key: str) -> None:
        self._session = session
        self._api_key = api_key

    def _headers(self, path: str) -> dict[str, str]:
        timestamp = str(round(time.time() * 1000))
        signature_raw = f"{path}\r\n{self._api_key}\r\n{timestamp}"
        signature = hashlib.md5(signature_raw.encode("utf-8")).hexdigest()
        return {
            "token": self._api_key,
            "timestamp": timestamp,
            "signature": signature,
            "lang": "en",
            "Content-Type": "application/json",
        }

    async def _post(self, path: str, body: dict[str, Any]) -> dict[str, Any]:
        async with self._session.post(
            f"{BASE_URL}{path}", headers=self._headers(path), json=body
        ) as resp:
            resp.raise_for_status()
            payload = await resp.json()

        errno = payload.get("errno")
        if errno:
            raise FoxEssCloudError(f"FoxESS Cloud API error {errno}: {payload.get('msg')}")

        return payload.get("result") or {}

    async def get_device_list(self) -> list[dict[str, Any]]:
        result = await self._post(
            DEVICE_LIST_PATH, {"currentPage": 1, "pageSize": 10}
        )
        return result.get("data", [])

    async def get_real_data(self, device_sn: str, variables: list[str]) -> dict[str, Any]:
        result = await self._post(
            REAL_QUERY_PATH, {"sn": device_sn, "variables": variables}
        )
        # result is a list with one entry per requested device SN
        entries = result if isinstance(result, list) else [result]
        data: dict[str, Any] = {}
        for entry in entries:
            for datapoint in entry.get("datas", []):
                data[datapoint["variable"]] = datapoint.get("value")
        return data
