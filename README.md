# GA4 × BigQuery × Python クラスタ分析可視化プロジェクト

## 🎯 概要
Google アナリティクス 4 (GA4) の BigQuery 連携データを活用し、
セッション・ユーザー単位の分析とクラスタリングを行いました。

データ抽出 → 分析 → 可視化の一連の流れを、実践形式でまとめています。

---

## 📊 使用データ
Google 提供のサンプルデータセット  
➡️ [GA4 E-commerce BigQuery Demo Dataset](https://developers.google.com/analytics/bigquery/web-ecommerce-demo-dataset?hl=ja)

---

## ⚙️ 使用技術
| 分野 | 技術 |
|------|------|
| データ基盤 | BigQuery |
| 分析 | Python（pandas, scikit-learn, matplotlib） |
| 可視化 | Looker Studio |
| データ | GA4 e-commerce サンプル |

---

## 📁 ディレクトリ構成
`````
ga4-bigquery-cluster-analysis/
├── README.md
├── sql/
│ ├── session_trend.sql
│ └── traffic_source.sql
├── python/
│ └── cluster_analysis.py
└── images/
└── looker_dashboard.png
`````

---

## 🧩 プロセス概要
1. **BigQueryでデータ整形**
   - PV・UU・Sessionの日別推移を集計
   - トラフィックソース別の割合を算出
2. **Pythonでクラスタリング分析**
   - KMeansによるセッション傾向の分類
   - エルボー法による最適クラスタ数の検討
3. **Looker Studioで可視化**
   - BigQueryの結果を直接接続してダッシュボード化

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1303394/127927b4-da39-4b63-97f5-e9d0a953e372.png)
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1303394/d175e5a5-1bb2-425d-bb0a-d8fcf7756d2d.png)

---

## 💡 この分析の狙い
GA4データはLooker Studioだけでも可視化可能ですが、  
BigQuery × Python を経由することで、
- カスタム指標の柔軟な抽出  
- 行動傾向をもとにしたユーザー群分析  
- データドリブンな施策立案  
が可能になります。

---

## 🧠 今後の発展
- クラスタ別にCV率やLTVを比較
- デモグラフィックデータを加えた多変量分析
- Vertex AI を使った自動セグメント化

---
