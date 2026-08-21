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
    # Totals
    "pvPower": ("PV Power", "kW", "power", "measurement"),
    "todayYield": ("Today's Yield", "kWh", "energy", "total_increasing"),
    "generation": ("Total Generation", "kWh", "energy", "total_increasing"),
    "gridConsumptionPower": ("Grid Consumption Power", "kW", "power", "measurement"),
    "feedinPower": ("Grid Feed-in Power", "kW", "power", "measurement"),
    "gridConsumption": ("Energy Imported from Grid", "kWh", "energy", "total_increasing"),
    "feedin": ("Energy Exported to Grid", "kWh", "energy", "total_increasing"),
    "loadsPower": ("Loads Power", "kW", "power", "measurement"),
    # PV strings (MPPT 1 and 2 — extend with pv3*/pv4* if your inverter has more)
    "pv1Volt": ("PV1 Voltage", "V", "voltage", "measurement"),
    "pv1Current": ("PV1 Current", "A", "current", "measurement"),
    "pv1Power": ("PV1 Power", "kW", "power", "measurement"),
    "pv2Volt": ("PV2 Voltage", "V", "voltage", "measurement"),
    "pv2Current": ("PV2 Current", "A", "current", "measurement"),
    "pv2Power": ("PV2 Power", "kW", "power", "measurement"),
    # Grid (single-phase — "R" phase)
    "RVolt": ("Grid Voltage", "V", "voltage", "measurement"),
    "RCurrent": ("Grid Current", "A", "current", "measurement"),
    "RFreq": ("Grid Frequency", "Hz", "frequency", "measurement"),
    "RPower": ("Grid Power", "kW", "power", "measurement"),
    "PowerFactor": ("Power Factor", None, "power_factor", "measurement"),
    # Inverter status
    "invTemperation": ("Inverter Temperature", "°C", "temperature", "measurement"),
    "ambientTemperation": ("Ambient Temperature", "°C", "temperature", "measurement"),
    "runningState": ("Running State", None, None, None),
    "currentFault": ("Current Fault Code", None, None, None),
}
