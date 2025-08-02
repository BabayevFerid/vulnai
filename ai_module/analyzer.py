import random

def analyze_services(xml_output):
    # Bu hissəni XML'dən JSON parsinqə bağlayacağıq
    return {
        "vulnerabilities": [
            {"service": "ssh", "risk": "high", "cve": "CVE-2020-15778"},
            {"service": "http", "risk": "medium", "cve": "CVE-2021-41773"}
        ],
        "summary": "System has potential remote code execution on SSH service."
    }
