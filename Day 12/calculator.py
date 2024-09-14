import streamlit as st

def calculator(num1, num2, operation):
    if operation == "Addition":
        result = num1 + num2
        return result
    elif operation == "Subtraction":
        result = num1 - num2
        return result
    elif operation == "Multiplication":
        result = num1 * num2
        return result
    elif operation == "Division":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = "Cannot divide by zero"
        return result

def main():
    st.title("Calculator")
    # get user input for the first number
    num1 = st.number_input("Enter first number", step=1)

    num2 = st.number_input("Enter second number", step=1)

    # radio button
    operator = st.radio("Choose the operator", ["Addition", "Subtraction", "Multiplication", "Division"])

    result = calculator(num1, num2, operator)

    st.write(f"The {operator} of {num1} and {num2} is {result}")


if __name__ == '__main__':
    main()

# lms.digitalschool.tech
