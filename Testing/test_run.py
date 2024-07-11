import os
import subprocess
from datetime import datetime
import logging
from robot import run

# Configure logging
log_file = 'C:/Users/A. Sahithi/PycharmProjects/CardinalHealth/Testing/task_log.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

logging.info('Task started')

try:
    test_case_file = 'C:/Users/A. Sahithi/PycharmProjects/CardinalHealth/Testing/login.robot'
    results_directory = 'C:/Users/A. Sahithi/PycharmProjects/CardinalHealth/Testing/results'

    # Ensure results directory exists
    os.makedirs(results_directory, exist_ok=True)

    # Get the current date to create a unique report name
    current_date = datetime.now().strftime('%Y-%m-%d')

    # # Command to run the Robot Framework tests
    command = [
        'robot',
        '--outputdir', results_directory,
        '--reporttitle', f"Weekly Test Report {current_date}",
        test_case_file
    ]

    run('C:/Users/A. Sahithi/PycharmProjects/CardinalHealth/Testing/login.robot', outputdir=results_directory)

    # Run the command
    # subprocess.run(command, check=True)
    # logging.info('Task completed successfully')

except Exception as e:
    logging.error(f'Error occurred: {e}')
