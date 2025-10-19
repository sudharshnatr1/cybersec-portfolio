import os
import django

# Setup Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import Profile, Education, Certification, Experience, Project, Skill
from django.contrib.auth import get_user_model

# Check if we should use personal data (for production)
USE_PERSONAL_DATA = os.environ.get('USE_PERSONAL_DATA', 'false').lower() == 'true'

# Clear existing data
Profile.objects.all().delete()
Education.objects.all().delete()
Certification.objects.all().delete()
Experience.objects.all().delete()
Project.objects.all().delete()
Skill.objects.all().delete()

if USE_PERSONAL_DATA:
    print("Using PERSONAL data from environment variables...")
    
    # Create Profile from environment variables
    profile = Profile.objects.create(
        name=os.environ.get('PORTFOLIO_NAME', 'Your Name'),
        title=os.environ.get('PORTFOLIO_TITLE', 'Cybersecurity Professional'),
        email=os.environ.get('PORTFOLIO_EMAIL', 'email@example.com'),
        phone=os.environ.get('PORTFOLIO_PHONE', '+1-234-567-8900'),
        linkedin=os.environ.get('PORTFOLIO_LINKEDIN', 'https://linkedin.com/in/profile'),
        github=os.environ.get('PORTFOLIO_GITHUB', 'https://github.com/username'),
        tryhackme=os.environ.get('PORTFOLIO_TRYHACKME', 'https://tryhackme.com/p/username'),
        tryhackme_user_id=os.environ.get('PORTFOLIO_THM_ID', '000000'),
        summary=os.environ.get('PORTFOLIO_SUMMARY', 'Professional summary here')
    )
    
    # Create Education
    Education.objects.create(
        degree="Master of Science in Cybersecurity",
        institution="National College of Ireland",
        location="Dublin",
        graduation_date="Aug 2025",
        grade="Second Class Honours (NFQ Level 9)",
        order=1
    )
    
    Education.objects.create(
        degree="Bachelor of Engineering in Electronics and Communication",
        institution="BNMIT, Visvesvaraya Technological University",
        location="Bangalore",
        graduation_date="Jul 2023",
        order=2
    )
    
    # Create Certifications
    Certification.objects.create(
        name="eJPT (eLearnSecurity Junior Penetration Tester)",
        issuer="INE Security",
        date="Oct 2025",
        credential_id="163172499",
        icon="shield-check"
    )
    
    Certification.objects.create(
        name="TryHackMe Top 10%",
        issuer="TryHackMe",
        date="2025",
        credential_id="Rank 181,501 | 53 Rooms | 9 Badges",
        icon="flag"
    )
    
    Certification.objects.create(
        name="Java Full Stack Development",
        issuer="Pentagon Space",
        date="Nov 2023 – May 2024",
        icon="code"
    )
    
    Certification.objects.create(
        name="Institutional Best Project Award",
        issuer="BNMIT",
        date="2023",
        credential_id="Laser-Guided Interactive Music System",
        icon="trophy"
    )
    
    # Create Experience
    Experience.objects.create(
        title="Cybersecurity Intern",
        company="Prinston Smart Engineers",
        location="Bangalore, India",
        start_date="Jul 2023",
        end_date="Jan 2024",
        description="""Conducted vulnerability assessments on 200+ network endpoints using Nmap and Nessus, identifying 45+ critical vulnerabilities with detailed CVSS scoring and exploitation analysis.

Performed penetration testing with Burp Suite and Metasploit, discovering SQL injection vulnerabilities in 8 web applications and XSS flaws in 12 client-side interfaces.

Authored 25+ technical remediation reports following OWASP methodology, contributing to 30% improvement in security posture and achieving ISO 27001 compliance.

Designed automated alerting workflows using Python and webhook integrations, reducing mean time to detect (MTTD) by 20%.""",
        order=1
    )
    
    Experience.objects.create(
        title="Data Science Intern",
        company="Prinston Smart Engineers",
        location="Bangalore, India",
        start_date="Feb 2023",
        end_date="Jul 2023",
        description="""Developed Python-based ML classification models using scikit-learn and TensorFlow for network traffic anomaly detection, achieving 85% accuracy across 50,000+ daily flows.

Optimized model performance through feature engineering and dimensionality reduction, decreasing false positives by 25% while maintaining 92% recall.

Built interactive dashboards using Flask and Plotly for real-time monitoring of 15+ threat indicators, improving incident triage efficiency by 15%.

Processed 2TB+ network logs using pandas and SQL, training supervised learning algorithms to enhance automated threat detection.""",
        order=2
    )
    
    # Create Projects
    Project.objects.create(
        title="Mobile Application Forensic Investigation",
        description="Conducted comprehensive forensic examinations of Android applications (Instagram, Facebook, Twitter), extracting 500+ artifacts from databases to identify data retention practices. Recovered sensitive authentication tokens and session data through advanced SQL queries and hex editing, exposing critical vulnerabilities. Authored a 35-page forensic report with chain of custody documentation and privacy risk assessments.",
        technologies="Android Forensics, SQL, SQLite, Hex Editing, Python, Digital Forensics",
        featured=True,
        order=1
    )
    
    Project.objects.create(
        title="Hardened WordPress Infrastructure on AWS Cloud",
        description="Architected security-hardened WordPress environment on AWS EC2 with SSL/TLS encryption, WAF rules, and least-privilege IAM policies protecting against OWASP Top 10. Configured monitoring with AWS CloudWatch and DataDog SIEM, establishing 50+ custom alerts and achieving 99.9% uptime over 6 months. Automated compliance monitoring using CIS Benchmark controls and AWS Config, reducing misconfigurations by 40%.",
        technologies="AWS EC2, S3, CloudWatch, IAM, WordPress, SSL/TLS, WAF, DataDog, CIS Benchmarks",
        featured=True,
        order=2
    )
    
    Project.objects.create(
        title="USB Rubber Ducky Security Analysis",
        description="Engineered Arduino-based USB HID emulation to analyze BadUSB attack vectors, testing 12+ exploitation techniques including keystroke injection and credential harvesting. Evaluated 5 EDR solutions, documenting evasion techniques and developing countermeasures that improved USB device detection by 85%. Created security awareness training materials educating 30+ team members on USB-based attack prevention.",
        technologies="Arduino, USB HID, BadUSB, EDR Solutions, Security Testing, Python",
        featured=True,
        order=3
    )
    
    # Create Skills - Security Testing
    security_skills = [
        ("Nmap", 95), ("Nessus", 90), ("Burp Suite", 92), ("Metasploit", 88),
        ("Wireshark", 90), ("Hydra", 85), ("SQLmap", 87), ("Nikto", 82),
        ("Hashcat", 80), ("John the Ripper", 80)
    ]
    for skill_name, proficiency in security_skills:
        Skill.objects.create(category='security', name=skill_name, proficiency=proficiency, icon='terminal')
    
    # Programming
    programming_skills = [
        ("Python", 95), ("Bash/Shell Scripting", 88), ("SQL", 90),
        ("Java", 75), ("pandas", 92), ("scikit-learn", 85),
        ("TensorFlow", 80), ("Flask", 82)
    ]
    for skill_name, proficiency in programming_skills:
        Skill.objects.create(category='programming', name=skill_name, proficiency=proficiency, icon='code')
    
    # Cloud & Infrastructure
    cloud_skills = [
        ("AWS EC2", 88), ("AWS S3", 85), ("AWS CloudWatch", 87),
        ("AWS IAM", 90), ("AWS VPC", 82), ("Docker", 80),
        ("Terraform", 75), ("WordPress Administration", 85)
    ]
    for skill_name, proficiency in cloud_skills:
        Skill.objects.create(category='cloud', name=skill_name, proficiency=proficiency, icon='cloud')
    
    # SIEM & Monitoring
    siem_skills = [
        ("DataDog", 85), ("AWS CloudWatch", 87), ("Splunk", 80),
        ("Log Analysis", 90), ("Incident Response", 88), ("Threat Hunting", 85)
    ]
    for skill_name, proficiency in siem_skills:
        Skill.objects.create(category='siem', name=skill_name, proficiency=proficiency, icon='chart-line')
    
    # Security Frameworks
    framework_skills = [
        ("ISO 27001", 85), ("NIST Cybersecurity Framework", 88), ("GDPR", 82),
        ("CIS Controls", 90), ("OWASP Top 10", 95), ("MITRE ATT&CK", 87)
    ]
    for skill_name, proficiency in framework_skills:
        Skill.objects.create(category='frameworks', name=skill_name, proficiency=proficiency, icon='book')
    
    # Operating Systems
    os_skills = [
        ("Kali Linux", 95), ("Ubuntu Server", 90), ("Ubuntu Desktop", 92),
        ("Windows Server 2019/2022", 85), ("Windows 10/11", 88), ("Raspberry Pi OS", 80)
    ]
    for skill_name, proficiency in os_skills:
        Skill.objects.create(category='os', name=skill_name, proficiency=proficiency, icon='desktop')
    
    # Create personal superuser
    User = get_user_model()
    admin_username = os.environ.get('ADMIN_USERNAME', 'admin')
    admin_email = os.environ.get('ADMIN_EMAIL', 'admin@example.com')
    admin_password = os.environ.get('ADMIN_PASSWORD', 'admin')
    
    if not User.objects.filter(username=admin_username).exists():
        User.objects.create_superuser(
            username=admin_username,
            email=admin_email,
            password=admin_password
        )
        print(f"Personal superuser '{admin_username}' created!")
    
    print("Personal data populated successfully!")
    
else:
    print("Using GENERIC data...")
    
    # Create Profile
    profile = Profile.objects.create(
        name="Your Name",
        title="Cybersecurity Professional | Penetration Tester",
        email="your.email@example.com",
        phone="+1-234-567-8900",
        linkedin="https://www.linkedin.com/in/yourprofile/",
        github="https://github.com/yourusername",
        tryhackme="https://tryhackme.com/p/yourusername",
        tryhackme_user_id="000000",
        summary="Experienced cybersecurity professional with expertise in penetration testing, vulnerability assessment, and security operations."
    )
    
    # Create Education
    Education.objects.create(
        degree="Master of Science in Cybersecurity",
        institution="University Name",
        location="City, Country",
        graduation_date="Month Year",
        grade="Grade/GPA",
        order=1
    )
    
    Education.objects.create(
        degree="Bachelor of Science in Computer Science",
        institution="University Name",
        location="City, Country",
        graduation_date="Month Year",
        order=2
    )
    
    # Create Certifications
    Certification.objects.create(
        name="Certified Ethical Hacker (CEH)",
        issuer="EC-Council",
        date="Month Year",
        credential_id="XXXXXX",
        icon="shield-check"
    )
    
    Certification.objects.create(
        name="CompTIA Security+",
        issuer="CompTIA",
        date="Month Year",
        credential_id="XXXXXX",
        icon="flag"
    )
    
    # Create Experience
    Experience.objects.create(
        title="Security Analyst",
        company="Company Name",
        location="City, Country",
        start_date="Month Year",
        end_date="Present",
        description="Performed security assessments and vulnerability testing.",
        order=1
    )
    
    # Create Projects
    Project.objects.create(
        title="Web Application Security Testing Framework",
        description="Developed an automated security testing framework.",
        technologies="Python, Burp Suite API, OWASP ZAP",
        featured=True,
        order=1
    )
    
    # Create Skills
    security_skills = [
        ("Nmap", 90), ("Burp Suite", 92), ("Metasploit", 88)
    ]
    for skill_name, proficiency in security_skills:
        Skill.objects.create(category='security', name=skill_name, proficiency=proficiency, icon='terminal')
    
    programming_skills = [
        ("Python", 95), ("Bash", 90), ("SQL", 88)
    ]
    for skill_name, proficiency in programming_skills:
        Skill.objects.create(category='programming', name=skill_name, proficiency=proficiency, icon='code')
    
    print("Generic data populated successfully!")

print(f"Created: {Profile.objects.count()} Profile")
print(f"Created: {Education.objects.count()} Education entries")
print(f"Created: {Certification.objects.count()} Certifications")
print(f"Created: {Experience.objects.count()} Experience entries")
print(f"Created: {Project.objects.count()} Projects")
print(f"Created: {Skill.objects.count()} Skills")
