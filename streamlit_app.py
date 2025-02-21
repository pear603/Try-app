import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'  # Start on the home page

# Function to navigate to home
def go_home():
    st.session_state.page = 'home'

# Home Page
if st.session_state.page == 'home':
    st.title("Home Page")
    st.write("Welcome to the main app!")

    # Button to navigate to Page 1
    if st.button("Go to Page 1"):
        st.session_state.page = 'page1'
        st.rerun()  # Refresh the app

    # Button to navigate to Page 2
    if st.button("Go to Page 2"):
        st.session_state.page = 'page2'
        st.rerun()  # Refresh the app

# Page 1
elif st.session_state.page == 'page1':
    st.title("Page 1")
    
    # Use st.components.v1.html to render the iframe
    st.components.v1.html(
        """
        <iframe
            src="https://30days.streamlit.app?embed=true"
            style="height: 450px; width: 100%;"
            frameborder="0">
        </iframe>
        """,
        height=450,
        width=700,
    )

    # Button to go back to Home
    if st.button("Back to Home"):
        go_home()

# Page 2
elif st.session_state.page == 'page2':
    st.title("Page 2")
    data2 = st.text_input("Enter data for Page 2:")
    
    if st.button("Submit"):
        st.session_state.data2 = data2
        st.success("Data submitted!")
    
    # Button to go back to Home
    if st.button("Back to Home"):
        go_home()

# Display saved data in sidebar
if 'data1' in st.session_state:
    st.sidebar.write("Data from Page 1:", st.session_state.data1)
if 'data2' in st.session_state:
    st.sidebar.write("Data from Page 2:", st.session_state.data2)
