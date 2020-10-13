============================
MicroPython RuuviTag Scanner
============================

Harvest data from `RuuviTag BLE Sensor Beacon <http://ruuvitag.com/>`_ with MicroPython.

micropython-ruuvitag supports RuuviTag Data Format 3 (RAWv1) and 5 (RAWv2) only. See `RuuviTag Sensor protocols <https://github.com/ruuvi/ruuvi-sensor-protocols>`_ for details.

The ruuvitag scanner for **Pycom devices** was transfered to a new repo `pycom-ruuvitag <https://github.com/rroemhild/pycom-ruuvitag>`_.


Installation
------------

Copy all files from the ``ruuvitag`` direcotory to the ``lib/ruuvitag`` directory on your device. Alternative you can use mpfshell to copy all files:

.. code-block:: shell

    mpfshell ttyUSB0 -s install.mpf


Example
-------

.. code-block:: python

    import time

    from ruuvitag import RuuviTag


    def cb(ruuvitag):
        print(ruuvitag)


    def run(self):
        try:
            while True:
                ruuvi.scan()
                time.sleep_ms(50000)
        except KeyboardInterrupt:
            ruuvi.stop()


    if __name__ == "__main__":
        ruuvi = RuuviTag()
        ruuvi._callback_handler = cb
        run(ruuvi)


Whitelist devices
-----------------

You can collect data from only the devices you want by define a whitelist with mac the devices addresses. Do not include ``:`` in the mac address. For example

.. code-block:: python

    whitelist = (b'aabbccddee21', b'aabbccddee42',)
    ruuvi = RuuviTag(whitelist=whitelist)


Blacklist persistence
---------------------

If the data from a Bluetooth device can not be decoded, the device get on a blacklist as long the MicroPython device is not resetted.


Named tuple formats
-------------------

Data Format 3 (RAWv1)
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    RuuviTagRAWv1 = namedtuple('RuuviTagRAWv1', (
        'mac',
        'rssi',
        'format',
        'humidity',
        'temperature',
        'pressure',
        'acceleration_x',
        'acceleration_y',
        'acceleration_z',
        'battery_voltage',
    ))


Data Format 5 (RAWv2)
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    RuuviTagRAWv2 = namedtuple('RuuviTagRAWv2', (
        'mac',
        'rssi',
        'format',
        'humidity',
        'temperature',
        'pressure',
        'acceleration_x',
        'acceleration_y',
        'acceleration_z',
        'battery_voltage',
        'power_info',
        'movement_counter',
        'measurement_sequence',
    ))
