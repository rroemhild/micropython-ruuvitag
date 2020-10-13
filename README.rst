============================
MicroPython RuuviTag Scanner
============================

Harvest data from `RuuviTag BLE Sensor Beacon <http://ruuvitag.com/>`_ with MicroPython.

**Work In Progress**

micropython-ruuvitag supports RuuviTag Data Format 3 (RAWv1) and 5 (RAWv2) only. See `RuuviTag Sensor protocols <https://github.com/ruuvi/ruuvi-sensor-protocols>`_ for details.

The ruuvitag scanner for **Pycom devices** was transfered to a new repo `pycom-ruuvitag <https://github.com/rroemhild/pycom-ruuvitag>`_.


Installation
------------

Copy all files from the ``ruuvitag`` direcotory to the ``lib/ruuvitag`` directory on your device. Alternative you can use mpfshell to copy all files:

.. code-block:: shell

    mpfshell ttyUSB0 -s install.mpf


Scanner
-------

``RuuviTagScanner`` scans for RuuviTags and decode the data format. The result is a list with named tuples.

Scan 10 seconds for RuuviTag sensors and print the result:

.. code-block:: python

    from ruuvitag.scanner import RuuviTagScanner

    rts = RuuviTagScanner()

    for ruuvitag in rts.find_ruuvitags(timeout=10):
        print(ruuvitag)


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

You can collect data from only the devices you want by define a whitelist with mac addresses. Other Devices then will be ignored. Whitelists can be used with RuuviTagScanner and RuuviTagTracker.

.. code-block:: python

    whitelist = (b'aa:bb:cc:dd:ee:21', b'aa:bb:cc:dd:ee:42',)
    rts = RuuviTagScanner(whitelist)


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
