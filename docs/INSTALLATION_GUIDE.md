# 6️⃣ INSTALLATION GUIDE

## Prerequisites
- Python 3.10 or higher
- Node.js 18 or higher (for the dashboard)
- Git

## 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Stock-Market-Data-Analyzer.git
cd Stock-Market-Data-Analyzer
```

## 2. Python Backend Setup

### Create a Virtual Environment
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Seed the Database with Sample Data
This script creates the database and fetches recent stock data for analysis.
```bash
python src/seed.py
```

## 3. Next.js Frontend Setup
```bash
cd apps/web
npm install
```

You are now ready to run the project locally! See the `HOW_TO_RUN.md` file for next steps.
