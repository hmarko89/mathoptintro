import requests
from bs4 import BeautifulSoup
import re

class Puzzle:
    BASE_URL = None

    @classmethod
    def _get_task(cls, path: str) -> str:
        response = requests.get(cls.BASE_URL + path)
        soup = BeautifulSoup(response.content, 'html.parser')
        pattern = re.compile( r"var task = '(.*?)';", re.MULTILINE | re.DOTALL )

        for script in soup.find_all( 'script' ):
            match = re.findall( pattern, str(script) )
            if match:
                return match[0]

        return None
    
    @classmethod
    def get_tasks(cls):
        for name, attr in cls.__dict__.items():
            if isinstance(attr, classmethod):
                func = attr.__func__
                print(f'{name} = \'{func(cls)}\'')

class Binairo(Puzzle):
    BASE_URL = 'https://www.puzzle-binairo.com/'

    @classmethod
    def random_6x6_easy(cls):
        return cls._get_task('binairo-6x6-easy/')

    @classmethod
    def random_6x6_hard(cls):
        return cls._get_task('binairo-6x6-hard/')

    @classmethod
    def random_8x8_easy(cls):
        return cls._get_task('binairo-8x8-easy/')

    @classmethod
    def random_8x8_hard(cls):
        return cls._get_task('binairo-8x8-hard/')

    @classmethod
    def random_10x10_easy(cls):
        return cls._get_task('binairo-10x10-easy/')

    @classmethod
    def random_10x10_hard(cls):
        return cls._get_task('binairo-10x10-hard/')

    @classmethod
    def random_14x14_easy(cls):
        return cls._get_task('binairo-14x14-easy/')

    @classmethod
    def random_14x14_hard(cls):
        return cls._get_task('binairo-14x14-hard/')

    @classmethod
    def random_20x20_easy(cls):
        return cls._get_task('binairo-20x20-easy/')

    @classmethod
    def random_20x20_hard(cls):
        return cls._get_task('binairo-20x20-hard/')

    @classmethod
    def daily(cls):
        return cls._get_task('daily-binairo/')

    @classmethod
    def weekly(cls):
        return cls._get_task('weekly-binairo/')

    @classmethod
    def monthly(cls):
        return cls._get_task('monthly-binairo/')

class Futoshiki(Puzzle):
    BASE_URL = 'https://www.puzzle-futoshiki.com/'

    @classmethod
    def random_4x4_easy(cls):
        return cls._get_task('futoshiki-4x4-easy/')

    @classmethod
    def random_5x5_easy(cls):
        return cls._get_task('futoshiki-5x5-easy/')

    @classmethod
    def random_5x5_normal(cls):
        return cls._get_task('futoshiki-5x5-normal/')

    @classmethod
    def random_5x5_hard(cls):
        return cls._get_task('futoshiki-5x5-hard/')

    @classmethod
    def random_7x7_easy(cls):
        return cls._get_task('futoshiki-7x7-easy/')

    @classmethod
    def random_7x7_normal(cls):
        return cls._get_task('futoshiki-7x7-normal/')

    @classmethod
    def random_7x7_hard(cls):
        return cls._get_task('futoshiki-7x7-hard/')

    @classmethod
    def random_9x9_easy(cls):
        return cls._get_task('futoshiki-9x9-easy/')

    @classmethod
    def random_9x9_normal(cls):
        return cls._get_task('futoshiki-9x9-normal/')

    @classmethod
    def random_9x9_hard(cls):
        return cls._get_task('futoshiki-9x9-hard/')

    @classmethod
    def daily(cls):
        return cls._get_task('daily-futoshiki/')

    @classmethod
    def weekly(cls):
        return cls._get_task('weekly-futoshiki/')

    @classmethod
    def monthly(cls):
        return cls._get_task('monthly-futoshiki/')

class Hitori(Puzzle):
    BASE_URL = 'https://www.puzzle-hitori.com/'

    @classmethod
    def random_5x5_easy(cls):
        return cls._get_task('')

    @classmethod
    def random_5x5_normal(cls):
        return cls._get_task('?size=1')

    @classmethod
    def random_5x5_hard(cls):
        return cls._get_task('?size=2')

    @classmethod
    def random_10x10_easy(cls):
        return cls._get_task('?size=3')

    @classmethod
    def random_10x10_normal(cls):
        return cls._get_task('?size=4')

    @classmethod
    def random_10x10_hard(cls):
        return cls._get_task('?size=5')

    @classmethod
    def random_15x15_easy(cls):
        return cls._get_task('?size=6')

    @classmethod
    def random_15x15_normal(cls):
        return cls._get_task('?size=7')

    @classmethod
    def random_15x15_hard(cls):
        return cls._get_task('?size=8')

    @classmethod
    def random_20x20_easy(cls):
        return cls._get_task('?size=9')

    @classmethod
    def random_20x20_normal(cls):
        return cls._get_task('?size=10')

    @classmethod
    def random_20x20_hard(cls):
        return cls._get_task('?size=11')

    @classmethod
    def daily(cls):
        return cls._get_task('?size=12')

    @classmethod
    def weekly(cls):
        return cls._get_task('?size=13')

    @classmethod
    def monthly(cls):
        return cls._get_task('?size=14')

class Kakurasu(Puzzle):
    BASE_URL = 'https://www.puzzle-kakurasu.com/'

    @classmethod
    def random_4x4_easy(cls):
        return cls._get_task('')

    @classmethod
    def random_4x4_hard(cls):
        return cls._get_task('?size=1')

    @classmethod
    def random_5x5_easy(cls):
        return cls._get_task('?size=2')

    @classmethod
    def random_5x5_hard(cls):
        return cls._get_task('?size=3')

    @classmethod
    def random_6x6_easy(cls):
        return cls._get_task('?size=4')

    @classmethod
    def random_6x6_hard(cls):
        return cls._get_task('?size=5')

    @classmethod
    def random_7x7_easy(cls):
        return cls._get_task('?size=6')

    @classmethod
    def random_7x7_hard(cls):
        return cls._get_task('?size=7')

    @classmethod
    def random_8x8_easy(cls):
        return cls._get_task('?size=8')

    @classmethod
    def random_8x8_hard(cls):
        return cls._get_task('?size=9')

    @classmethod
    def random_9x9_easy(cls):
        return cls._get_task('?size=10')

    @classmethod
    def random_9x9_hard(cls):
        return cls._get_task('?size=11')

    @classmethod
    def daily(cls):
        return cls._get_task('?size=12')

    @classmethod
    def weekly(cls):
        return cls._get_task('?size=13')

    @classmethod
    def monthly(cls):
        return cls._get_task('?size=14')

class Masyu(Puzzle):
    BASE_URL = 'https://www.puzzle-masyu.com/'

    @classmethod
    def random_6x6_easy(cls):
        return cls._get_task('')

    @classmethod
    def random_8x8_easy(cls):
        return cls._get_task('?size=1')

    @classmethod
    def random_8x8_normal(cls):
        return cls._get_task('?size=2')

    @classmethod
    def random_8x8_hard(cls):
        return cls._get_task('?size=3')

    @classmethod
    def random_10x10_easy(cls):
        return cls._get_task('?size=4')

    @classmethod
    def random_10x10_normal(cls):
        return cls._get_task('?size=5')

    @classmethod
    def random_10x10_hard(cls):
        return cls._get_task('?size=6')

    @classmethod
    def random_15x15_easy(cls):
        return cls._get_task('?size=7')

    @classmethod
    def random_15x15_normal(cls):
        return cls._get_task('?size=8')

    @classmethod
    def random_15x15_hard(cls):
        return cls._get_task('?size=9')

    @classmethod
    def random_20x20_easy(cls):
        return cls._get_task('?size=10')

    @classmethod
    def random_20x20_normal(cls):
        return cls._get_task('?size=11')

    @classmethod
    def random_20x20_hard(cls):
        return cls._get_task('?size=12')

    @classmethod
    def random_25x25_easy(cls):
        return cls._get_task('?size=16')

    @classmethod
    def random_25x25_normal(cls):
        return cls._get_task('?size=17')

    @classmethod
    def random_25x25_hard(cls):
        return cls._get_task('?size=18')

    @classmethod
    def daily(cls):
        return cls._get_task('?size=13')

    @classmethod
    def weekly(cls):
        return cls._get_task('?size=14')

    @classmethod
    def monthly(cls):
        return cls._get_task('?size=15')

class Pipes(Puzzle):
    BASE_URL = 'https://www.puzzle-pipes.com/'

    @classmethod
    def random_4x4(cls):
        return cls._get_task('')

    @classmethod
    def random_5x5(cls):
        return cls._get_task('?size=1')

    @classmethod
    def random_7x7(cls):
        return cls._get_task('?size=2')

    @classmethod
    def random_10x10(cls):
        return cls._get_task('?size=3')

    @classmethod
    def random_15x15(cls):
        return cls._get_task('?size=4')

    @classmethod
    def random_20x20(cls):
        return cls._get_task('?size=5')

    @classmethod
    def random_25x25(cls):
        return cls._get_task('?size=6')

    @classmethod
    def daily(cls):
        return cls._get_task('?size=7')

    @classmethod
    def weekly(cls):
        return cls._get_task('?size=8')

    @classmethod
    def monthly(cls):
        return cls._get_task('?size=9')

    @classmethod
    def random_4x4_wrap(cls):
        return cls._get_task('?size=10')

    @classmethod
    def random_5x5_wrap(cls):
        return cls._get_task('?size=11')

    @classmethod
    def random_7x7_wrap(cls):
        return cls._get_task('?size=12')

    @classmethod
    def random_10x10_wrap(cls):
        return cls._get_task('?size=13')

    @classmethod
    def random_15x15_wrap(cls):
        return cls._get_task('?size=14')

    @classmethod
    def random_20x20_wrap(cls):
        return cls._get_task('?size=15')

    @classmethod
    def random_25x25_wrap(cls):
        return cls._get_task('?size=16')

    @classmethod
    def daily_wrap(cls):
        return cls._get_task('?size=17')

    @classmethod
    def weekly_wrap(cls):
        return cls._get_task('?size=18')

    @classmethod
    def monthly_wrap(cls):
        return cls._get_task('?size=19')

class Renzoku(Puzzle):
    BASE_URL = 'https://www.puzzle-futoshiki.com/'

    @classmethod
    def random_4x4_easy(cls):
        return cls._get_task('renzoku-4x4-easy/')

    @classmethod
    def random_5x5_easy(cls):
        return cls._get_task('renzoku-5x5-easy/')

    @classmethod
    def random_5x5_normal(cls):
        return cls._get_task('renzoku-5x5-normal/')

    @classmethod
    def random_5x5_hard(cls):
        return cls._get_task('renzoku-5x5-hard/')

    @classmethod
    def random_7x7_easy(cls):
        return cls._get_task('renzoku-7x7-easy/')

    @classmethod
    def random_7x7_normal(cls):
        return cls._get_task('renzoku-7x7-normal/')

    @classmethod
    def random_7x7_hard(cls):
        return cls._get_task('renzoku-7x7-hard/')

    @classmethod
    def random_9x9_easy(cls):
        return cls._get_task('renzoku-9x9-easy/')

    @classmethod
    def random_9x9_normal(cls):
        return cls._get_task('renzoku-9x9-normal/')

    @classmethod
    def random_9x9_hard(cls):
        return cls._get_task('renzoku-9x9-hard/')

    @classmethod
    def daily(cls):
        return cls._get_task('daily-renzoku/')

    @classmethod
    def weekly(cls):
        return cls._get_task('weekly-renzoku/')

    @classmethod
    def monthly(cls):
        return cls._get_task('monthly-renzoku/')

class Skyscrapers(Puzzle):
    BASE_URL = 'https://www.puzzle-skyscrapers.com/'

    @classmethod
    def random_4x4_easy(cls):
        return cls._get_task('')

    @classmethod
    def random_4x4_normal(cls):
        return cls._get_task('?size=1')

    @classmethod
    def random_4x4_hard(cls):
        return cls._get_task('?size=2')

    @classmethod
    def random_5x5_easy(cls):
        return cls._get_task('?size=3')

    @classmethod
    def random_5x5_normal(cls):
        return cls._get_task('?size=4')

    @classmethod
    def random_5x5_hard(cls):
        return cls._get_task('?size=5')

    @classmethod
    def random_6x6_easy(cls):
        return cls._get_task('?size=6')

    @classmethod
    def random_6x6_normal(cls):
        return cls._get_task('?size=7')

    @classmethod
    def random_6x6_hard(cls):
        return cls._get_task('?size=8')

    @classmethod
    def daily(cls):
        return cls._get_task('?size=9')

    @classmethod
    def weekly(cls):
        return cls._get_task('?size=10')

    @classmethod
    def monthly(cls):
        return cls._get_task('?size=11')
    
class Slitherlink(Puzzle):
    BASE_URL = 'https://www.puzzle-loop.com/'

    @classmethod
    def random_5x5_normal(cls):
        return cls._get_task('')

    @classmethod
    def random_5x5_hard(cls):
        return cls._get_task('?size=4')

    @classmethod
    def random_7x7_normal(cls):
        return cls._get_task('?size=10')

    @classmethod
    def random_7x7_hard(cls):
        return cls._get_task('?size=11')

    @classmethod
    def random_10x10_normal(cls):
        return cls._get_task('?size=1')

    @classmethod
    def random_10x10_hard(cls):
        return cls._get_task('?size=5')

    @classmethod
    def random_15x15_normal(cls):
        return cls._get_task('?size=2')

    @classmethod
    def random_15x15_hard(cls):
        return cls._get_task('?size=6')

    @classmethod
    def random_20x20_normal(cls):
        return cls._get_task('?size=3')

    @classmethod
    def random_20x20_hard(cls):
        return cls._get_task('?size=7')

    @classmethod
    def random_25x30_normal(cls):
        return cls._get_task('?size=8')

    @classmethod
    def random_25x30_hard(cls):
        return cls._get_task('?size=9')

    @classmethod
    def daily(cls):
        return cls._get_task('?size=13')

    @classmethod
    def weekly(cls):
        return cls._get_task('?size=12')

    @classmethod
    def monthly(cls):
        return cls._get_task('?size=14')
    
class Sudoku(Puzzle):
    BASE_URL = 'https://www.puzzle-sudoku.com/'

    @classmethod
    def random_basic(cls):
        return cls._get_task('')

    @classmethod
    def random_easy(cls):
        return cls._get_task('?size=1')

    @classmethod
    def random_intermediate(cls):
        return cls._get_task('?size=2')

    @classmethod
    def random_advanced(cls):
        return cls._get_task('?size=3')

    @classmethod
    def random_extreme(cls):
        return cls._get_task('?size=4')

    @classmethod
    def random_evil(cls):
        return cls._get_task('?size=5')

    @classmethod
    def daily(cls):
        return cls._get_task('?size=9')

class Thermometers(Puzzle):
    BASE_URL = 'https://www.puzzle-thermometers.com/'

    @classmethod
    def random_4x4(cls):
        return cls._get_task('')

    @classmethod
    def random_4x4_curved(cls):
        return cls._get_task('?size=1')

    @classmethod
    def random_6x6(cls):
        return cls._get_task('?size=2')

    @classmethod
    def random_6x6_curved(cls):
        return cls._get_task('?size=3')

    @classmethod
    def random_10x10(cls):
        return cls._get_task('?size=4')

    @classmethod
    def random_10x10_curved(cls):
        return cls._get_task('?size=5')

    @classmethod
    def random_15x15(cls):
        return cls._get_task('?size=6')

    @classmethod
    def random_15x15_curved(cls):
        return cls._get_task('?size=7')

    @classmethod
    def daily(cls):
        return cls._get_task('?size=8')

    @classmethod
    def daily_curved(cls):
        return cls._get_task('?size=9')

    @classmethod
    def weekly(cls):
        return cls._get_task('?size=10')

    @classmethod
    def weekly_curved(cls):
        return cls._get_task('?size=11')

    @classmethod
    def monthly(cls):
        return cls._get_task('?size=12')

    @classmethod
    def monthly_curved(cls):
        return cls._get_task('?size=13')

if __name__ == '__main__':
    #print( f'sudoku_instance = \'{Sudoku.random_evil()}\'' )
    print( f'sudoku_instance = \'{Skyscrapers.random_6x6_easy()}\'' )
