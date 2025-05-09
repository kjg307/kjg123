# import streamlit as st

# st.title("🎈 선준이의 첫번째 생일")
# st.info('선준이의 행복한 생일파티')
# st.write("모두 선준이를 축하해주세요.")

# # st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
# tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

# with tab1:
#     st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfFtatUZg2gKrMUEuHrQRYLhXQrgR0xZ7Ebg&s")
#     st.info('보람그룹 지원')  # 첫 번째 탭에 표시할 내용
# with tab2:
#     st.image('https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzJtOGt4Z3NrcGE3MzVhNmQ3YzkwaW8xMzM4bzdlMWtvNm1mMWdhZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/osjgQPWRx3cac/giphy.gif')
#   # 두 번째 탭에 표시할 내용

# name = st.text_area("이름을 입력해주세요")
# st.error(name+"님 보람찬 하루입니다!")

# # 여러 옵션 중 하나 선택
# gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
# st.write("선택한 성별:", gender)

# if gender == '남성':
#     st.image('https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYThsMWk1aW84aHZuZDQzMWJhaHg2YTMycjRpZjZlM2V6d3FzaXpmbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/EC6AQrFYSrhkhonESV/giphy.gif')


# import openai

# user_api_key = st.text_input("키를 입력해주세요.")

# if user_api_key:
        
#     from openai import OpenAI

#     client = OpenAI(api_key = user_api_key)
#     prompt = st.text_input("프롬프트를 입력해주세요.")

#     completion = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     st.markdown("### 💡 GPT의 답변:")
#     st.write(completion.choices[0].message.content)

import streamlit as st
import openai

# 페이지 기본 설정
st.set_page_config(page_title="🎂 선준이의 첫번째 생일", page_icon="🎈", layout="centered")

# 타이틀 및 소개 문구
st.title("🎈 선준이의 첫번째 생일")
st.markdown("""
<div style='text-align: center; font-size: 20px;'>
    👶🏻 사랑스러운 선준이의 생일을 모두 함께 축하해주세요!<br>
    🎉 소중한 메시지도 남겨주시고, 파티를 즐겨보세요.
</div>
""", unsafe_allow_html=True)

st.info('선준이의 행복한 생일파티에 오신 걸 환영합니다!')

# 탭 구성
tab1, tab2 = st.tabs(["🎁 보람그룹 축하", "🎊 선물 애니메이션"])

with tab1:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfFtatUZg2gKrMUEuHrQRYLhXQrgR0xZ7Ebg&s", use_column_width=True)
    st.success('🎉 보람그룹의 따뜻한 지원이 도착했어요!')

with tab2:
    st.image('https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzJtOGt4Z3NrcGE3MzVhNmQ3YzkwaW8xMzM4bzdlMWtvNm1mMWdhZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/osjgQPWRx3cac/giphy.gif', use_column_width=True)

# 이름 입력
st.markdown("## ✍️ 이름을 남겨주세요")
name = st.text_input("여기에 이름을 입력해주세요:")

if name:
    st.error(f"🎉 {name}님, 오늘도 보람찬 하루 보내세요!")

# 성별 선택
st.markdown("## 🚻 성별을 선택해주세요")
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
st.write("👉 선택한 성별:", gender)

if gender == '남성':
    st.image('https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYThsMWk1aW84aHZuZDQzMWJhaHg2YTMycjRpZjZlM2V6d3FzaXpmbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/EC6AQrFYSrhkhonESV/giphy.gif')

# GPT 프롬프트 입력 및 출력
st.markdown("## 🤖 GPT에게 축하 메시지 만들기")

user_api_key = st.secrets["openai"]["api_key"]
if user_api_key:
    prompt = st.text_input("💬 GPT에게 어떤 메시지를 만들지 말해주세요:")
    
    if prompt:
        from openai import OpenAI
        client = OpenAI(api_key=user_api_key)
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        st.markdown("### 💡 GPT의 답변:")
        st.success(completion.choices[0].message.content)
