from django.urls import reverse
import re

ALPHABET = {
    # <utf-code>: (engname, hebname, rusname, number, can_be_with_dagesh)
    1488: ('alef', 'אָלֶף', 'алеф', 1, False),
    1489: ('vet', 'בֵית',  'вэт', 2, 'бэт'),
    1490: ('gimel', 'גִּימֵל', 'гимел', 3, False),
    1491: ('dalet', 'דָּלֶת', 'далет', 4, False),
    1492: ('he', 'הֵא', 'хе', 5, False),
    1493: ('vav', 'וָו', 'вав', 6, False),
    1494: ('zayin', 'זַיִן', 'зайн', 7, False),
    1495: ('chet', 'חֵית', 'хэт', 8, False),
    1496: ('tet', 'טֵית', 'тэт', 9, False),
    1497: ('yod', 'יוֹד', 'йуд', 10, False),
    1498: ('kaf sofit', 'כַף סוֹפִית', 'хаф софит', -1, 'каф софит'),
    1499: ('kaf', 'כַף', 'хаф', 20, 'каф'),
    1500: ('lamed', 'לָמֶד', 'ламед', 30, False),
    1501: ('mem sofit', 'מֵם סוֹפִית', 'мем софит', -1, False),
    1502: ('mem', 'מֵם', 'мем', 40, False),
    1503: ('nun sofit', 'נוּן סוֹפִית', 'нун софит', -1, False),
    1504: ('nun', 'נוּן', 'нун', 50, False),
    1505: ('samech', 'סָמֶך', 'самэх', 60, False),
    1506: ('ayin', 'עַיִן',  'айн', 70, False),
    1507: ('pay sofit', 'פֵּא סוֹפִית', 'фэй софит', -1, 'пэй софит'),
    1508: ('pay', 'פֵא, פה', 'фэй', 80, 'пэй'),
    1509: ('tsade sofit', 'צַדִי סוֹפִית', 'цади софит', -1, False),
    1510: ('tsade', 'צַדִי', 'цади', 90, False),
    1511: ('qof', 'קוֹף', 'коф', 100, False),
    1512: ('resh', 'רֵישׁ', 'рэш', 200, False),
    1513: ('shin', 'שִׁין', 'шин', 300, 'син'),
    1514: ('tav', 'תו', 'тав', 400, False)
}

PUNCTUATIONS = {
    1470: 'maqaf',
    1472: 'paseq',
    1475: 'sof pasuq',
    1476: 'nun hafukha',
    1523: 'geresh',
    1524: 'gershayim'
}

LEGATURES = {
    1520: 'Yiddish Double Vav',
    1521: 'Yiddish Vav Yod',
    1522: 'Yiddish Double Yod',
}

MODIFICATORS = {
    1468: ('dagesh', 'дагеш'),
    1473: ('shin-dot', 'шин'),
    1474: ('sin-dot', 'син'),
}

NIQQUD = {
    1456: ('shva', 'בְ'),
    1457: ('hataf segol', 'חֱ'),
    1458: ('hataf patah', 'חֲ'),
    1459: ('hataf kamats', 'חֳ'),
    1460: ('hiriq', ' ִי '),
    1461: ('tsere', ' ֵי '),
    1462: ('segol', 'בֶ'),
    1463: ('patach', 'בַ'),
    1464: ('kamatz', 'בָ'),
    1465: ('holam', 'וֹ'),
    1467: ('kubutz', 'בֻ'),
    1468: ('shuruk', 'וּ'),
    1471: ('rafe', 'בֿ')

}

ALL_HEBREW_UTF_CODES = ALPHABET.keys() | NIQQUD.keys() | PUNCTUATIONS.keys() | MODIFICATORS.keys() | LEGATURES.keys()


class Letter:
    def __init__(self, record):
        self.utf_code = record[0]
        self.id = self.utf_code - 1487
        self.letter = chr(self.utf_code)
        self.params = record[1]
        self.engname = self.params[0]
        self.hebname = self.params[1]
        self.rusname = self.params[2]
        self.number = self.params[3] if self.params[3] > 0 else ""
        if self.utf_code == 1513:
            self.name_with_mod = self.params[4]
            self.letter_with_mod = self.letter + chr(1474)
            self.letter += chr(1473)
        elif self.params[4]:
            self.name_with_mod = self.params[4]
            self.letter_with_mod = self.letter + chr(1468)
        else:
            self.name_with_mod = None
            self.letter_with_mod = None

    def get_absolute_url(self):
        return reverse('symbol_details_url', kwargs={'id': self.id})


class Symbols:
    def __init__(self):
        #
        # Simple Lettters
        #
        self.alef = chr(1488)
        self.vet = chr(1489)
        self.gimel = chr(1490)
        self.dalet = chr(1491)
        self.he = chr(1492)
        self.vav = chr(1493)
        self.zayin = chr(1494)
        self.chet = chr(1495)
        self.tet = chr(1496)
        self.yod = chr(1497)
        self.kaf_sofit = chr(1498)
        self.kaf = chr(1499)
        self.lamed = chr(1500)
        self.mem_sofit = chr(1501)
        self.mem = chr(1502)
        self.nun_sofit = chr(1503)
        self.nun = chr(1504)
        self.samech = chr(1505)
        self.ayin = chr(1506)
        self.pay_sofit = chr(1507)
        self.pay = chr(1508)
        self.tsade_sofit = chr(1509)
        self.tsade = chr(1510)
        self.qof = chr(1511)
        self.resh = chr(1512)
        self.shin = chr(1513)
        self.tav = chr(1514)
        #
        #  MODIFICATORS
        #
        self.dagesh = chr(1468)
        self.shin_dot = chr(1473)
        self.sin_dot = chr(1474)
        #
        #  NIQQUD
        #
        self.shva = chr(1456)
        self.hataf_segol = chr(1457)
        self.hataf_patah = chr(1458)
        self.hataf_kamats = chr(1459)
        self.hiriq = chr(1460)
        self.tsere = chr(1461)
        self.segol = chr(1462)
        self.patach = chr(1463)
        self.kamatz = chr(1464)
        self.holam = chr(1465)
        self.kubutz = chr(1467)
        self.rafe = chr(1471)
        self.shuruk = chr(1468)


def remove_mods(heb_with_cons):
    # Removes dageshes, niqqud etc from hebrew word
    hebrew = [i for i in heb_with_cons if ord(i) in ALPHABET.keys()]
    return ''.join(hebrew)


def remove_niqqud(heb_word):
    # Removes niqqud  from hebrew word
    hebrew = [i for i in heb_word if ord(i) not in NIQQUD.keys()]
    return ''.join(hebrew)


def remove_niqqud_from_last_n_letter(heb_word, n=-1):
    # Removes niqqud from the last n letter of hebrew word.
    # If n == -1 - remove all niqquds
    #
    # Remove all symbols excluding ALPHABET, NIQQUD, MODIFICATORS, LEGATURES, PUNCTUATIONS
    heb_word = ''.join([ch for ch in heb_word if ord(ch) in ALL_HEBREW_UTF_CODES])

    if len(heb_word) <= 1 or n == 0:
        return heb_word

    if n == -1:
        return ''.join([ch for ch in heb_word if ord(ch) not in NIQQUD.keys()])

    reg = re.compile(r'[א-ת][^א-ת]*')
    chars = reg.findall(heb_word)
    lgth = len(chars)
    newchars = [chars[i] if lgth-i > n else remove_niqqud(chars[i]) for i in range(lgth)]
    return ''.join(newchars)


def remove_niqqud_from_last_letter(heb_word):
    # Removes niqqud from the last  letter of hebrew word.
    #
    return remove_niqqud_from_last_n_letter(heb_word, 1)

def hebrew_letters_only(chars):
    # Removes all exclude hebrew letters ALPHABET.
    #
    return ''.join([ch for ch in chars if ord(ch) in ALPHABET.keys()])