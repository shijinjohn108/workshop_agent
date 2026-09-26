import streamlit as st


def calc(expression):
    return eval(expression, {"__builtins__": {}}, {})


def agent(goal):
    if "calc" in goal.lower():
        expression = goal.replace("calc", "", 1).strip()
        return calc(expression)
    raise ValueError("Please enter a calculation starting with 'calc'.")


st.title("Calculator Agent")
st.write("Enter a math expression with the word 'calc' to evaluate it.")

user_input = st.text_input("Goal", "calc 10 + 5")

if st.button("Calculate"):
    try:
        result = agent(user_input)
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(str(e))

st.caption("Examples: calc 10 + 5, calc 12 * 8 - 6, calc (15 + 5) * 3")
              