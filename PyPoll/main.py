#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import os

dirname, _filename = os.path.split(os.path.abspath(__file__)) # Sometimes it was not running and got this 
                                                      # from https://stackoverflow.com/a/1296522
actual_file = os.path.join(dirname, "Resources/election_data.csv") # save tbe path to file

with open (actual_file, mode="r") as fd: # open election results 
    header = fd.readline().strip().split(',') # https://stackoverflow.com/a/52240256
    final_results = dict() # track final results
    tally = dict() # track the final tally
    total_voters = 0 # track total votes
    election_results = csv.DictReader(fd, fieldnames=header) 
    for result in election_results: 
        if not result['Candidate'] in final_results: # if candidate does not match existing candidate
            final_results[result['Candidate']] = list() 
            final_results[result['Candidate']].append(result) 
        elif result['Candidate'] in final_results:
            final_results[result['Candidate']].append(result)
    for i in final_results.keys():
        this_total = len(final_results[i]) 
        total_voters += this_total 
        tally[i] = this_total 

winner = ""
winner_string = ""
for k in tally:
        if not winner:
            winner = k
        elif tally[winner] < tally[k]:
            winner = k
        this_ratio = 100 * tally[k]/total_voters
        winner_string += f"{k}: {this_ratio:.3f}% ({tally[k]})\n"
# print results to terminal
election_results = (
    f"Election Results\n"
    f"------------------------------\n"
    f"Total Votes {total_voters}\n"
    f"------------------------------\n"
    f"{winner_string}"
    f"------------------------------\n"
    f"Winner: {winner}\n"
    f"------------------------------\n"
    )

print(election_results)

# Report printed to file
results_file = os.path.join(dirname, "analysis/election_results.txt")
with open(results_file, "w") as results_dataset:
    print(election_results, file=results_dataset)
