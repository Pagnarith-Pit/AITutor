import streamlit as st

def main():
    st.title("Simple Streamlit Server Test")
    st.write("This is a simple app to test server functionality.")

    # Text input form
    user_input = st.text_input("Enter some text:")
    
    if st.button("Submit"):
        st.write("You entered:", user_input)

if __name__ == "__main__":
    main()