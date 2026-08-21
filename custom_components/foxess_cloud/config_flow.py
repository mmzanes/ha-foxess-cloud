"""Config flow for FoxESS Cloud."""
from __future__ import annotations

from typing import Any

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .api import FoxEssCloudClient, FoxEssCloudError
from .const import CONF_API_KEY, CONF_DEVICE_SN, DOMAIN

STEP_API_KEY_SCHEMA = vol.Schema({vol.Required(CONF_API_KEY): str})


async def _fetch_devices(hass: HomeAssistant, api_key: str) -> list[dict[str, Any]]:
    session = async_get_clientsession(hass)
    client = FoxEssCloudClient(session, api_key)
    return await client.get_device_list()


class FoxEssCloudConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for FoxESS Cloud."""

    VERSION = 1

    def __init__(self) -> None:
        self._api_key: str | None = None
        self._devices: list[dict[str, Any]] = []

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.ConfigFlowResult:
        errors: dict[str, str] = {}

        if user_input is not None:
            try:
                devices = await _fetch_devices(self.hass, user_input[CONF_API_KEY])
            except FoxEssCloudError:
                errors["base"] = "invalid_auth"
            except Exception:  # noqa: BLE001
                errors["base"] = "cannot_connect"
            else:
                if not devices:
                    errors["base"] = "no_devices_found"
                else:
                    self._api_key = user_input[CONF_API_KEY]
                    self._devices = devices
                    return await self.async_step_device()

        return self.async_show_form(
            step_id="user", data_schema=STEP_API_KEY_SCHEMA, errors=errors
        )

    async def async_step_device(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.ConfigFlowResult:
        device_map = {d["deviceSN"]: d.get("deviceSN") for d in self._devices}

        if user_input is not None:
            device_sn = user_input[CONF_DEVICE_SN]
            await self.async_set_unique_id(device_sn)
            self._abort_if_unique_id_configured()
            return self.async_create_entry(
                title=f"FoxESS Cloud ({device_sn})",
                data={CONF_API_KEY: self._api_key, CONF_DEVICE_SN: device_sn},
            )

        schema = vol.Schema({vol.Required(CONF_DEVICE_SN): vol.In(device_map)})
        return self.async_show_form(step_id="device", data_schema=schema)
