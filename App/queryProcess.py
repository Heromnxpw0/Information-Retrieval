from spellchecker import SpellChecker
# from abbreviations_py.textes.abbreviator import fix


abbreviations_dict = {
    "AI": "Artificial Intelligence",
    "ML": "Machine Learning",
    "API": "Application Programming Interface",
    "URL": "Uniform Resource Locator",
    "HTTP": "Hypertext Transfer Protocol",
    "HTML": "Hypertext Markup Language",
    "CSS": "Cascading Style Sheets",
    "JS": "JavaScript",
    "SQL": "Structured Query Language",
    "TCP": "Transmission Control Protocol",
    "UDP": "User Datagram Protocol",
    "RAM": "Random Access Memory",
    "ROM": "Read-Only Memory",
    "BIOS": "Basic Input/Output System",
    "GPU": "Graphics Processing Unit",
    "CPU": "Central Processing Unit",
    "SSD": "Solid State Drive",
    "HDD": "Hard Disk Drive",
    "VPN": "Virtual Private Network",
    "IoT": "Internet of Things",
    "NLP": "Natural Language Processing",
    "OCR": "Optical Character Recognition",
    "RPA": "Robotic Process Automation",
    "SaaS": "Software as a Service",
    "PaaS": "Platform as a Service",
    "IaaS": "Infrastructure as a Service",
    "DL": "Deep Learning",
    "RL": "Reinforcement Learning",
    "KNN": "K-Nearest Neighbors",
    "DDoS": "Distributed Denial of Service",
    "IDS": "Intrusion Detection System",
    "IPS": "Intrusion Prevention System",
    "SIEM": "Security Information and Event Management",
    "MFA": "Multi-Factor Authentication",
    "TLS": "Transport Layer Security",
    "SSL": "Secure Sockets Layer",
    "PKI": "Public Key Infrastructure",
    "AES": "Advanced Encryption Standard",
    "RSA": "Rivest–Shamir–Adleman",
    "XSS": "Cross-Site Scripting",
    "CSRF": "Cross-Site Request Forgery",
    "APT": "Advanced Persistent Threat",
    "FIM": "File Integrity Monitoring",
    "RAT": "Remote Access Trojan",
    "CSP": "Content Security Policy",
    "EFS": "Encrypting File System",
    "TTP": "Tactics, Techniques, and Procedures",
    "MITM": "Man in the Middle",
    "SOC": "Security Operations Center",
    "HIPS": "Host Intrusion Prevention System",
    "WAF": "Web Application Firewall",
    "DLP": "Data Loss Prevention",
    "BAS": "Bug Bounty Program",
    "VLAN": "Virtual Local Area Network",
    "B2B": "Business to Business",
    "B2C": "Business to Consumer"
}


def fix_spelling(query):
    checker = SpellChecker()
    fixed_query = " ".join([checker.correction(word) for word in query.split()])
    return fixed_query, fixed_query != query

def fix_abbreviations(query):
    new_query = ""
    for word in query.split():
        if word.upper() in abbreviations_dict:
            new_query += abbreviations_dict[word.upper()].lower() + " "
        else:
            new_query += word + " "
    return new_query, new_query != query

def process_query(query):
    query = query.lower().strip()
    query, misspell = fix_spelling(query)
    abrv_query, abbrev = fix_abbreviations(query)
    return query, abrv_query, misspell, abbrev
    