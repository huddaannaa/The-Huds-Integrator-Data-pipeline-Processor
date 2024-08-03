# The-Huds-Integrator-Data-pipeline-Processor
## Documentation for the Enrichment Program

## Overview

This program is designed to enrich JSON data files by processing and augmenting them with additional information. It reads input JSON files, performs enrichment using various functions, and outputs the enriched data. The program is modular, allowing different types of enrichment by defining specific functions.

### Files and Their Purpose

1. **utils.py**
   - Contains utility functions for reading and writing files.

2. **calls.py**
   - Main entry point for enrichment jobs.
   - Handles the processing of JSON files and calls specific enrichment functions.

3. **core.py**
   - [Not inspected, presumably contains core functionalities]

4. **enrichment.yaml**
   - Configuration file specifying parameters for the enrichment process.

5. **functions.py**
   - Contains specific enrichment functions to process and augment data.

6. **link.py**
   - Links the functions defined in `functions.py` with the configuration in `enrichment.yaml`.

### Detailed Description of Each File

#### utils.py

Utility functions for file operations:

- **`writer(filex, data)`**
  - Appends `data` to the file specified by `filex`.
  - **Parameters:**
    - `filex` (str): The file path.
    - `data` (str): The data to write.

- **`writer_mem(filex, data)`**
  - Writes `data` to the file specified by `filex`, overwriting any existing content.
  - **Parameters:**
    - `filex` (str): The file path.
    - `data` (str): The data to write.

- **`reader(file_n)`**
  - Reads all lines from the file specified by `file_n`.
  - **Parameters:**
    - `file_n` (str): The file path.
  - **Returns:**
    - List of lines read from the file, stripped of newline characters.

#### calls.py

Main script for running enrichment jobs:

- **Imports:**
  - Imports necessary functions and configurations from `functions.py`, `link.py`, and `utils.py`.

- **`job(json_data_filepath, new_file_name, config)`**
  - Processes a JSON data file and performs enrichment.
  - **Parameters:**
    - `json_data_filepath` (str): Path to the JSON data file to be processed.
    - `new_file_name` (str): Name of the new file to write enriched data.
    - `config` (dict): Configuration parameters for the job.

- **`threat_actor_enrichment(params)`**
  - Enriches data with threat actor information based on predefined patterns.
  - **Parameters:**
    - `params` (dict): Parameters for the enrichment, including JSON data and key to enrich.
  - **Returns:**
    - Dictionary containing the enrichment results.

#### link.py

Links functions to configuration:

- **Imports:**
  - Imports `re` for regular expressions and `yaml` for YAML parsing.

- **Function Definitions:**
  - Reads `functions.py` to find all defined functions.
  - Loads configuration from `enrichment.yaml`.

#### functions.py

Contains specific enrichment functions:

- **Specific Function Details:**
  - Contains custom enrichment functions defined by the user.
  - Functions are designed to process and augment specific fields in the JSON data.

### How to Use the Program

1. **Configuration:**
   - Ensure `enrichment.yaml` is properly configured with necessary parameters.
   
2. **Running an Enrichment Job:**
   - Call the `job` function from `calls.py` with appropriate parameters:
     - `json_data_filepath`: Path to the input JSON file.
     - `new_file_name`: Name of the output file for enriched data.
     - `config`: Configuration dictionary from `enrichment.yaml`.

3. **Example Usage:**
   ```python
   from calls import job
   from link import config

   json_data_filepath = 'path/to/input.json'
   new_file_name = 'path/to/output.json'

   job(json_data_filepath, new_file_name, config)
   ```

### Dependencies

- **Python Modules:**
  - `re`
  - `yaml`
  - `json`
  - `os`
  - `hashlib`

### Notes

- Make sure all paths and configurations are correctly set before running the program.
- Customize the enrichment functions in `functions.py` as needed for specific data processing requirements.

