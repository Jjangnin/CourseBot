import pandas as pd

# 파일 경로
file1 = '전공2학기_12.xlsx'
file2 = '전공2학기_34.xlsx'

# 각 파일의 데이터를 읽어오기
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# 두 데이터프레임을 합치기
combined_df = pd.concat([df1, df2])

# 합친 데이터를 새로운 엑셀 파일로 저장하기
combined_df.to_excel('전공2학기.xlsx', index=False)

print("두 파일이 성공적으로 합쳐졌습니다.")
