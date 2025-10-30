import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import schedule
import time

receiver_email = "your eamil" # enter your email
sender = "your email"    # enter your email
password = "your App password"  # Your Gmail App Password

def generate_pdf():
    class PDF(FPDF):
        def header(self):
            self.set_font("Arial", "B", 14)
            self.cell(0, 10, "Daily Job Digest", 0, 1, "C")
            self.set_font("Arial", "", 10)
            self.cell(0, 10, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0, 1, "C")
            self.ln(5)

        def chapter_title(self, title):
            self.set_font("Arial", "B", 12)
            self.cell(0, 10, title, 0, 1, "L")
            self.ln(2)

        def chapter_body(self, jobs):
            self.set_font("Arial", "", 11)
            for company, url in jobs:
                self.multi_cell(0, 8, f"{company}: {url}")
            self.ln(5)

    jobs = {
        "Entry-Level Data Analyst": [
            ("Google", "https://careers.google.com/jobs/results/data-analyst/"),
            ("LinkedIn", "https://www.linkedin.com/jobs/view/1234567890/")
        ],
        "Front-End Developer": [
            ("Facebook", "https://www.facebook.com/careers/jobs/frontend-developer/"),
            ("Naukri", "https://www.naukri.com/front-end-developer-jobs")
        ],
        "Full Stack Developer": [
            ("Amazon", "https://www.amazon.jobs/en/jobs/full-stack-developer"),
            ("AngelList", "https://angel.co/jobs/full-stack-developer")
        ],
        "Software Developer": [
            ("Microsoft", "https://careers.microsoft.com/software-developer-jobs"),
            ("Indeed", "https://www.indeed.com/q-software-developer-jobs.html")
        ]
    }

    pdf = PDF()
    pdf.add_page()
    for role, data in jobs.items():
        pdf.chapter_title(role)
        pdf.chapter_body(data)
    filename = "daily_job_digest.pdf"
    pdf.output(filename)
    print("✅ PDF generated.")
    return filename

def send_email(pdf_filename):
    try:
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = receiver_email
        msg["Subject"] = "Daily Job Digest"

        msg.attach(MIMEText("Find attached today's job search results.", "plain"))

        with open(pdf_filename, "rb") as f:
            attach = MIMEApplication(f.read(), _subtype="pdf")
            attach.add_header("Content-Disposition", "attachment", filename=pdf_filename)
            msg.attach(attach)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(msg)

        print("✅ Email sent successfully.")
    except Exception as e:
        print("❌ Failed to send email:", str(e))

def main_task():
    print("⏰ Running job at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    pdf = generate_pdf()
    send_email(pdf)

# TEMP: Run every 1 minute for testing
schedule.every(1).minutes.do(main_task)

print("🚀 Script started. Waiting for scheduled task every 1 minute...\n")
while True:
    schedule.run_pending()
    time.sleep(1)
