import asyncio

from src.CsrankingSpider.collector import get_all_professor_information_from_file, close_session, get_professor_indexes, \
    get_all_professor_information_from_network
from src.CsrankingSpider.persistence import save_to_file


async def schedule_tasks(out_directory, professor_information, batch_size):
    for pointer in range(0, len(professor_information), batch_size):
        batch = [
            info
            for info in professor_information[pointer:pointer + batch_size]
        ]

        task_batch = [
            get_professor_indexes(i)
            for i in batch
        ]

        results = await asyncio.gather(*task_batch, return_exceptions=True)

        for index, result in enumerate(results):
            if isinstance(result, str):
                info = batch[index]
                save_to_file(out_directory, f'{info[0]}_{info[1]}.pkl', result)


async def main(out_directory='out/', batch_size=10, csranking_file_path='csranking.csv'):
    choice = input('Update professor page list(y/n)? (This process may be very slow in some regions.)')
    if choice == 'y' or choice == 'Y':
        info = await get_all_professor_information_from_network()
    else:
        info = await get_all_professor_information_from_file(csranking_file_path)
    await schedule_tasks(out_directory, info, batch_size)
    await close_session()
