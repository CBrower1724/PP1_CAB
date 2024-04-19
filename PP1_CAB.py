# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:39:15 2024

@author: Browe
"""
import streamlit as st

def calculate_era(earned_runs, innings_pitched):
    if innings_pitched == 0:
        return float('inf')
    return round((earned_runs * 9) / innings_pitched, 3)

def calculate_batting_avg(hits_allowed, at_bats):
    if at_bats == 0:
        return float('inf')
    return round(hits_allowed / at_bats, 3)

def calculate_whip(hits_allowed, walks_allowed, innings_pitched):
    if innings_pitched == 0:
        return float('inf')
    return round((hits_allowed + walks_allowed) / innings_pitched, 3)

def main():
    st.title("Pitching Statistics")

    add_pitcher = True
    pitcher_count = 0
    pitchers = []

    while add_pitcher:
        pitcher_count += 1
        pitcher = {}
        pitcher["name"] = st.text_input(f"Name (Pitcher {pitcher_count})")
        pitcher["er"] = st.number_input(f"Earned Runs (Pitcher {pitcher_count})", value=0)
        pitcher["ip"] = st.number_input(f"Innings Pitched (Pitcher {pitcher_count})", value=0.0)
        pitcher["ha"] = st.number_input(f"Hits Allowed (Pitcher {pitcher_count})", value=0)
        pitcher["bba"] = st.number_input(f"Walks Allowed (Pitcher {pitcher_count})", value=0)
        pitcher["ab"] = st.number_input(f"At Bats Against (Pitcher {pitcher_count})", value=0)
        pitchers.append(pitcher)

        add_pitcher = st.checkbox(f"Add Another Pitcher {pitcher_count}", key=f"add_pitcher_{pitcher_count}")

    for idx, pitcher in enumerate(pitchers):
        st.write(f"{pitcher['name']} ERA:", calculate_era(pitcher["er"], pitcher["ip"]))
        st.write(f"{pitcher['name']} Batting Average Against:", calculate_batting_avg(pitcher["ha"], pitcher["ab"]))
        st.write(f"{pitcher['name']} WHIP:", calculate_whip(pitcher["ha"], pitcher["bba"], pitcher["ip"]))

if __name__ == "__main__":
    main()





