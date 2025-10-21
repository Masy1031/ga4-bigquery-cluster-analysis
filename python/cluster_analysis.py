from google.colab import auth
auth.authenticate_user()

from google.cloud import bigquery
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# BigQuery クライアント設定
project_id = "<プロジェクトID>"
client = bigquery.Client(project=project_id)

# クエリ実行
query = """
select
  *
from
  `作成したテーブル`
"""
df = client.query(query).to_dataframe()

# 不要カラム削除
df = df.drop("user_pseudo_id", axis=1)

# クラスタ分析
km = KMeans(n_clusters=3, random_state=42)
df["cluster"] = km.fit_predict(df)

# クラスタ別の平均値と件数を出力
print(pd.concat([df.groupby("cluster").mean(), df["cluster"].value_counts()], axis=1))

# 最適クラスタ数を確認 (エルボー法)
sse_list = []
for i in range(1, 10):
    km = KMeans(n_clusters=i, random_state=42)
    km.fit(df)
    sse_list.append(km.inertia_)

plt.figure(figsize=(8, 4))
plt.plot(range(1, 10), sse_list, marker="o")
plt.title("Elbow Method for Optimal Clusters")
plt.xlabel("Number of clusters")
plt.ylabel("SSE")
plt.show()
