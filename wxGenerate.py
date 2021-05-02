# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 451,321 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu2 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Whinar Kukuh Rizky Ardana", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem2 )

		self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"192410102041", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem3 )

		self.m_menubar2.Append( self.m_menu2, u"Identity" )

		self.SetMenuBar( self.m_menubar2 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_buttonClear = wx.Button( self, wx.ID_ANY, u"CLEAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_buttonClear, 0, wx.ALL, 5 )

		self.m_buttonPersen = wx.Button( self, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_buttonPersen, 0, wx.ALL, 5 )

		self.m_buttonPangkat = wx.Button( self, wx.ID_ANY, u"X^2", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_buttonPangkat, 0, wx.ALL, 5 )

		self.m_buttonAkar = wx.Button( self, wx.ID_ANY, u"X^1/2", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_buttonAkar, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_button8, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_button9, 0, wx.ALL, 5 )

		self.m_buttonKali = wx.Button( self, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_buttonKali, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_button4, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_buttonTambah = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_buttonTambah, 0, wx.ALL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_buttonKurang = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_buttonKurang, 0, wx.ALL, 5 )

		self.m_buttonKoma = wx.Button( self, wx.ID_ANY, u".", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_buttonKoma, 0, wx.ALL, 5 )

		self.m_button0 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_button0, 0, wx.ALL, 5 )

		self.m_buttonHasil = wx.Button( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_buttonHasil, 0, wx.ALL, 5 )

		self.m_buttonBagi = wx.Button( self, wx.ID_ANY, u"/", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_buttonBagi, 0, wx.ALL, 5 )


		bSizer1.Add( wSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonClear.Bind( wx.EVT_BUTTON, self.deleteAll )
		self.m_buttonPersen.Bind( wx.EVT_BUTTON, self.handleOperator )
		self.m_buttonPangkat.Bind( wx.EVT_BUTTON, self.secondRank )
		self.m_buttonAkar.Bind( wx.EVT_BUTTON, self.seconRankRoot )
		self.m_button8.Bind( wx.EVT_BUTTON, self.onClick )
		self.m_button7.Bind( wx.EVT_BUTTON, self.onClick )
		self.m_button9.Bind( wx.EVT_BUTTON, self.onClick )
		self.m_buttonKali.Bind( wx.EVT_BUTTON, self.handleOperator )
		self.m_button4.Bind( wx.EVT_BUTTON, self.onClick )
		self.m_button5.Bind( wx.EVT_BUTTON, self.onClick )
		self.m_button6.Bind( wx.EVT_BUTTON, self.onClick )
		self.m_buttonTambah.Bind( wx.EVT_BUTTON, self.handleOperator )
		self.m_button1.Bind( wx.EVT_BUTTON, self.onClick )
		self.m_button2.Bind( wx.EVT_BUTTON, self.onClick )
		self.m_button3.Bind( wx.EVT_BUTTON, self.onClick )
		self.m_buttonKurang.Bind( wx.EVT_BUTTON, self.handleOperator )
		self.m_buttonKoma.Bind( wx.EVT_BUTTON, self.onClick )
		self.m_button0.Bind( wx.EVT_BUTTON, self.onClick )
		self.m_buttonHasil.Bind( wx.EVT_BUTTON, self.hasil )
		self.m_buttonBagi.Bind( wx.EVT_BUTTON, self.handleOperator )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def deleteAll( self, event ):
		event.Skip()

	def handleOperator( self, event ):
		event.Skip()

	def secondRank( self, event ):
		event.Skip()

	def seconRankRoot( self, event ):
		event.Skip()

	def onClick( self, event ):
		event.Skip()














	def hasil( self, event ):
		event.Skip()



