from system_environment.paths_and_variables import *
import requests

def get_token():
    body = requests.post(post_generate_token_json_path, data=token_data)
    with open(f'{path_to_specific_information}token.txt', 'w') as token:
        token.write(f'{body.json()["access_token"]}')
        token.close()
    print('- '*45)
    print('\n-->\tToken generated and registered!\n')
    print('- '*45)
