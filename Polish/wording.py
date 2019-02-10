#Plik zawierajacy listy zwrotow i synonimow. W tej wersji nadmiernie rozbudowany.
#Po wdrożeniu analizy inputu i podobienstwa za pomoca biblioteki difflib bedzie uproszczony


#pozegnania
goodbye = ['bądź zdrów', 'ciao' , 'czesc', 'cześć', 'czolem', 'czołem', 'hej', 'pa', 'serwus', 'zegnaj', 'żegnaj',
           'elo', 'eloszki', 'hejka', 'hejoszki', 'hejsia', 'siema', 'siemasz', 'siemka']

#kategorie aut
carCategories = ['miejskie', 'kompaktowe', 'sedan', 'hatchback', 'liftback', 'coupé',
                 'limuzyna', 'suv', 'van', 'minivan', 'targa', 'kabriolet', 'kombi', 'combi', 'roadster', 'pickup', 'pick-up']

car_categories_for_listing = ['miejskie', 'kompaktowe', 'sedan', 'hatchback', 'liftback', 'coupe',
                 'limuzyna', 'Suv', 'Van', 'minivan', 'targa', 'kabriolet', 'combi', 'roadster', 'pickup']

#marki aut
carBrands = ['toyota', 'honda', 'daihatsu', 'nissan', 'suzuki', 'mazda', 'mitsubishi', 'subaru', 'isuzu',
             'kawasaki', 'yamaha', 'mitsuoka']

#potwierdzenie
confirmation = ['ano', 'dokładnie', 'dokladnie', 'faktycznie', 'istotnie', 'jak najbardziej', 'naturalnie',
                'nie inaczej', 'no', 'no tak', 'tak', 'oczywiście', 'oczywiscie', 'owszem', 'mhm', 'pewnie' 'racja',
                'rzecz jasna', 'w istocie,' 'w rzeczy samej', 'właśnie', 'zaiste' ,'ok', 'porządku', 'porzadku']

#zaprzeczenie
negation = ['akurat', 'bynajmniej', 'gdzież', 'nigdy', 'życiu', 'skąd', 'skad', 'skądże', 'skadze', 'nie']

#synonimy marki
brand = ['marka', 'marki', 'firmy', 'firma', 'nazwa']

#synonimy typu
types = ['kategoria', 'klasa', 'model', 'odmiana', 'odmiany', 'podgatunek', 'podklasa', 'podtyp', 'rodzaj', 'rodzaje', 'seria', 'typ', 'typy',
         'subkategoria', 'wariant', 'warianty', 'wersja', 'wersje']

#synonimy słowa wszystko
everything = ['całokształt', 'caloksztalt', 'całość', 'calosc', 'komplet', 'ogół', 'ogol', 'pełnia', 'suma', 'wsio', 'wszystko']

#synonimy słowa który
which = ['ktory', 'ktora', 'która', 'który', 'jaki', 'jaka', 'jakie']
#synonimy słowa czego
what = ['czego', 'co']

#synonimy słowa brak
missing = ['brak', 'brakuje', 'potrzeba', 'potrzebujesz']

#synonimy słowa godzina/czas
hour = ['godzina', 'godzinka', 'czas', 'pora']

#synonimy słowa kto
who = ['kto', 'ktoz']

#synonimy słowa stworzenie
made = ['stworzył', 'stworzyl', 'napisał', 'napisal', 'wytworzyl', 'zakodował', 'zaprogramowal']


included_dictionares = ["goodbye", "carCategories", "carBrands", "confirmation", "negation", "brand", "types", "what", "missing",
                        "everything", "which", "hour"]
