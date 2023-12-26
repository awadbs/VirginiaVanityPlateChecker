# VirginiaVanityPlateChecker
![Screenshot of example output](/assets/exampleOutputs.png)

[Virginia DMV](https://www.dmv.virginia.gov/dmvnet/plate_purchase/select_plate.asp) allows you to check whether custom vanity plates are available for your vehicle. But it's very slow to check multiple plates, this script automates the process and allows you to check multiple plates at a time!

Just create a txt file ("input.txt") with all the plate names you want to check, and run the script. It will output a file called "output.txt" to show whether those plates are available or not.

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

Now you're ready to run the script.
Edit 'input.txt' and write the plates that you want to check for.

```
python main.py
```
Open output.py to see which ones are available or not.

![Screenshot of website](/assets/website.png)
![Screenshot of website](/assets/ripImissHimEveryday.jpg)

