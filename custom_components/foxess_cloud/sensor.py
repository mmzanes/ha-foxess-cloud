"""Sensor platform for FoxESS Cloud."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, VARIABLES
from .coordinator import FoxEssCloudCoordinator

DEVICE_CLASS_MAP = {
    "power": SensorDeviceClass.POWER,
    "energy": SensorDeviceClass.ENERGY,
    "battery": SensorDeviceClass.BATTERY,
}
STATE_CLASS_MAP = {
    "measurement": SensorStateClass.MEASUREMENT,
    "total_increasing": SensorStateClass.TOTAL_INCREASING,
}


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    coordinator: FoxEssCloudCoordinator = hass.data[DOMAIN][entry.entry_id]

    entities = [
        FoxEssCloudSensor(coordinator, entry.unique_id or coordinator.device_sn, variable)
        for variable in VARIABLES
    ]
    async_add_entities(entities)


class FoxEssCloudSensor(CoordinatorEntity[FoxEssCloudCoordinator], SensorEntity):
    """Representation of a single FoxESS Cloud variable."""

    _attr_has_entity_name = True

    def __init__(
        self, coordinator: FoxEssCloudCoordinator, device_sn: str, variable: str
    ) -> None:
        super().__init__(coordinator)
        name, unit, device_class, state_class = VARIABLES[variable]

        self._variable = variable
        self._attr_name = name
        self._attr_native_unit_of_measurement = unit
        self._attr_device_class = DEVICE_CLASS_MAP.get(device_class)
        self._attr_state_class = STATE_CLASS_MAP.get(state_class)
        self._attr_unique_id = f"{device_sn}_{variable}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, device_sn)},
            name=f"FoxESS Inverter {device_sn}",
            manufacturer="FoxESS",
        )

    @property
    def native_value(self):
        return self.coordinator.data.get(self._variable)
