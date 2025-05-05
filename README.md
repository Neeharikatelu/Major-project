# Hypergraph-Based Analysis of ERC-721 Token Transactions on Ethereum

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Blockchain-Ethereum-black.svg" alt="Blockchain Badge"/>
  <img src="https://img.shields.io/badge/Graph%20Theory-Hypergraph-red.svg" alt="Hypergraph Badge"/>
  <img src="https://img.shields.io/badge/NFT-ERC721-purple.svg" alt="NFT Badge"/>
  
</p>

---

## 📌 Overview
This project presents a comprehensive analysis of Ethereum's ERC-721 token (NFT) transactions using **hypergraph theory** to capture complex, multi-party interactions in the NFT ecosystem. Traditional graph theory, which only captures pairwise relationships, was found insufficient — leading to the adoption of hypergraphs.

By treating each **token** as a **hyperedge** and participating **wallets** as **nodes**, this project uncovers hidden patterns, community structures, and temporal dynamics in NFT trading behavior.

---

## ⚡ Limitations of Traditional Graphs
-  Only captures pairwise relationships — missing multi-wallet transactions.
-  No token-specific insights.
-  Hard to model higher-order (group) interactions.
-  Community detection between wallets is difficult.

Thus, **hypergraph modeling** provides a better and deeper understanding of NFT ecosystems.

---

## 📊 Dataset
- **Source:** Ethereum blockchain (XBlock-ETH Dataset)
- **Duration:** 2015 – 2024
- **Fields:**
  - Block Number
  - Timestamp
  - Transaction Hash
  - Sender and Recipient Addresses
  - Smart Contract Flags

---

## 🛠️ Preprocessing Steps
- Converted Unix timestamps to `yy-mm-dd` format.
- Split the dataset into **daywise files**.
- Labeled Ethereum addresses for easy tracking.
- Structured data to fit hypergraph construction format.

- **Timestamp Conversion:**  
  Implemented in `timestamp.ipynb`, this notebook converts Unix timestamps in the transaction data to a human-readable `yy-mm-dd` format.

- **Daywise Splitting:**  
  The `datewisesplit.ipynb` script splits the entire dataset into separate files for each day to facilitate daily hypergraph construction.

- **Address Labelling:**  
  In `labelling.ipynb`, Ethereum addresses are labeled to distinguish between smart contracts and externally owned accounts (EOAs).

---

## 🔗 Hypergraph Construction
- **Tokens** are treated as **hyperedges**.
- **Wallet addresses** are treated as **nodes**.
- For each day:
  - Hypergraphs were created connecting wallets participating in token transfers.
- Stored hypergraphs in **JSON** format for efficient analysis.
  
- **Hypergraph Construction Preparation:**  
  `hypergraph_try.ipynb` processes the cleaned and labeled data to structure it in a format suitable for hypergraph modeling, treating each token as a hyperedge and wallets as nodes.
---

## 📈 Analytical Steps
- **Token vs Days Analysis:** Tracked number of tokens transferred daily.
- **Hyperedge Classification:** Counted 1-hyperedges, 2-hyperedges, 3-hyperedges, etc.
- **Recurring Community Detection:** Tracked recurring sets of wallets interacting across different days.
- **Temporal Distance Analysis:** Calculated time gaps between repeated community appearances.
- **s-Adjacency Analysis:** Checked if hyperedges share s common nodes.
- **s-Component Detection:** Detected community clusters by analyzing s-connected hyperedges.

---

## 🏆 Results and Key Insights
- Temporal evolution of NFT trades mapped from 2015–2024.
- Degree distributions followed power-law behavior.
- Strong recurring communities were detected.
- Major s-components revealed strong wallet clusters.

---

## 🧰 Tools & Technologies Used
- **Python 3.10+**
- **Pandas**, **NumPy** — Data processing
- **NetworkX**, **HyperNetX** — Graph and Hypergraph modeling
- **Matplotlib**, **Seaborn** — Visualization
- **JSON** — Data storage

---

## 📂 Folder Structure
├── Codes/
│ ├── timestamp.ipynb
│ ├── datewisesplit.ipynb
│ ├── labelling.ipynb
│ ├── hypergraph_try.ipynb
│ ├── blocknumber.ipynb
│ ├── csv_day_major.ipynb
│ ├── datewise_split.py
│ ├── degree_chnages.ipynb
│ ├── s_adjacency.ipynb
│ ├── s_components.ipynb
│ ├── ...
├── Plots_hyperedges_temporal/
├── hyperedges_by_size/
├── hyperedges_occurrences_by_size/
├── hypergraph_everyday_Null_clean/
├── null_clean_plots/
├── repeated_hyperedges_by_size/
├── smart_filtered_hyperedges_by_size/
├── temporal_distance_plots/
├── temporal_distance_plots_log_x/
├── temporal_distance_plots_log_x_y/
├── temporal_distance_plots_log_y/
├── temporal_distances_by_size/
├── results/
│ ├── *.png
│ ├── *.csv
├── 3_hyperedges_occurrences.csv
├── Hypergraph_Report.pdf
├── Major_Neeharika_final_report.pdf
├── README.md

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/Neeharikatelu/Major-project.git

```
### 2. Install Requirements
Install the required Python libraries:
```
pip install -r requirements.txt
requirements.txt:
```

### Required Libraries
- `numpy>=2.2.5`
- `pandas>=2.2.2`
- `networkx>=3.3`
- `hypernetx>=2.4.0`
- `matplotlib>=3.10.1`
- `seaborn>=0.13.2`

### 3. Run Scripts
- Preprocess transaction data
- Create daily hypergraphs
- Perform hypergraph analyses

### 4. Visualize and Analyze
- Plot token transfers over time
- Track recurring wallet groups
- Analyze temporal distances
- Detect s-components and communities

---

✍️ **Author**  
Neeharika Telu  
Roll No: CS21B1029  
B.Tech in Computer Science and Engineering  
Indian Institute of Information Technology, Raichur

👨‍🏫 **Supervisor**  
Dr. Priodyuti Pradhan  
Department of Computer Science and Engineering  
Indian Institute of Information Technology, Raichur

