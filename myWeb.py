import streamlit as st

st.title("다항식의 +, -, * 연산")
st.text("첫번째 다항식입니다. a1x^2+b1x+c1")
a1 = st.number_input('a1 : ')
b1 = st.number_input('b1 : ')
c1 = st.number_input('c1 : ')

st.text("두번째 다항식입니다. a2x^2+b2x+c2")
a2 = st.number_input('a2 : ')
b2 = st.number_input('b2 : ')
c2 = st.number_input('c2 : ')

operator_list = ["+", "-", "*"]
operator_ = st.selectbox("어떤 연산을 실행하나요?", operator_list)
if operator_=="+"or operator_=="-" or operator_=="*":
    repeatCheck = False
    if operator_=="+":
        a3 = a1 + a2
        b3 = b1 + b2
        c3 = c1 + c2
        if b3 > 0:
            b3 = "+"+str(b3)
        if c3 > 0:
            c3 = "+"+str(c3)
        st.text(f"{a3}x^2{b3}x{c3}")
    elif operator_=="-":
        a3 = a1 - a2
        b3 = b1 - b2
        c3 = c1 - c2
        if b3 > 0:
            b3 = "+"+str(b3)
        if c3 > 0:
            c3 = "+"+str(c3)
        st.text(f"{a3}x^2{b3}x{c3}")
    elif operator_=="*":
        a3 = a1*a2
        b3 = a1*b2 + a2*b1
        c3 = a1*c2 + a2*c1 + b1*b2
        d3 = b1*c2 + b2*c1
        e3 = c1*c2
        if b3 > 0:
            b3 = "+"+str(b3)
        if c3 > 0:
            c3 = "+"+str(c3)
        if d3 > 0:
            d3 = "+"+str(d3)
        if e3 > 0:
            e3 = "+"+str(e3)
        st.text(f"{a3}x^4{b3}x^3{c3}x2{d3}x{e3}")


