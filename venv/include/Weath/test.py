import pandas as pd

file = pd.read_csv('city_code.csv')

for str in file:
    for str1 in str:
        print("_", str1)

if __name__ == "__main__":
    print("this is running self")
else:
    print("this is running _ %s" % __name__)
