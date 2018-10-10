from pinance import Pinance

symbol = "OGEN"

stock = Pinance(symbol)

stock.get_quotes()

print((stock.quotes_data))