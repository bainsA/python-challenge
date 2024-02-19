import csv
voterid = []
county = []
candidate = []
# I created three list for each of the column heads
# First step is to open the csv file called Election
with open('C:/Users/Karamjit/Documents/Election.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")

    for row in csvreader:
        # print(row)
        voterid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
# print(voterid)
# print(county)
# print(candidate)

totalvotes = len(voterid)
charles_num_of_votes = candidate.count("Charles Casper Stockham")
diana_num_of_votes = candidate.count("Diana DeGette")
raymon_num_of_votes = candidate.count("Raymon Anthony Doane")
# Total votes calculated through len() function
# The votes received by each candidate is computed using the .count tool with the parameter being the candidate's name represented as a String

charles_percent = (charles_num_of_votes / totalvotes) * 100
diana_percent = (diana_num_of_votes / totalvotes) * 100
raymon_percent = (raymon_num_of_votes / totalvotes) * 100
# Percentage voted is the number of votes a candidate received divided by the total votes. Multiply the result by 100
round1 = round(charles_percent, 3)
round2 = round(diana_percent, 3)
round3 = round(raymon_percent, 3)
# The above are storing the rounded percentage of votes received by each Candidate to 3 decimal places. 
def most_frequent(candidate):
    return max(set(candidate), key = candidate.count)
winner = most_frequent(candidate)
# The above sets about finding the candidate that appears most freqently in the candidate list. 
# This method essentially gives the winner of the election. 
print("Election Results")
print("-------------------")
print("Total votes: " + str(totalvotes))
print("-------------------")
print("Charles Casper Stockham: " + str(round1) + "% (" + str(charles_num_of_votes) + ")")
print("Diana DeGette: " + str(round2) + "% (" + str(diana_num_of_votes) + ")")
print("Raymond Anthony Doane: " + str(round3) + "% (" + str(raymon_num_of_votes) + ")")
print("-------------------")
print("Winner: " + winner)