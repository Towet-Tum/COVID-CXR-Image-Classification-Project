import os
from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import (DataIngestionConfig, 
                                                DataPreprocessingConfig,
                                                TrainingConfig)

class ConfigurationManager:
    def __init__(self,
                 config_file_path = CONFIG_FILE_PATH,
                 params_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_preprocessing_config(self) -> DataPreprocessingConfig:
        
        dataset = os.path.join("artifacts", "data_ingestion", "COVID_IEEE")
        config = self.config.data_preprocessing
        create_directories([config.root_dir, config.split_folder])
        data_preprocessing_config = DataPreprocessingConfig(
            root_dir = config.root_dir,
            dataset = Path(dataset),
            split_folder = config.split_folder
        )
        return data_preprocessing_config
    
    def get__training_config(self) -> TrainingConfig:
        config = self.config.training 
        params = self.params
        create_directories([config.root_dir])
        training_config = TrainingConfig(
            root_dir = config.root_dir,
            epochs = params.EPOCHS,
            imgsz=params.IMG_SZ,
            include_top=params.INCLUDE_TOP,
            batch_size=params.BATCH_SIZE,
            weights=params.WEIGHTS,
            lr=params.LEARNING_RATE,
            model_path=Path(config.trained_model_path),
            num_class=params.CLASSES
        )
        return training_config