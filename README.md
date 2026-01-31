# 🛍️ Business Intelligence (IN) - Superstore 🛒

Welcome to the **Superstore Business Intelligence Project**!  
This project leverages **Python** and **machine learning** to analyze sales trends, forecast performance, and help make **data-driven decisions** for a fictional superstore.

You can try the **live app online** via [Streamlit Cloud](https://in-superstore.streamlit.app/) 🚀

---

## 🛠️ Optional Local Installation

If you want to **edit the app** or run it locally, follow these steps. Otherwise, enjoy the deployed version online.

### 🔹 Prerequisites

- [Git](https://git-scm.com/)  
- [Python 3.13](https://www.python.org/downloads/)  

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/psantro/in-superstore.git
cd in-superstore
```

### 2️⃣ Create a Virtual Environment

- **Windows**:
```bash
python -m venv .venv
```

- **macOS / Linux / WSL**:
```bash
python3 -m venv .venv
```

### 3️⃣ Activate the Virtual Environment

- **Windows**:
```bash
.venv\Scripts\activate
```

- **macOS / Linux / WSL**:
```bash
source .venv/bin/activate
```
### 4️⃣ Install Project Dependencies

- **User Installation** (basic dependencies):
```bash
pip install -e .
```

- **Developer Installation** (with dev dependencies):
```bash
pip install -e .[dev]
```

### 5️⃣ Configure .streamlit/secrets.toml 🔑

Create `.streamlit/secrets.toml` inside the project folder with the following content:
```toml
[data]
data_dirname = "data"
superstore_filename = "Superstore.csv"
geographic_filename = "US.txt"
```

You can also create it via a single command:

- **Linux / macOS / WSL**:
```bash
mkdir -p .streamlit && cat > .streamlit/secrets.toml <<EOL
[data]
data_dirname = "data"
superstore_filename = "Superstore.csv"
geographic_filename = "US.txt"
EOL
```

- **Windows**:
```bash
mkdir .streamlit 2>nul && (
echo [data]> .streamlit\secrets.toml
echo data_dirname = "data">> .streamlit\secrets.toml
echo superstore_filename = "Superstore.csv">> .streamlit\secrets.toml
echo geographic_filename = "US.txt">> .streamlit\secrets.toml
)
```

### 6️⃣ Run the App 🚀
```bash
streamlit run src/in_supermarket/dashboard/app.py
```

Open your browser at the specified port (usually `http://localhost:8501`).

### 7️⃣ Exit the App ❌

Press `Ctrl + C` to stop the Streamlit app.

- Deactivate the virtual environment:
```bash
deactivate
```

---

**✨ Now you’re ready to explore your Superstore BI dashboard locally!**
