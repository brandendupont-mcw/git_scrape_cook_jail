# Scrape Cook County's Jail Population Report 

A Python script that collects Cook jail population and community correction data. 

## Execution :

- the Github Action action is scheduled daily.

- the `flat.yml` specifies the action, triggers the install of ghostscript, and required dependencies. This includes [camelot.py](https://camelot-py.readthedocs.io/en/master/) which is used to parse the Cook County Jail's PDF reports.

- the `postprocess.py` script is then trigged and parses the daily pdf table into a cleaned pandas dataframe. Then, an existing .csv of past jail records is imported and the parsed csv is appened to that file and saved at `data/cook-jail-data.csv`.
- the jail occasionally will fail to upload a pdf or the pdf will be corrupted in a way that makes parsing the pdf table fail. In these cases data is stored in the `data/failed_url.csv` file.
- The most recent parsed pdf table is saved at `data/[date-of-pdf]-parsed-pdf-table.csv`. This filed is not filtered or subset.
  
## Data Notes

- Data is taken from Cook County [Cook Jail Population Data](https://www.cookcountysheriffil.gov/jail-population-data/)
- Data begins at 01-01-2018 and is updated daily. Data collected between 2018-2020 is taken from a prior Loyola Center for Criminal Justice Project and was collected by hand. We imputed the few jail records where the Cook County Jail failed to add a pdf report for that day. Data from 2021-present is populated through a backfill of the pdf scraper that triggers daily. Both files were combined to create the `data/cook-jail-data.csv` file that updates daily.


## Maintainted by the Loyola Center for Criminal Justice.

<img src="https://loyolaccj.org/static/images/ccj-loyola-black.svg" alt="drawing" width="250"/> 