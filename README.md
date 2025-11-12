# The AI & Employment Monitor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-employment-dashboard-twd4brsc6ibrdw7ju5wdd5.streamlit.app/)

An interactive Streamlit dashboard built in Python to visualize the impact of Artificial Intelligence on global and Canadian job markets.

This project, part of VisiVault Analytics, tracks key metrics on job displacement, job creation, and the emerging skills gap.

---

## 📊 Key Features

* **Executive Summary:** At-a-glance KPIs on net job impact, the wage premium for AI-skilled jobs, and the growth rate of AI-exposed industries.
* **Job Transformation:** A Plotly bar chart showing the top professions at risk of automation, based on data from Goldman Sachs and the WEF.
* **Job Creation:** A bar chart of the fastest-growing AI-related roles, such as AI/ML Specialists and Data Scientists.
* **Canada Focus:** A dedicated section on the Canadian labor market, showing which industries are planning to hire AI staff and the expected impact on employment numbers.

---

## 🛠️ Tech Stack

* **Python:** The core language for the application.
* **Streamlit:** Used to build and serve the interactive web dashboard.
* **Pandas:** For all data manipulation and preparation.
* **Plotly:** To create the interactive, publication-quality charts.

---

## 🚀 How to Run Locally

To run this dashboard on your own machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/tonymah2024/ai-employment-dashboard.git](https://github.com/tonymah2024/ai-employment-dashboard.git)
    cd ai-employment-dashboard
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # On macOS/Linux
    python3 -m venv venv
    source vVenv/bin/activate
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    ```bash
    streamlit run dashboard.py
    ```
    Your browser will automatically open to the dashboard.

---

## 📈 Data Sources

This dashboard uses static data compiled from the following 2024/2025 reports:

* **World Economic Forum (WEF):** "Future of Jobs Report"
* **PwC:** "Global AI Jobs Barometer"
* **Goldman Sachs:** "The Potentially Large Effects of Artificial Intelligence on Economic Growth"
* **Statistics Canada:** "Canadian Survey on Business Conditions (Q3 2025)"

### A Note on the Live Data Feed

This project was originally built to connect directly to the live Statistics Canada data API.

A key challenge during development was the "data gap" from Statistics Canada. The `.zip` file links for the quarterly reports are **deleted from the server** the moment a new collection period begins, often *before* the new data is published. This resulted in persistent `404 Not Found` errors.

As of this writing (November 2025), the Q3 data is offline, and the Q4 data is not yet published.

To ensure the app remains functional for demonstration and deployment, this dashboard is **currently using a static version** of the Q3 2025 data. This ensures the app remains functional for demonstration and deployment. The code to re-establish the live API connection (using the `stats-can` library) is ready for implementation once the new quarterly data is available from Statistics Canada.
