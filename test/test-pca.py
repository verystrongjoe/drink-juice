import  pandas as pd

df = pd.DataFrame(columns=['calory', 'breakfast', 'lunch', 'dinner', 'exercise', 'body_shape'])


df.loc[0] = [1200, 1, 0, 0, 2, 'Skinny']
df.loc[1] = [2800, 1, 1, 1, 1, 'Normal']
df.loc[2] = [3500, 2, 2, 1, 0, 'Fat']
df.loc[3] = [1400, 0, 1, 0, 3, 'Skinny']
df.loc[4] = [5000, 2, 2, 2, 0, 'Fat']
df.loc[5] = [1300, 0, 0, 1, 2, 'Skinny']
df.loc[6] = [3000, 1, 0, 1, 1, 'Normal']
df.loc[7] = [4000, 2, 2, 2, 0, 'Fat']
df.loc[8] = [2600, 0, 2, 0, 0, 'Normal']
df.loc[9] = [3000, 1, 2, 1, 1, 'Fat']

# print(df.head(10))

X = df[['calory', 'breakfast','lunch', 'dinner', 'exercise']]
X.head(9)

# Y is labels
Y = df[['body_shape']]


from sklearn.preprocessing import StandardScaler
x_std = StandardScaler().fit_transform(X)

# print(x_std)

import numpy as np

# features are columns from x_std
features = x_std.T
covariance_matrix = np.cov(features)
print(covariance_matrix)


eig_vals, eig_vecs = np.linalg.eig(covariance_matrix)

print('Eigenvectors \n%s' % eig_vecs)

eig_vals[0]
