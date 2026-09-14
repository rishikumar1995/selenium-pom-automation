#!/bin/bash

echo "===== Starting AWS Test Execution ====="

echo "Pulling latest code..."
git pull origin main || exit 1

echo "Activating virtual environment..."
source ~/selenium_aws/.venv/bin/activate || exit 1

echo "Installing dependencies..."
pip install -r requirements.txt || exit 1

echo "Running PyTest..."
pytest -v --html=reports/report.html --self-contained-html

TEST_STATUS=$?

if [ $TEST_STATUS -eq 0 ]; then
    echo "===== TESTS PASSED ====="
else
    echo "===== TESTS FAILED ====="
fi

echo "Test exit code: $TEST_STATUS"

exit $TEST_STATUS
