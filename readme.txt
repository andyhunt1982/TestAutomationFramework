HELPFUL LINKS
==============================================================================
app.quicktype.io                    parse JSON to Python classes
codebeautify.org/jsonviewer         view JSON as structured data
python.org                          Python documentation
docs.pytest.org                     PyTest documentation

DOCUMENT REQUIRED DEPENDENCIES
==============================================================================
pip freeze > requirements.txt       list installed packages
pip install -r requirements.txt     install requirements

PYTEST VIA COMMAND LINE
==============================================================================
pytest -v -n5 --browser=chrome --environment=test --headless test_json_parser.py --html=test_results.html

pytest:                             execution command
-v:                                 verbose output
-n5:                                run 5 tests in parallel
test_json_parser.py:                test file
--html=test_results.html:           HTML report
-m "not slow":                      skip slow tests
-m smoke_tests:                     run tests with smoke_tests tag
-rA:                                report summary on all tests executed
--markers:                          list all markers
--disable-warnings:                 disable all warnings
--collect-only:                     only collect tests
--self-contained-html:              generate self-contained HTML report
--browser=chrome:                   browser to use for test run
--environment=test:                 environment to use for test run
--headless:                         run tests in headless mode
