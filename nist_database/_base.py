"""
"""
import os
from os.path import dirname, exists
import glob
import pandas as pd


def _creat_compounds_data(path):
    """Считывает файлы из nist/*/*.сsv, объединяет их во фрейм данных и итеративно возвращает по составам;
    состав = директория внутри nist

    Parameters
    ----------
    path : string
        Путь до директории nist

    Returns
    -------
    pd_compound_file : pd.DataFrame
        Фрейм данных с данными внутри одной директории состава
    """
    for folder in os.listdir(path = '{}\\nist'.format(path)):
        file_name = '{}\\nist\\{}\\Thermo*.csv'.format(path, folder)
        all_filenames = [name for name in glob.glob(file_name)]
        pd_compound_file = pd.concat([pd.read_csv(filename,
                                                  index_col=None,
                                                  header=0,
                                                  sep=';') for filename in all_filenames])
        
        yield pd_compound_file


def load_nist_data():
    """Вызывает функцию _creat_compounds_data и объединяет фрейм составов в общий фрейм

    Returns
    -------
    pd_nist_data : pd.DataFrame
        Фрем содержит все данные из директории nist/*
    """
    path = dirname(__file__)
    pd_compounds_files = [file for file in _creat_compounds_data(path)]
    pd_nist_data = pd.concat([file for file in pd_compounds_files])
    pd_nist_data.reset_index(drop=True, inplace=True)
    pd_nist_data.sort_values('T (K)')
    
    return pd_nist_data


def compounds_mask(data):
    """Получает фрейм данных (рекомендуется передавать файл из функции load_nist_data) и
    разбивает столбец Compounds на составляющие и на его основании создаёт новые столбцы
    с веществами со значениями True/False
    
    Parameters
    ----------
    data : pd.DataFrame
        Фрейм данных для создания маски по столбцу Compounds

    Returns
    -------
    data : pd.DataFrame
        Результирующий фрейм данных с маской по составу
    """
    if 'Compounds' in data:
        comp_list = []
        for value in data['Compounds'].unique():
            for name in value.split(' + '):
                    
                if name not in comp_list:
                    comp_list.append(name)
                    data[name] = [name in row.split(' + ') for row in data['Compounds']]
                    
        data.drop(columns='Compounds', inplace=True)
        data = data * 1

        if 'Hydrate sII' in data:
            if 'H2O in Hydrate sII' in data:
                data['H2O in Hydrate sII'] = data['H2O in Hydrate sII'] + data['Hydrate sII']
            else:
                data['H2O in Hydrate sII'] = data['Hydrate sII']
            data.drop(columns='Hydrate sII', inplace=True)
            
        if 'Aqueous Liquid' in data:
            if 'H2O in Aqueous Liquid' in data:
                data['H2O in Aqueous Liquid'] = data['H2O in Aqueous Liquid'] + data['Aqueous Liquid']
            else: data['H2O in Aqueous Liquid'] = data['Aqueous Liquid']
            data.drop(columns='Aqueous Liquid', inplace=True)
            
        if 'xH2O' in data:
            data.drop(columns='xH2O', inplace=True)

        if 'xCO2.1' in data:
            data.drop(columns='xCO2.1', inplace=True)
        
    return data


def mole_ratio_data(data):
    """Получает фрейм данных (рекомендуется передавать файл из функции load_nist_data) и
    оставляет сроки, содержащие данные о мольных отношениях

    Parameters
    ----------
    data : pd.DataFrame
        Фрейм данных для отбора по мольным отношениям

    Returns
    -------
    data : pd.DataFrame
        Результирующий фрейм данных со строками, содержащими мольные отношения
    """
    columns_names = data.columns.tolist()
    columns_mask = [s for s in columns_names if '/' in s]
    if columns_mask:
        bool_mask = data[columns_mask].isna().sum(axis=1) != len(columns_mask)
        data = data.loc[bool_mask]
    
    return data


def mole_fraction_data(data):
    """Получает фрейм данных (рекомендуется передавать файл из функции load_nist_data) и
    оставляет сроки, содержащие данные о мольных концентрациях

    Parameters
    ----------
    data : pd.DataFrame
        Фрейм данных для отбора по мольным концентрациям

    Returns
    -------
    data : pd.DataFrame
        Результирующий фрейм данных со строками, содержащими мольные концентрации
    """
    columns_names = data.columns.tolist()
    columns_mask = [s for s in columns_names if 'x' in s]
    if columns_mask:
        bool_mask = data[columns_mask].isna().sum(axis=1) != len(columns_mask)
        data = data.loc[bool_mask]
    
    return data
