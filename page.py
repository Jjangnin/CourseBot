import tkinter as tk
from datatable import DataTablePage, DataTablePage2
import pandas as pd
from PIL import ImageTk, Image

class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        image = Image.open(r"안양대 로고 불투명.png")
        image = image.resize((950, 950), Image.BICUBIC)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo)
        label.image = photo  # reference를 유지하여 이미지가 GC되지 않도록 함
        label.place(x=-10, y=300, relwidth=1, relheight=1)

        title_frame = tk.Frame(self, bg="skyblue")
        title_frame.pack(pady=100, padx=10, fill="x")
        # 위쪽 파란색 줄
        top_yellow_line = tk.Frame(title_frame, bg="blue", height=10)
        top_yellow_line.pack(fill="x", side="top")

        label = tk.Label(title_frame, text="안양대학교 소프트웨어 강의조회", font=("Helvetica", 50,"bold"), bg="skyblue")
        label.pack(pady=100, padx=30)

        # 아래쪽 파란색 줄
        bottom_yellow_line = tk.Frame(title_frame, bg="blue", height=10)
        bottom_yellow_line.pack(fill="x", side="bottom")

        button_frame = tk.Frame(self)
        button_frame.pack(pady=20, padx=20)

        # 버튼이 들어갈 프레임 생성
        frame1 = tk.Frame(button_frame, width=300, height=100)  # 픽셀 단위로 프레임 크기 설정
        frame1.pack_propagate(False)  # 프레임 크기 고정
        frame1.grid(row=0, column=0, padx=10)

        frame2 = tk.Frame(button_frame, width=300, height=100)
        frame2.pack_propagate(False)
        frame2.grid(row=0, column=1, padx=10)

        # 프레임 내에 버튼 추가
        button1 = tk.Button(frame1, text="전공과목",command=lambda: controller.show_frame("SecondPage"), bg="lightblue", font=("Helvetica", 25, "bold"))
        button1.pack(fill=tk.BOTH, expand=True)

        button2 = tk.Button(frame2, text="교양과목",command=lambda: controller.show_frame("ThirdPage"), bg="lightblue", font=("Helvetica", 25, "bold"))
        button2.pack(fill=tk.BOTH, expand=True)

         # 하늘색 네모 상자 추가
        bottom_frame = tk.Frame(self, bg="skyblue", height=100)
        bottom_frame.pack(side="bottom", fill="x", pady=0)

        bottom_label = tk.Label(bottom_frame, text="[파이썬 프로그래밍 프로젝트]_송민규, 전지선, 장인서", font=("Helvetica", 20, "bold"), bg="skyblue")
        bottom_label.pack(pady=10)

        # 작은 파란색 네모 상자 추가 (하늘색 네모 상자 위에)
        top_small_frame = tk.Frame(self, bg="blue", height=10)
        top_small_frame.pack(side="bottom", fill="x", pady=0)
        

class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

         # 파란색 굵은 줄 추가
        top_line = tk.Frame(self, bg="blue", height=10)
        top_line.pack(fill="x")

        # 하늘색 배경의 직사각형 상자 생성
        title_frame = tk.Frame(self, bg="skyblue")
        title_frame.pack(fill="x")

        # 제목 레이블
        label = tk.Label(title_frame, text="전공과목", font=("Helvetica", 40, "bold"), bg="skyblue")
        label.pack(pady=100, padx=30)

        # 아래 파란색 굵은 줄 추가
        bottom_line = tk.Frame(self, bg="blue", height=10)
        bottom_line.pack(fill="x")

        button_frame = tk.Frame(self)
        button_frame.pack(pady=100)
        
        button_font = ("Helvetica", 30,"bold")

        button1 = tk.Button(button_frame, text="1학년", command=lambda: controller.show_frame("FirstYearPage"), bg="lightblue", width=20, height=3, font=button_font)
        button1.grid(row=0, column=0, padx=5)

        button2 = tk.Button(button_frame, text="2학년", command=lambda: controller.show_frame("SecondYearPage"), bg="lightblue", width=20, height=3, font=button_font)
        button2.grid(row=0, column=1, padx=5)

        button3 = tk.Button(button_frame, text="3학년", command=lambda: controller.show_frame("ThirdYearPage"), bg="lightblue", width=20, height=3, font=button_font)
        button3.grid(row=0, column=2, padx=5)

        button4 = tk.Button(button_frame, text="4학년", command=lambda: controller.show_frame("FourthYearPage"), bg="lightblue", width=20, height=3, font=button_font)
        button4.grid(row=0, column=3, padx=5)

        button_back = tk.Button(self, text="메인페이지로 돌아가기", command=lambda: controller.show_frame("FirstPage"), font=("Helvetica", 15, "bold"), bg="lightblue", width=20, height=3)
        button_back.pack(pady=10)
         # 하늘색 네모 상자 추가
        bottom_frame = tk.Frame(self, bg="skyblue", height=100)
        bottom_frame.pack(side="bottom", fill="x", pady=0)

        bottom_label = tk.Label(bottom_frame, text="[파이썬 프로그래밍 프로젝트]_송민규, 전지선, 장인서", font=("Helvetica", 20, "bold"), bg="skyblue")
        bottom_label.pack(pady=10)

        # 작은 파란색 네모 상자 추가 (하늘색 네모 상자 위에)
        top_small_frame = tk.Frame(self, bg="blue", height=10)
        top_small_frame.pack(side="bottom", fill="x", pady=0)
        
        

class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # 파란색 굵은 줄 추가
        top_line = tk.Frame(self, bg="blue", height=10)
        top_line.pack(fill="x")

        # 하늘색 배경의 직사각형 상자 생성
        title_frame = tk.Frame(self, bg="skyblue")
        title_frame.pack(fill="x")

        # 제목 레이블
        label = tk.Label(title_frame, text="교양과목", font=("Helvetica", 40, "bold"), bg="skyblue")
        label.pack(pady=100, padx=30)

        # 아래 파란색 굵은 줄 추가
        bottom_line = tk.Frame(self, bg="blue", height=10)
        bottom_line.pack(fill="x")
        
        button_frame = tk.Frame(self)
        button_frame.pack(pady=100)
        
        
        button_font = ("Helvetica", 30,"bold")
        
        # 각 버튼의 command에서 특정 학기 데이터 로딩을 위해 load_data 메소드 호출
        button1 = tk.Button(button_frame, text="1학기", 
                            command=lambda: self.load_data(controller, "1학기"), bg="lightblue", width=20, height=3, font=button_font)
        button1.grid(row=0, column=0, padx=5)

        button2 = tk.Button(button_frame, text="2학기", 
                            command=lambda: self.load_data(controller, "2학기"), bg="lightblue", width=20, height=3, font=button_font)
        button2.grid(row=0, column=1, padx=5)

        button = tk.Button(self, text="메인페이지로 돌아가기", command=lambda: controller.show_frame("FirstPage"),font=("Helvetica", 15, "bold"), bg="lightblue", width=20, height=3)
        button.pack(pady=10)
         # 하늘색 네모 상자 추가
        bottom_frame = tk.Frame(self, bg="skyblue", height=100)
        bottom_frame.pack(side="bottom", fill="x", pady=0)

        bottom_label = tk.Label(bottom_frame, text="[파이썬 프로그래밍 프로젝트]_송민규, 전지선, 장인서", font=("Helvetica", 20, "bold"), bg="skyblue")
        bottom_label.pack(pady=10)

        # 작은 파란색 네모 상자 추가 (하늘색 네모 상자 위에)
        top_small_frame = tk.Frame(self, bg="blue", height=10)
        top_small_frame.pack(side="bottom", fill="x", pady=0)
        
    def load_data(self, controller, term):
        file_path = f"./교양{term}.xlsx"
        df = pd.read_excel(file_path)
        
        # 예제에서는 모든 데이터를 사용하므로 필터링 과정은 생략합니다.
        columns_to_display = [
            '과목명', '분반', '이수\n구분', '과목\n구분', '역량', '대표교수', 
            '주야\n구분', '온라인\n강의\n비율', '학점', '상대\n평가\n유형', '패스\n과목\n여부', '시간표'
        ]
        filtered_data = df[columns_to_display]
        data_page = DataTablePage2(controller.frames["ThirdPage"].master, controller, filtered_data)
        controller.frames["DataTablePage2"] = data_page
        data_page.grid(row=0, column=0, sticky="nsew")
        controller.show_frame("DataTablePage2")
        

class FirstYearPage(tk.Frame):# 1학년 페이지
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # 파란색 굵은 줄 추가
        top_line = tk.Frame(self, bg="blue", height=10)
        top_line.pack(fill="x")

        # 하늘색 배경의 직사각형 상자 생성
        title_frame = tk.Frame(self, bg="skyblue")
        title_frame.pack(fill="x")

        # 제목 레이블
        label = tk.Label(title_frame, text="1학년 전공과목", font=("Helvetica", 40, "bold"), bg="skyblue")
        label.pack(pady=100, padx=30)

        # 아래 파란색 굵은 줄 추가
        bottom_line = tk.Frame(self, bg="blue", height=10)
        bottom_line.pack(fill="x")

        button_frame = tk.Frame(self)
        button_frame.pack(pady=100)
        
        button_font = ("Helvetica", 30,"bold")
        

        button1 = tk.Button(button_frame, text="1학기", command=lambda: self.show_data1(controller), bg="lightblue", width=20, height=3, font=button_font)
        button1.grid(row=0, column=0, padx=5)

        button2 = tk.Button(button_frame, text="2학기", command=lambda: self.show_data2(controller), bg="lightblue", width=20, height=3, font=button_font)
        button2.grid(row=0, column=1, padx=5)

        button = tk.Button(self, text="전공과목으로 돌아가기", command=lambda: controller.show_frame("SecondPage"),font=("Helvetica", 15, "bold"), bg="lightblue", width=20, height=3)
        button.pack(pady=10)
         # 하늘색 네모 상자 추가
        bottom_frame = tk.Frame(self, bg="skyblue", height=100)
        bottom_frame.pack(side="bottom", fill="x", pady=0)

        bottom_label = tk.Label(bottom_frame, text="[파이썬 프로그래밍 프로젝트]_송민규, 전지선, 장인서", font=("Helvetica", 20, "bold"), bg="skyblue")
        bottom_label.pack(pady=10)

        # 작은 파란색 네모 상자 추가 (하늘색 네모 상자 위에)
        top_small_frame = tk.Frame(self, bg="blue", height=10)
        top_small_frame.pack(side="bottom", fill="x", pady=0)

    
    def show_data1(self, controller):
        file_path = "./전공1학기.xlsx"
        df = pd.read_excel(file_path)
        filtered_data = df[df["개설\n학년"] == 1]
        columns_to_display = ['과목명', '분반', '이수\n구분', '과목\n구분', '대표교수', '온라인\n강의\n비율', '학점', '상대\n평가\n유형', '패스\n과목\n여부', '시간표']
        filtered_data = filtered_data[columns_to_display]
        data_page = DataTablePage(controller.frames["SecondPage"].master, controller, filtered_data)
        controller.frames["DataTablePage"] = data_page
        data_page.grid(row=0, column=0, sticky="nsew")
        controller.show_frame("DataTablePage") 

    def show_data2(self, controller):
        file_path = "./전공2학기.xlsx"
        df = pd.read_excel(file_path)
        filtered_data = df[df["개설\n학년"] == 1]
        columns_to_display = ['과목명', '분반', '이수\n구분', '과목\n구분', '대표교수', '온라인\n강의\n비율', '학점', '상대\n평가\n유형', '패스\n과목\n여부', '시간표']
        filtered_data = filtered_data[columns_to_display]
        data_page = DataTablePage(controller.frames["SecondPage"].master, controller, filtered_data)
        controller.frames["DataTablePage"] = data_page
        data_page.grid(row=0, column=0, sticky="nsew")
        controller.show_frame("DataTablePage")
         
        

class SecondYearPage(tk.Frame): #2학년 페이지
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # 파란색 굵은 줄 추가
        top_line = tk.Frame(self, bg="blue", height=10)
        top_line.pack(fill="x")

        # 하늘색 배경의 직사각형 상자 생성
        title_frame = tk.Frame(self, bg="skyblue")
        title_frame.pack(fill="x")

        # 제목 레이블
        label = tk.Label(title_frame, text="2학년 전공과목", font=("Helvetica", 40, "bold"), bg="skyblue")
        label.pack(pady=100, padx=30)

        # 아래 파란색 굵은 줄 추가
        bottom_line = tk.Frame(self, bg="blue", height=10)
        bottom_line.pack(fill="x")
        button_frame = tk.Frame(self)
        button_frame.pack(pady=100)
        
        button_font = ("Helvetica", 30,"bold")

        button1 = tk.Button(button_frame, text="1학기", command=lambda: self.show_data1(controller), bg="lightblue", width=20, height=3, font=button_font)
        button1.grid(row=0, column=0, padx=5)

        button2 = tk.Button(button_frame, text="2학기", command=lambda: self.show_data2(controller), bg="lightblue", width=20, height=3, font=button_font)
        button2.grid(row=0, column=1, padx=5)

        button = tk.Button(self, text="전공과목으로 돌아가기", command=lambda: controller.show_frame("SecondPage"), font=("Helvetica", 15, "bold"), bg="lightblue", width=20, height=3)
        button.pack(pady=10)
         # 하늘색 네모 상자 추가
        bottom_frame = tk.Frame(self, bg="skyblue", height=100)
        bottom_frame.pack(side="bottom", fill="x", pady=0)

        bottom_label = tk.Label(bottom_frame, text="[파이썬 프로그래밍 프로젝트]_송민규, 전지선, 장인서", font=("Helvetica", 20, "bold"), bg="skyblue")
        bottom_label.pack(pady=10)

        # 작은 파란색 네모 상자 추가 (하늘색 네모 상자 위에)
        top_small_frame = tk.Frame(self, bg="blue", height=10)
        top_small_frame.pack(side="bottom", fill="x", pady=0)

    def show_data1(self, controller):
        file_path = "./전공1학기.xlsx"
        df = pd.read_excel(file_path)
        filtered_data = df[df["개설\n학년"] == 2]
        columns_to_display = ['과목명', '분반', '이수\n구분', '과목\n구분', '대표교수', '온라인\n강의\n비율', '학점', '상대\n평가\n유형', '패스\n과목\n여부', '시간표']
        filtered_data = filtered_data[columns_to_display]
        data_page = DataTablePage(controller.frames["SecondPage"].master, controller, filtered_data)
        controller.frames["DataTablePage"] = data_page
        data_page.grid(row=0, column=0, sticky="nsew")
        controller.show_frame("DataTablePage")

    def show_data2(self, controller):
        file_path = "./전공2학기.xlsx"
        df = pd.read_excel(file_path)
        filtered_data = df[df["개설\n학년"] == 2]
        columns_to_display = ['과목명', '분반', '이수\n구분', '과목\n구분', '대표교수', '온라인\n강의\n비율', '학점', '상대\n평가\n유형', '패스\n과목\n여부', '시간표']
        filtered_data = filtered_data[columns_to_display]
        data_page = DataTablePage(controller.frames["SecondPage"].master, controller, filtered_data)
        controller.frames["DataTablePage"] = data_page
        data_page.grid(row=0, column=0, sticky="nsew")
        controller.show_frame("DataTablePage") 

class ThirdYearPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # 파란색 굵은 줄 추가
        top_line = tk.Frame(self, bg="blue", height=10)
        top_line.pack(fill="x")

        # 하늘색 배경의 직사각형 상자 생성
        title_frame = tk.Frame(self, bg="skyblue")
        title_frame.pack(fill="x")

        # 제목 레이블
        label = tk.Label(title_frame, text="3학년 전공과목", font=("Helvetica", 40, "bold"), bg="skyblue")
        label.pack(pady=100, padx=30)

        # 아래 파란색 굵은 줄 추가
        bottom_line = tk.Frame(self, bg="blue", height=10)
        bottom_line.pack(fill="x")

        button_frame = tk.Frame(self)
        button_frame.pack(pady=100)
        
        button_font = ("Helvetica", 30,"bold")

        button1 = tk.Button(button_frame, text="1학기", command=lambda: self.show_data1(controller), bg="lightblue", width=20, height=3, font=button_font)
        button1.grid(row=0, column=0, padx=5)

        button2 = tk.Button(button_frame, text="2학기", command=lambda: self.show_data2(controller), bg="lightblue", width=20, height=3, font=button_font)
        button2.grid(row=0, column=1, padx=5)

        button = tk.Button(self, text="전공과목으로 돌아가기", command=lambda: controller.show_frame("SecondPage"), font=("Helvetica", 15, "bold"), bg="lightblue", width=20, height=3)
        button.pack(pady=10)
         # 하늘색 네모 상자 추가
        bottom_frame = tk.Frame(self, bg="skyblue", height=100)
        bottom_frame.pack(side="bottom", fill="x", pady=0)

        bottom_label = tk.Label(bottom_frame, text="[파이썬 프로그래밍 프로젝트]_송민규, 전지선, 장인서", font=("Helvetica", 20, "bold"), bg="skyblue")
        bottom_label.pack(pady=10)

        # 작은 파란색 네모 상자 추가 (하늘색 네모 상자 위에)
        top_small_frame = tk.Frame(self, bg="blue", height=10)
        top_small_frame.pack(side="bottom", fill="x", pady=0)
    
    def show_data1(self, controller):
        file_path = "./전공1학기.xlsx"
        df = pd.read_excel(file_path)
        filtered_data = df[df["개설\n학년"] == 3]
        columns_to_display = ['과목명', '분반', '이수\n구분', '과목\n구분', '대표교수', '온라인\n강의\n비율', '학점', '상대\n평가\n유형', '패스\n과목\n여부', '시간표']
        filtered_data = filtered_data[columns_to_display]
        data_page = DataTablePage(controller.frames["SecondPage"].master, controller, filtered_data)
        controller.frames["DataTablePage"] = data_page
        data_page.grid(row=0, column=0, sticky="nsew")
        controller.show_frame("DataTablePage")

    def show_data2(self, controller):
        file_path = "./전공2학기.xlsx"
        df = pd.read_excel(file_path)
        filtered_data = df[df["개설\n학년"] == 3]
        columns_to_display = ['과목명', '분반', '이수\n구분', '과목\n구분', '대표교수', '온라인\n강의\n비율', '학점', '상대\n평가\n유형', '패스\n과목\n여부', '시간표']
        filtered_data = filtered_data[columns_to_display]
        data_page = DataTablePage(controller.frames["SecondPage"].master, controller, filtered_data)
        controller.frames["DataTablePage"] = data_page
        data_page.grid(row=0, column=0, sticky="nsew")
        controller.show_frame("DataTablePage") 

class FourthYearPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # 파란색 굵은 줄 추가
        top_line = tk.Frame(self, bg="blue", height=10)
        top_line.pack(fill="x")

        # 하늘색 배경의 직사각형 상자 생성
        title_frame = tk.Frame(self, bg="skyblue")
        title_frame.pack(fill="x")

        # 제목 레이블
        label = tk.Label(title_frame, text="4학년 전공과목", font=("Helvetica", 40, "bold"), bg="skyblue")
        label.pack(pady=100, padx=30)

        # 아래 파란색 굵은 줄 추가
        bottom_line = tk.Frame(self, bg="blue", height=10)
        bottom_line.pack(fill="x")

        button_frame = tk.Frame(self)
        button_frame.pack(pady=100)
        
        button_font = ("Helvetica", 30,"bold")

        button1 = tk.Button(button_frame, text="1학기", command=lambda: self.show_data1(controller), bg="lightblue", width=20, height=3, font=button_font)
        button1.grid(row=0, column=0, padx=5)

        button2 = tk.Button(button_frame, text="2학기", command=lambda: self.show_data2(controller), bg="lightblue", width=20, height=3, font=button_font)
        button2.grid(row=0, column=1, padx=5)

        button = tk.Button(self, text="전공과목으로 돌아가기", command=lambda: controller.show_frame("SecondPage"), font=("Helvetica", 15, "bold"), bg="lightblue", width=20, height=3)
        button.pack(pady=10)

         # 하늘색 네모 상자 추가
        bottom_frame = tk.Frame(self, bg="skyblue", height=100)
        bottom_frame.pack(side="bottom", fill="x", pady=0)

        bottom_label = tk.Label(bottom_frame, text="[파이썬 프로그래밍 프로젝트]_송민규, 전지선, 장인서", font=("Helvetica", 20, "bold"), bg="skyblue")
        bottom_label.pack(pady=10)

        # 작은 파란색 네모 상자 추가 (하늘색 네모 상자 위에)
        top_small_frame = tk.Frame(self, bg="blue", height=10)
        top_small_frame.pack(side="bottom", fill="x", pady=0)

    def show_data1(self, controller):
        file_path = "./전공1학기.xlsx"
        df = pd.read_excel(file_path)
        filtered_data = df[df["개설\n학년"] == 4]
        columns_to_display = ['과목명', '분반', '이수\n구분', '과목\n구분', '대표교수', '온라인\n강의\n비율', '학점', '상대\n평가\n유형', '패스\n과목\n여부', '시간표']
        filtered_data = filtered_data[columns_to_display]
        data_page = DataTablePage(controller.frames["SecondPage"].master, controller, filtered_data)
        controller.frames["DataTablePage"] = data_page
        data_page.grid(row=0, column=0, sticky="nsew")
        controller.show_frame("DataTablePage")

    def show_data2(self, controller):
        file_path = "./전공2학기.xlsx"
        df = pd.read_excel(file_path)
        filtered_data = df[df["개설\n학년"] == 4]
        columns_to_display = ['과목명', '분반', '이수\n구분', '과목\n구분', '대표교수', '온라인\n강의\n비율', '학점', '상대\n평가\n유형', '패스\n과목\n여부', '시간표']
        filtered_data = filtered_data[columns_to_display]
        data_page = DataTablePage(controller.frames["SecondPage"].master, controller, filtered_data)
        controller.frames["DataTablePage"] = data_page
        data_page.grid(row=0, column=0, sticky="nsew")
        controller.show_frame("DataTablePage") 
