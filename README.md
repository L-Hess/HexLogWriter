# HexLogWriter
Creates excel sheet containing trial on- and offsets from output log file

How to install the requirements:
1. Install python - https://www.python.org/downloads/
2. Install Conda: https://conda.io/projects/conda/en/latest/user-guide/install/index.html
3. Create an environment with numpy, pandas, datetime, argparse and pathlib installed

How to run the script:
1. Open the conda prompt and execute HexLogWriter.py
2. Input the path to the log file when prompted (for example C:\Users\Gebruiker\Documents\HexLogWriter\2019-01-16_10-43-01_hextrack_log)
3. Input the path to the directory in which the excel sheet needs to be saved (for example C:\Users\Gebruiker\Documents\HexLogWriter)
4. ???
5. Profit

Important notes:
Trial count continues for the entire log file (thus after mouse 1 is done, the counter keeps going on for the next mouse), these thus need to be adjusted when inputting the rest of the data.
Sometimes the log file contains no 'real' trials, these then need to be deleted from the excel sheet.
