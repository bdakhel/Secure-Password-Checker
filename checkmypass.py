import requests
import hashlib
import sys

# Request data from API with first 5 digits of hash
def request_data(five_hash):
    
    url = 'https://api.pwnedpasswords.com/range/' + str(five_hash)
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f'Error requesting: {response.status_code}, check API and try again')
    else:
        return response

# Encode password using SHA-1 hash, convert to hexadecimal and uppercase
def encode(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

# Split hash into first five characters and the rest of the hash
def process_hash(hash):
    return hash[:5], hash[5:]

# Split data at line breaks, then use dictionary to 
def process_response(response):
    split_list = [line.split(':') for line in response.text.splitlines()]
    processed = dict()
    for hash, count in split_list:
        processed[hash] = count
    return processed

# Check if any hashes from response match with password hash; return count
def check_pass(processed, hash):
    for k in processed:
        if k == hash:
            return processed[hash]
    return 0

def main(passwords):
    for password in passwords:
        hash = encode(password)
        hash1, hash2 = process_hash(hash)
        response = request_data(hash1)
        processed = process_response(response)
        print(processed)
        count = check_pass(processed,hash2)
        if count == 0:
            print(f"Your password is secure.\nThere are {count} matches to \'{password}\'.")
        else:
            print(f'Oh no! Your password is not secure.\nThere are {count} matches to \'{password}\'.')
    return

main(sys.argv[1:])

