import streamlit as st
import match_algo
import pandas as pd

def display_match_UI():
  st.write("Load data from DB to dataframe:")
  if st.button("Prep data"):
    st.write("Preparing data...")
    st.session_state.data, st.session_state.email_ids, \
      st.session_state.fdf, st.session_state.idx_dict = match_algo.prep_data()
    st.write("Done!")
  if st.button("Assign scores"):
    st.write("Assigning scores...")
    st.session_state.scores_df = match_algo.score_buddies(
        st.session_state.fdf, st.session_state.data, st.session_state.idx_dict
      )
    st.write("Done!")
  if st.button("Match buddies"):
    st.write("Matching buddies...")
    st.session_state.matched_df = match_algo.match_buddies(
      st.session_state.data, st.session_state.scores_df, st.session_state.email_ids, 
      st.session_state.idx_dict
    )
    st.write("Done!")
  if st.button("Save matches to DB"):
    st.write("Saving matches to DB...")
    match_algo.save_matches_db(st.session_state.matched_df)
    st.write("Done!")
  if st.button("Analyze matches"):
    st.write("Analyzing matches...")
    match_algo.analyze_matches()
    st.write("Done!")
  if st.button("Send emails"):
    match_algo.email_notifications()
    st.write("Done!")
