import sys
import os
import tkinter as tk
import pandas as pd

# 현재 파일의 디렉토리를 모듈 검색 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from page import FirstPage, SecondPage, ThirdPage, FirstYearPage, SecondYearPage, ThirdYearPage, FourthYearPage
from datatable import DataTablePage
from datatable import DataTablePage2

class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("파이썬 프로그래밍 프로젝트")
        self.state("zoomed")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage, FirstYearPage, SecondYearPage, ThirdYearPage, FourthYearPage, DataTablePage):
            page_name = F.__name__
            if page_name == "DataTablePage":
                frame = F(parent=container, controller=self, data=pd.read_excel("./전공1학기.xlsx"))
            else:
                frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            self.frames[page_name].grid(row=0, column=0, sticky="nsew")

        self.show_frame("FirstPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
