# FoxESS Cloud for Home Assistant

Custom integration that polls the official [FoxESS Cloud Open API](https://www.foxesscloud.com/public/i18n/en/OpenApiDocument.html)
and exposes your inverter's live data as sensors. Built for WEG SIW200G/SIW400G
inverters (which are FoxESS T-series hardware under a different badge), but works
for any inverter registered on FoxESS Cloud.

## Sensors

- PV Power
- Today's Yield
- Total Generation
- Grid Consumption Power
- Loads Power
- Battery SoC (if applicable)

## Installation

### Via HACS (custom repository)

1. HACS → Integrations → ⋮ → Custom repositories.
2. Add this repo's URL, category "Integration".
3. Install "FoxESS Cloud", restart Home Assistant.

### Manual

Copy `custom_components/foxess_cloud` into your Home Assistant `config/custom_components/`
directory and restart.

## Setup

1. Log in to [foxesscloud.com](https://www.foxesscloud.com), go to
   **User Profile → API Management → Generate API key**. Copy it immediately —
   it's shown only once per generation.
2. In Home Assistant: **Settings → Devices & Services → Add Integration → FoxESS Cloud**.
3. Paste the API key, then pick your inverter's serial number from the list.

## Notes

- Polling interval defaults to 300s (`DEFAULT_SCAN_INTERVAL` in `const.py`) — the
  FoxESS Cloud API is rate-limited, so don't set this too aggressively.
- This integration only talks to the cloud. For a fully local, no-internet-dependency
  setup, see [LucasTor/FoxESS-T-series](https://github.com/LucasTor/FoxESS-T-series),
  which reads the inverter directly over RS485/Modbus.
