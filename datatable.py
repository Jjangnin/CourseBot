import tkinter as tk
from tkinter import ttk
import pandas as pd
import tkinter.font as tkfont
#from page import FirstPage, SecondPage, ThirdPage, FirstYearPage, SecondYearPage, ThirdYearPage, FourthYearPage

class DataTablePage(tk.Frame):
    def __init__(self, parent, controller, data):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.data = data

       # 열 이름에서 공백과 줄바꿈 제거
        self.data.columns = [col.strip().replace('\n', '') for col in self.data.columns]

        # 하늘색 배경의 직사각형 상자 생성
        title_frame = tk.Frame(self, bg="lightblue", padx=5, pady=5)
        title_frame.grid(row=0, column=0, pady=10, padx=10, columnspan=2, sticky="ew")

        # 제목 레이블 상단 파란색 줄
        top_blue_line = tk.Frame(title_frame, bg="blue", height=5)
        top_blue_line.pack(fill="x", side="top")

        # 제목 레이블
        label = tk.Label(title_frame, text="전공 개설 강좌", font=("Helvetica", 25, "bold"), bg="lightblue")
        label.pack(fill="both", expand=True)

        # 제목 레이블 하단 파란색 줄
        bottom_blue_line = tk.Frame(title_frame, bg="blue", height=5)
        bottom_blue_line.pack(fill="x", side="bottom")

        self.canvas = tk.Canvas(self)
        self.canvas.grid(row=1, column=0, sticky="nsew")

        self.tree_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.tree_frame, anchor="nw")

        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=1, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        columns = [col.replace('\n', '') for col in data.columns]

        
        # Treeview 스타일 설정
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 16, "bold"), borderwidth=1, relief="solid")
        style.configure("Treeview", font=("Helvetica", 14), rowheight=70)
        
        style.map("Treeview", background=[("selected", "blue")], foreground=[("selected", "white")])
        style.layout("Treeview", [
            ("Treeview.treearea", {"sticky": "nswe"})
        ])

        self.tree = ttk.Treeview(self.tree_frame, columns=columns, show='headings', style="Treeview")
        self.tree.pack(side="top", fill="both", expand=True)

        for col in columns:
            self.tree.heading(col, text=col, anchor=tk.W)
            if col == "시간표":
                self.tree.column(col, minwidth=0, width=1500, stretch=tk.YES)  # 시간표 열 너비 조정

            elif col == "과목명":
                self.tree.column(col, minwidth=0, width=300, stretch=tk.YES) 
            elif col == "분반":
                self.tree.column(col, minwidth=0, width=100, stretch=tk.YES)
            elif col == "이수구분":
                self.tree.column(col, minwidth=0, width=150, stretch=tk.YES)
            elif col == "과목구분":
                self.tree.column(col, minwidth=0, width=150, stretch=tk.YES)
            elif col == "대표교수":
                self.tree.column(col, minwidth=0, width=150, stretch=tk.YES)
            elif col == "온라인강의비율":
                self.tree.column(col, minwidth=0, width=220, stretch=tk.YES)
            elif col == "주야구분":
                self.tree.column(col, minwidth=0, width=80, stretch=tk.YES)
        
            elif col == "학점":
                self.tree.column(col, minwidth=0, width=100, stretch=tk.YES)
            
            elif col == "상대평가유형":
                self.tree.column(col, minwidth=0, width=200, stretch=tk.YES)
            
            elif col == "패스과목여부":
                self.tree.column(col, minwidth=0, width=200, stretch=tk.YES)

            else:
                self.tree.column(col, minwidth=0, width=250, stretch=tk.YES)

        for i, row in data.iterrows():
            values = list(row)
            self.tree.insert("", "end", values=values)

        self.tree_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        button = tk.Button(self, text="[전공과목]으로 돌아가기", command=lambda: controller.show_frame("SecondPage"), bg="lightblue", width=30, height=4, font=("Helvetica", 12))
        button.grid(row=2, column=0, pady=10, padx=10, columnspan=2)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # 대화 기능 추가
        self.chat_input = tk.Entry(self, font=("Helvetica", 16))
        self.chat_input.grid(row=3, column=0, pady=10, padx=10, sticky="ew", columnspan=2, ipady=10)
        self.chat_input.bind("<Return>", self.handle_chat_input)

        self.chat_display = tk.Text(self, height=10, wrap="word", font=("Helvetica", 16))
        self.chat_display.grid(row=4, column=0, pady=10, padx=10, sticky="nsew", columnspan=2)
        self.chat_display.config(state=tk.DISABLED)

        self.grid_rowconfigure(4, weight=1)

    def handle_chat_input(self, event):
        user_input = self.chat_input.get()
        self.chat_input.delete(0, tk.END)
        response = self.generate_response(user_input)
        self.display_response(response)

    def generate_response(self, user_input):
        query = user_input.strip().lower()
        response = ""
        
        def get_column_data(column_name):
            try:
                return ", ".join(self.data[column_name].dropna().unique().astype(str).tolist()) + "\n"
            except KeyError:
                return "챗봇: '{}' 열을 찾을 수 없습니다.\n".format(column_name)

        if "과목명" in query:
            if "전공" in query:
                response += "아냥봇: 전공 과목 목록입니다.\n"
                response += get_column_data("과목명")
            else:
                response += "아냥봇: 이번 학기 개설되는 과목 목록입니다.\n"
                response += get_column_data("과목명")

        elif "분반" in query:
            response += "아냥봇: 분반 목록입니다.\n"
            response += get_column_data("분반")

        elif "이수구분" in query:
            response += "아냥봇: 이수구분 목록입니다.\n"
            response += get_column_data("이수구분")

        elif "과목구분" in query:
            response += "아냥봇: 과목구분 목록입니다.\n"
            response += get_column_data("과목구분")

        elif "대표교수" in query:
            response += "아냥봇: 각 과목의 대표교수 목록입니다.\n"
            response += get_column_data("대표교수")

        elif "온라인 강의" in query:
            response += "아냥봇: 온라인 강의 비율은 {}%입니다.\n".format(get_column_data("온라인강의비율"))
        elif "학점" in query:
            response += "아냥봇: 각 과목의 학점 목록입니다.\n"
            response += ", ".join(map(str, self.data["학점"].tolist())) + "\n"

        elif "상대평가" in query:
            response += "아냥봇: 상대평가가 적용되는 과목 목록입니다.\n"
            response += get_column_data("상대평가유형")

        elif "패스 과목" in query:
            response += "아냥봇: 패스 과목 목록입니다.\n"
            pass_courses = self.data[self.data["패스과목여부"] == 1.0][["과목명", "분반"]]
            if not pass_courses.empty:
                for course_name, class_section in zip(pass_courses["과목명"], pass_courses["분반"]):
                    response += f"과목명: {course_name}, 분반: {class_section}\n"
            else:
                response += "패스 과목이 없습니다.\n"

        elif "시간표" in query:
            response += "아냥봇: 시간표 목록입니다.\n"
            response += get_column_data("시간표")

        else:
            response += "아냥봇: 죄송합니다. 요청하신 정보를 찾을 수 없습니다.\n"

        return response

    def display_response(self, response):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, response + "\n")
        self.chat_display.config(state=tk.DISABLED)

#==================================================================
class DataTablePage2(tk.Frame):
    def __init__(self, parent, controller, data):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.data = data

        # 열 이름에서 공백과 줄바꿈 제거
        self.data.columns = [col.strip().replace('\n', '') for col in self.data.columns]

        # 하늘색 배경의 직사각형 상자 생성
        title_frame = tk.Frame(self, bg="lightblue", padx=5, pady=5)
        title_frame.grid(row=0, column=0, pady=10, padx=10, columnspan=2, sticky="ew")

        # 제목 레이블 상단 파란색 줄
        top_blue_line = tk.Frame(title_frame, bg="blue", height=5)
        top_blue_line.pack(fill="x", side="top")

        # 제목 레이블
        label = tk.Label(title_frame, text="교양 개설 강좌", font=("Helvetica", 25, "bold"), bg="lightblue")
        label.pack(fill="both", expand=True)

        # 제목 레이블 하단 파란색 줄
        bottom_blue_line = tk.Frame(title_frame, bg="blue", height=5)
        bottom_blue_line.pack(fill="x", side="bottom")


        self.canvas = tk.Canvas(self)
        self.canvas.grid(row=1, column=0, sticky="nsew")

        self.tree_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.tree_frame, anchor="nw")

        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=1, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        columns = [col.replace('\n', '') for col in data.columns]

        
        # Treeview 스타일 설정
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), borderwidth=1, relief="solid")
        style.configure("Treeview", font=("Helvetica", 10), rowheight=70)
        
        style.map("Treeview", background=[("selected", "blue")], foreground=[("selected", "white")])
        style.layout("Treeview", [
            ("Treeview.treearea", {"sticky": "nswe"})
        ])

        self.tree = ttk.Treeview(self.tree_frame, columns=columns, show='headings', style="Treeview")
        self.tree.pack(side="top", fill="both", expand=True)

        for col in columns:
            self.tree.heading(col, text=col, anchor=tk.W)
            if col == "시간표":
                self.tree.column(col, minwidth=0, width=1500, stretch=tk.YES)  # 시간표 열 너비 조정

            elif col == "과목명":
                self.tree.column(col, minwidth=0, width=380, stretch=tk.YES) 
            elif col == "분반":
                self.tree.column(col, minwidth=0, width=50, stretch=tk.YES)
            elif col == "이수구분":
                self.tree.column(col, minwidth=0, width=80, stretch=tk.YES)
            elif col == "과목구분":
                self.tree.column(col, minwidth=0, width=80, stretch=tk.YES)
            elif col == "대표교수":
                self.tree.column(col, minwidth=0, width=180, stretch=tk.YES)
            elif col == "역량":
                self.tree.column(col, minwidth=0, width=90, stretch=tk.YES)
            elif col == "대표교수":
                self.tree.column(col, minwidth=0, width=200, stretch=tk.YES)
            elif col == "주야구분":
                self.tree.column(col, minwidth=0, width=80, stretch=tk.YES)
        
            elif col == "학점":
                self.tree.column(col, minwidth=0, width=60, stretch=tk.YES)
            
            elif col == "상대평가유형":
                self.tree.column(col, minwidth=0, width=130, stretch=tk.YES)
            
            elif col == "패스과목여부":
                self.tree.column(col, minwidth=0, width=130, stretch=tk.YES)

            else:
                self.tree.column(col, minwidth=0, width=130, stretch=tk.YES)

        for i, row in data.iterrows():
            values = list(row)
            self.tree.insert("", "end", values=values)

        self.tree_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        button = tk.Button(self, text="[교양과목]으로 돌아가기", command=lambda: controller.show_frame("ThirdPage"), bg="lightblue", width=30, height=4, font=("Helvetica", 12))
        button.grid(row=2, column=0, pady=10, padx=10, columnspan=2)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # 대화 기능 추가
        self.chat_input = tk.Entry(self, font=("Helvetica", 16))
        self.chat_input.grid(row=3, column=0, pady=10, padx=10, sticky="ew", columnspan=2, ipady=10)
        self.chat_input.bind("<Return>", self.handle_chat_input)

        self.chat_display = tk.Text(self, height=10, wrap="word", font=("Helvetica", 16))
        self.chat_display.grid(row=4, column=0, pady=10, padx=10, sticky="nsew", columnspan=2)
        self.chat_display.config(state=tk.DISABLED)

        self.grid_rowconfigure(4, weight=1)

    def handle_chat_input(self, event):
        user_input = self.chat_input.get()
        self.chat_input.delete(0, tk.END)
        response = self.generate_response(user_input)
        self.display_response(response)

    def generate_response(self, user_input):
        query = user_input.strip().lower()
        response = ""
        
        def get_column_data(column_name):
            try:
                return ", ".join(self.data[column_name].dropna().unique().astype(str).tolist()) + "\n"
            except KeyError:
                return "챗봇: '{}' 열을 찾을 수 없습니다.\n".format(column_name)

        if "과목명" in query:
            if "전공" in query:
                response += "아냥봇: 교양 과목 목록입니다.\n"
                response += get_column_data("과목명")
            else:
                response += "아냥봇: 이번 학기 개설되는 과목 목록입니다.\n"
                response += get_column_data("과목명")

        elif "분반" in query:
            response += "아냥봇: 분반 목록입니다.\n"
            response += get_column_data("분반")

        elif "이수구분" in query:
            response += "아냥봇: 이수구분 목록입니다.\n"
            response += get_column_data("이수구분")
        
        elif "교양필수" in query:
            response += "아냥봇: 교양필수 과목 목록입니다.\n"
            try:
                filtered_data = self.data[self.data["이수구분"].str.contains("교양필수", na=False)]
                response += ", ".join(filtered_data["과목명"].dropna().unique().astype(str).tolist()) + "\n"
            except KeyError:
                response += "챗봇: '이수구분' 열을 찾을 수 없습니다.\n"
        
        elif "교양선택" in query:
            response += "아냥봇: 교양선택 과목 목록입니다.\n"
            try:
                filtered_data = self.data[self.data["이수구분"].str.contains("교양선택", na=False)]
                response += ", ".join(filtered_data["과목명"].dropna().unique().astype(str).tolist()) + "\n"
            except KeyError:
                response += "챗봇: '이수구분' 열을 찾을 수 없습니다.\n"

        elif "과목구분" in query:
            response += "아냥봇: 과목구분 목록입니다.\n"
            response += get_column_data("과목구분")

        elif "대표교수" in query or "교수" in query or "교수님" in query:
            response += "아냥봇: 각 과목의 대표교수 목록입니다.\n"
            response += get_column_data("대표교수")

        elif "온라인 강의" in query:
            response += "아냥봇: 온라인 강의 비율은 {}%입니다.\n".format(get_column_data("온라인강의비율"))
        
        elif "학점" in query:
            response += "아냥봇: 각 과목의 학점 목록입니다.\n"
            response += ", ".join(map(str, self.data["학점"].tolist())) + "\n"

        elif "상대평가" in query:
            response += "아냥봇: 상대평가가 적용되는 과목 목록입니다.\n"
            response += get_column_data("상대평가유형")

        elif "패스 과목" in query:
            response += "아냥봇: 패스 과목 목록입니다.\n"
            try:
                pass_courses = self.data[self.data["패스과목여부"] == 1][["과목명", "분반"]]
                if not pass_courses.empty:
                    for course_name, class_section in zip(pass_courses["과목명"], pass_courses["분반"]):
                        response += f"과목명: {course_name}, 분반: {class_section}\n"
                else:
                    response += "패스 과목이 없습니다.\n"
            except KeyError:
                response += "챗봇: '패스과목여부' 열을 찾을 수 없습니다.\n"

        elif "시간표" in query:
            response += "아냥봇: 시간표 목록입니다.\n"
            response += get_column_data("시간표")
        
        elif query.startswith("A:"):
            input_subject = query.split(":", 1)[1].strip()
            try:
                filtered_data = self.data[self.data["과목명"].str.contains(input_subject, na=False)]
                if not filtered_data.empty:
                    for i, row in filtered_data.iterrows():
                        response += f"과목명: {row['과목명']}\n이수구분: {row['이수구분']}\n대표교수: {row['대표교수']}\n역량: {row.get('역량', 'N/A')}\n시간표: {row['시간표']}\n"
                else:
                    response += "해당 과목을 찾을 수 없습니다.\n"
            except KeyError:
                response += "챗봇: '과목명' 열을 찾을 수 없습니다.\n"

        else:
            response += "아냥봇: 죄송합니다. 요청하신 정보를 찾을 수 없습니다.\n"

        return response

    def display_response(self, response):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, response + "\n")
        self.chat_display.config(state=tk.DISABLED)