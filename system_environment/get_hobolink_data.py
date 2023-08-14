from system_environment.paths_and_variables import *
import requests


def get_hobolink_data_from_specific_loggers(selected_loggers):
    start_date_for_requests_file = open(f'{path_to_specific_information}start_date_for_requests.txt', 'r').readlines()[0]
    end_date_for_requests_file = open(f'{path_to_specific_information}end_date_for_requests.txt', 'r').readlines()[0]
    data_params_specific_loggers = {'loggers': selected_loggers, 'start_date_time': start_date_for_requests_file, 'end_date_time': end_date_for_requests_file}
    token = open(f'{path_to_specific_information}token.txt', 'r').readlines()[0]
    get_hobolink_data_headers = {"authorization": f'Bearer {token}'}
    body = requests.get(get_hobolink_data_path, params=data_params_specific_loggers, headers=get_hobolink_data_headers)
    
    if body.status_code != 200:
        print(f'{"- "*45}\n\nERROR: status code was {body.status_code}, not 200.\nThis might have been caused by incorrect format of timestamps, verify them.\nElse, try executing the software again.\nIf problem persists, contact the owner.\n\nResponsible Developer and Architect:\tZac Milioli\n\t\t\t\t\tzacmilioli@gmail.com\n\t\t\t\t\t55(47)9 9772-8275\n\t\t\t\t\thttps://www.linkedin.com/in/zac-milioli\n{"- "*45}\n')
        return 0
    
    print(f'\n-->\tHOBOlink data returned! Status code [{body.status_code}]\n')
    print('- '*45)
    return body.json()
