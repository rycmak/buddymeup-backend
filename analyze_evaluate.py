"""
functions to analyze the dataset and evaluate the matched buddies
"""
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import pandas as pd
dt_today = str(dt.datetime.today().strftime("%m_%d_%Y"))


def evaluate_matches(df_matched):
    # plot_score_hist
    scores = pd.concat([df_matched['score_u1'], df_matched['score_u2']], ignore_index=True)
    sns.displot(scores, bins=len(scores), color='red', kde=False)
    plt.title('Scoring distribution', fontsize=18)
    plt.ylabel('Frequency', fontsize=16)
    # scores
    avg_sc = scores.sum() / (2 *len(df_matched))
    min_sc = scores.min()
    max_sc = scores.max()
    st.write("\nthe average score is: ", avg_sc)
    st.write("\nthe minimum score is: ", min_sc)
    st.write("\nthe maximum score is: ", max_sc)
    low_scored = df_matched.loc[((df_matched["score_u1"] < 0.70) | (df_matched["score_u2"] < 0.70))]
    st.write("manually check low scored matches:", low_scored[["email_1", "email_2"]])


# def get_buddies(name1, df_matched):
#     name2 = df_matched.loc[df_matched["person_a"].str.contains(name1), "person_b"].iloc[0]
#     name1 = df_matched.loc[df_matched["person_a"].str.contains(name2), "person_b"].iloc[0]
#
#     buddy_match_df = data.loc[data.name.isin([name1, name2])]
#     return buddy_match_df