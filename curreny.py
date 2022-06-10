# import pycountry


# # country = pycountry.countries.get(name='Usa')
# # currency = pycountry.currencies.get(numeric=country.numeric)

# # print (currency.alpha_3)
# # print (currency.name)
# li = list(pycountry.countries)
# print(li)

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkcalendar import DateEntry

DateEntry(locale='en_US').pack()

sfg = 'yyyy.MM.dd'



DateEntry( date_pattern=sfg).pack()

tk.mainloop()