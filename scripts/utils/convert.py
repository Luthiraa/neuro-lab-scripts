import scipy.io
import pandas as pd

def convert_mat_to_csv(mat_file, csv_file, expected_shape):
    # Load the .mat file
    mat = scipy.io.loadmat(mat_file)
    mat = {k: v for k, v in mat.items() if k[0] != '_'}
    data = pd.DataFrame(mat[list(mat.keys())[0]])
    if data.shape != expected_shape:
        raise ValueError(f"Data shape {data.shape} does not match expected shape {expected_shape}")
    data.to_csv(csv_file, index=False)
    print(f"Data from {mat_file}:")
    print(data)
    print(f"Shape: {data.shape}")

# convert sfap2.mat, sfap5.mat, and sfap10.mat to CSV with expected shapes
convert_mat_to_csv('sfap2.mat', 'sfap2.csv', (5, 702))
convert_mat_to_csv('sfap5.mat', 'sfap5.csv', (5, 501))
convert_mat_to_csv('sfap10.mat', 'sfap10.csv', (5, 300))