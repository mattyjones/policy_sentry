"""
Just a common storage space for storing some constants.
"""
from pathlib import Path

# General Folders
HOME = str(Path.home())
CONFIG_DIRECTORY = '/.policy_sentry/'
ANALYSIS_DIRECTORY_NAME = 'analysis'
ANALYSIS_DIRECTORY_PATH = HOME + CONFIG_DIRECTORY + ANALYSIS_DIRECTORY_NAME

# Database
DATABASE_FILE_NAME = 'aws.sqlite3'
DATABASE_FILE_PATH = HOME + CONFIG_DIRECTORY + DATABASE_FILE_NAME

# Boto3
DEFAULT_CREDENTIALS_FILE = HOME + '/.aws/credentials'

# Policy constants
# https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_version.html
POLICY_LANGUAGE_VERSION = "2012-10-17"

# Audit functionality constants
AUDIT_DIRECTORY_FOLDER = 'audit/'
AUDIT_DIRECTORY_PATH = HOME + CONFIG_DIRECTORY + AUDIT_DIRECTORY_FOLDER
DEFAULT_AUDIT_FILE_NAME = '/privilege-escalation.txt'
DEFAULT_AUDIT_FILE_PATH = AUDIT_DIRECTORY_PATH + DEFAULT_AUDIT_FILE_NAME
