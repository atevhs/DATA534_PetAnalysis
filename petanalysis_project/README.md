# Package - petanalysis [![Pet Analysis Testing](https://github.com/atevhs/DATA534_PetAnalysis/actions/workflows/python-package.yml/badge.svg)](https://github.com/atevhs/DATA534_PetAnalysis/actions/workflows/python-package.yml)
This Python-package `petanalysis` contains 11 wrapper functions to get pet available data of the US. These functions process API [https://api.petfinder.com/v2/organizations?page=1](https://api.petfinder.com/v2/organizations?page=1e) to get data from shelter information and process API [https://api.petfinder.com/v2/animals?page=1](https://api.petfinder.com/v2/animals?page=1) to get the animal data. One function provide information for shelters and others provide information about animals. This package contains 8 internal functions, 2 for requesting API, 2 for data wrangling for shelter data, and 2 for data wrangling of animal data for association rules, and 2 for building plots which are not available to user. The list of 3 wrapper functions available to user is given below:


```
1. get_shelter(postcode = None)
2. assoc_rules(pets_data_df, min_supp, min_conf, sort_by_col, rule_cnt)
3. visualize()
``` 

# To Use the Package
1. Install the package by typing: pip install petanalysis
2. Add package to the python instance by typing: import petanalysis as pta


##### Notes:
- This package comes with a dataset that was collected using the api listed above. For a refreshed dataset the user will need to get an api key usig the link below and follow the steps given to download the data. Scripts on how to collect multiple pages at a time can be viewed in the 'API data extraction.ipynb' notebook located in the github repo.
- For detail please find in our tutorial document.
- Data Resource: https://www.petfinder.com/developers/
