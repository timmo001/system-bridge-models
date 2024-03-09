"""Test the CPU module model."""

from dataclasses import asdict

from systembridgemodels.fixtures.modules.cpu import FIXTURE_CPU
from systembridgemodels.modules.cpu import CPU, CPUFrequency, CPUStats, CPUTimes, PerCPU


def _test_per_cpu(per_cpu: PerCPU):
    """Test the PerCPU model."""
    assert isinstance(per_cpu, PerCPU)
    assert per_cpu.id == 0
    assert isinstance(per_cpu.frequency, CPUFrequency)
    assert per_cpu.frequency.current == 2.3
    assert per_cpu.power == 50.0
    assert isinstance(per_cpu.times, CPUTimes)
    assert per_cpu.times.user == 120.0
    assert per_cpu.times.system == 30.0
    assert per_cpu.times.idle == 600.0
    assert per_cpu.times.interrupt == 0.0
    assert per_cpu.times.dpc == 0.0
    assert isinstance(per_cpu.times_percent, CPUTimes)
    assert per_cpu.times_percent.user == 20.0
    assert per_cpu.times_percent.system == 5.0
    assert per_cpu.times_percent.idle == 100.0
    assert per_cpu.times_percent.interrupt == 0.0
    assert per_cpu.times_percent.dpc == 0.0
    assert per_cpu.usage == 20.0
    assert per_cpu.voltage == 1.2


def test_cpu(cpu: CPU = FIXTURE_CPU):
    """Test the CPU model."""
    assert isinstance(cpu, CPU)
    assert cpu.count == 4
    assert isinstance(cpu.frequency, CPUFrequency)
    assert cpu.frequency.current == 2.3
    assert cpu.load_average == 1.5
    assert isinstance(cpu.per_cpu, list)
    _test_per_cpu(cpu.per_cpu[0])
    assert cpu.power == 200.0
    assert isinstance(cpu.stats, CPUStats)
    assert cpu.stats.ctx_switches == 1000
    assert cpu.stats.interrupts == 500
    assert cpu.stats.soft_interrupts == 200
    assert cpu.stats.syscalls == 8000
    assert cpu.temperature == 45.0
    assert isinstance(cpu.times, CPUTimes)
    assert cpu.times.user == 480.0
    assert cpu.times.system == 120.0
    assert cpu.times.idle == 2400.0
    assert cpu.times.interrupt == 0.0
    assert cpu.times.dpc == 0.0
    assert isinstance(cpu.times_percent, CPUTimes)
    assert cpu.times_percent.user == 80.0
    assert cpu.times_percent.system == 20.0
    assert cpu.times_percent.idle == 400.0
    assert cpu.times_percent.interrupt == 0.0
    assert cpu.times_percent.dpc == 0.0
    assert cpu.usage == 80.0
    assert cpu.voltage == 1.2


def test_cpu_dict():
    """Test CPU dict."""
    cpu_dict = asdict(FIXTURE_CPU)
    assert isinstance(cpu_dict["frequency"], dict)
    assert isinstance(cpu_dict["per_cpu"], list)
    assert isinstance(cpu_dict["per_cpu"][0], dict)
    assert isinstance(cpu_dict["per_cpu"][0]["id"], int)
    assert isinstance(cpu_dict["per_cpu"][0]["frequency"], dict)
    assert isinstance(cpu_dict["per_cpu"][0]["power"], float)
    assert isinstance(cpu_dict["per_cpu"][0]["times"], dict)
    assert isinstance(cpu_dict["per_cpu"][0]["times_percent"], dict)
    assert isinstance(cpu_dict["per_cpu"][0]["usage"], float)
    assert isinstance(cpu_dict["per_cpu"][0]["voltage"], float)
    assert isinstance(cpu_dict["stats"], dict)
    assert isinstance(cpu_dict["times"], dict)
    assert isinstance(cpu_dict["times_percent"], dict)
    assert isinstance(cpu_dict["stats"], dict)

    cpu_converted = CPU(**cpu_dict)
    test_cpu(cpu_converted)


def test_cpu_per_cpu_dict():
    """Test CPU PerCPU dict."""
    assert isinstance(FIXTURE_CPU.per_cpu, list)

    per_cpu = FIXTURE_CPU.per_cpu[0]
    per_cpu_dict = asdict(per_cpu)
    assert isinstance(per_cpu_dict["id"], int)
    assert isinstance(per_cpu_dict["frequency"], dict)
    assert isinstance(per_cpu_dict["power"], float)
    assert isinstance(per_cpu_dict["times"], dict)
    assert isinstance(per_cpu_dict["times_percent"], dict)
    assert isinstance(per_cpu_dict["usage"], float)
    assert isinstance(per_cpu_dict["voltage"], float)

    per_cpu_converted = PerCPU(**per_cpu_dict)
    _test_per_cpu(per_cpu_converted)
