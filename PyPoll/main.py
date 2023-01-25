#Import Dependencies
import pandas as pd

#Create reference to CSV file
csv_path = 'Resources/election_data.csv'
pypoll = pd.read_csv(csv_path, encoding = "ISO-8859-1")
winner_count = 0
winner_name = ""
#Counts number of values in Ballot ID column and stores them in Variable and prints
votes = pypoll["Ballot ID"].value_counts()
print("Total Votes:" + str(len(votes)))
vote = (len(votes))

#Establish dataframe that isolates Charles Stockham's ballot results and stores his total vote count in variable
new_df = pypoll.loc[pypoll["Candidate"] == "Charles Casper Stockham"]
CSSvotes = new_df["Ballot ID"].value_counts()
CSSvote = (len(new_df))
print(CSSvote)

#Establish dataframe that isolates Dianna DeGette's ballot results and stores her total vote count in variable
dosnew_df = pypoll.loc[pypoll["Candidate"] == "Diana DeGette"]
DDvotes = dosnew_df["Ballot ID"].value_counts()
DDvote = (len(dosnew_df))

#Establish dataframe that isolates Raymon Doane's ballot results and stores his total vote count in variable
tresnew_df = pypoll.loc[pypoll["Candidate"] == "Raymon Anthony Doane"]
RADvotes = tresnew_df["Ballot ID"].value_counts()
RADvote = (len(tresnew_df))

#Calculates percentage of votes for each candidate and prints their results and the winner
perc = (int(CSSvote) / int(vote)) * 100
print("Charles Casper Stockham: " + str(perc) + "%  " + str(len(new_df)))

if int(CSSvote) > winner_count:
    winner_name = "Charles Casper Stockham"
    winner_count = int(CSSvote)

perc2 = (int(DDvote) / int(vote)) * 100
print("Diana DeGette: " + str(perc2) + "%  " + str(len(dosnew_df)))

if int(DDvote) > winner_count:
    winner_name = "Diana DeGette"
    winner_count = int(DDvote)

perc3 = (int(RADvote) / int(vote)) * 100
print(f"Raymon Anthony Doane: " + str(perc3) + "%  " + str(len(tresnew_df)))

if int(RADvote) > winner_count:
    winner_name = "Raymon Anthony Doane"
    winner_count = int(RADvote)

print(f"Winner: {winner_name}")

#Create text file that displays results of poll

Output = f"""
Election Results
-------------------------
Total Votes: {(len(votes))}
-------------------------
Charles Casper Stockham: {perc:.2f}% ({CSSvote:,})
Diana DeGette: {perc2:.2f}% ({DDvote:,})
Raymon Anthony Doane: {perc3:.2f}% ({RADvote:,})
-------------------------
Winner: {winner_name}
-------------------------
"""

print(Output)

with open ("Analysis/pypoll_ouput.txt","w") as out_file:
    out_file.write(Output)



