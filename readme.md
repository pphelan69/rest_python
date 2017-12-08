[Work in Progress ..........]
# DataCloud Hybrid Integration Manager Automation
Python test automation framework used to test DataCloud Hybrid Integration Manager API's.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 2.7.x or 3.6.x
- git
- pip
- pytest



#### Html Reporting for the pytest Execution

Reference URL:  https://pypi.python.org/pypi/pytest-html/

- Using pytest-html to generate Html reports for test execution
- Installation : pip install pytest-html
- Executing tests: pytest --html=report.html --self-contained-html
- Using Metadata Eg.: pytest --metadata Environment Backup_Stage  --html=report.html  --self-contained-html

  Note: By using above command, we get a self contained html report which can be shared with anyone without dependencies.
        we can set metadata related to execution using --metadata Eg. Environment


## Authors
***Peter Phelan** - *Initial work*

***Atul Dadhich**


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

