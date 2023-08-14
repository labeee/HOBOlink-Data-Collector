from system_environment.paths_and_variables import *
import pandas as pd
from glob import glob
import os


def generate_dataframes(body_json):
    
    ## Error handler
    if body_json == 0:
        return None
    elif len(body_json['observation_list']) == 0:
        start_date_for_requests_file = open(f'{path_to_specific_information}start_date_for_requests.txt', 'r').readlines()[0]
        end_date_for_requests_file = open(f'{path_to_specific_information}end_date_for_requests.txt', 'r').readlines()[0]
        print(f'\n{"- "*45}\n-->\tEmpty body! The loggers you selected do not have\n\tdata between choosen timestamps.\n\ntimestamps:\n{start_date_for_requests_file} --- {end_date_for_requests_file}\n{"- "*45}')
        return None

    body_json['observation_list'] = [item for item in body_json['observation_list'] if str(item['data_type_id']) == '1']
    for item in body_json['observation_list']:
        item.pop('data_type_id')
        item.pop('us_value')
        item.pop('us_unit')
        item.pop('si_unit')
        item.pop('sensor_key')
        item.pop('scaled_value')
        item.pop('scaled_unit')
        item.pop('sensor_sn')
        item['timestamp'] = item['timestamp'][0:18]
        item['si_value'] = round(item['si_value'], 1)

    print(f'\n-->\tInformation filtered! Total logs after filter: {len(body_json["observation_list"])}\n')
    print('- '*45)
    print('\n-->\tStarting process!\n')
    print('- '*45)
    print('\nWARNING! Do not open or delete the dataframes while software is processing information,\nit will stop the generation mid proccess.\nThis can only be done without a problem while in the menus.\n')
    print('- '*45)

    globed = glob(path_output_df+'*.csv')
    globed = [item.replace('\\', '/') for item in globed]
    new = []
    updated = []

    csv_name = f'{path_output_df}BigDataFrame.csv'
    dataframe_from_json = pd.DataFrame(body_json['observation_list'])
    dataframe_from_json = dataframe_from_json.pivot_table(index=['logger_sn', 'timestamp'], columns='sensor_measurement_type', values='si_value').reset_index()
    if csv_name not in globed:
        dataframe_from_json.to_csv(csv_name, sep=";", index=False, na_rep=None)
        globed.append(csv_name)
        new.append(csv_name)
    else:
        big_dataframe = pd.read_csv(csv_name, sep=';', header=0)
        os.remove(csv_name)
        final_dataframe = pd.concat([big_dataframe, dataframe_from_json], ignore_index=True)
        final_dataframe.sort_values(by='timestamp', ignore_index=True, inplace=True)
        final_dataframe.drop_duplicates(ignore_index=True, inplace=True)
        final_dataframe.to_csv(csv_name, sep=';', index=False, na_rep=None)
        updated.append(csv_name)

    counter = 0
    for item in body_json['observation_list']:
        csv_name = f'{path_output_df}Logs_in_logger_{item["logger_sn"]}.csv'
        dataframe_from_json = pd.DataFrame([item])
        if csv_name not in globed:
            globed.append(csv_name)
            dataframe_from_json.to_csv(csv_name, sep=";", index=False)
            new.append(csv_name)
        elif csv_name in new:
            dataframe = pd.read_csv(path_output_df+'Logs_in_logger_'+item["logger_sn"]+'.csv', sep=';', header=0)
            final_dataframe = pd.concat([dataframe, dataframe_from_json], ignore_index=True)
            final_dataframe.to_csv(csv_name, sep=';', index=False)
        elif csv_name in globed and csv_name not in new:
            if csv_name in updated:
                dataframe = pd.read_csv(path_output_df+'Logs_in_logger_'+item["logger_sn"]+'_update.csv', sep=';', header=0)
                final_dataframe = pd.concat([dataframe, dataframe_from_json], ignore_index=True)
                final_dataframe.to_csv(csv_name[:-4]+'_update.csv', sep=";", index=False)
            else:
                updated.append(csv_name)
                dataframe_from_json.to_csv(csv_name[:-4]+'_update.csv', sep=";", index=False)
        counter += 1
        print(f'\tMaking progress ....{counter} / {len(body_json["observation_list"])}', end='\r')
    
    globed.remove(f'{path_output_df}BigDataFrame.csv')
    for item in globed:
        if item in new:
            print(f'{"- "*45}\n-->\tMaking adjustments to {item}\n{"- "*45}', end='\r')
            dataframe = pd.read_csv(item, sep=';', header=0)
            dataframe = dataframe.pivot_table(index=['logger_sn', 'timestamp'], columns='sensor_measurement_type', values='si_value').reset_index()
            dataframe.to_csv(item, sep=';', index=False)
        elif item in updated:
            print(f'{"- "*45}\n-->\tMaking adjustments to {item}\n{"- "*45}', end='\r')
            dataframe_before = pd.read_csv(item, sep=';', header=0)
            dataframe_update = pd.read_csv(item[:-4]+'_update.csv', sep=';', header=0) 
            dataframe_update = dataframe_update.pivot_table(index=['logger_sn', 'timestamp'], columns='sensor_measurement_type', values='si_value').reset_index()
            dataframe_update = pd.concat([dataframe_before, dataframe_update], ignore_index=True)
            dataframe_update.sort_values(by='timestamp', ignore_index=True, inplace=True)
            dataframe_update.drop_duplicates(ignore_index=True, inplace=True)
            dataframe_update.to_csv(item, sep=';', index=False)
            os.remove(item[:-4]+'_update.csv')

    print('\n'*150)
    print('- '*45)
    print(f'\n-->\tDataFrames updated:\n- {len(updated)} DataFrames\n- {updated}\n')
    print('- '*45)
    print(f'\n-->\tDataFrames created:\n- {len(new)} DataFrames\n- {new}\n')
    print('- '*45)
