import requests
import sys

# URL to subnet where API ctf was located #

url = "http://10.3.10.104:3000"

# Endpoints for this secific CTFs different stages #

tokenEndpoint = "/api/token"

verifyEndpoint = "/api/verify"

flagExchangeEndpoint = "/api/flag"



############ token fetch stage ###########################

def get_token ():

    separator ()
    print (f"Fetching token @ {url}{tokenEndpoint}")
    
    try:
        
        response = requests.post(f"{url}{tokenEndpoint}", timeout = 5)

        if response.status_code == 201:
            data =response.json()
            token = data["token"]
            print ("[+] Success :D")
            print ("[+] Status code:", response.status_code)
            print ("[+] Token:", token)
            return token
        else: 
            print (f"[-] Failed to fetch token :(")
            print (f"[-] Status code:", response.status_code)
    
    except: 
        print ("ERROR at token fetch stage.")
        if TimeoutError:
            print ("Request timed out. Possible connection issue.")
        separator ()
        sys.exit(1)


############## token verification stage #######################


def verify_token (token):

    separator ()
    print (f"Atempting verification @ {url}{verifyEndpoint}")

    try:
        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.post(f"{url}{verifyEndpoint}", headers=headers, timeout=5)

        if response.status_code == 200:
            data = response.json()
            status = data["status"]
            key = data["secret"]
            print ("[+] Success :D")
            print (f"[+] Verification status:", status)
            print ("[+] Status code:", response.status_code)
            print (f"[+] Secret key obtained:", key)
            return key

        else: 
            print ("[-] Could not verify token :(")
            print ("[-] Status code:", response.status_code)
    
    except:
        print ("ERROR at token verification stage.")
        separator ()
        sys.exit(1)


################# flag obtaining stage #########################


def get_flag (token, key): 
    
    separator ()
    print (f" Submittiing Token + Key for Flag @ {url}{flagExchangeEndpoint}")

    try: 

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        body = {
            "secret": f"{key}"
        }

        response = requests.post (f"{url}{flagExchangeEndpoint}", headers=headers, json=body, timeout=5)

        if response.status_code == 200:
            data = response.json()
            flag = data["flag"]
            print ("[+] Success :D")
            print ("[+] Status code:", response.status_code)
            print ("[+] Flag obtained:", flag)
            separator ()
        else:
            print ("[-] Could not obtain flag :(")
            print ("[-] Status code:", response.status_code)
            separator ()

        

    except:
        print ("ERROR at flag exchange stage")
        separator ()
        sys.exit(1)


# cosmetics #

def separator ():
    print ()
    print ("--------------------------------------------------")
    print ()

##############

def main ():

    token = get_token ()
    key = verify_token (token)
    get_flag (token, key)


if __name__=="__main__":
   main()
