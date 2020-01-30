# Cs Ranking Spider

## Introduction
A small program which is used to fetch all personal page of professors on http://csrankings.org. The program uses lots of methods of asyncio library, which means you need to ensure your python version is above 3.7.

## Getting Start
1. Install pipenv with ```pip3 install pipenv```
2. Install dependencies with ```pipenv install```
3. Run program with ```pipenv run python3 Starup.py```

## Configuration
You can change the configuration in the ```Starup.py```

- ```output_directory``` indicates where pages will be stored.
- ```batch_size``` how many requests will be sent concurrently.
- ```csranking_csv_file``` the path of ```csranking.csv``` that saves the professor's name and homepage
