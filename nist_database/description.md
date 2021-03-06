**Источник данных:** https://gashydrates.nist.gov/

**Описание:** в каталоге представленны данные по термбарическим условиям процесса
гидратообразования газовы из таблицы 1 с образующимися в процессе структурами
из таблицы 3. В таблице 2 отображены столбцы данных, которые содержатся
в таблицах. Ниже описана структура каталога для удобства использования.

**Таблица 1: Газы, данные о которых содержатся в каталоге**

| Тип                                   | Газы                   |
| ------------------------------------- | ---------------------- |
| Углеводородные, гидратообразователи   | CH4, C2H6, C3H8, C4H10 |
| Неуглеводородные, гидратообразователи | CO2, N2, H2S           |

**Таблица 2: Содержание столбцов таблиц**

| Наименование столбца | Содержание                          |
| -------------------- | ----------------------------------- |
| Number of Data       | Номер таблицы из БД                 |
| Title                | Название статьи                     |
| Author               | Автор статьи                        |
| Source               | Источник публикации                 |
| Year                 | Год публикации                      |
| Compounds            | Структура смеси                     |
| T (K)                | Температура смеси                   |
| p (kPa)              | Давление смеси                      |
| Mole Fraction (xA)   | Мольные доли компонентов смеси      |
| Mole Ratio (nA/B)    | Мольные отношения компонентов смеси |

**Таблица 3: Фазы встречающиеся в данных (Compounds)**

| Название структуры    | Расшифровка                        |
| --------------------- | ---------------------------------- |
| CH4                   | Метан                              |
| C2H6                  | Этан                               |
| C3H8                  | Пропан                             |
| C4H10                 | Изобутан                           |
| Nonpolar Liquid       | Неполярная жидкость (углеводороды) |
| CO2                   | Углекислый газ                     |
| H2S                   | Сероводород                        |
| N2                    | Азот                               |
| Vapoor                | Газ                                |
| Aqueous Liquid        | Жидкоя вода                        |
| H2O in Aqueous Liquid | Жидкая вода                        |
| Ice                   | Лёд                                |
| H2O in Hydrate        | Гидрат                             |
| H2O in Hydrate sI     | Гидрат первой структуры            |
| H2O in Hydrate sII    | Гидрат второй структуры            |
| Hydrate sII           | Гидрат второй структуры            |

**Содержание директорий каталога:**

    examples.ipynb:
      В блокноте содержится пример использование скриптов из _base.py для
      чтения и преобразования данных из директории nist с последующим
      сохранением в директорию datasets.

    nist:
      Директория содержит данные с сайта в виде пронумерованных таблиц
      разложенных по папкам с названиями учавствующих компонентов. По умолчанию
      данные с сайти сохраняются в Thermo*.xls, где вместо * - номер дата сета,
      который позже идёт в столбец данных из таблицы 2. Файлы Thermo*.csv
      создавались вручную для удобства использования в коде.

    datasets:
      Примеры получаемых наборов данных из examples.ipynb.

    __init__.py:
      Для импорта скриптов и данных в другие проекты

    _base.py:
      Содержатся функции для обработки данных с их описанием

**Структура каталога:**

    |-- nist
    |   |__ *
    |       |-- Thermo*.xls
    |       |__ Thermo*.csv
    |-- datasets
    |   |-- compounds_mask.csv
    |   |-- mole_fraction_compounds_mask.csv
    |   |-- mole_fraction.csv
    |   |-- mole_ratio_compounds_mask.csv
    |   |__ mole_ratio.csv
    |-- __init__.py
    |-- _base.py
    |-- examles.ipynb
    |__ Данный файл соответсвенно
