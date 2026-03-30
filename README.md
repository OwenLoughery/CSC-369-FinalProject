# This Project

## Question:

Is there a difference in review dip periods (spike in negative reviews for a game) versus normal review periods for video games?

## Hypothesis:

Most times when games experience a huge inflow of negative reviews at once it is a direct response to something the developer implemented like a poor update, monetization, or something else that makes the players unhappy. So I would theorize that these negative review periods that happen are made up of the more commited community of the game vs. normal reviews games get I think would be new player sentiment. So looking into seeing if there is a difference in these types of review periods can help developers make game changes to fix problems with new players issues and also those of the more commited community.

## Data

I found the data I am using at https://www.kaggle.com/datasets/kieranpoc/steam-reviews

The dataset used for my analysis is a large scale Steam Reviews dataset (~40GB in original CSV format), containing over 100 million user reviews. The dataset includes important variables such as review timestamps, recommendation status (positive or negative), playtime metrics, weighted voting score (helpfulness score that is steam generated), and engagement indicators (votes and comments).

## What’s in this repo

1) Preprocessing (Large Dataset → Analysis-Ready)
Script to clean and restructure the raw Steam reviews dataset so it’s usable for analysis (filtering, parsing timestamps, and creating the datasets used in the analysis).

First did very basic preprocessing to do EDA then the final preprocessing script was completed after doing EDA of the dataset.

File: `preprocess.py`

2) Exploratory Data Analysis (EDA)
Initial exploration of review behavior over time, including identifying “review dip” periods (spikes in negative reviews) and comparing them to normal review periods. All work that led to my final conclusions in my report can be found here plus other areas I explored relating to my project question.

Files: `EDA.ipynb` / `EDA.md`

3) Final Report (Review Dip vs Normal Period Comparison)
Main writeup and results comparing negative-review spike periods to baseline review behavior, with plots + conclusions tied to the project question.

Files: `Report.ipynb` / `Report.md`
