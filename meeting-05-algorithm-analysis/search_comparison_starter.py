def load_data(filename):
    with open(filename,"r",encoding="utf-8") as f:
        return [int(x.strip()) for x in f if x.strip()]

data=load_data("../data/search_data_10000.txt")
# TODO: add/import instrumented search functions.
# Compare favorable, middle, late, and missing targets.
