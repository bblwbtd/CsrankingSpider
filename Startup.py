import asyncio

from src.CsrankingSpider.main import main

output_directory = 'out/'
batch_size = 10
csranking_csv_file = 'csranking.csv'

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(output_directory, batch_size, csranking_csv_file))
    loop.run_until_complete(asyncio.sleep(0.250))
    loop.close()
