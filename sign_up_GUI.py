# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 20:43:28 2021

@author: Owner
"""


class SignUpGUI():
    def __init__(self, LoginLogout,popup_GUI_object,username,password,
                 ReenteredPassword,SecurityQuestionAnswer,LoginGUIObject):
        self.LoginLogout = LoginLogout
        self.popup_GUI_object = popup_GUI_object
        self.username = username
        self.password = password
        self.ReenteredPassword = ReenteredPassword
        self.SecurityQuestionAnswer = SecurityQuestionAnswer
        self.LoginGUIObject = LoginGUIObject
        
    def HandleSignUpEvent():
        pass
    def HandleCloseEvent():
        pass
    def CreateMainFrame():
        pass
    def CreateUsernamePasswordFrame():
        pass
    def CreateSecurityQuestionFrame():
        pass