from pathlib import Path

directories = [
    "src/components",
    "src/configuration",
    "src/cloud_storage",
    "src/data_access",
    "src/constants",
    "src/entity",
    "src/exception",
    "src/logger",
    "src/pipeline",
    "src/utils",

    "src/tests",
    "src/schema",
    "src/monitoring",

    "notebooks",

    "data/raw",
    "data/processed",
    "data/interim",
    "data/external",

    "artifacts/model",
    "artifacts/reports",
    "artifacts/logs",
    "artifacts/metrics",

    "config",

    "scripts",
    "logs",
]

files = [
    "src/__init__.py",

    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_validation.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/components/model_pusher.py",

    "src/configuration/__init__.py",
    "src/configuration/mongo_db_connection.py",
    "src/configuration/aws_connection.py",

    "src/cloud_storage/__init__.py",
    "src/cloud_storage/aws_storage.py",

    "src/data_access/__init__.py",
    "src/data_access/vehicle_insurance_data.py",

    "src/constants/__init__.py",
    "src/constants/application.py",
    "src/constants/training.py",

    "src/entity/__init__.py",
    "src/entity/config_entity.py",
    "src/entity/artifact_entity.py",
    "src/entity/estimator.py",
    "src/entity/s3_estimator.py",

    "src/exception/__init__.py",
    "src/exception/custom_exception.py",

    "src/logger/__init__.py",
    "src/logger/logging.py",

    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",

    "src/utils/__init__.py",
    "src/utils/main_utils.py",
    "src/utils/file_utils.py",

    "src/tests/__init__.py",
    "src/tests/test_pipeline.py",

    "src/schema/data_schema.py",

    "src/monitoring/drift_detection.py",

    "notebooks/Used_Cars_Analysis.ipynb",
    "notebooks/Model_Experiments.ipynb",

    "app.py",
    "demo.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "setup.py",
    "pyproject.toml",
    ".gitignore",
    "README.md",

    "config/model.yaml",
    "config/schema.yaml",
    "config/logging.yaml",

    "scripts/train.py",
    "scripts/predict.py",
]

for dir_path in directories:
    Path(dir_path).mkdir(parents=True, exist_ok=True)

for file_path in files:
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.touch()
        print(f"Created: {file_path}")
    else:
        print(f"Already exists: {file_path}")
        print(f"Already exists: {file_path}")