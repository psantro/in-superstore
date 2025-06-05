# 🛍️ Business Intelligence (IN) - Superstore 🛒

A business intelligence project for a fictional superstore — leveraging Python and machine learning to analyze sales trends, forecast performance, and enable data-driven decision-making.

---

## 🛠️ (Optional Local) Installation Guide

**This installation is optional**. This is needed only if you want to edit the application or run it locally.
**You can already access the working app deployed online via [streamlit cloud](https://in-superstore.streamlit.app/).**

To get started, ensure you have the following installed:

- [Git](https://git-scm.com/)
- [Python 3.13](https://www.python.org/downloads/)

### 1. Clone the Repository

```bash
git clone https://github.com/psantro/in-superstore.git
cd in-superstore
```

### 2. Create a Virtual Environment

- **Windows**:
```bash
python -m venv .venv
```

- **macOS/Linux/WSL**:
```bash
python3 -m venv .venv
```

### 3. Activate the Virtual Environment

- **Windows**:
```bash
.venv\Scripts\activate
```

- **macOS/Linux/WSL**:
```bash
source .venv/bin/activate
```

### 4. Install Project with Dependencies

Choose one of the following options:

- **User Installation**:

```bash
pip install -e .
```

- **Developer Installation (with dev dependencies)**

```bash
pip install -e .[dev]
```

### 5. Configure `.streamlit/secrets.toml`

Create `.streamlit/secrets.toml` file (inside the project folder `) with the following content:

```toml
[data]
data_dirname = "data"
superstore_filename = "Superstore.csv"
geographic_filename = "US.txt"
```

### 6. Run the project

```bash
streamlit run src/in_supermarket/dashboard/app.py
```

And then open your web browser with the specified port. 

### 7. Exit

Press `Control + C` to terminate the `streamlit` app.
And then close the Virtual Environment: 

```bash
deactivate
```
