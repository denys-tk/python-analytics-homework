import pandas as pd

data = { "city": [ "Kyiv", "Lviv", "Odesa" ], 
         "sales": [ 1200, 950, 500 ] }
df = pd.DataFrame(data)
print( "Продажі по містах (тимчасова версія): " )
print( df )
print( "Середнє значення:", round( df[ "sales" ].mean(), 2 ) )