<h1 align="center">Election Analysis</h1>

## Overview of Election Audit
The purpose of this project is to summarize the number of votes by county and by candidate, as well as to identify the county with the largest number of votes and the winning candidate.

## Election Audit Results

* There are  369,711 votes that were cast in this congressional election. 
* There are three counties in this election. They are Jefferson with 38,855 votes (10.51%), Denver with 306,055 votes (82.78%), and Arapahoe with 24,801 votes (6.71%).
* Denver Had the largest number of votes.
* There are three candidates in the election. They are Charles Casper Stockham with 85,213 votes (23.0%), Diana DeGette with 272,892 votes (73.8%), and Raymon Anthony Doane with 11,606 votes (3.1%).
* Diana DeGette won the election.  She got 272,892 votes, which was 73.8% of the total votes. 

The screenshot below shows the above results as how they printed in the terminal. 
![](https://github.com/lu-chang-axonic/Election_Analysis/blob/main/Results%20Printed%20to%20the%20Terminal.PNG)

## Election Audit Summary
This script can be repurposed for other election analysis. Two examples:
1. For election audit summarize other parameters such as gender, race, or education, etc, the code below can be modified to navigate to the desired parameter (be it a string or a numerical value) to conduct similar summary of results.

    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]
        
2. For other analysis, such as finding what % of each candidate's votes was from each county, the code below can be modified by replacing the total number of votes in the denominator to the number of votes in each county.

    
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n\n")



