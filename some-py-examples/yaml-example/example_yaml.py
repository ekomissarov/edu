# https://stackabuse.com/reading-and-writing-yaml-to-a-file-in-python/
# https://pyyaml.org/wiki/PyYAMLDocumentation

import yaml

with open(r'categories.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    fruits_list = yaml.load(file, Loader=yaml.FullLoader)

    print(fruits_list)
