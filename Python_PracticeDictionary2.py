voting_data = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438}]
for vd in voting_data:
    print(f'{vd["county"]} has {vd["registered_voters"]:,} registered voters')