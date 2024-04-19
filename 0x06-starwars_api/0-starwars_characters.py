#!/usr/bin/env python3
"""Script that prints all characters names of a Star Wars movie
using the 'https://swapi-api.alx-tools.com/api' API
"""
import aiohttp
import asyncio
from sys import argv, exit
from typing import List

# The main API URL
main_URL = 'https://swapi-api.alx-tools.com/api'


async def get_characters_URLs_list(movie_id: str) -> List[str]:
    """Query the API to get characters URLs list
    """

    global main_URL

    # Get characters URLs list through `/films/<movie_id>`
    async with aiohttp.ClientSession() as session:
        movie = await session.get(main_URL + '/films/' + movie_id)
        movie_dict = await movie.json()

    characters = movie_dict.get('characters')
    return characters


def get_tasks(session, characters_URLs: List[str]) -> List:
    """Create tasks (coroutines) for each character URL"""

    # Request each character URL and keep it as a task
    tasks = []
    for url in characters_URLs:
        # Create task and append it
        task = asyncio.create_task(session.get(url))
        tasks.append(task)

    # Return tasks list
    return tasks


async def print_characters_names(characters_URLs: List[str]) -> None:
    """Fetch and print_characters_name based on `characters_URLs`"""

    # Get names by gethering tasks
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session, characters_URLs)
        characters = await asyncio.gather(*tasks)

        # Get and print each character name
        for character in characters:

            # Get JSON dictionnary
            character_dict = await character.json()

            # Print character's name
            print(character_dict.get('name'))


if __name__ == '__main__':
    import time

    # Check argv
    if len(argv) != 2:
        print('Usage: ./0-starwars_characters.py <movie_id>')
        exit(1)

    # Retrieve movie_id
    movie_id = argv[1]

    # Check that movie_id is an integer
    try:
        int(movie_id)
    except ValueError:
        print('<movie_id> should be an integer')
        exit(1)

    # Count time
    start = time.time()

    # Get characters URLs list
    characters_URLs = asyncio.run(get_characters_URLs_list(movie_id))

    # Print characters names
    asyncio.run(print_characters_names(characters_URLs))

    print('\nTook', time.time() - start, 'seconds')
