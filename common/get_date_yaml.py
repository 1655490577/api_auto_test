import yaml


class ReadFileData():

    def __init__(self):
        pass

    @staticmethod
    def load_yaml(file_path):
        with open(file_path, encoding='utf-8') as f:
            read_data = yaml.safe_load(f)
        return read_data


data = ReadFileData()
