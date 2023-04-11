from flask import Flask

from Instruments.Option import Option
from Instruments.OptionType import OptionType
from Pricers.OptionPricers.BSMPricer import BSMPricer

app = Flask(__name__)

@app.route("/")
def hello():
    myOption = Option(100, 100,.05, 1, .02,0,OptionType.CALL)
    myOption2 = Option(100, 100, .05, 1, .02, 0, OptionType.PUT)
    optionPricer = BSMPricer()
    print("P1= $"+str(optionPricer.price(myOption))+"\nP2= $"+str(optionPricer.price(myOption2)))

    return "Hello Choggy"

if __name__ == "__main__":
  app.run()
