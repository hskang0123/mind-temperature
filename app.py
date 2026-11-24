
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="마음온도",
    page_icon="🌱",
    layout="wide"
)

# 제목
st.title("🌱 마음온도")
st.subheader("나의 마음을 살펴보는 시간")
st.write("최근 2주 동안의 마음 상태를 생각하며 답변해주세요.")

st.info(
    "이 검사는 우울감 자가점검을 위한 참고 도구이며, "
    "의학적 진단을 대신하지 않습니다."
)

# 1. 리스트를 이용해 질문 저장
questions = [
    "1. 평소 즐겁게 느끼던 일들이 더 이상 즐겁지 않거나 흥미가 줄어들었나요?",
    "2. 특별한 이유 없이 우울하거나 공허하고 슬픈 기분이 자주 들었나요?",
    "3. 잠들기 어렵거나 자주 깨거나 평소보다 지나치게 많이 잤나요?",
    "4. 충분히 쉬었는데도 피곤하고 무기력한 느낌이 자주 들었나요?",
    "5. 식욕이 줄거나 반대로 평소보다 많이 먹는 변화가 있었나요?",
    "6. 자신이 쓸모없거나 부족한 사람이라고 느끼고 스스로를 자주 탓했나요?",
    "7. 평소보다 집중력이 떨어지고 일상적인 결정을 내리기 어려웠나요?",
    "8. 사라지고 싶다는 생각이나 자신을 해치고 싶다는 생각이 들었나요?"
]

choices = [
    "1. 매우 그렇다",
    "2. 그렇다",
    "3. 보통이다",
    "4. 아니다",
    "5. 매우 아니다"
]

# 2. 함수를 이용해 점수 계산
def calculate_score(answer):
    score = {
        choices[0]: 4,
        choices[1]: 3,
        choices[2]: 2,
        choices[3]: 1,
        choices[4]: 0
    }
    return score[answer]


# 3. 조건문을 이용해 결과 구분
def get_result(total):
    if total <= 7:
        return (
            "건강",
            "현재 우울 관련 증상이 비교적 적게 나타납니다. "
            "지금처럼 자신의 마음을 잘 돌봐주세요."
        )

    elif total <= 15:
        return (
            "주의",
            "우울감이나 무기력감이 반복되고 있을 수 있습니다. "
            "충분한 휴식과 주변 사람의 도움을 받아보세요. "
            "상태가 지속된다면 전문가와 상담해보세요."
        )

    else:
        return (
            "위험",
            "우울 관련 어려움이 상당할 수 있습니다. "
            "혼자 감당하려 하지 말고 정신건강 전문가나 "
            "병원에서 정확한 평가를 받아보길 권유합니다."
        )


# 4. 반복문으로 질문 출력 및 답변 받기
with st.form("depression_test"):

    answers = []

    for question in questions:
        answer = st.radio(
            question,
            choices,
            key=question,
            horizontal=True
        )
        answers.append(answer)

    submitted = st.form_submit_button(
        "나의 마음 상태 확인하기"
    )


# 결과 출력
if submitted:

    total_score = 0

    for answer in answers:
        total_score += calculate_score(answer)

    level, comment = get_result(total_score)

    # 8번 질문은 별도의 안전 확인
    safety_concern = answers[7] in choices[:3]

    st.divider()
    st.header("🌼 검사 결과")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="나의 마음 점수",
            value=f"{total_score}점 / 32점"
        )

        st.progress(total_score / 32)

        if safety_concern:
            st.error("안전 확인이 필요합니다.")

            st.write(
                "자신을 해치고 싶거나 사라지고 싶다는 "
                "생각이 있었다면 총점과 관계없이 "
                "전문가에게 도움을 요청해주세요."
            )

        st.subheader(f"현재 상태: {level}")
        st.write(comment)

    with col2:
        st.subheader("💚 당신에게 전하는 응원")

        if level == "건강":
            st.success(
                "오늘도 당신의 마음을 돌보는 시간을 가져보세요. "
                "당신의 작은 행복도 소중합니다."
            )

        elif level == "주의":
            st.warning(
                "힘든 마음을 억지로 참지 않아도 괜찮아요. "
                "당신의 감정은 충분히 존중받을 가치가 있습니다."
            )

        else:
            st.error(
                "넌 혼자가 아니야. 지금 힘든 시간을 보내고 "
                "있더라도 도움을 받을 수 있어. "
                "당신은 소중한 사람입니다."
            )

    # 상담기관 안내
    st.divider()
    st.header("📞 도움이 필요할 때")

    st.write("정신건강 상담전화: **1577-0199** (24시간)")
    st.write("자살예방 상담전화: **109** (24시간)")

    st.caption(
        "자신을 해칠 위험이 임박했다면 혼자 있지 말고 "
        "가까운 사람에게 알린 뒤 119 또는 112에 연락하거나 "
        "가까운 응급실로 가세요."
    )

    st.markdown(
        "[정신건강복지센터 및 상담 정보 확인하기](https://www.129.go.kr/109)"
    )

    st.divider()
    st.caption(
        "본 결과는 자체 제작한 자가점검 결과이며 "
        "전문의의 진단을 대체하지 않습니다."
    )
