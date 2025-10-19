import os
import django

# Setup Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import Profile, Education, Certification, Experience, Project, Skill

# Clear existing data
Profile.objects.all().delete()
Education.objects.all().delete()
Certification.objects.all().delete()
Experience.objects.all().delete()
Project.objects.all().delete()
Skill.objects.all().delete()

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
    summary="Experienced cybersecurity professional with expertise in penetration testing, vulnerability assessment, and security operations. Skilled in identifying and mitigating security risks across various platforms and environments."
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

Certification.objects.create(
    name="OSCP (Offensive Security Certified Professional)",
    issuer="Offensive Security",
    date="Month Year",
    icon="code"
)

# Create Experience
Experience.objects.create(
    title="Security Analyst",
    company="Company Name",
    location="City, Country",
    start_date="Month Year",
    end_date="Present",
    description="""Performed security assessments and vulnerability testing across enterprise infrastructure.

Developed and implemented security policies and procedures following industry best practices.

Collaborated with development teams to identify and remediate security vulnerabilities in applications.

Monitored security events and responded to incidents using SIEM tools.""",
    order=1
)

Experience.objects.create(
    title="Penetration Tester",
    company="Company Name",
    location="City, Country",
    start_date="Month Year",
    end_date="Month Year",
    description="""Conducted penetration testing engagements for clients across various industries.

Identified and exploited security vulnerabilities in web applications, networks, and systems.

Provided detailed reports with remediation recommendations.

Performed social engineering assessments and security awareness training.""",
    order=2
)

# Create Projects
Project.objects.create(
    title="Web Application Security Testing Framework",
    description="Developed an automated security testing framework for web applications that identifies common vulnerabilities including SQL injection, XSS, and CSRF. Integrated with CI/CD pipelines for continuous security testing.",
    technologies="Python, Burp Suite API, OWASP ZAP, Jenkins, Docker",
    featured=True,
    order=1
)

Project.objects.create(
    title="Network Security Monitoring Solution",
    description="Implemented a comprehensive network monitoring solution using open-source tools to detect and alert on suspicious activities. Configured custom detection rules and automated incident response workflows.",
    technologies="Suricata, ELK Stack, Zeek, Python, Ansible",
    featured=True,
    order=2
)

Project.objects.create(
    title="Cloud Security Assessment Tool",
    description="Created an automated tool to assess cloud infrastructure security posture across AWS, Azure, and GCP. Identifies misconfigurations and generates compliance reports against CIS benchmarks.",
    technologies="Python, Boto3, Azure SDK, GCP API, Terraform",
    featured=True,
    order=3
)

# Create Skills - Security Testing
security_skills = [
    ("Nmap", 90), ("Nessus", 85), ("Burp Suite", 92), ("Metasploit", 88),
    ("Wireshark", 90), ("Hydra", 85), ("SQLmap", 87), ("Nikto", 80),
    ("Hashcat", 82), ("John the Ripper", 80)
]
for skill_name, proficiency in security_skills:
    Skill.objects.create(category='security', name=skill_name, proficiency=proficiency, icon='terminal')

# Programming
programming_skills = [
    ("Python", 95), ("Bash/Shell Scripting", 90), ("SQL", 88),
    ("JavaScript", 75), ("PowerShell", 80), ("Go", 70)
]
for skill_name, proficiency in programming_skills:
    Skill.objects.create(category='programming', name=skill_name, proficiency=proficiency, icon='code')

# Cloud & Infrastructure
cloud_skills = [
    ("AWS", 88), ("Azure", 82), ("Docker", 85),
    ("Kubernetes", 78), ("Terraform", 80), ("Ansible", 82)
]
for skill_name, proficiency in cloud_skills:
    Skill.objects.create(category='cloud', name=skill_name, proficiency=proficiency, icon='cloud')

# SIEM & Monitoring
siem_skills = [
    ("Splunk", 85), ("ELK Stack", 88), ("QRadar", 75),
    ("Log Analysis", 90), ("Incident Response", 88), ("Threat Hunting", 85)
]
for skill_name, proficiency in siem_skills:
    Skill.objects.create(category='siem', name=skill_name, proficiency=proficiency, icon='chart-line')

# Security Frameworks
framework_skills = [
    ("OWASP Top 10", 95), ("NIST CSF", 85), ("ISO 27001", 80),
    ("CIS Controls", 88), ("MITRE ATT&CK", 90), ("PCI-DSS", 75)
]
for skill_name, proficiency in framework_skills:
    Skill.objects.create(category='frameworks', name=skill_name, proficiency=proficiency, icon='book')

# Operating Systems
os_skills = [
    ("Kali Linux", 95), ("Ubuntu", 90), ("CentOS/RHEL", 85),
    ("Windows Server", 82), ("Windows 10/11", 88), ("macOS", 80)
]
for skill_name, proficiency in os_skills:
    Skill.objects.create(category='os', name=skill_name, proficiency=proficiency, icon='desktop')

print("✅ Profile data populated successfully!")
print(f"Created: {Profile.objects.count()} Profile")
print(f"Created: {Education.objects.count()} Education entries")
print(f"Created: {Certification.objects.count()} Certifications")
print(f"Created: {Experience.objects.count()} Experience entries")
print(f"Created: {Project.objects.count()} Projects")
print(f"Created: {Skill.objects.count()} Skills")
