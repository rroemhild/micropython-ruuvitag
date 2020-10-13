from ucollections import namedtuple


RuuviTagRAWv1 = namedtuple(
    "RuuviTagRAWv1",
    (
        "mac",
        "rssi",
        "format",
        "humidity",
        "temperature",
        "pressure",
        "acceleration_x",
        "acceleration_y",
        "acceleration_z",
        "battery_voltage",
    ),
)

RuuviTagRAWv2 = namedtuple(
    "RuuviTagRAWv2",
    (
        "mac",
        "rssi",
        "format",
        "humidity",
        "temperature",
        "pressure",
        "acceleration_x",
        "acceleration_y",
        "acceleration_z",
        "battery_voltage",
        "power_info",
        "movement_counter",
        "measurement_sequence",
    ),
)
