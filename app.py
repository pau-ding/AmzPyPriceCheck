# INSTRUCTIONS - INSTRUCTIONS - INSTRUCTIONS - INSTRUCTIONS - INSTRUCTIONS - INSTRUCTIONS - INSTRUCTIONS - INSTRUCTIONS - INSTRUCTIONS - INSTRUCTIONS - INSTRUCTIONS
#
#
# Use case is basically `python ./your_file.py https://amazonurl`, should output the price on that url.
#
# 1) Implement command line python script/module that takes an Amazon product URL or maybe a part number or something convenient to look up (URL will be the easiest)
#
# 2) Use some library (probably requests or urllib) to download the contents of that page
#
# 3) Use `xml.etree` or similar library to properly load the response body (i.e. don't just write a regex or process the string representation)
#
# 4) Use xpath or similar to find the 'price' of the item on the url.
#
# 5) Return that price on standard out.
#
# When done, please put it in a project in GitHub/GitLab and share it or share it via email.
#
#
# INSTRUCTIONS - INSTRUCTIONS - INSTRUCTIONS - INSTRUCTIONS - INSTRUCTIONS - INSTRUCTIONS - INSTRUCTIONS - INSTRUCTIONS - INSTRUCTIONS - INSTRUCTIONS - INSTRUCTIONS




# Create Clear Space on run
i = 0
while i < 144:
    print(' ')
    i = i + 1




### INDEX ############################################################################################################################################################
##
#
# A0A - System Imports - These are the native tools we'll need to make the magic happen
#
# A1A - Dependency Check - If you don't have a required dependency, let's go ahead and get it.  For the rest of the magic.
#
# A2A - CLI URL Setting - Assign first command line argument to URL and force string
#
# A3A - Header - Set a header to avoid being flagged as a bot and rejected
#
# A4A - Request, Response and Status - Let's try our request, then we'll check to make sure it's a live page and return what we find
#
# A5A - Return Response - Filter data and format result to be returned to command line
#
##
######################################################################################################################################################################



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# A0A - SYSTEM IMPORTS ------------------------------------------------------------------------------------------------------------------------------------------------
# These are the native libraries we'll need to make the magic happen

import subprocess
import sys




# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# A1A - DEPENDENCY CHECK ----------------------------------------------------------------------------------------------------------------------------------------------
# If you don't have a required dependency, let's go ahead and get it

try:
    from bs4 import BeautifulSoup as bsoup
except ImportError:
    subprocess.check_call(["pip", "install", "beautifulsoup4"])
finally:
    from bs4 import BeautifulSoup as bsoup

try:
    import requests
except ImportError:
    subprocess.check_call(["pip", "install", 'requests'])
finally:
    import requests

try:
    import lxml
except ImportError:
    subprocess.check_call(["pip", "install", 'lxml'])
finally:
    import lxml




# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# A2A - CLI URL SETTING -----------------------------------------------------------------------------------------------------------------------------------------------
# Assign First Command Line Argument to URL and force string

cliURL = sys.argv[1]
url = str(cliURL)




# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# A3A - HEADER --------------------------------------------------------------------------------------------------------------------------------------------------------
# Add header to avoid bot detection, Amazon is rather sensetive about that

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}




# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# A4A - REQUEST, RESPONSE & STATUS ------------------------------------------------------------------------------------------------------------------------------------
# Try the request, then check to make sure it's a live page and return what we find; 

# Setting a switch
price  = 0

try:
    request = requests.get(url, headers=headers)
    if request.status_code == 200:
        soup = bsoup(request.content, "lxml")
        price = soup.find(id='priceblock_ourprice').getText()
    else:
        print('Couldn\'t find page, please check your url and try again...')
        print('ex: https://www.amazon.com/some-product-url ')
        print('You sent: ' + url ) 
except:
    print('Please enter a valid Amazon product URL ...') 
    print('ex: python a-price-peek.py "https://www.amazon.com/some-product-url" ')
    print('You sent: ' + url) 



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# A5A - RETURN RESPONSE -----------------------------------------------------------------------------------------------------------------------------------------------
# Return our final result

if price:
    print(price)

