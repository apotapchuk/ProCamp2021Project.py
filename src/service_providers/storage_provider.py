from cosmosid.storage.base import ProviderFactory
from src.config import CONFIG


class StorageProvider:
    STORAGE = ProviderFactory.init_storage_factory

    @staticmethod
    def form_s3_location(path: str):
        path = path.lstrip('/')
        if path.startwith(CONFIG.AUTO_SAMPLES_FOLDER):
            path = CONFIG.AUTO_SAMPLES_FOLDER+path
        return path

    @staticmethod
    def s3(CONFIG, AWS_REGION):
        CONFIG.AWS_REGION
        return AWS_REGION

    def get_storageProviderType(self):
        self.STORAGE = STORAGE
        storageProviderType = get.storageProviderType(STORAGE)
        return storageProviderType
