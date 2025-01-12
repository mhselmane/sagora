# Sagora Capital 

This project implements ...

## Project Structure

*   **Automation:**
    *   Evening Job
    *   Morning Job
    *   Reconciliation Job
*   **Dashboard:**
    *   PnL
    *   K-Factors
    *   Jobs Monitoring
*   **Automated Trading:**
*   **Utils:**

    


## Getting Started

### Prerequisites

*   Python 3.9 (or later)
*   `pip` (Python package installer)
*   A cryptocurrency exchange account with API keys

### Installation

1.  Clone the repository:
    ```bash
    git clone [invalid URL removed]
    ```
2.  Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
3.  Activate the virtual environment:
    ```bash
    source venv/bin/activate 
    ```
4.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1.  Create a `config.yaml` file (see `config.example.yaml` for an example).
2.  Enter your exchange API keys and other settings.

### Running the bot

1.  To run the automated trading script:
    ```bash
    python automation/execution_scripts.py
    ```
2.  To start the dashboard:
    ```bash
    python dashboard/app.py
    ```

