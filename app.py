import streamlit as st

def ln(a, b, c):
    return max(a, b, c)

def main():
    st.title("T-Max: Find the Greatest Number")
    st.write("Enter three numbers")
    num1 = st.number_input("Enter first number", value=0)
    num2 = st.number_input("Enter second number", value=0)
    num3 = st.number_input("Enter third number", value=0)
    
    if st.button("Find Greatest"):
        largest = ln(num1, num2, num3)
        st.write(f"The greatest number is: {largest}")

if __name__ == "__main__":
    main()
