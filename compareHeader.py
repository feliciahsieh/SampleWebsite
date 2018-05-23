#!/usr/bin/python3
""" compareHeader.py """
if __name__ == "__main__":
    """ __main__ """
    import requests
    import sys

    # Accept 2 URLS from command line
    # Format: python3 compareHeader.py [URL1] [URL2]
    # Example: python3 compareHeader.py http://198.41.215.162 http://www.cloudflare.com
    if len(sys.argv) == 3:
        try:
            rG = requests.get(sys.argv[1])
            print("URL1: {}".format(sys.argv[1]))
            # Print Header options of URL1
            for kG, vG in rG.headers.items():
                print("{}: {}".format(kG, vG))
        except:
            sys.exit(0)

        try:
            rC = requests.get(sys.argv[2])
            print("\nURL2: {}".format(sys.argv[2]))
            # Print Header options of URL2
            for kC, vC in rC.headers.items():
                print("{}: {}".format(kC, vC))
        except:
            sys.exit(0)
    else:
        print("Please enter 2 URLs")
