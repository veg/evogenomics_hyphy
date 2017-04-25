import json
import pprint
json_file = "pb2_subset_relax.json"
with open(json_file, "r") as f:
    parsed_json = json.load(f)
    
pprint.pprint(parsed_json[u"relaxation-test"]) #{u'LR': 32.28388659252232, u'p': 1.332134691445219e-08}

print(parsed_json[u"fits"].keys()) #[u'Alternative', u'Partitioned MG94xREV', u'Null']
pprint.pprint(parsed_json[u"fits"][u"Alternative"])
pprint.pprint(parsed_json[u"fits"][u"Null"])

# Alt
# u'rate-distributions': {u'Reference': [[0.01165196560177873,
#                                         0.9755743485752828],
#                                        [1,
#                                         0.02437217593037505],
#                                        [228.8408151168252,
#                                         5.34754943421435e-05]],
#                         u'Test': [[0.04383562765948364,
#                                    0.9755743485752828],
#                                   [1,
#                                    0.02437217593037505],
#                                   [45.43080501293446,
#                                    5.34754943421435e-05]]},
