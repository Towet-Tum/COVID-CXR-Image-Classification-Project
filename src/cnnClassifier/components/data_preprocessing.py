import splitfolders
from cnnClassifier.entity.config_entity import DataPreprocessingConfig
class DataPreprocessing:
    def __init__(self, config:DataPreprocessingConfig):
        self.config = config

    def split_data(self):
        splitfolders.ratio(self.config.dataset, self.config.split_folder, seed=1337,
                           ratio=(.7,.2,.1), group_prefix=None, move=False)