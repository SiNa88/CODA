from matching import Player
from matching.games import HospitalResident

import urllib
import yaml
from yaml import load, dump, Loader

resident_preferences = yaml.full_load(open('microservices.yml', 'r'))
hospital_preferences = yaml.full_load(open('resources.yml', 'r'))
hospital_capacities = yaml.full_load(open('capacities.yml', 'r'))


#print(len(resident_preferences), len(hospital_preferences), sum(hospital_capacities.values()))


game = HospitalResident.create_from_dictionaries(
    resident_preferences, hospital_preferences, hospital_capacities
)

matching = game.solve(optimal="resident")
print(matching)

assert game.check_validity()
assert game.check_stability()

matched_residents = []
for _, residents in matching.items():
    for resident in residents:
        matched_residents.append(resident.name)

unmatched_residents = set(resident_preferences.keys()) - set(matched_residents)
print(unmatched_residents)