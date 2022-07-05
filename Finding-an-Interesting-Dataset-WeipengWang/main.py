import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

ceo_data = pandas.read_csv("CEO_compensation_top50_2020.csv")

print(ceo_data)