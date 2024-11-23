#!/usr/bin/env python3
import sys
import subprocess

def run_command(command):
    """Menjalankan perintah shell dan mencetak output error jika ada"""
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error saat menjalankan perintah: {command}")
        print(e)

def main():
    if len(sys.argv) != 2:
        print("Usage: ./script.py domain")
        sys.exit(1)

    domain = sys.argv[1]

    # Menjalankan subfinder
    subfinder_command = f"subfinder -d {domain} -o {domain}_subfinder.txt"
    run_command(subfinder_command)

    # Menjalankan katana
    katana_command = f"katana -list {domain}_subfinder.txt -o {domain}_katana.txt"
    run_command(katana_command)

    # Menjalankan gf dengan filter xss
    gf_xss_command = f"cat {domain}_katana.txt | gf xss > gf_xss.txt"
    run_command(gf_xss_command)

    # Menjalankan gf dengan filter sqli dan xss
    gf_sqli_command = f"cat {domain}_katana.txt | gf sqli xss > gf_sqli.txt"
    run_command(gf_sqli_command)

    # Menjalankan gf dengan filter lfi dan xss
    gf_lfi_command = f"cat {domain}_katana.txt | gf lfi xss > gf_lfi.txt"
    run_command(gf_lfi_command)

    # Menjalankan gf dengan filter aws-keys dan xss
    gf_aws_keys_command = f"cat {domain}_katana.txt | gf aws-keys xss > gf_aws-keys.txt"
    run_command(gf_aws_keys_command)

    # Menjalankan gf dengan filter takeovers dan xss
    gf_takeovers_command = f"cat {domain}_katana.txt | gf takeovers xss > gf_takeovers.txt"
    run_command(gf_takeovers_command)

    print(f"Proses selesai untuk domain: {domain}")

if __name__ == "__main__":
    main()
