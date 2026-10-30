# Riosca - Irish Stock Exchange (Euronext Dublin) Risk Analysis Application

An interactive Machine Learning web application designed for investors to analyse the financial risk profile of companies listed on the **Irish Stock Exchange (Euronext Dublin)**. 

The application uses an **XGBoost Classifier** trained on key fundamental financial ratios—such as liquidity, leverage, profitability, and debt coverage—to classify companies as **Low Risk / Financially Stable** or **High Risk / Financially Distressed**.

---

## Key Features

* **🏢 Irish Stock Exchange Explorer:** Select listed Irish companies (e.g., *CRH, Ryanair, Bank of Ireland, AIB, Kerry Group, Glanbia*) from a dropdown menu to instantly view their core financial metrics.
* **🤖 Automated ML Risk Assessment:** Generates an immediate risk verdict along with probabilistic confidence scores.
* **💡 Actionable Investor Guidance:** Provides clear recommendations on whether a company is suitable for investment based on its solvency profile.
* **🎛️ Custom Scenario Simulator:** Test custom financial ratios to model speculative or unlisted companies in real-time.

---

## Dataset Ratios & Features

The model evaluates company health using six fundamental financial metrics:

| Metric | Category | Description |
| :--- | :--- | :--- |
| **Current Ratio** | Liquidity | Ability to cover short-term obligations (Anything greater than €1 is healthy). |
| **Debt-to-Equity** | Solvency / Leverage | Financial leverage (Anything greater than €2 indicates higher debt risk). |
| **Return on Equity (ROE)** | Profitability | Efficiency at generating profits from net assets. |
| **Net Profit Margin** | Profitability | Percentage of revenue remaining as net income. |
| **Cash Flow to Debt** | Solvency | Operating cash flow relative to total debt obligations. |
| **Interest Coverage** | Debt Service | Ability to pay interest on outstanding debt (3 times the debt amount is preferred). |

---

## Repository Structure

```text
├── irish_stock_exchange_companies.csv   # Dataset of Euronext Dublin listed companies
├── train_model.py                      # Script to train and export the XGBoost model
├── company_risk_model.pkl              # Saved trained machine learning model
├── app.py                              # Streamlit web application script
├── requirements.txt                    # List of required Python dependencies
└── README.md                           # Documentation
```
## References
1. Davy Stockbrokers (2026) ISEQ index: Markets and share prices, Available at: https://www.davy.ie/market-and-insights (Accessed: 30 October 2026).
2. Euronext (2026) All stocks listed on Euronext Dublin, the Irish Stock Exchange, Available at: https://live.euronext.com/en/markets/dublin/equities/list (Accessed: 30 October 2026).
3. Euronext Markets (2026) Equities, shares and national indices: ISEQ 20, Available at: https://live.euronext.com/en/products/equities (Accessed: 30 October 2026).
   
