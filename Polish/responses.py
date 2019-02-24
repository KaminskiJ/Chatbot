start = 'Cześć! Jestem Tytus i jestem botem! Stworzono mnie bym pomógł Ci w zakupie japońskiego samochodu. ' \
        '\nNa początku potrzebuje Twojej decyzji jaką markę i typ auta bierzesz pod uwagę. Powiedz mi proszę co Cie interesuje?' \
        '\nJeśli nie wiesz jakie są możliwe opcje po prostu spytaj :-)'

selected_brand = '{} to naprawdę porządna marka, Jakiego typu auta szukasz?'

selected_category = 'Ok. A więc interesuje Cię {}. Jakiej marki?'

summary_both_options = 'Dla pewności pozwól, że spytam. Chciałbyś zobaczyć {} produkowany/e przez firmę {}?'

cant_find_response = 'Przepraszam ale nie rozumiem :-( Spróbuj proszę inaczej sformułować swoją odpowiedź'

cant_find_response_confirmation = 'Przepraszam ale nie rozumiem :-( Czy wybrana marka ({}) oraz typ auta ({}) jest w porządku?'

what_needs_to_be_changed = 'W takim razie, który wybór chcesz zmienić? Wybraną markę ({}) czy typ auta ({})?'

wrong_summary_message = 'Wybacz, mój błąd. Pozwól, że się poprawię! Co się nie zgadza? Marka czy rodzaj auta?'

#below need to be implemented
loopRestart = 'Skoro usuneliśmy błędne dane to co powinienem dodać w ich miejsce?'

#below need to be implemented
userBackout = 'Czyli wszystko jest w porządku? Potwierdź jeśli chciałbyś przejść do podsumowania lub raz jeszcze powiedz co chciałbyś zmienić'

removed_selection = 'Ok! Usunąłem ten wybór. Na jaki chcesz go zmienić?'

removed_selections = 'Ok! Najwyraźniej coś pomieszałem, wybacz. Zacznijmy proszę od nowa! :-) Jaką markę lub jaki rodzaj auta bierzesz pod uwagę?'

time_now = 'Jest {}:{}'

list_of_car_manufacturers = 'Oto lista wszystkich japońskich marek samochodów: '

list_of_car_types = 'Oto lista wszystkich dostępnych typów samochodów: '

status_missing_brand = 'Jak na razie wiem, że interesuje Cię {} ale potrzebuje jeszcze od Ciebie informacji jakiej marki samochody chcesz zobaczyć?'

status_missing_type = 'Jak na razie wiem, że interesuje Cię {} ale potrzebuje jeszcze od Ciebie informacji jakiego typu auta chcesz zobaczyć?'

status_missing_both = 'Na razie wciąż nie wiem co Cię interesuje. Powiedz mi proszę nad jaką marką czy typem auta się zastanawiasz?'

who_made_you = 'Zostałem stworzony przez Kubę Kamińskiego na początku roku 2019'

demo_finish = 'Koniec programu. Otrzymano zmienne: {} oraz {}.\nTe zmienne następnie przechodzą w poniższą kwerende SQL:\n'

sql_query = '\"SELECT CarCategoryColumn, CarBrandColumn FROM car_list_table WHERE CarCategoryColumn = {} AND CarBrandColumn = {};\"\n'

ending = 'Następnie ta kwerenda jest wysłana do bazy sql skąd bot zaciąga listę obiektów spełniających kryteria użytkownika.' \
         '\nPo zdobyciu tych danych rozmowa byłaby prowadzona dalej tak by doprecyzować/zmienić kryteria bądź wyszukać konkrentą ofertę.'