import streamlit as st
from infrance import translation
st.set_page_config(page_title="Senior Project", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

st.markdown(
    """
    <style>
    .reportview-container{
        background-color: #4CAF54;  /* Custom background color */
        color: #333;  /* Custom text color */
    }
    .stButton > button {
        background-color: #4CAF50;  /* Custom button color */
        color: white;  /* Button text color */
    }
    </style>
    """,
    unsafe_allow_html=True
)


if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

if 'output' not in st.session_state:
    st.session_state.output = ""  # Initialize output as an empty string

# Define functions for page navigation
def go_to_home():
    st.session_state.current_page = 'home'

def go_to_translate():
    st.session_state.current_page = 'translate'

def go_to_history():
    st.session_state.current_page = 'history'





# Page 1: Home
if st.session_state.current_page == 'home':
    for i in range(15):
        st.write("")
    st.markdown("<h1 style='text-align: center;'>  Home Page</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>  Translate on the go</h1>", unsafe_allow_html=True)

    for i in range(10):
        st.write("")

    button_columns = st.columns([1.9, 2, 1], vertical_alignment="center")
    button_columns[1].button("Start translating", on_click=go_to_translate)




# Page 2: translate
elif st.session_state.current_page == 'translate':
 

    st.header("Saudi dilect translation")

    if 'label1' not in st.session_state:
        st.session_state.label1 = 'Dilect'
        st.session_state.label2 = 'MSA'
        
    
    
    left, right = st.columns((4, 1), vertical_alignment="center")

    swap_button = right.button(label="Swap",use_container_width=True)


    with left:
        left_text = st.text_input(label=st.session_state.label1)
        # right_text = st.text_input(label=st.session_state.label2 )


    if swap_button:
        # left_text, right_text = right_text, left_text
        st.session_state.label1, st.session_state.label2 = st.session_state.label2, st.session_state.label1



    def click():
          # Use the output variable from the outer scope
        st.session_state.output = translation(left_text)

    st.button("Translate", on_click=click)
    
        
    # Show the translation only after the button is clicked
    if st.session_state.output:
        st.markdown(f"<h3 style='text-align: center;'> الترجمة: \n {st.session_state.output}</h3>", unsafe_allow_html=True)
        
        
    for i in range(50):
        st.write("")



    footer_container = st.container(border = True)


    with footer_container:
        
        left, right = footer_container.columns([7, 1], vertical_alignment="center")
        left.button("Return to home page ", on_click=go_to_home)
        right.button("History ", on_click=go_to_history)
            
            
            
            
            
# Page 3: History
if st.session_state.current_page == 'history':
    st.title("History")
    
    for i in range(50):
        st.write("")
    footer_container = st.container(border = True)


    with footer_container:
        
        left, right = footer_container.columns([5, 1], vertical_alignment="center")
        left.button("Return to home page ", on_click=go_to_home)
        right.button("Translation ", on_click=go_to_translate)
