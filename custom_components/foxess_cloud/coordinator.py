"""DataUpdateCoordinator for FoxESS Cloud."""
from __future__ import annotations

from datetime import timedelta
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import FoxEssCloudClient, FoxEssCloudError
from .const import DEFAULT_SCAN_INTERVAL, VARIABLES

_LOGGER = logging.getLogger(__name__)


class FoxEssCloudCoordinator(DataUpdateCoordinator[dict]):
    """Polls the FoxESS Cloud API for a single device on an interval."""

    def __init__(self, hass: HomeAssistant, client: FoxEssCloudClient, device_sn: str) -> None:
        super().__init__(
            hass,
            _LOGGER,
            name="FoxESS Cloud",
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )
        self._client = client
        self.device_sn = device_sn

    async def _async_update_data(self) -> dict:
        try:
            return await self._client.get_real_data(self.device_sn, list(VARIABLES))
        except FoxEssCloudError as err:
            raise UpdateFailed(str(err)) from err
