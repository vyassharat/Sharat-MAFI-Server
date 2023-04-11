from Instruments.Option import Option
from Instruments.OptionType import OptionType
from Pricers.IPricer import IPricer
import numpy as np
from scipy.stats import norm

class BSMPricer(IPricer):
    def price(self, option: Option):
        d1 = self.compute_d1(
            option.spotPrice,
            option.strikePrice,
            option.riskFreeRate,
            option.dividendYield,
            option.volatility,
            option.timeToMaturity)

        d2 = self.compute_d2(
            d1,
            option.volatility,
            option.timeToMaturity)

        if option.optionType == OptionType.CALL:
            price = (option.spotPrice * np.exp(-1 * option.dividendYield * option.timeToMaturity) * norm.cdf(d1))
            price -= (option.strikePrice * np.exp(-1 * option.riskFreeRate * option.timeToMaturity) * norm.cdf(d2))
        else:
            price = -1 * (option.spotPrice * np.exp(-1 * option.dividendYield * option.timeToMaturity) * norm.cdf(-1 * d1))
            price += (option.strikePrice * np.exp(-1 * option.riskFreeRate * option.timeToMaturity) * norm.cdf(-1 * d2))

        return price

    # Used to centralize computations for D1
    def compute_d1(self, S, K, r, delta, sigma, TTM):
        numerator = np.log(S / K) + (r - delta + ((sigma ** 2) / 2) * TTM)
        denominator = sigma * np.sqrt(TTM)

        return numerator / denominator

    # Used to centralize computations for D2
    def compute_d2(self, d1, sigma, TTM):
        return d1 - sigma * np.sqrt(TTM)