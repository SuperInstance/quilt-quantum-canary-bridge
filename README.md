# quilt-quantum-canary-bridge

> **Improving quantum polyformalism.**
> Bridging strategies for making quantum canary match classical canary.

## TL;DR

```python
from quilt_quantum_canary_bridge import bridge_canary

result = bridge_canary()
print(f"Fleet: 0x{result['fleet_canary']:016x}")
for scheme, strategies in result['bridges'].items():
    for strategy, qc in strategies.items():
        match = "✓" if qc == result['fleet_canary'] else "✗"
        print(f"  {scheme:8} {strategy:10}: 0x{qc:016x} ({match})")
```

## License

MIT — Casey / SuperInstance, Sept 23, 2026
