# portfolio-mgmt-sys

Portfolio Risk Management and Rebalancing System that simulates real fund management operations.

## Project Structure

```
portfolio-mgmt-sys/
├── src/
│   ├── instruments/
│   │   ├── factory.py          # Factory Pattern
│   │   ├── equity.py
│   │   ├── bond.py
│   │   └── derivative.py
│   ├── market_data/
│   │   └── manager.py          # Singleton Pattern
│   ├── portfolio/
│   │   ├── portfolio.py        # Observer Pattern
│   │   ├── builder.py          # Builder Pattern
│   │   └── strategies/         # Strategy Pattern
│   │       ├── mean_reversion.py
│   │       ├── momentum.py
│   │       └── risk_parity.py
│   ├── risk/
│   │   ├── calculator.py
│   │   └── monitors.py
│   └── utils/
│       ├── performance.py
│       └── reports.py
├── data/
│   ├── sample_prices.csv
│   └── benchmarks.json
├── tests/
└── examples/
    └── fund_management_simulation.py
```
