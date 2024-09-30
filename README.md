# PagerDuty Lab

This repository contains Python scripts designed to automate tasks related to managing PagerDuty users and incidents.

## Table of Contents
  - [Table of Contents](#table-of-contents)
  - [Scripts Overview](#scripts-overview)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Scripts Overview
Here’s a list of the script in this repository along with its description:

1. **[pagerduty_user_export.py](pagerduty_user_export.py)**: Exports a list of users from PagerDuty, including their details such as roles, contact information, and on-call schedules.

## Requirements
- **Python 3.x**: Ensure that Python 3 is installed on your system.
- **PagerDuty API**: Install the required libraries to interact with the PagerDuty API.
- **API Keys**: You will need a PagerDuty API token to authenticate API requests.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo-name/pagerduty-automation-scripts.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your PagerDuty API token and other necessary credentials in environment variables:
   ```bash
   export PAGERDUTY_API_TOKEN="your-token-here"
   ```

## Usage
Run the desired script from the command line or integrate it into your PagerDuty workflows.

Example:
```bash
python3 pagerduty_user_export.py
```

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the functionality or add new features.

## License
This project is licensed under the MIT License.
