import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('diamonds.csv')

# # Ensure the 'price' column is numeric
df['price'] = pd.to_numeric(df['price'], errors='coerce')

def price():
    # Find the maximum price value
    max_price = df['price'].max()

    # Output the highest price
    print(f'The highest price of a diamond is: {max_price} nis')

def average():
    # Find the average price value 
    average_price = df['price'].mean()

    # Output the average price
    print(f'The average price of the diamonds is: {average_price} nis')

def cut():
    desired_cut = 'Ideal'
    filtered_df = df[df['cut'] == desired_cut]
    count = filtered_df.shape[0]

    print(f'The amount of Diamonds with cut "{desired_cut}" is: "{count}"')

def diamond_colors():
    df['color'] = df['color'].astype(str)
    color_counts = df['color'].value_counts()
    print('Number of diamonds for each color:')
    for color, count in color_counts.items():
        print(f'{color}: {count}')

def medean_premium():
    df['cut'] = df['cut'].astype(str)
    df['carat'] = pd.to_numeric(df['carat'], errors='coerce')

    # get only 'premium' diamonds
    premium_diamonds = df[df['cut'] == 'Premium']

    # check medean for diamond from type premium
    median_carat = premium_diamonds['carat'].median()
    # print medean
    print(f'The median carat of diamonds with cut "Premium" is: {median_carat}')

def average_by_cut():

        # Group by the 'cut' column and calculate the average carat for each cut
        average_carat_by_cut = df.groupby('cut')['carat'].mean()

        # Print the results
        for cut_type, avg_carat in average_carat_by_cut.items():
          print(f'The average carat for {cut_type} cut is: {avg_carat}')

def average_price_per_color():
    df['color'] = df['color'].astype(str)
    average_price_per_color = df.groupby('color')['price'].mean()

    # Print the results
    print('Average price for each color:')
    for color, avg_price in average_price_per_color.items():
            print(f'Color {color}: {avg_price} nis')


price()
average()
cut()
diamond_colors()
medean_premium()
average_by_cut()
average_price_per_color()