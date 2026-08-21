# Changelog

All notable changes to this project are documented here.
This project follows [Semantic Versioning](https://semver.org/).

## [0.3.0] - 2026-08-21

### Fixed
- `manifest.json` version, which had drifted out of sync since 0.2.0.

## [0.2.0] - 2026-08-21

### Added
- PV string sensors: PV1/PV2 voltage, current, power.
- Grid sensors: voltage, current, frequency, feed-in power, power factor.
- Inverter status: inverter temperature, ambient temperature, running state, fault code.

## [0.1.0] - 2026-08-21

### Added
- Initial custom component scaffold: config flow (API key + device picker),
  `DataUpdateCoordinator`-based polling, and core sensors (PV power, today's
  yield, total generation, grid consumption, loads power, battery SoC).
