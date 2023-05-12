import yaml
import csv


def convert_csv_to_dict(filename):
    dict_list = []

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(dict(row))

    return dict_list

def convert_dict_to_yaml(dictionary):
    yaml_string = yaml.dump(dictionary, sort_keys=False)
    return yaml_string