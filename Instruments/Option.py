from Instruments.InstrumentType import InstrumentType
from Instruments.Instrument import Instrument
from Instruments.OptionType import OptionType


class Option(Instrument):
    def __init__(self,strikePrice:float,spotPrice:float,riskFreeRate:float,timeToMaturity:float,volatility:float,divYield:float,optionType:OptionType):
        self.volatility = volatility
        self.timeToMaturity = timeToMaturity
        self.riskFreeRate = riskFreeRate
        self.spotPrice = spotPrice
        self.strikePrice = strikePrice
        self.optionType = optionType
        self.dividendYield = divYield
        self.instrumentType = InstrumentType.OPTION

    def toString(self):
        return "Sharat"

    def getInstrumentType(self):
        return self.instrumentType
