from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path 
    source_URL: Path 
    local_data_file: Path 
    unzip_dir: Path

@dataclass(frozen=True)
class DataPreprocessingConfig:
    root_dir: Path
    split_folder: Path
    dataset: Path

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path 
    model_path: Path
    epochs: int
    imgsz: int
    batch_size: int
    lr: float
    weights: str
    num_class: int
    include_top: bool