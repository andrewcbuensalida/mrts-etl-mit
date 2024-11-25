## Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment (mac/linux):

```bash
source .venv/bin/activate
```

For Windows
```bash
.venv\Scripts\activate.bat
```

In the future, to deactivate venv
```bash
.venv\Scripts\deactivate.bat 
```

## Install dependencies. This is not needed if doing a pip install in the notebook
pip install -r requirements.txt

## To save dependencies into requirements.txt
pip freeze > requirements.txt


## Install dependencies. This is not needed if doing a pip install in the notebook
pip install -r requirements.txt

## To save dependencies into requirements.txt
pip freeze > requirements.txt

## 
Download xls
Import to Google sheets
Download as csv
Using python, create DDL to create a mysql database with tables such as sales, NAICS code, Kind of Business, NAICS code-Kind of business association table.
In the sales table, it will have columns id, sales amount, month, year, kind of business.
In the NAICS code table, the columns will be id, and NAICS code.
In the kind of business table, it will have columns id, and kind of business.
In the NAICS code-kind of business association table, columns will be naic id, and kind of business id.
There are some data that have a string (S) instead of a proper sales amount, and some are empty. Just don't insert these sales. 
Insert the data from the csv into sql.
Verify the data is in sql by checking mysql workbench, and writing python test scripts. To run the test script, in the terminal, enter python test.py.
