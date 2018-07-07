# load
import os 
import csv

# files to load
file_to_load = os.path.join("Resources", "election_data.csv")

# read the csv and convert it into a list of dictionaries
with open(file_to_load, 'r', encoding='utf-8-sig') as voting_data:
    csv_reader = csv.DictReader(voting_data)
    poll_data = list(csv_reader)
    vote_ids = [ x ['Voter ID'] for x in poll_data ]
    
    # make sure nobody voted more than once   
    unique_vote_ids = list(set(vote_ids))
    # error validate each vote only once
    #if len(unique_vote_ids) < len(vote_ids):
    #    raise Exception("You can only vote once")

    # total # of votes cast                                                                                                   
    total_votes = len(poll_data)

    # list of candidates                                                                                                      
    list_candidates = [ x ['Candidate'] for x in poll_data ]
    list_candidates = list(set(list_candidates))
    
    # dict for vote tally including candidates                                                                                                  
    md = {}
    for candidate in list_candidates:
        md[candidate] = 0

    # count votes for each candidate                                                                                          
    for vote in poll_data:
        md[vote['Candidate']] += 1

    # make a list and sort it                                                                                               
    result_list = []
    for key,value in md.items():
        result_list.append([key,value])
        result_list.sort(key=lambda x:x[1], reverse=True)
  
    # list results                                                                                                     
    results = []
    results.append("")
    results.append("Election Results")
    results.append("-"*50)
    results.append(f"Total Votes: {total_votes}")
    results.append("-"*50)
    for candidate in result_list:
        results.append(f"Candidate {candidate[0]}:{candidate[1] / total_votes*100:.3f}% ({candidate[1]})")
    results.append("-"*50)
    results.append(f"Winner Candidate: {result_list[0][0]}")
    results.append("-"*50)
  
    # print to file                                                                                                         
    for line in results:
        print(line)                                                                                                          
    with open('election_results.txt','w') as outfile:
        for line in results:
            outfile.write(line+'\n')
    
