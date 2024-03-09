"""Test the memory module model."""

from dataclasses import asdict

from systembridgemodels.fixtures.modules.memory import FIXTURE_MEMORY
from systembridgemodels.modules.memory import Memory, MemorySwap, MemoryVirtual


def test_memory(memory: Memory = FIXTURE_MEMORY):
    """Test the memory model."""
    assert isinstance(memory, Memory)
    assert isinstance(memory.swap, MemorySwap)
    assert memory.swap.total == 1000
    assert memory.swap.used == 500
    assert memory.swap.free == 500
    assert memory.swap.percent == 50.0
    assert memory.swap.sin == 100
    assert memory.swap.sout == 100
    assert isinstance(memory.virtual, MemoryVirtual)
    assert memory.virtual.total == 1000
    assert memory.virtual.available == 500
    assert memory.virtual.percent == 50.0
    assert memory.virtual.used == 500
    assert memory.virtual.free == 500
    assert memory.virtual.active == 500
    assert memory.virtual.inactive == 500
    assert memory.virtual.buffers == 500
    assert memory.virtual.cached == 500
    assert memory.virtual.wired == 500
    assert memory.virtual.shared == 500


def test_memory_dict():
    """Test memory dict."""
    memory_dict = asdict(FIXTURE_MEMORY)
    assert isinstance(memory_dict, dict)
    assert isinstance(memory_dict["swap"], dict)
    assert memory_dict["swap"]["total"] == 1000
    assert memory_dict["swap"]["used"] == 500
    assert memory_dict["swap"]["free"] == 500
    assert memory_dict["swap"]["percent"] == 50.0
    assert memory_dict["swap"]["sin"] == 100
    assert memory_dict["swap"]["sout"] == 100
    assert isinstance(memory_dict["virtual"], dict)
    assert memory_dict["virtual"]["total"] == 1000
    assert memory_dict["virtual"]["available"] == 500
    assert memory_dict["virtual"]["percent"] == 50.0
    assert memory_dict["virtual"]["used"] == 500
    assert memory_dict["virtual"]["free"] == 500
    assert memory_dict["virtual"]["active"] == 500
    assert memory_dict["virtual"]["inactive"] == 500
    assert memory_dict["virtual"]["buffers"] == 500
    assert memory_dict["virtual"]["cached"] == 500
    assert memory_dict["virtual"]["wired"] == 500
    assert memory_dict["virtual"]["shared"] == 500

    memory_converted = Memory(**memory_dict)
    test_memory(memory_converted)
