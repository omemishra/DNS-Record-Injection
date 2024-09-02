# **DNS Record Injection Tool**
**DNS Server Dynamic Update Record Injection**

## **Overview**

The DNS Record Injection Tool is a Python script designed to exploit DNS servers that are vulnerable to dynamic update record injection. This tool allows users to inject unauthorized A records into a target DNS server, potentially redirecting traffic to a specified IP address. It can be a valuable asset for penetration testers, security researchers, and network administrators to assess and demonstrate the risks associated with insecure DNS configurations.

## **Features**

- **Automated Record Injection**: Easily inject A records into vulnerable DNS servers.
- **TCP Communication**: Utilizes TCP to communicate with the DNS server for record injection, ensuring reliable transmission.
- **Error Handling**: Provides detailed error messages to assist in troubleshooting and analysis.
- **User-Friendly Input**: Prompts for necessary details like the target DNS IP, domain name, and desired A record IP.

## **Usage**

### **Prerequisites**

Ensure that you have Python installed and that the `dnspython` library is available. You can install `dnspython` using pip:

```bash
pip install dnspython
```

### **Running the Script**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/omemishra/DNS-Record-Injection.git
   cd DNS-Record-Injection
   ```

2. **Run the Script**:
   Execute the script and provide the required inputs when prompted:
   ```bash
   python DNSinjection.py
   ```

   You will be asked to input the following:
   - **Vulnerable DNS Server IP**: The IP address of the DNS server that is vulnerable to record injection.
   - **Domain Name**: The domain name (e.g., `example.com`) for which you want to inject an A record.
   - **A Record IP**: The IP address that you want to associate with the domain name.

3. **Example Output**:
   If the injection is successful, you will see:
   ```plaintext
   [+] Successfully injected the A record for example.com with IP 1.X.X.X
   ```

   If the injection fails, the script will output the response code or an error message.

## **Code Explanation**

The script works as follows:

1. **Create a DNS Update Object**:
   - The `dns.update.Update` class is used to create an update object for the specified domain.

2. **Add the A Record**:
   - The script uses the `replace` method to add or replace an A record for the domain.

3. **Send the Update**:
   - The update is sent to the target DNS server using `dns.query.tcp`.

4. **Handle Responses**:
   - The script checks the response code to determine whether the injection was successful.

## **Prevention Recommendations**

To mitigate the risks associated with DNS dynamic update record injection:

- **Restrict Dynamic Updates**: Configure DNS servers to accept dynamic updates only from trusted and authorized sources.
- **Implement DNSSEC**: Use DNSSEC (Domain Name System Security Extensions) to protect DNS records from unauthorized modifications.
- **Regular Audits**: Regularly audit DNS server configurations to ensure compliance with security best practices.

## **Disclaimer**

This tool is intended for educational purposes and authorized security testing only. Unauthorized use of this tool against systems you do not own or have explicit permission to test is illegal and unethical.

## **Contributing**

Feel free to contribute to this project by opening an issue or submitting a pull request.
