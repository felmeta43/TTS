import re

# List of (regular expression, replacement) pairs for abbreviations in Afaan Oromoo:
abbreviations_ao = [(re.compile('\\b%s\\.' % x[0], re.IGNORECASE), x[1])
                  for x in [
                      ('dr', 'dooctar'),
                      ('inj', 'injiiner'),
                      ('jen', 'jeneraal'),
                      ('prof', 'proofeesar'),
                      ('Aadd', 'Aadde'),
                      ('kkf', 'kan kana fakkaatan'),
                      ('wkf', 'waan kana fakkaatan'),
                      ('fkn', 'fakkeenyaaf'),
                      ('hub', 'hubachiisaa'),
                      ('obb', 'obbo'),
                      ('A.L.I', 'Akka Lakkoofsa Itiyoophiyaa'),
                      ('A.L.A', 'Akka Lakkoofsa Awurooppaa'),
                      ('M/Murti', 'Mana Murtii'),
                      ('WD', 'Waaree Dura'),
                      ('WB', 'Waaree Booda'),
                      ('Lakk.', 'Lakkoofsa'),
                      ('M/', 'Magaalaa'),
                      ('Bul/', 'Bulchiinsa'),
                  ]]
