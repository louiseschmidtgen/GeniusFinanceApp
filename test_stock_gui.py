from tkinter import *
from stock_gui import StockGUI
from test_user import create_valid_user_object
from main import set_env_variables
set_env_variables()
root = Tk()
root.geometry("515x490")

stock_symbol = "TSLA"
stockData = {'TSLA':{'currentRatio': 1.508, 'trailingEPS': 1.897, 'PERatio': 412.6252, 'DebtToEquityRatio': 42.552, 'stockPrice': 782.75}}
stock_graph_values = [[1633507200, 1633508100, 1633509000, 1633509900, 1633510800, 1633511700, 1633512600, 1633513500, 1633514400, 1633515300, 1633516200, 1633517100, 1633518000, 1633518900, 1633519800, 1633520700, 1633521600, 1633522500, 1633523400, 1633524300, 1633525200, 1633526100, 1633527000, 1633527900, 1633528800, 1633529700, 1633530600, 1633531500, 1633532400, 1633533300, 1633534200, 1633535100, 1633536000, 1633536900, 1633537800, 1633538700, 1633539600, 1633540500, 1633541400, 1633542300, 1633543200, 1633544100, 1633545000, 1633545900, 1633546800, 1633547700, 1633548600, 1633549500, 1633550400, 1633551300, 1633552200, 1633553100, 1633554000, 1633554900, 1633555800, 1633556700, 1633557600, 1633558500, 1633559400, 1633560300, 1633561200, 1633562100, 1633563000, 1633563900],\
                      [771.38, 771.99, 770.71, 771.96, 769.56, 769.79, 767.5, 766.7, 767.93, 768.0, 769.21, 769.0, 769.88, 772.74, 771.67, 771.15, 772.59, 772.81, 773.0, 773.97, 772.34, 774.9, 776.7391967773438, 785.364990234375, 776.405029296875, 778.2611083984375, 781.1599731445312, 782.1798706054688, 784.5, 782.0599975585938, 780.280029296875, 783.2999877929688, 784.7501220703125, 779.7999877929688, 777.5800170898438, 779.3800048828125, 778.2999877929688, 778.0, 780.3900146484375, 782.3115234375, 782.2000122070312, 783.3150024414062, 783.8900146484375, 784.0999755859375, 781.510009765625, 782.010009765625, 780.1849975585938, 780.4099731445312, 782.75, 781.99, 782.31, 782.065, 782.0, 781.875, 781.985, 782.165, 782.25, 783.14, 783.0, 783.5, 783.5, 784.74, 783.36, 783.52]]
newslink = "https://finance.yahoo.com/news/tesla-verdict-owen-diaz-194928289.html"
userObject = create_valid_user_object()
loginGUIObject = StockGUI(root,stock_symbol, stockData, stock_graph_values, newslink,userObject )
root.mainloop()