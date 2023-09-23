![AYOT LOGO](https://github.com/Chawki-BS/AYOT/assets/86046707/78af343b-294d-4fa1-9cc0-31fc3fef7757)
# AYOT
AYOT is a Python-based command-line tool for analyzing web pages and performing various operations such as port scanning, domain lookup, and form analysis. This tool uses the following libraries:
- 'requests' for making HTTP requests
- 'lxml' for parsing HTML and XML documents
- 'Wappalyzer' for identifying web technologies used by a site
- 'whois' for looking up domain registration information
- 'nmap3' for performing port scans
## Installation
You can clone the repository to your local machine using the following command:
```
git clone https://github.com/Chawki-BS/AYOT.git
```
To install the dependencies, run the following command:
```
pip install -r requirements.txt
```
![1](https://github.com/Chawki-BS/AYOT/assets/86046707/18c23ee8-4e2a-420f-a1ba-7137aca9ab8e)
To run the script, simply execute the main.py file using the following command:
```
python main.py --help
```
```
python main.py <command> <arguments>
```
Replace <command> with one of the available commands (analyze, is_form, domain_lookup, port_scan) and replace <arguments> with any necessary command-line arguments.
## Usage
To use this project, run the main.py file with one of the available commands:
### Analyze 
Analyze a web page and display information about the web framework and versions:
```
python main.py analyze <url> [--proxy=<proxy>]
```
### IsForm
Find forms in a web page and print information about each form's input fields:
```
python main.py is_form <url> [--proxy=<proxy>]
```
Replace <url> with the URL of the web page you want to analyze, and optionally specify a proxy using the --proxy argument.
### DomainLookup
![3](https://github.com/Chawki-BS/AYOT/assets/86046707/eb8ec294-af67-41c2-a8da-e8afe305eb63)
Perform a WHOIS lookup on a domain and print information about the domain registrant:
```
python main.py domain_lookup <name>
```
Replace <name> with the domain name you want to look up.
### PortScan
Perform a port scan on a target IP address or hostname and print information about each open or closed port:
```
python main.py port_scan <target> [--top=<number>]
```
Replace <target> with the IP address or hostname of the target you want to scan, and optionally specify the number of top ports to scan using the --top argument (default is 10).
## Features 
- Analyze web pages and display framework and versions.
- Find a form in a page and print form details.
- Print the domain registrant's name and organization.
- Perform a port scan against a target and print the open ports and services.
## Contributing
Contributions to this project are welcome! To contribute, please create a pull request with your changes. If you encounter any issues or have any suggestions for new features, please create an issue in the GitHub repository.
## Work in Progress
This tool is actively under development, and new features and improvements are being added regularly. Some of the planned features include:
- Find hidden files and directorries.
- Gobuster integration.
- Bruteforce HTML forms.
- BurpSuite extension to extract JavaScript include references.
## License
This project is licensed under the MIT License.
## Acknowledgments
This project uses several external libraries, including 'typer', 'whois', 'nmap3', 'requests', 'lxml', and 'Wappalyzer'. Thank you to the developers of these libraries for their contributions to the open source community.
