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
