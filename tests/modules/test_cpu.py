"""Test the CPU model."""

from dataclasses import asdict

from systembridgemodels.modules.cpu import CPU, CPUFrequency, CPUStats, CPUTimes, PerCPU

model = CPU(
    count=4,
    frequency=CPUFrequency(
        current=2.3,
        min=0.8,
        max=3.1,
    ),
    load_average=1.5,
    per_cpu=[
        PerCPU(
            id=0,
            frequency=CPUFrequency(
                current=2.3,
                min=0.8,
                max=3.1,
            ),
            power=50.0,
            times=CPUTimes(
                user=120.0,
                system=30.0,
                idle=600.0,
                interrupt=0.0,
                dpc=0.0,
            ),
            times_percent=CPUTimes(
                user=20.0,
                system=5.0,
                idle=100.0,
                interrupt=0.0,
                dpc=0.0,
            ),
            usage=20.0,
            voltage=1.2,
        )
    ],
    power=200.0,
    stats=CPUStats(
        ctx_switches=1000,
        interrupts=500,
        soft_interrupts=200,
        syscalls=8000,
    ),
    temperature=45.0,
    times=CPUTimes(
        user=480.0,
        system=120.0,
        idle=2400.0,
        interrupt=0.0,
        dpc=0.0,
    ),
    times_percent=CPUTimes(
        user=80.0,
        system=20.0,
        idle=400.0,
        interrupt=0.0,
        dpc=0.0,
    ),
    usage=80.0,
    voltage=1.2,
)


def test_cpu(cpu: CPU = model):
    """Test the CPU model."""
    assert isinstance(cpu, CPU)
    assert cpu.count == 4
    assert isinstance(cpu.frequency, CPUFrequency)
    assert cpu.frequency.current == 2.3
    assert cpu.load_average == 1.5
    assert isinstance(cpu.per_cpu, list)
    assert isinstance(cpu.per_cpu[0], PerCPU)
    assert cpu.per_cpu[0].id == 0
    assert isinstance(cpu.per_cpu[0].frequency, CPUFrequency)
    assert cpu.per_cpu[0].frequency.current == 2.3
    assert cpu.per_cpu[0].power == 50.0
    assert isinstance(cpu.per_cpu[0].times, CPUTimes)
    assert cpu.per_cpu[0].times.user == 120.0
    assert cpu.per_cpu[0].times.system == 30.0
    assert cpu.per_cpu[0].times.idle == 600.0
    assert cpu.per_cpu[0].times.interrupt == 0.0
    assert cpu.per_cpu[0].times.dpc == 0.0
    assert isinstance(cpu.per_cpu[0].times_percent, CPUTimes)
    assert cpu.per_cpu[0].times_percent.user == 20.0
    assert cpu.per_cpu[0].times_percent.system == 5.0
    assert cpu.per_cpu[0].times_percent.idle == 100.0
    assert cpu.per_cpu[0].times_percent.interrupt == 0.0
    assert cpu.per_cpu[0].times_percent.dpc == 0.0
    assert cpu.per_cpu[0].usage == 20.0
    assert cpu.per_cpu[0].voltage == 1.2
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
    cpu_dict = asdict(model)
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
    assert isinstance(model.per_cpu, list)

    per_cpu = model.per_cpu[0]
    per_cpu_dict = asdict(per_cpu)
    assert isinstance(per_cpu_dict["id"], int)
    assert isinstance(per_cpu_dict["frequency"], dict)
    assert isinstance(per_cpu_dict["power"], float)
    assert isinstance(per_cpu_dict["times"], dict)
    assert isinstance(per_cpu_dict["times_percent"], dict)
    assert isinstance(per_cpu_dict["usage"], float)
    assert isinstance(per_cpu_dict["voltage"], float)

    per_cpu_converted = PerCPU(**per_cpu_dict)
    assert isinstance(per_cpu_converted, PerCPU)
    assert isinstance(per_cpu_converted.id, int)
    assert isinstance(per_cpu_converted.frequency, CPUFrequency)
    assert isinstance(per_cpu_converted.times, CPUTimes)
    assert isinstance(per_cpu_converted.times_percent, CPUTimes)
    assert isinstance(per_cpu_converted.usage, float)
    assert isinstance(per_cpu_converted.voltage, float)
    assert per_cpu_converted.id == 0
    assert per_cpu_converted.frequency.current == 2.3
    assert per_cpu_converted.power == 50.0
    assert per_cpu_converted.times.user == 120.0
    assert per_cpu_converted.times.system == 30.0
    assert per_cpu_converted.times.idle == 600.0
    assert per_cpu_converted.times.interrupt == 0.0
    assert per_cpu_converted.times.dpc == 0.0
    assert per_cpu_converted.times_percent.user == 20.0
    assert per_cpu_converted.times_percent.system == 5.0
    assert per_cpu_converted.times_percent.idle == 100.0
    assert per_cpu_converted.times_percent.interrupt == 0.0
    assert per_cpu_converted.times_percent.dpc == 0.0
    assert per_cpu_converted.usage == 20.0
    assert per_cpu_converted.voltage == 1.2
