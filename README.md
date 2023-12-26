# VirginiaVanityPlateChecker
![Screenshot of example output](/assets/exampleOutputs.png)

[Virginia DMV](https://www.dmv.virginia.gov/dmvnet/plate_purchase/select_plate.asp) allows you to check for custom vanity plate for your vehicle. But their website is very slow to check multiple plates, this script automates the process and allows you to check multiple plates at a time!

## Getting Started

Dependencies:
* Python 3.9.10 
    * [Requests](https://pypi.org/project/requests/)
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) 
* [tqdm](https://pypi.org/project/tqdm/)

Run the following commands to install the dependencies
```
python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
```

Edit 'input.txt' and write the custom plates that you want to check for.
Now run the script:

```
python main.py
```
Output.py will display which plates are available or not.

![Screenshot of website](/assets/website.png)
![Screenshot of website](/assets/ripImissHimEveryday.jpg)

