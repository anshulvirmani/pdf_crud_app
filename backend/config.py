import os
import boto3
from pydantic_settings import BaseSettings

# Note: BaseSettings Class: By inheriting from BaseSettings, your Settings class automatically loads environment variables and performs type validation. This means that each attribute of the Settings class corresponds to an environment variable that Pydantic will try to load.
# Note: Attributes: Each variable (DATABASE_HOST, DATABASE_NAME, etc.) is defined with a specific type (e.g., str or int). Pydantic will enforce these types when loading the environment variables, ensuring that your configuration matches the expected structure and types.
# Note: Default Values: You've set a default value for app_name. If the app_name environment variable is not found, Pydantic will use "Full Stack To Do App" as its value. The other variables do not have default values, so they must be present in the environment or the .env file.


class Settings(BaseSettings):
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    app_name: str = "Full Stack PDF App"
    AWS_KEY: str
    AWS_SECRET: str
    AWS_S3_BUCKET: str = "anshul-pdf-bucket"

    @staticmethod
    def get_s3_client():
        return boto3.client(
            's3',
            aws_access_key_id=Settings().AWS_KEY,
            aws_secret_access_key=Settings().AWS_SECRET
        )

    class Config:
        env_file = ".env"
        extra = "ignore"        