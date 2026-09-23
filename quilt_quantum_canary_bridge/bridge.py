"""Bridge the polyformalism canary to quantum substrates.

The classical fleet canary is fnv1a-64("café Δ 日本語") = 0x024a555471370b18d.
The quantum encoding diverges. This module tries to bridge.
"""
import os
import sys
import struct

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "quilt-quantum-audio"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "quilt-canary"))

from quilt_quantum_audio import lore_to_quantum_canon, QUANTUM_SCHEMES


def _fnv1a_64(s: str) -> int:
    h = 0xcbf29ce484222325
    for b in s.encode("utf-8"):
        h = h ^ b
        h = (h * 0x100000001b3) & 0xffffffffffffffff
    return h


CANARY_INPUT = "café Δ 日本語"


def try_normalize(scheme: str = "QPAM") -> int:
    """Try normalizing the audio amplitude before quantum encoding."""
    # The classical FNV-1a is over UTF-8 bytes.
    # The quantum encoding maps to amplitude, then measures.
    # The measurement bits are derived from amplitude magnitude.
    # If we normalize amplitude to be exactly canonical per byte, the bits might align.
    
    # Get quantum state
    result = lore_to_quantum_canon(CANARY_INPUT, scheme=scheme)
    bits = result["measurement_bits"]
    
    # Normalize: replace each bit with the byte that produces it canonically
    canonical_bytes = bytes(b % 256 for b in bits)
    return _fnv1a_64(canonical_bytes.decode("utf-8", errors="replace"))


def try_partial_hash(scheme: str = "QPAM", n_bits: int = 8) -> int:
    """Try hashing only the first n_bits measurement indices."""
    result = lore_to_quantum_canon(CANARY_INPUT, scheme=scheme)
    bits = result["measurement_bits"][:n_bits]
    bit_str = "".join(str(b % 2) for b in bits)
    return _fnv1a_64(bit_str)


def bridge_canary() -> dict:
    """Try multiple bridging strategies."""
    fleet = _fnv1a_64(CANARY_INPUT)
    out = {"fleet_canary": fleet, "bridges": {}}
    
    for scheme in QUANTUM_SCHEMES:
        out["bridges"][scheme] = {
            "normalize": try_normalize(scheme),
            "partial_8": try_partial_hash(scheme, 8),
            "partial_4": try_partial_hash(scheme, 4),
        }
    
    return out


if __name__ == "__main__":
    print("=== Quantum-polyformalism canary BRIDGE exploration ===")
    fleet = _fnv1a_64(CANARY_INPUT)
    print(f"Fleet canary (classical): 0x{fleet:016x}")
    print()
    
    bridges = bridge_canary()
    for scheme, results in bridges["bridges"].items():
        print(f"=== {scheme} ===")
        for name, qc in results.items():
            match = "✓" if qc == fleet else "✗"
            print(f"  {name:10}: 0x{qc:016x}  ({match})")
        print()
    
    # Check if any match
    any_match = False
    for scheme, results in bridges["bridges"].items():
        for name, qc in results.items():
            if qc == fleet:
                any_match = True
                print(f"🎯 FOUND MATCH: {scheme} via {name}")
    if not any_match:
        print("No bridging strategy matches. Quantum canon is genuinely speculative.")
