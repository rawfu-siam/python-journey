pr_title = "feat: integrate email notification pipeline"
pr_body = """
### 🛠️ What this PR does:
- Connects smtplib to our client reporting system.
- Sends automatic logs every Monday morning at 9am.

### 🧪 Manual Testing Instructions:
- Step 1: Run `.\\dev_env\\Scripts\\Activate.ps1` to wake up your environment.
- Step 2: Run `pytest tests/test_alerts.py` to trigger the pipeline tests.
"""

print(f"📬 PULL REQUEST LOGGED:\nTitle: {pr_title}\n{pr_body}")
