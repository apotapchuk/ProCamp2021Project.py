def ENV = 'vat'
def BROWSER = 'chrome_remote'
def TESTTYPE = 'smoke'
def TESTS = 'src/tests'

def gitRepo = cosmoid@vs-ssh
def gitCredentials = '...'
def test_job_name = "common.test"
def SLACK_CHANNEL = "#monitiring"
def EMAIL_LC_LIST_TEMPLATE = '...'
def SUBJ_TEMPLATE = 'CosmoID'
def EMAIL_TEMPLATE = ""
""" _TEST_REPORT__"""
stripMargin().stripIndent()
properties ([
    gitParameter(branch:
            branchFick
            defaultValue
            description
            listsize:
                name:)
])