#Import Dependencies
import pandas as pd

#Create reference to CSV file
csv_path = 'Resources/election_data.csv'
pypoll = pd.read_csv(csv_path, encoding = "ISO-8859-1")

#Counts number of values in Ballot ID column and stores them in Variable and prints
votes = pypoll["Ballot ID"].value_counts()
print("Total Votes:" + str(len(votes)))
vote = (len(votes))

#Establish dataframe that isolates Charles Stockham's ballot results and stores his total vote count in variable
new_df = pypoll.loc[pypoll["Candidate"] == "Charles Casper Stockham"]
CSSvotes = new_df["Ballot ID"].value_counts()
CSSvote = (len(new_df))

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

perc2 = (int(DDvote) / int(vote)) * 100
print("Diana DeGette: " + str(perc2) + "%  " + str(len(dosnew_df)))

perc3 = (int(RADvote) / int(vote)) * 100
print(f"Raymon Anthony Doane: " + str(perc3) + "%  " + str(len(tresnew_df)))

print("Winner: Diana DeGettes")

#Create text file that displays results of poll
PyPolltxt = open("file.txt", "w")
PyPolltxt.write("Election Results \n")
PyPolltxt.write("Total Votes:369711 \n")
PyPolltxt.write("Charles Casper Stockham: 23.04%  85213 \n")
PyPolltxt.write("Diana DeGette: 74.81%  272892 \n")
PyPolltxt.write("Raymon Anthony Doane: 3.13%  11606 \n")
PyPolltxt.write("Winner: Diana DeGettes \n")