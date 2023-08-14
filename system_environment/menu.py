from system_environment.get_token import *
from system_environment.get_hobolink_data import *
from system_environment.generate_dataframes import *
from system_environment.paths_and_variables import *

def display_menu():
    print('\n'*150)
    execute = True
    start_date_for_requests_file = open(f'{path_to_specific_information}start_date_for_requests.txt', 'r').readlines()[0]
    end_date_for_requests_file = open(f'{path_to_specific_information}end_date_for_requests.txt', 'r').readlines()[0]
    okay = True
    datef = False
    while okay:
        if datef:
            print('Date format incorrect\n')
            datef = False
        print(welcome)
        start_date_for_requests_file = open(f'{path_to_specific_information}start_date_for_requests.txt', 'r').readlines()[0]
        end_date_for_requests_file = open(f'{path_to_specific_information}end_date_for_requests.txt', 'r').readlines()[0]
        option = input(f'\n{"- "*45}\nInsert the timestamps you wish to gather data in between (can be changed again in the menu)\n\n\tStart\t\t\tEnd\n\t{start_date_for_requests_file}\t{end_date_for_requests_file}\n\n\t[0] Change start timestamp\n\t[1] Change end timestamp\n\t[2] Change end timestamp to current datetime\n\n\t[ENTER] Start options screen\n{"- "*45}\n\n...')
        if option == '':   
            okay = False
            print('\n'*150)
        else:
            if option == "0":
                print('\n'*150)
                new_date = input(f'\n{"- "*45}\nTo insert a specific date and time use YYYY-MM-DD hh:mm:ss\n\nTo insert only a specific date use YYYY-MM-DD\n\nTo change the time use hh:mm:ss\n\n[ENTER] Cancel\n{"- "*45}\n\nNew datetime: ')
                if new_date != '':
                    if len(new_date) == 19:
                        open(f'{path_to_specific_information}start_date_for_requests.txt', 'w').write(new_date)
                    elif len(new_date) == 10:
                        open(f'{path_to_specific_information}start_date_for_requests.txt', 'w').write(f'{new_date} 00:00:00')
                    elif len(new_date) == 8:
                        open(f'{path_to_specific_information}start_date_for_requests.txt', 'w').write(f'{start_date_for_requests_file[0:10]} {new_date}')
                    else:
                        datef = True
                print('\n'*150)   
            elif option == "1":
                print('\n'*150)
                new_date = input(f'\n{"- "*45}\nTo insert a specific date and time use YYYY-MM-DD hh:mm:ss\n\nTo insert only a specific date use YYYY-MM-DD\n\nTo change the time use hh:mm:ss\n\n[ENTER] Cancel\n{"- "*45}\n\nNew datetime: ')
                if new_date != '':
                    if len(new_date) == 19:
                        open(f'{path_to_specific_information}end_date_for_requests.txt', 'w').write(new_date)
                    elif len(new_date) == 10:
                        open(f'{path_to_specific_information}end_date_for_requests.txt', 'w').write(f'{new_date} 00:00:00')
                    elif len(new_date) == 8:
                        open(f'{path_to_specific_information}end_date_for_requests.txt', 'w').write(f'{end_date_for_requests_file[0:10]} {new_date}')
                    else:
                        datef = True
                print('\n'*150)
            elif option == "2":
                open(f'{path_to_specific_information}end_date_for_requests.txt', 'w').write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                print('\n'*150)
                print('End date updated!\n')
    while execute:
        print('\n'*150)
        if open(f'{path_to_specific_information}start_date_for_requests.txt', 'r').readlines()[0] >= open(f'{path_to_specific_information}end_date_for_requests.txt', 'r').readlines()[0]:
            print(f'{warning_art}\n\nThe inserted START TIMESTAMP is GREATER or EQUAL to the END TIMESTAMP.')
            opt = input(f'\n{"- "*45}\nSelect an option to execute\n\n\t[0] Change/view current timestamps for requests\n\n\t[ENTER] Exit\n{"- "*45}\n\n...')
        else:
            print(pc_art)
            opt = input(f'\n{"- "*45}\nSelect an option to execute\n\n\t[0] Change/view current timestamps for requests\n\t[1] Select loggers to gather data from\n\n\t[ENTER] Exit\n{"- "*45}\n\n...')
        print('\n'*150)
        if opt == '0':
            okay = True
            datef = False
            while okay:
                if datef:
                    print('Date format incorrect\n')
                    datef = False
                print(timestamp)
                start_date_for_requests_file = open(f'{path_to_specific_information}start_date_for_requests.txt', 'r').readlines()[0]
                end_date_for_requests_file = open(f'{path_to_specific_information}end_date_for_requests.txt', 'r').readlines()[0]
                option = input(f'\n{"- "*45}\nThe returned data is what is registered between these timestamps.\n\n\tStart\t\t\tEnd\n\t{start_date_for_requests_file}\t{end_date_for_requests_file}\n\n\t[0] Change start timestamp\n\t[1] Change end timestamp\n\t[2] Change end timestamp to current datetime\n\n\t[ENTER] Go back to menu\n{"- "*45}\n\n...')
                if option == '':   
                    okay = False
                    print('\n'*150)
                else:
                    if option == "0":
                        print('\n'*150)
                        new_date = input(f'\n{"- "*45}\nTo insert a specific date and time use YYYY-MM-DD hh:mm:ss\n\nTo insert only a specific date use YYYY-MM-DD\n\nTo change the time use hh:mm:ss\n\n[ENTER] Cancel\n{"- "*45}\n\nNew datetime: ')
                        if new_date != '':
                            if len(new_date) == 19:
                                open(f'{path_to_specific_information}start_date_for_requests.txt', 'w').write(new_date)
                            elif len(new_date) == 10:
                                open(f'{path_to_specific_information}start_date_for_requests.txt', 'w').write(f'{new_date} 00:00:00')
                            elif len(new_date) == 8:
                                open(f'{path_to_specific_information}start_date_for_requests.txt', 'w').write(f'{start_date_for_requests_file[0:10]} {new_date}')
                            else:
                                datef = True
                        print('\n'*150)
                    elif option == "1":
                        print('\n'*150)
                        new_date = input(f'\n{"- "*45}\nTo insert a specific date and time use YYYY-MM-DD hh:mm:ss\n\nTo insert only a specific date use YYYY-MM-DD\n\nTo change the time use hh:mm:ss\n\n[ENTER] Cancel\n{"- "*45}\n\nNew datetime: ')
                        if new_date != '':
                            if len(new_date) == 19:
                                open(f'{path_to_specific_information}end_date_for_requests.txt', 'w').write(new_date)
                            elif len(new_date) == 10:
                                open(f'{path_to_specific_information}end_date_for_requests.txt', 'w').write(f'{new_date} 00:00:00')
                            elif len(new_date) == 8:
                                open(f'{path_to_specific_information}end_date_for_requests.txt', 'w').write(f'{end_date_for_requests_file[0:10]} {new_date}')
                            else:
                                datef = True
                        print('\n'*150)
                    elif option == "2":
                        open(f'{path_to_specific_information}end_date_for_requests.txt', 'w').write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        print('\n'*150)
                        print('End date updated!\n')
       
        elif opt == '1':
            print(mx1102_logger_art)
            print(many_loggers_art)
            selected_loggers = input(f'\n{"- "*45}\nInform the loggers you would like to request data from\n\nNOTICE: the loggers should be comma [,] separated. ex: 1234,5678,9101,0000\n\nThe logger limit per request is 10\n\n[ENTER] Cancel\n{"- "*45}\n\n...')
            okay = True
            if selected_loggers == '':
                print('\n'*150)
            else:
                if len(str(selected_loggers).split(','))>10:
                    okay = False
                    print(f'\n{"- "*45}\n-->\tProblem! The max limit of loggers per request is 10.\n\n{"- "*45}')
                    input('\n\nPress [ENTER] to go back\n\n')
                    print('\n'*150)
                if okay:    
                    print('\n'*150)
                    get_token()
                    generate_dataframes(get_hobolink_data_from_specific_loggers(selected_loggers))
                    input('\n\nPress [ENTER] to reboot menu\n\n')
                    print('\n'*150)
        else:
            execute = False
            print(f'\n\n{end_message}\n\nPublic Version\n\nSoftware fully developed by: Zac Milioli\nContact me at:\tzacmilioli@gmail.com\n\t\thttps://www.linkedin.com/in/zac-milioli\n\n\nPC ASCII Art from https://www.asciiart.eu/\nASCII Art texts from https://fsymbols.com/generators/blocky/\nAll free of copyright\n\n')
