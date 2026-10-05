# ATCS Unit 1 - Linear Search Datasets

These datasets are intentionally **unsorted** for linear-search experiments.

## Suggested experiments
- Search for the first value (favorable case).
- Search for a middle value.
- Search for the last value (worst-case successful search).
- Search for a guaranteed-missing value (worst-case unsuccessful search).
- Count comparisons rather than relying only on elapsed time.

## Known targets

| File | Size | First | Middle | Last | Guaranteed Missing |
|---|---:|---:|---:|---:|---:|
| linear_search_100.txt | 100 | 4536 | 866 | 9776 | 10000 |
| linear_search_1000.txt | 1,000 | 26034 | 40934 | 15397 | 100000 |
| linear_search_10000.txt | 10,000 | 598949 | 798162 | 324196 | 1000000 |
| linear_search_50000.txt | 50,000 | 940153 | 985484 | 2774766 | 5000000 |
| student_records_5000.csv | 5,000 | 874630 | 148793 | 617337 | 9999999 |

`student_records_5000.csv` provides a more realistic record-search task: search by ID and return the associated record.