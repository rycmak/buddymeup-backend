import streamlit as st
from match_UI import display_match_UI
import pandas as pd

st.set_page_config(page_title="BuddyMeUp Backend", page_icon="assets/images/icon_buddymeup.png")

def main():
    display_match_UI()

if __name__ == "__main__":
    main()
