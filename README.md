# Election Analysis

## Overview of Election Audit

A Colorato Board of Elections employee has given me some tasks to complete an election audit of a recent local congressional election. The tasks are as follows:

1. Calculate the total number of votes cast in the election.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Calculate the voter turnout for each county.
7. Calculate the percentage of votes each county received out of the total number of votes.
8. Determine the county with the highest turnout.

### Purpose

This project analyzes election data to complete an election audit which outputs results for the above tasks. This analysis will help the Colorado Board of Elections to gain the information they want from the election data.

## Election-Audit Results

The results and analysis of the election audit is as follows:

1. There were 369,711 total votes cast in this election.

2. There were three counties involved in this election. The voter turnout per county is listed below:
  * Jefferson: 10.5% (38,855)
  * Denver: 82.8% (306,055)
  * Arapahoe: 6.7% (24,801)
The code used to generate the results are displayed here:

![Calculating_percentage_votes_county](https://github.com/Zarif601/Election_Analysis/blob/main/Resources/Calculating_percentage_votes_county.png)

3. Denver was the county with the largest voter turnout.

4. There were three candidates in the election. Their total number of votes and vote percentages is stated below:
  * Charles Casper Stockham: 23.0% (85,213)
  * Diana DeGette: 73.8% (272,892)
  * Raymon Anthony Doane: 3.1% (11,606)
The code that generated the above results are displayed as follows:

![Calculating_winning_candiate_and_percentage_votes](https://github.com/Zarif601/Election_Analysis/blob/main/Resources/Calculating_winning_candiate_and_percentage_votes.png)

5. The election was won by candidate Diana DeGette. She won with a vote percentage of 73.8% and a total vote count of 272,892.
The following code generated the winner:

![Determining_winner](https://github.com/Zarif601/Election_Analysis/blob/main/Resources/Determining_winner.png)

Here is a glance of the results of the election-audit:

![Election_Results](https://github.com/Zarif601/Election_Analysis/blob/main/Resources/Election_Results.png)

## Election-Audit Summary

With some modifications to the code, the script can be used by the election commission to analyze any election data. A few modifications are suggested below that can help in doing so:

1. For different elections, the rows may be in different order. Instead of hard coding the values of candidate_name and county_name, we can find a way to make sure the column of values we are looking at contains the correct data for the variable we are assigning it to, programatically. A way do this could be by using if-statements and putting conditions using the header row to identify the column we want to select.

2. We can also use the script to analyze multiple election data simultaneously. To do so, we can convert our total_votes variable to a dictionary. The dictionary can hold key, value pairs with keys being the name or information of the election and the values being the total votes cast in that election. This way, if we work with data from multiple elections, we can keep track of the total votes cast in all of them in one place and easily access them when needed.
