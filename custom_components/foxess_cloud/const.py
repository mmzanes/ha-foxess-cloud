"""Constants for the FoxESS Cloud integration."""

DOMAIN = "foxess_cloud"

CONF_API_KEY = "api_key"
CONF_DEVICE_SN = "device_sn"

BASE_URL = "https://www.foxesscloud.com"
DEVICE_LIST_PATH = "/op/v0/device/list"
REAL_QUERY_PATH = "/op/v0/device/real/query"

DEFAULT_SCAN_INTERVAL = 300  # seconds

# variable name -> (friendly name, unit, device_class, state_class)
VARIABLES = {
    "pvPower": ("PV Power", "kW", "power", "measurement"),
    "todayYield": ("Today's Yield", "kWh", "energy", "total_increasing"),
    "generation": ("Total Generation", "kWh", "energy", "total_increasing"),
    "gridConsumptionPower": ("Grid Consumption Power", "kW", "power", "measurement"),
    "loadsPower": ("Loads Power", "kW", "power", "measurement"),
    "batSoC": ("Battery SoC", "%", "battery", "measurement"),
}
