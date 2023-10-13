# Scrape Cook County's Jail Population Report

A postprocess script in Github's Flat Data actions is used to fire a Python script that collects Cook jail population and community correction data.

## Execution :

- the Flat Data action is scheduled daily.

- the `postprocess.ts` script is then run, triggers the install of python packages (including geopandas!), and runs the main python script `postprocess.py`.

- `postprocess.py` prints out its received arguments, and then parses a pdf table into a CSV file `parsed_pdf_test.csv`. Then, an existing .csv of past jail records is imported and the parsed csv is appened to that file and saved.
- 
## Data Notes

- [Cook Jail Population Data](https://www.cookcountysheriffil.gov/jail-population-data/)


## Thanks

- Thanks to the Github Octo Team
- Thanks to [Pierre-Olivier Simonard](https://github.com/pierrotsmnrd/flat_data_py_example) for his repo on implementing Flat data as a Python postprocess file.

