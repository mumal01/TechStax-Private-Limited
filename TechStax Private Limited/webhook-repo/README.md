# 📬 Webhook Receiver – Dev Assessment

This repository is part of the **Developer Assessment** task to build a Flask-based webhook receiver that listens to GitHub events (`push`, `pull_request`, and optionally `merge`), stores the relevant information into **MongoDB**, and displays them via a UI that polls every 15 seconds.

---

## ⚙️ Setup Instructions

Follow these steps to set up the Flask app with MongoDB integration:

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/your-username/webhook-repo.git
cd webhook-repo






# Create virtual environment
pip install virtualenv
virtualenv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate



pip install -r requirements.txt



python run.py



gunicorn run:app
