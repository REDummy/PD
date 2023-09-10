import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('Toko Buah _MELON ;)_.csv', delimiter='\t')

# Clean up the data
# Replace any non-numeric values in "Harga Total" with NaN
df['Harga Total'] = pd.to_numeric(df['Harga Total'], errors='coerce')

# Replace negative values in "Jumlah" columns with 0
jumlah_columns = ['Jumlah pesanan Jeruk :', 'Jumlah pesanan Salak:', 'Jumlah pesanan Rambutan:',
                  'Jumlah pesanan Kelengkeng :', 'Jumlah pesanan Blimbing :']
for col in jumlah_columns:
    df[col] = df[col].apply(lambda x: max(x, 0))

# Perform min-max normalization on "Harga Total" column
min_harga_total = df['Harga Total'].min()
max_harga_total = df['Harga Total'].max()
df['Harga Total'] = (df['Harga Total'] - min_harga_total) / (max_harga_total - min_harga_total)

# Perform min-max normalization on "Jumlah" columns
for col in jumlah_columns:
    min_val = df[col].min()
    max_val = df[col].max()
    df[col] = (df[col] - min_val) / (max_val - min_val)

# Save the cleaned and normalized DataFrame to a new CSV file
df.to_csv('cleaned_normalized_data.csv', index=False)
