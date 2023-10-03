# Ccheck Checklist App User Manual

## Introduction

Welcome to Ccheck, a Mac checklist app with a table-like interface. Ccheck allows you to create and manage checklists with customizable checkboxes, editable name and notes columns for each item. This user manual will guide you through the installation process and provide instructions on how to use the app effectively.

## Installation

To install Ccheck, please follow the steps below:

1. Ensure that you have Python installed on your Mac. Ccheck is developed using Python, so it is necessary to have Python installed to run the app.

2. Clone or download the Ccheck repository from [GitHub](https://github.com/your-repo-link).

3. Open a terminal window and navigate to the directory where you have cloned or downloaded the Ccheck repository.

4. Create a virtual environment (optional but recommended) by running the following command:
   ```
   python3 -m venv ccheck-env
   ```

5. Activate the virtual environment by running the following command:
   ```
   source ccheck-env/bin/activate
   ```

6. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

## Usage

To start using Ccheck, follow the steps below:

1. Open a terminal window and navigate to the directory where you have cloned or downloaded the Ccheck repository.

2. Activate the virtual environment (if you created one) by running the following command:
   ```
   source ccheck-env/bin/activate
   ```

3. Run the Ccheck app by executing the following command:
   ```
   python main.py
   ```

4. The Ccheck app window will open, displaying an empty checklist.

5. To add an item to the checklist, click the "Add Item" button.

6. Each item in the checklist will have editable Name and Notes columns. Click on the respective entry fields to edit the content.

7. To track different states for each item, multiple customizable checkboxes are available. By default, two checkboxes named "State A" and "State B" are provided. You can click on the checkboxes to toggle their state.

8. To add more checkboxes, click the "Add Checkbox" button within each item.

9. To remove an item from the checklist, click the "Remove" button within the item.

10. To exit the Ccheck app, simply close the app window.

## Conclusion

Congratulations! You have successfully installed and learned how to use the Ccheck checklist app. Enjoy organizing your tasks and tracking their states with ease. If you have any further questions or need assistance, please refer to the [Ccheck GitHub repository](https://github.com/your-repo-link) for more information or contact our support team. Happy checklist-ing!