# Changelog
## 2019-10-24
### Added
* Added boto3 and botocore to setup.py
* Cutting a new release to provide a quick fix for those issues
* This fixes #28
### Changed
* Updated Pipfile.lock
* Fixed an issue with the list_policies command
* Fixed the help text for the `download-policies --include-unattached` flag

## 2019-10-19
### Added
* `analyze-iam-policy` Code to create policy-analysis directory, was missing with last release... added it
### Changed
* Removed leftover code before access-level overrides was a feature

## 2019-10-18, part 2
### Added
* access-level overrides now includes a TON of overrides Fixes #18.
* Services: Deepracer, Signer, EventBridge
* Releasing 0.5.1 because of all the major changes to the database
### Changed
* Links documents
* Improvements to the documentation updating scripts.

## 2019-10-18
### Added
* We can now override Access levels so we aren't entirely dependent upon accurate AWS documentation for proper ACLs. Fixes #8.
* Test cases for the new Access level override functions
* You can now supply a custom YML file as part of the initialize command to test out your own overrides (so you don't have to depend on updates to this repository if you don't want to)
* Created `policy_sentry/shared/data/access-level-overrides.yml` for a preloaded set, based on the current known issues with AWS IAM access levels.
* Cut a new release because this is a big improvement (and because I moved around a function or two)

## 2019-10-16
### Added
* Added test cases for YML files that have missing access level blocks - for example, if someone wants to generate a policy that doesn't include "Tagging" or "Permissions Management"
### Changed
* Test cases to allow missing access level blocks 

## 2019-10-15
### Added
* Unit tests for the policy template generation
* `download-policies` command added
  - Downloads policies to `~/.policy_sentry/account-id/aws-managed` or `~/.policy_sentry/account-id/customer-managed`.

## 2019-10-14
### Changed
* `short_help` for Click commands to improve help messages
* `create-template` command added to make policy file writing easier.

## 2019-10-12
### Added
* Updated to 0.4.1
* New services added for coverage:
  - iq
  - iq-permission
  - deepracer
  - dbqms
  - forecast
  - lakeformation
  - rds-data
  
### Changed
* `utils/get_links.py` script had an issue with paths

## 2019-10-06
### Added
* Added `analyze` functionality to analyze a policy according to access levels, not just a list of actions.

### Changed
* Updated the HTML documentation to get the latest updates. 
* Fixed old references to `scripts` directory; now it is the `utils` directory
* Fixed the path of the policy_sentry/shared/data/docs directory in the download-docs.sh script, since its previous reference was the root directory, which was accurate before we moved to pypi compatibility.
 
## 2019-10-02
### Changed
* Sanitizing directory before moving to GitHub
* Remove _docs directory since we are using the wiki

## 2019-09-19
### Added
* `write-policy-dir` command
* input-dir and output-dir directories under examples, to show `write-policy-dir` command usage

## 2019-09-14
### Changed
* Project structure now follows pypi format
* Changed download-docs stuff to utils folder.
* `create_all_tables` command is now `initialize`
* Changed Matty's folder structure a bit so the setup.py file is now in the root directory, which makes more sense.
* Fixed underscore vs. hyphen typo in the docs.
* html files still live in the main policy_sentry pypi package. The user can quickly generate the SQLite database using the initialize function (formerly create_all_tables)
* Lots of other cleanup.

### Added 
* pypi modifications, such as the MANIFEST.in file
* Database file now resides in `$HOME/.policy_sentry/aws.sqlite3`
* Default audit file now resides in `$HOME/.policy_sentry/audit/permissions-access-level.txt`

## 2019-09-11
### Added
* Added modified unit tests in test_write_policy.py
* Created a policy.py file to contain ArnActionGroup

### Changed
* Moved Minimization functions over to their own file
* Instead of ArnActionCollection, now using ArnActionGroup name
* Moved functionality from the write_policy file to the relevant files in the shared folder. 
* Fixed risky-iam.txt file name

## 2019-09-08
### Changed
* Modified the write_policy_with_actions function so it uses the write_policy with crud stuff. We can now delete a lot of the functions that we don't use anymore.
* Removed all the code that is now unused

## 2019-09-04
### Changed
* lots of code reviews and doc strings

## 2019-09-03
### Added
* pipfile and lockfile
* Feature to scrape docs locally: grab_docs.sh, utils/download-docs.sh, utils/get_links.py
* pylintrc file
* disabled *line-too-long* in pylint
* editorconfig file
* bandit as a dependency

### Changed
* update readme links to short version
* Feature to scrape docs locally: grab_docs.sh, utils/download-docs.sh, utils/get_links.py

### 2019-09-02

* Added Unit tests. Fixes #20

### 2019-09-01

* Feature: CRUD Functionality supports user-supplied input now (fixes GH-05)
* Database file now checked into git
* We now assume that you are using the same database file
* Just need to trim the write_policy file and combine functions
* Trimmed the command flags to make thing simpler
* Updated documentation to reflect reduced command flags.

### 2019-08-30 (pt 2)

* Added Condition keys table
* Actions Table now separates the Condition Keys by commas instead of double spaces

### 2019-08-30

* Version bump (0.1.0)
* Fixed class structure
* Moved command-specific documentation to the `_docs` folder for cleanliness

### 2019-08-26

* Added `create_all_tables` command
* Updated functions to include all services (it wasn't grabbing all services before).
* Added Note in README about the 3 services missing from the Actions, Resources, and Condition Keys page
* Added `analyze_iam_policy` command with test files
* Gives a warning when your action matches fishy IAM actions
* Split connect_db and create_tables out into different functions
* Permits using existing database.
* Added expand functionality.
* Added flag to `analyze_iam_policy` to allow custom audit file
* Fixed issue #3 for ecr and codecommit overlap
* Added minimize functionality

### 2019-08-23

* Removed check_access and moved it to a separate repository.
* Fixed imports

### 2019-08-05

* retired check_permissions_usage (Access Advisor check), since CloudMapper generates a great report using that.
* Write_policy now uses SQLite instead of funky objects
* CRUD Functionality now supported
