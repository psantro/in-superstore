# :bar_chart: Business Intelligence (IN) - Superstore :shopping_cart:

 - [:clipboard: Project Summary](#clipboard-project-summary)
 - [:wrench: **Optional** Installation](#wrench-optional-installation):
   - [:zero: Prerequisites](#zero-prerequisites)
   - [:one: Clone the Repository](#one-clone-the-repository)
   - [:two: Configure `.streamlit/secrets.toml` :key:](#two-configure-streamlitsecretstoml-key)
   - [:three: Create a Virtual Environment and install dependencies](#three-create-a-virtual-environment-and-install-dependencies)
   - [:four:. Run the App :rocket:](#four-run-the-app-rocket)
   - [:five: Exit the App :x:](#five-exit-the-app-x)

### :busts_in_silhouette: Authors:
 - Garrido Massé, Antonio
 - Sánchez Troncoso, Pablo

---

## :clipboard: Project Summary

Welcome to the **Superstore Business Intelligence Project**!  
This project leverages **Python** and **machine learning** to analyze sales trends, forecast performance, and help make **data-driven decisions** for a fictional superstore.

You can try the **live app online** via [Streamlit Cloud](https://in-superstore.streamlit.app/) :rocket:

For a deeper look at our design and development decisions and the insights we uncovered, [**see the full lab report**](lab-report.pdf) :memo:.

---

## :wrench: **Optional** Installation

If you want to edit **run the app locally**, follow these steps. Otherwise, enjoy the deployed version online.

### :zero: Prerequisites

- [Git](https://git-scm.com/)  
- [Python 3.13](https://www.python.org/downloads/)  

---

### :one: Clone the Repository

```bash
git clone https://github.com/psantro/in-superstore.git
cd in-superstore
```

### :two: Configure `.streamlit/secrets.toml` :key:

Create ``.streamlit/secrets.toml`` inside the project folder with the following content:
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


### :three: Create a Virtual Environment and install dependencies

- **Linux / macOS / WSL**:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .

```

- **Windows**:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

### :four:. Run the App :rocket:
```bash
streamlit run src/in_supermarket/dashboard/app.py
```

Open your browser at the specified port (streamlit default is [`http://localhost:8501`](http://localhost:8501)).

### :five: Exit the App :x:

On the cmd, press `Ctrl + C`  to stop the Streamlit app and then deactivate the virtual environment:
```bash
deactivate
```

---

**:sparkles: Now you’re ready to explore your Superstore BI dashboard locally!**
