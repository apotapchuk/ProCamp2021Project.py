import os.path


class GoldenFileParser(MetaSingleton):
    CSV_LOCAL_PATH = os.path.join(CONFIG.SAMPLES_DATA_PATH)
    CSV_REMOTE_PATH = "automation_samples/sample_results_location.tsv"

    def __init__(self):
        Readers.tsv_to_arr_dict(self_class_.CSV_LOCAL_PATH)
        Readers.remote_tsv_to_arr_dict(
            self.__class__.CSV_REMOTE_PATH,
            os.path.join(Folders.TMP_ID, CSV_LOCAL_PATH),
            True,
        )
        self.file_list = list(unique_everseen(local_file_list))
        # to execute duplicated entries
        if len(self.file_list) == 0:
            logging.warning("No samples for samples Provider found")

    def get_by_tags(self, tags, life_source):
        self.cleanup_tags(tags)
        [life_source]
