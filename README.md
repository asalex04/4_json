
# Prettify JSON
`pprint_json.py` program is designed to format data from a file in `json` format for convenient reading

# Quickstart
How to run:
```bash
$ python pprint_json.py <path to file>

```
Example of script launch on Linux, Python 3.5:

```bash
$ python3 pprint_json.py test.json
[
    {
        "Cells": {
            "Address": "улица Академика Павлова, дом 10",
            "AdmArea": "Западный административный округ",
            "ClarificationOfWorkingHours": null,
            "District": "район Кунцево",
            "IsNetObject": "да",
            "Name": "Ароматный Мир",
            "OperatingCompany": "Ароматный Мир",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ],
            "TypeService": "реализация продовольственных товаров",
            "WorkingHours": [
                {
                    "DayOfWeek": "понедельник",
                    "Hours": "09:30-22:30"
                },
```
# Project Goals
The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
