def compute(n: int) -> str:
    digitals = [
        ''' * * *
*     *
*     *
*     *

*     *
*     *
*     *
 * * *''',
        '''
      *
      *
      *

      *
      *
      *
''',
        ''' * * *
      *
      *
      *
 * * *
*
*
*
 * * * ''',
        ''' * * *
      *
      *
      *
 * * *
      *
      *
      *
 * * *''',
        '''
*     *
*     *
*     *
 * * *
      *
      *
      *
''',
        ''' * * *
*
*
*
 * * *
      *
      *
      *
 * * *''',
        ''' * * *
*
*
*
 * * *
*     *
*     *
*     *
 * * *''',
        ''' * * *
      *
      *
      *

      *
      *
      *
''',
        ''' * * *
*     *
*     *
*     *
 * * *
*     *
*     *
*     *
 * * *''',
        ''' * * *
*     *
*     *
*     *
 * * *
      *
      *
      *
 * * *''',
]
    return digitals[n]

if __name__ == '__main__':
    print(compute(int(input())))