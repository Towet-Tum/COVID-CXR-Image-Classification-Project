from cnnClassifier import logger
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.training import Training

STAGE_NAME = "Training Stage"
class TrainingPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        train_config = config.get__training_config()
        training = Training(config=train_config)
        training.train()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> The {STAGE_NAME} has started >>>>>  ")
        train = TrainingPipeline()
        train.main()
        logger.info(f">>>>>>>>> The {STAGE_NAME} has completed succefully >>>>>  ")
    except Exception as e:
        logger.exception(e)
        raise e