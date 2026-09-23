"""quilt-quantum-canary-bridge — improve quantum polyformalism.

The polyformalism canary is canon across classical substrates but NOT
across quantum substrates (0/5 schemes match).

This repo explores BRIDGES that might bring quantum into canon. We
try:
- Normalize audio amplitude to a canonical encoding
- Use only the canary's first 8 bytes (the variation is in tail)
- Hash the measurement bits in a different way
- Try schemes in canonical order
- Add a normalization layer
"""
from .bridge import bridge_canary, try_normalize, try_partial_hash

__version__ = "0.1.0"
__all__ = ["bridge_canary", "try_normalize", "try_partial_hash"]
