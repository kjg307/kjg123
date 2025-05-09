import streamlit as st

st.title("🎈 선준이의 첫번째 생일")
st.info('선준이의 행복한 생일파티')
st.write("모두 선준이를 축하해주세요.")

# st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

with tab1:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfFtatUZg2gKrMUEuHrQRYLhXQrgR0xZ7Ebg&s")
    st.info('보람그룹 지원')  # 첫 번째 탭에 표시할 내용
with tab2:
    st.image('https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzJtOGt4Z3NrcGE3MzVhNmQ3YzkwaW8xMzM4bzdlMWtvNm1mMWdhZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/osjgQPWRx3cac/giphy.gif')
  # 두 번째 탭에 표시할 내용

name = st.text_area("이름을 입력해주세요")
st.error(name+"님 보람찬 하루입니다!")

# 여러 옵션 중 하나 선택
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
st.write("선택한 성별:", gender)

if gender == '남성':
    st.image('https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYThsMWk1aW84aHZuZDQzMWJhaHg2YTMycjRpZjZlM2V6d3FzaXpmbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/EC6AQrFYSrhkhonESV/giphy.gif')

