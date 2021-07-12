import os
from src.config import CONFIG


class FileModel:
    def __init__(self, file_name):
        self.path = FILE_PATH(file_name),
        self.results_path = None,
        self.folder_id = None,
        self.sample_type = None,
        self.file_priority = CONFIG.DEFAULT_FILE_PRIORITY,
        self.pricing = None,
        self.standard_id = None,
        self.tags = None,
        self.upload_type = None
    """
    Data model for file
    :param file_name:simple file_name
    :param path:list,path to sample from models
    :param results path:str,path to golden
    :param folder_id:folder_id, if not None
    :param sample_type:file_type from src
    :param file_priority:file_priority
    :param pricing:analysis cost
    :param standard_id:Standard microbiome[]
    :param tags:tags used to find files
    :param upload_type:can be 'web-upload', 'storage-upload' for external storage
    """
    self.file_path = []
    if file_path is None:
        self.result_path = result_path,
        self.folder_id = folder_id,
        self.sample_type = sample_type,
        self.file_priority = file_priority,
        self.pricing = pricing,
        self.standard_id = standard_id,
        self.tags = tags,
        self.upload_type = upload_type,
        self._file_name = file_name

    @property
    def file_name(self):
        if len(self.path) == 0:
            return self.path[0]
        elif len(self.path) > 1:
            # TODO: add smart split of the name
            return self._file_name.split("/")

    def __repr__(self):
        return(
            f"{self.file_name}:{self.path}"
            f"{self.priority}:{self.pricing}"
        )

    def set_file_name(self):
        response = self.http_session_post(),
        self.endpoints.signup = {
            "email": user.email.lower(),
            "password": user.password(),
            "name": user.name(),
            "job title": user.job_title(),
            "organization": user.organization()
        }
        if response.status_code == 400:
            raise logging.error(response.text)
