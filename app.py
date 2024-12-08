import streamlit as st

def run_gad7_test():
    st.title('불안장애 자가진단 테스트 (GAD-7)')
    st.write('지난 2주간 다음과 같은 문제들로 인해서 얼마나 자주 방해를 받았습니까?')
    
    questions = [
        "초조하거나 불안하거나 조마조마하게 느낀다",
        "걱정하는 것을 멈추거나 조절할 수 없다",
        "여러가지 것들에 대해 너무 많이 걱정한다",
        "편하게 있기가 어렵다",
        "너무 안절부절못해서 가만히 있기가 힘들다",
        "쉽게 짜증나거나 쉽게 성이 난다",
        "마치 끔찍한 일이 일어날 것처럼 두렵게 느껴진다"
    ]
    
    options = {
        "전혀 없음": 0,
        "며칠 동안": 1,
        "일주일 이상": 2,
        "거의 매일": 3
    }
    
    scores = []
    
    st.write('---')
    
    for i, question in enumerate(questions, 1):
        st.subheader(f'{i}. {question}')
        answer = st.radio(
            "빈도를 선택하세요:",
            options.keys(),
            key=f"q{i}"
        )
        scores.append(options[answer])
        st.write('---')
    
    if st.button('결과 확인하기'):
        total_score = sum(scores)
        st.subheader('검사 결과')
        st.write(f'총점: {total_score}점')
        
        if total_score <= 4:
            st.success('정상 범위입니다.')
        elif total_score <= 9:
            st.info('가벼운 불안감이 있습니다.')
        elif total_score <= 14:
            st.warning('중등도의 불안장애가 의심됩니다. 전문가와 상담을 고려해보세요.')
        else:
            st.error('심한 불안장애가 의심됩니다. 전문가의 도움을 받아보시길 권장합니다.')
        
        st.write('---')
        st.write('주의: 이 테스트는 참고용이며, 정확한 진단을 위해서는 반드시 전문가와 상담하시기 바랍니다.')
        
        if total_score >= 10:
            st.write('''
            ### 도움받을 수 있는 곳
            - 정신건강상담전화: (02) 2204-0114
            - 가까운 정신건강복지센터 찾기: [링크](https://www.mentalhealth.go.kr/portal/health/fac/PotalHealthFacListTab2.do)
            - 좀더 많은 정보를 알고 싶다면: [링크](https://lzhakko.tistory.com/)
            ''')

if __name__ == '__main__':
    run_gad7_test()
