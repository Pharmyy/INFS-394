import pandas as pd

# Read data from CSV file into a DataFrame
df = pd.read_csv('spotify_top_songs_audio_features.csv')

# Display column names
print("Original columns:")
print(df.columns)

'''
# Reduce DataFrame to five specific columns
selected_columns = df[['acousticness', 'danceability', 'energy', 'loudness', 'speechiness', 'genre']]

df = df[selected_columns]


# Report number of rows in the DataFrame
print("Number of rows before removing rows:", df.count())

# Remove rows based on certain criteria
df = df.query('danceability > 0.5')  # Example criteria: remove songs with danceability less than 0.5

# Report number of rows after removing rows
print("Number of rows after removing rows:", df.count())

# Create a new column indicating something about one of the numeric columns
df['energy_gt_0.7'] = 0

# Set the value of the new column based on values in a numeric column
df.loc[df['energy'] > 0.7, 'energy_gt_0.7'] = 1

# Create dummy variables for a column with categorical values
df = pd.get_dummies(df, columns=['genre'])

# Display the first 7 rows
print("First 7 rows:")
print(df.head(7))

# Display the last 4 rows
print("Last 4 rows:")
print(df.tail(4))

# Save DataFrame to a new CSV file without the index
df.to_csv('cleaned_spotify_data.csv', index=False)

'''
