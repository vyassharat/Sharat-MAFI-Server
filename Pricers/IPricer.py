from Instruments.Instrument import Instrument


class IPricer:
    def price(self, instrument:Instrument) -> float:
        pass