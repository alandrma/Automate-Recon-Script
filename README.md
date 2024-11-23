# Automate Recon Script

## Description
**Domain Recon Script** is a Python-based automation tool designed for domain reconnaissance. It integrates several popular tools such as `subfinder`, `katana`, and `gf` to gather subdomains, crawl URLs, and filter potential vulnerabilities like XSS, SQLi, LFI, AWS key leaks, and subdomain takeovers.

## Features
- Utilizes `subfinder` for subdomain enumeration.
- Leverages `katana` for crawling and collecting URLs from subdomains.
- Integrates `gf` (Gf-Patterns) to identify potential vulnerabilities:
  - **XSS (Cross-Site Scripting)**
  - **SQL Injection**
  - **Local File Inclusion (LFI)**
  - **AWS Key Exposure**
  - **Subdomain Takeover**

## Prerequisites
Ensure you have the following tools installed on your system:
1. **Python 3.x** (Mandatory)
2. **subfinder** ([Installation Guide](https://github.com/projectdiscovery/subfinder))
3. **katana** ([Installation Guide](https://github.com/projectdiscovery/katana))
4. **gf** ([Installation Guide](https://github.com/tomnomnom/gf))

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/username/domain-recon-script.git
cd domain-recon-script
```

### 2. Install Python Dependencies
Use `pip` to install the required Python dependencies:
```bash
pip install -r requirements.txt
```

### 3. Install External Tools
You also need to install the following external tools:

- **subfinder**: Install via `go install`:
  ```bash
  go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
  ```
- **katana**: Install via `go install`:
  ```bash
  go install -v github.com/projectdiscovery/katana/cmd/katana@latest
  ```
- **gf**: Install using the `tomnomnom/gf` script:
  ```bash
  go install github.com/tomnomnom/gf@latest
  ```

Don’t forget to import `gf-patterns`:
```bash
git clone https://github.com/1ndianl33t/Gf-Patterns
mv Gf-Patterns/*.json ~/.gf
```

## Usage
1. Make the script executable:
   ```bash
   chmod +x script.py
   ```

2. Run the script with a target domain:
   ```bash
   ./script.py example.com
   ```

The script will:
- Generate a list of subdomains using `subfinder`.
- Crawl and collect URLs from the subdomains using `katana`.
- Filter potential vulnerabilities using `gf` with specific patterns.

## Output Files
The script generates the following output files:
- `example.com_subfinder.txt`: List of subdomains found by `subfinder`.
- `example.com_katana.txt`: URLs crawled by `katana`.
- `gf_xss.txt`: Potential XSS vulnerabilities.
- `gf_sqli.txt`: Potential SQLi vulnerabilities.
- `gf_lfi.txt`: Potential LFI vulnerabilities.
- `gf_aws-keys.txt`: Potential AWS key exposures.
- `gf_takeovers.txt`: Potential subdomain takeovers.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
