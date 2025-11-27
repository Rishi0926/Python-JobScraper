📄 Job Scraper – README

This project automatically generates a Daily Job Digest PDF and emails it to a specified inbox using Gmail App Password authentication.

🚀 Features

Scrapes or collects job links (static in current version)

Generates a clean PDF digest using FPDF

Sends the PDF as an email attachment

Uses Gmail App Password (safe method; avoids normal password usage)

Runs once per execution
🛠️ Prerequisites

Install required Python libraries:

pip install requests beautifulsoup4 fpdf

✉️ Setting Up Gmail App Password

Since Google no longer allows “less secure apps,” you MUST use a Gmail App Password.

🧩 STEP 1: Enable 2-Step Verification

Go to 👉 https://myaccount.google.com/security

Turn ON 2-Step Verification

Complete the setup (phone OTP)

🔐 STEP 2: Create an App Password

Open: https://myaccount.google.com/apppasswords

Login if needed

Under Select App, choose:
➝ Mail

Under Select Device, choose:
➝ Other (Custom name) → type: Python Script

Google generates a 16-character app password, like:

abcd efgh ijkl mnop


Copy it — you will use it in the script.

📥 STEP 3: Add It to Your Script

Replace:

sender = "your email"
password = "your App password"
receiver_email = "your email"


Example:

sender = "myemail@gmail.com"
password = "abcd efgh ijkl mnop"
receiver_email = "myemail@gmail.com"


❗ Important:
Never share this password publicly.
If leaked, revoke it instantly from the App Passwords page.

▶️ Running the Script

Once your Gmail setup is done, simply run:

python script.py


You will see:

🚀 Script started...
⏰ Running job at: 2025-11-27 15:30:10
✅ PDF generated.
✅ Email sent successfully.
