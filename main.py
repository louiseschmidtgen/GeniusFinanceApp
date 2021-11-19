from tkinter import *
from loginGUI import LoginGUI
import os

def set_env_variables():
    #export variables to environment for yahoo finance
    os.environ["X_RapidAPI_Host"]= "yh-finance.p.rapidapi.com"
    os.environ["X_RapidAPI_Key"]= '8a0078eb09mshe392d2a22c70852p124c55jsn28f16bd77fb6'
    os.environ["GENIUS_FINC_DB_NAME"]= "GeniusFinanceDB"
    os.environ['SQLUser']='root'
    os.environ['SQLPassword']= 'July2001'
    os.environ['SQLHost'] = "localhost"
    os.environ['DB_NAME'] ='GeniusFinanceDB'

def main():
    #contains what is happening when APP is started
    set_env_variables()
    #logging.basicConfig(filename='geniusfinclogs.log', encoding='utf-8', level=print, force=True)    
    #create DB manager
    #db_manager_object = DB()
    
    root = Tk()
    root.geometry("515x490")
    loginGUIObject = LoginGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()