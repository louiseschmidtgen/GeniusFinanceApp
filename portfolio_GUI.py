from tkinter import *
import tkinter as tk
from tkinter import ttk
import yahoo_api


class PortfolioGUI():
    def __init__(self,master, stocksymbol_price_change_dict, portfolio_value, userObject):
        self.master = master
        self.master.title("Portfolio")
        self.createMainFrame(userObject)
        #self.portfolio_controllerObject = portfolio_controller.PortfolioController()
        self.stocksymbol_price_change_dict = stocksymbol_price_change_dict
        self.portfolio_value = portfolio_value
        self.userObject = userObject
        self.yahoo_api_object = yahoo_api.YahooAPI()

    '''
    Intent: creates the main frame for the Portfolio GUI
    * Preconditions: master is connected to TKinter. 
    * createLoginFrame has the appropriate GUI code to be called in this method.
    * Postconditions:
    * Post0. main frame for Portfolio is created
    '''
    def createMainFrame(self,userObject): 
        # logo on top left side
        self.logo = Label(self.master, text="Genius Finance",font='Helvetica 12',height = 6, width = 13,borderwidth=2, relief="solid").grid(row=0,column=0, pady=5, padx=5)
        self.portfolioTitle = Label(self.master, text="My Stocks",font='Helvetica 12',height = 2, width = 13,borderwidth=2, relief="solid").grid(row=0,column=1, pady=5, padx=5, sticky="s")
        self.portoflioValueTitle = Label(self.master, text="Portfolio Value: ",font='Helvetica 12',height = 2, width = 13,borderwidth=2, relief="solid").grid(row=0,column=1, pady=5, padx=5, sticky="se")
        
        self.createMyStocksFrame(userObject)
        self.exitButton = Button(self.master,text="Exit", command=lambda:self.closeWindow()).grid(row = 4,column=1,sticky="se")
        self.removeButton = Button(self.master,text="Remove", command=lambda:self.removeStock()).grid(row = 4,column=1,sticky="s")
        self.WatchlistButton = Button(self.master,text="Go to Watchlist", command=lambda:self.openWatchlist()).grid(row = 4,column=1,sticky="sw")
    
    
    '''
    Intent: creates the users stocks frame for the portfolio GUI
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. user's stocks frame is created
    '''
    def createMyStocksFrame(self,userObject):
        stockName = Label(self.master, text="Stock Name",font='Helvetica 12',height = 1, width = 10,borderwidth=2, relief="solid").grid(row=1,column=1, sticky="w")
        self.portfolio = Listbox(self.master,height=20, width=40, borderwidth=2, relief="sunken")
        self.portfolio.grid(row = 2,column=1)
        self.yahoo_api_object = yahoo_api.YahooAPI()
    
        for i in userObject.current_user_stocks:
            self.portfolio.insert(END,i)
            
        #self.listBox.bind("<<ListboxSelect>>",lambda event,i=i: self.detailsPage(i))
        
       

        #scrollbar
        self.scrollbar = Scrollbar(self.master)
        #self.scrollbar.pack(side = RIGHT, fill = BOTH)


        
    
    '''
    Intent: close the portfolio window .
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. closes the portfolio window
    '''    
    def closeWindow(self):
        self.master.destroy()

    '''
    Intent: remove stock from list of stocks in portfolio window .
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. removes stock from portfolio window
    '''            
    def removeStock(self):
        pass
    
    '''
    Intent: creates a button on the frame that allows user to go to watchlist gui
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. allows user to go to watchlist gui from portfolio window
    '''  
    def openWatchlist(self):
        pass
    
'''
stocksymbol_price_change_dict = None
portfolio_value = None
   
root = Tk()
root.geometry("515x490")
loginGUIObject = PortfolioGUI(root, stocksymbol_price_change_dict, portfolio_value)
root.mainloop()
'''


