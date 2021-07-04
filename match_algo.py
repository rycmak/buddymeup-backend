import prep as p
import score as s
import match as m
import analyze_evaluate as ae
import streamlit as st
import pandas as pd


def prep_data():
  data, email_ids, fdf, idx_dict = p.prep_data()
  return data, email_ids, fdf, idx_dict

def score_buddies(fdf, data, idx_dict):
  scores_df = s.scoring_alg(fdf, data, idx_dict)
  return scores_df

def match_buddies(data, scores_df, email_ids, idx_dict):
  matched_df = m.pair_participants(data, scores_df, email_ids, idx_dict)
  return matched_df

def analyze_matches(matched_df):
  ae.evaluate_matches(matched_df)
  #st.write("Saving matches to db or .csv...")
  #m.save_matches(df_matched)

def save_matches_db(matched_df):
  m.save_matches(matched_df)

def show_matches():
  st.write("Show matches...")

def email_notifications():
  st.write("create and save .csv for email sending")
  m.csv_announcement_email(df_matched)
