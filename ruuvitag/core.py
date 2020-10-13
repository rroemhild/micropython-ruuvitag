import ubinascii
import ubluetooth

from .decoder import decode_raw_1, decode_raw_2

from micropython import const


_IRQ_SCAN_RESULT = const(5)
_IRQ_SCAN_DONE = const(6)

_RUUVITAG = b"\x99\x04"
_RUUVITAG_RAW_1 = const(3)
_RUUVITAG_RAW_2 = const(5)


class RuuviTag:
    def __init__(self, whitelist=None, blacklist=[]):
        self._ble = ubluetooth.BLE()
        self._ble.active(True)
        self._ble.irq(self.irq_handler)
        self._tags = []  # store for processed tags reset each scan
        self._addrs = []  # store for received addresses reset each scan
        self._callback_handler = None
        self._whitelist = whitelist
        self._blacklist = blacklist

    def irq_handler(self, event, data):
        if event == _IRQ_SCAN_RESULT:
            addr_type, addr, connectable, rssi, adv_data = data

            addr = ubinascii.hexlify(addr)

            # Return early if tag allready scanned or in blacklist
            if addr in self._addrs or addr in self._blacklist:
                return

            # Remove meta data from adv_data
            data = adv_data[5:]

            # Return if tag is not manufacturer Ruuvi Innovations and add
            # device to blacklist
            if not data[:2] == _RUUVITAG:
                self._blacklist.append(addr)
                return

            # Append tag addr to scanned addresses to prevent multible results
            # for one tag in this scan
            self._addrs.append(addr)

            # If a whitelist is defined, only allow tags from that list.
            # Return early if the address is not on whitelist and add
            # the address to the blacklist to skip this address earlier on
            # the next scan.
            if self._whitelist is not None:
                if addr not in self._whitelist:
                    self._blacklist.append(addr)
                    return

            # Support only format 3 (RAWv1) and 5 (RAWv2)
            # Decode data and pass the namedtuple to callback handler
            if data[2] == _RUUVITAG_RAW_1:
                self._callback_handler(decode_raw_1(addr, rssi, data))
            elif data[2] == _RUUVITAG_RAW_2:
                self._callback_handler(decode_raw_2(addr, rssi, data))
        elif event == _IRQ_SCAN_DONE:
            # Scan duration finished or manually stopped.
            pass

    def scan(self):
        self._tags = []
        self._addrs = []
        self._ble.gap_scan(5000, 30000, 30000)

    def stop(self):
        self._ble.gap_scan(None)
