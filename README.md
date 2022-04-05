# Election_Analysis

# Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on the popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that
 - There were 'x' votes cast in the election.
 - The candidates were:
 -    1. Charles Casper Stockham
 -    2. Diana Degette
 -    3. Raymon Anthony Doane
 - The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana Degette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
 - The winner of the election was:
    - Diana Degette who received 272,892 votes for 73.8% of the vote.
 
## Challenge Overview
 - The purpose of this election overview was to reaffirm the results by going through the data. Using Python in a CSV file to iterate through all of the ballots was a far more effecient way of tabulating the votes. Seeing as there were 369,711 votes to check using Python was the only realistic solution. In a real setting it would be far more effecient to write lines of code to get the results rather than multiple people spending countless hours going through it by hand.
 - The county vote totals ranked by total votes were as follows:
 1. Denver - 306,055 votes that made up 82.8%
 2. Jefferson - 38,855 votes that made up 10.5%.
 3. Arapahoe - 24,801 votes that made up 6.7%.
## Challenge Summary
In summary, this script can be used for any state looking to go through their voter rows quickly. As long as the data is organized by county there can be a breakdown by county and candidate as to how the voting broke down quickly.
If you were a candidate looking to see where to mount a challenge to a sitting representative this script could be useful. By modifying it ever so slightly you can see where your opponent's strong and weak counties are by breaking down their votes by counties. This script could also be modified to be used by an election commission to quickly tabulate votes as data comes in the night of the election. You'd be able to continue running the script and give out updates via the terminal results.
