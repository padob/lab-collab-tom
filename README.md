11111111111111111111111111111111
22222o
333333333333333333333333333
# lab-results-service

Receives results from laboratory analyzers, validates specimens,
flags abnormal and critical values and prepares reports for physicians.

## Configuration

- `config/reference_ranges.conf` - normal ranges (L / H flags)
- `config/critical_values.conf` - limits that trigger a phone call
