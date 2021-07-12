import selenium.webdriver
from selenium.webdriver.common.by import By


class ComparativeReportMatrix:
    """
    Matrix table tab in comparative analysis
    """
    display_names = (By.CSS_SELECTOR, "tr:nth-child")
    cohorts = (By.CSS_SELECTOR, "tr:nth-child")

    def __init__(self, app):
        self.app = app

    def get_sample_display_name(self, sample_pass):
        return self.app.get_attribute(
            "title",
            By.CSS_SELECTOR, f"tr:nth-child>th:nth-child{sample_pass}"
        )

    @staticmethod
    def _get_title():
        for n in name:
            return[
                n.get_attribute("title")
            ]

    def assert_sample_display_name(self, sample_pass):
        assert current_name == expected_name
        return self.app.get_attribute(
            'sample_display_name',
            By.CSS_SELECTOR, f"tr:nth-child>th:nth-child{sample_pass}"
        )

    def get_cohort_name(self, cohort_position):
        return self.app.get_attribute(
            'title',
            By.CSS_SELECTOR, f"tr:nth-child>th:nth-child{cohort_position}"
        )
