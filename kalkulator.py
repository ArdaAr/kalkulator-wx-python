import wx
from wxGenerate import MyFrame1

app = wx.App()
class frameKalkulator(MyFrame1):
    def __init__(self, parent):
        super().__init__(parent)
        self.firstNumber = 0
        self.secondNumber = 0
        self.nilaiHasil = 0
        self.waitingSecondNum = False
        self.operator = ''
        self.isDecimal = False

    def deleteAll(self, event):
        self.m_textCtrl1.Clear()
        self.secondNumber = 0
        self.firstNumber = 0
        self.nilaiHasil = 0
        self.waitingSecondNum = False
        self.operator = ''
        self.isDecimal = False

    def onClick(self, event):
        if self.waitingSecondNum == False:
            self.m_textCtrl1.Clear()
            angka = event.GetEventObject().GetLabel()
            self.m_textCtrl1.SetValue(angka)
        else:
            angka = event.GetEventObject().GetLabel()
            self.m_textCtrl1.AppendText(angka)
        self.waitingSecondNum = True

    def handleOperator(self, event):
        self.operator = event.GetEventObject().GetLabel()
        if self.waitingSecondNum == False:
            if self.operator=='+' or self.operator=='x' or self.operator=='/':
                pass
            else:
                self.m_textCtrl1.AppendText(self.operator)
                self.waitingSecondNum = True
        else:
            self.firstNumber = self.m_textCtrl1.GetValue()
            if '.' in self.firstNumber:
                self.firstNumber = float(self.firstNumber)
                self.isDecimal = True
            else :
                self.firstNumber = int(self.firstNumber)
                self.waitingSecondNum = False

    def hitung(self):
        if self.operator == '+':
            self.nilaiHasil = self.firstNumber + self.secondNumber
        elif self.operator == '-':
            self.nilaiHasil = self.firstNumber - self.secondNumber
        elif self.operator == 'x':
            self.nilaiHasil = self.firstNumber*self.secondNumber
        elif self.operator == '/':
            self.nilaiHasil = self.firstNumber/self.secondNumber
            if self.firstNumber%self.secondNumber == 0:
                self.nilaiHasil = int(self.nilaiHasil)

    def seconRankRoot(self,event):
        self.firstNumber = self.m_textCtrl1.GetValue()
        self.nilaiHasil = float(self.firstNumber)**(1/2)
        self.m_textCtrl1.SetValue(str(self.nilaiHasil))
        self.firstNumber = self.nilaiHasil

    def secondRank(self,event):
        self.firstNumber = self.m_textCtrl1.GetValue()
        self.nilaiHasil = pow(float(self.firstNumber),2)
        self.m_textCtrl1.SetValue(str(self.nilaiHasil))
        self.firstNumber = self.nilaiHasil

    def hasil(self,event):
        self.secondNumber = self.m_textCtrl1.GetValue()
        if self.isDecimal:
            self.secondNumber = float(self.secondNumber)
        else :
            self.secondNumber = int(self.secondNumber)
        self.hitung()
        self.m_textCtrl1.SetValue(str(self.nilaiHasil))
        self.firstNumber = self.nilaiHasil

kalkulator1 = frameKalkulator(parent=None)
kalkulator1.Show()
app.MainLoop()