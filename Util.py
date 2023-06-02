import yaml
import csv


def convert_csv_to_dict(filename):
    dict_list = []

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_list.append(dict(row))

    return dict_list

def str_representer(dumper, data):
    if isinstance(data, str):
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style="'")
    return dumper.represent_data(data)

def convert_dict_to_yaml(dictionary):
    yaml.add_representer(str, str_representer)
    yaml_string = yaml.dump(dictionary, sort_keys=False)
    return yaml_string


def remove_quotes_from_yaml_keys(yaml_file):
    with open(yaml_file, 'r') as file:
        yaml_content = file.read()
        data = yaml.safe_load(yaml_content)

    modified_data = remove_quotes_from_dict_keys(data)
    modified_yaml_content = yaml.dump(modified_data, sort_keys=False)

    return modified_yaml_content

def remove_quotes_from_dict_keys(data):
    if isinstance(data, dict):
        return {key.strip("'"): remove_quotes_from_dict_keys(value) for key, value in data.items()}
    if isinstance(data, list):
        return [remove_quotes_from_dict_keys(item) for item in data]
    return data