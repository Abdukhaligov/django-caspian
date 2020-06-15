from django.core.handlers.base import logger
from django.core.management.base import BaseCommand
import random
from faker import Faker

from django.db import connection

from caspian.models import *

MODE_REFRESH = 'refresh'

MODE_CLEAR = 'clear'


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        # self.stdout.write('seeding data...')
        run_seed(self, options['mode'])


def reset_and_alter_table(model):
    logger.info("Deleting %s" % (model.__name__))
    cursor = connection.cursor()
    model.objects.all().delete()
    sql = "ALTER TABLE %s AUTO_INCREMENT = 1;" % (model._meta.db_table,)
    cursor.execute(sql)


def enter_seeds(model, array):
    logger.info("Creating %s" % (model.__name__))
    model.objects.bulk_create(array)


def create_degrees():
    degrees = [
        Degree(name='PhD'),
        Degree(name='Doctor'),
        Degree(name='Corresponding member'),
        Degree(name='Academician')
    ]

    enter_seeds(Degree, degrees)


def create_regions():
    regions = [
        Region(mask='+247-####', cc='AC', name='Ascension', description='', name_ru='Остров Вознесения',
               description_ru=''),
        Region(mask='+376-###-###', cc='AD', name='Andorra', description='', name_ru='Андорра', description_ru=''),
        Region(mask='+971-5#-###-####', cc='AE', name='United Arab Emirates', description='mobile',
               name_ru='Объединенные Арабские Эмираты', description_ru='мобильные'),
        Region(mask='+971-#-###-####', cc='AE', name='United Arab Emirates', description='',
               name_ru='Объединенные Арабские Эмираты', description_ru=''),
        Region(mask='+93-##-###-####', cc='AF', name='Afghanistan', description='', name_ru='Афганистан',
               description_ru=''),
        Region(mask='+1(268)###-####', cc='AG', name='Antigua & Barbuda', description='', name_ru='Антигуа и Барбуда',
               description_ru=''),
        Region(mask='+1(264)###-####', cc='AI', name='Anguilla', description='', name_ru='Ангилья', description_ru=''),
        Region(mask='+355(###)###-###', cc='AL', name='Albania', description='', name_ru='Албания', description_ru=''),
        Region(mask='+374-##-###-###', cc='AM', name='Armenia', description='', name_ru='Армения', description_ru=''),
        Region(mask='+599-###-####', cc='AN', name='Caribbean Netherlands', description='',
               name_ru='Карибские Нидерланды', description_ru=''),
        Region(mask='+599-###-####', cc='AN', name='Netherlands Antilles', description='',
               name_ru='Нидерландские Антильские острова', description_ru=''),
        Region(mask='+599-9###-####', cc='AN', name='Netherlands Antilles', description='Curacao',
               name_ru='Нидерландские Антильские острова', description_ru='Кюрасао'),
        Region(mask='+244(###)###-###', cc='AO', name='Angola', description='', name_ru='Ангола', description_ru=''),
        Region(mask='+672-1##-###', cc='AQ', name='Australian bases in Antarctica', description='',
               name_ru='Австралийская антарктическая база', description_ru=''),
        Region(mask='+54(###)###-####', cc='AR', name='Argentina', description='', name_ru='Аргентина',
               description_ru=''),
        Region(mask='+1(684)###-####', cc='AS', name='American Samoa', description='', name_ru='Американское Самоа',
               description_ru=''),
        Region(mask='+43(###)###-####', cc='AT', name='Austria', description='', name_ru='Австрия', description_ru=''),
        Region(mask='+61-#-####-####', cc='AU', name='Australia', description='', name_ru='Австралия',
               description_ru=''),
        Region(mask='+297-###-####', cc='AW', name='Aruba', description='', name_ru='Аруба', description_ru=''),
        Region(mask='+994-##-###-##-##', cc='AZ', name='Azerbaijan', description='', name_ru='Азербайджан',
               description_ru=''),
        Region(mask='+387-##-#####', cc='BA', name='Bosnia and Herzegovina', description='',
               name_ru='Босния и Герцеговина', description_ru=''),
        Region(mask='+387-##-####', cc='BA', name='Bosnia and Herzegovina', description='',
               name_ru='Босния и Герцеговина', description_ru=''),
        Region(mask='+1(246)###-####', cc='BB', name='Barbados', description='', name_ru='Барбадос', description_ru=''),
        Region(mask='+880-##-###-###', cc='BD', name='Bangladesh', description='', name_ru='Бангладеш',
               description_ru=''),
        Region(mask='+32(###)###-###', cc='BE', name='Belgium', description='', name_ru='Бельгия', description_ru=''),
        Region(mask='+226-##-##-####', cc='BF', name='Burkina Faso', description='', name_ru='Буркина Фасо',
               description_ru=''),
        Region(mask='+359(###)###-###', cc='BG', name='Bulgaria', description='', name_ru='Болгария',
               description_ru=''),
        Region(mask='+973-####-####', cc='BH', name='Bahrain', description='', name_ru='Бахрейн', description_ru=''),
        Region(mask='+257-##-##-####', cc='BI', name='Burundi', description='', name_ru='Бурунди', description_ru=''),
        Region(mask='+229-##-##-####', cc='BJ', name='Benin', description='', name_ru='Бенин', description_ru=''),
        Region(mask='+1(441)###-####', cc='BM', name='Bermuda', description='', name_ru='Бермудские острова',
               description_ru=''),
        Region(mask='+673-###-####', cc='BN', name='Brunei Darussalam', description='', name_ru='Бруней-Даруссалам',
               description_ru=''),
        Region(mask='+591-#-###-####', cc='BO', name='Bolivia', description='', name_ru='Боливия', description_ru=''),
        Region(mask='+55(##)####-####', cc='BR', name='Brazil', description='', name_ru='Бразилия', description_ru=''),
        Region(mask='+55(##)7###-####', cc='BR', name='Brazil', description='mobile', name_ru='Бразилия',
               description_ru='мобильные'),
        Region(mask='+55(##)9####-####', cc='BR', name='Brazil', description='mobile', name_ru='Бразилия',
               description_ru='мобильные'),
        Region(mask='+1(242)###-####', cc='BS', name='Bahamas', description='', name_ru='Багамские Острова',
               description_ru=''),
        Region(mask='+975-17-###-###', cc='BT', name='Bhutan', description='', name_ru='Бутан', description_ru=''),
        Region(mask='+975-#-###-###', cc='BT', name='Bhutan', description='', name_ru='Бутан', description_ru=''),
        Region(mask='+267-##-###-###', cc='BW', name='Botswana', description='', name_ru='Ботсвана', description_ru=''),
        Region(mask='+375(##)###-##-##', cc='BY', name='Belarus', description='', name_ru='Беларусь (Белоруссия)',
               description_ru=''),
        Region(mask='+501-###-####', cc='BZ', name='Belize', description='', name_ru='Белиз', description_ru=''),
        Region(mask='+243(###)###-###', cc='CD', name='Dem. Rep. Congo', description='',
               name_ru='Дем. Респ. Конго (Киншаса)', description_ru=''),
        Region(mask='+236-##-##-####', cc='CF', name='Central African Republic', description='',
               name_ru='Центральноафриканская Республика', description_ru=''),
        Region(mask='+242-##-###-####', cc='CG', name='Congo (Brazzaville)', description='',
               name_ru='Конго (Браззавиль)', description_ru=''),
        Region(mask='+41-##-###-####', cc='CH', name='Switzerland', description='', name_ru='Швейцария',
               description_ru=''),
        Region(mask='+225-##-###-###', cc='CI', name='Cote d’Ivoire (Ivory Coast)', description='',
               name_ru='Кот-д’Ивуар', description_ru=''),
        Region(mask='+682-##-###', cc='CK', name='Cook Islands', description='', name_ru='Острова Кука',
               description_ru=''),
        Region(mask='+56-#-####-####', cc='CL', name='Chile', description='', name_ru='Чили', description_ru=''),
        Region(mask='+237-####-####', cc='CM', name='Cameroon', description='', name_ru='Камерун', description_ru=''),
        Region(mask='+86(###)####-####', cc='CN', name='China (PRC)', description='', name_ru='Китайская Н.Р.',
               description_ru=''),
        Region(mask='+86(###)####-###', cc='CN', name='China (PRC)', description='', name_ru='Китайская Н.Р.',
               description_ru=''),
        Region(mask='+86-##-#####-#####', cc='CN', name='China (PRC)', description='', name_ru='Китайская Н.Р.',
               description_ru=''),
        Region(mask='+57(###)###-####', cc='CO', name='Colombia', description='', name_ru='Колумбия',
               description_ru=''),
        Region(mask='+506-####-####', cc='CR', name='Costa Rica', description='', name_ru='Коста-Рика',
               description_ru=''),
        Region(mask='+53-#-###-####', cc='CU', name='Cuba', description='', name_ru='Куба', description_ru=''),
        Region(mask='+238(###)##-##', cc='CV', name='Cape Verde', description='', name_ru='Кабо-Верде',
               description_ru=''),
        Region(mask='+599-###-####', cc='CW', name='Curacao', description='', name_ru='Кюрасао', description_ru=''),
        Region(mask='+357-##-###-###', cc='CY', name='Cyprus', description='', name_ru='Кипр', description_ru=''),
        Region(mask='+420(###)###-###', cc='CZ', name='Czech Republic', description='', name_ru='Чехия',
               description_ru=''),
        Region(mask='+49(####)###-####', cc='DE', name='Germany', description='', name_ru='Германия',
               description_ru=''),
        Region(mask='+49(###)###-####', cc='DE', name='Germany', description='', name_ru='Германия', description_ru=''),
        Region(mask='+49(###)##-####', cc='DE', name='Germany', description='', name_ru='Германия', description_ru=''),
        Region(mask='+49(###)##-###', cc='DE', name='Germany', description='', name_ru='Германия', description_ru=''),
        Region(mask='+49(###)##-##', cc='DE', name='Germany', description='', name_ru='Германия', description_ru=''),
        Region(mask='+49-###-###', cc='DE', name='Germany', description='', name_ru='Германия', description_ru=''),
        Region(mask='+253-##-##-##-##', cc='DJ', name='Djibouti', description='', name_ru='Джибути', description_ru=''),
        Region(mask='+45-##-##-##-##', cc='DK', name='Denmark', description='', name_ru='Дания', description_ru=''),
        Region(mask='+1(767)###-####', cc='DM', name='Dominica', description='', name_ru='Доминика', description_ru=''),
        Region(mask='+1(809)###-####', cc='DO', name='Dominican Republic', description='',
               name_ru='Доминиканская Республика', description_ru=''),
        Region(mask='+1(829)###-####', cc='DO', name='Dominican Republic', description='',
               name_ru='Доминиканская Республика', description_ru=''),
        Region(mask='+1(849)###-####', cc='DO', name='Dominican Republic', description='',
               name_ru='Доминиканская Республика', description_ru=''),
        Region(mask='+213-##-###-####', cc='DZ', name='Algeria', description='', name_ru='Алжир', description_ru=''),
        Region(mask='+593-##-###-####', cc='EC', name='Ecuador ', description='mobile', name_ru='Эквадор ',
               description_ru='мобильные'),
        Region(mask='+593-#-###-####', cc='EC', name='Ecuador', description='', name_ru='Эквадор', description_ru=''),
        Region(mask='+372-####-####', cc='EE', name='Estonia ', description='mobile', name_ru='Эстония ',
               description_ru='мобильные'),
        Region(mask='+372-###-####', cc='EE', name='Estonia', description='', name_ru='Эстония', description_ru=''),
        Region(mask='+20(###)###-####', cc='EG', name='Egypt', description='', name_ru='Египет', description_ru=''),
        Region(mask='+291-#-###-###', cc='ER', name='Eritrea', description='', name_ru='Эритрея', description_ru=''),
        Region(mask='+34(###)###-###', cc='ES', name='Spain', description='', name_ru='Испания', description_ru=''),
        Region(mask='+251-##-###-####', cc='ET', name='Ethiopia', description='', name_ru='Эфиопия', description_ru=''),
        Region(mask='+358(###)###-##-##', cc='FI', name='Finland', description='', name_ru='Финляндия',
               description_ru=''),
        Region(mask='+679-##-#####', cc='FJ', name='Fiji', description='', name_ru='Фиджи', description_ru=''),
        Region(mask='+500-#####', cc='FK', name='Falkland Islands', description='', name_ru='Фолклендские острова',
               description_ru=''),
        Region(mask='+691-###-####', cc='FM', name='F.S. Micronesia', description='', name_ru='Ф.Ш. Микронезии',
               description_ru=''),
        Region(mask='+298-###-###', cc='FO', name='Faroe Islands', description='', name_ru='Фарерские острова',
               description_ru=''),
        Region(mask='+262-#####-####', cc='FR', name='Mayotte', description='', name_ru='Майотта', description_ru=''),
        Region(mask='+33(###)###-###', cc='FR', name='France', description='', name_ru='Франция', description_ru=''),
        Region(mask='+508-##-####', cc='FR', name='St Pierre & Miquelon', description='', name_ru='Сен-Пьер и Микелон',
               description_ru=''),
        Region(mask='+590(###)###-###', cc='FR', name='Guadeloupe', description='', name_ru='Гваделупа',
               description_ru=''),
        Region(mask='+241-#-##-##-##', cc='GA', name='Gabon', description='', name_ru='Габон', description_ru=''),
        Region(mask='+1(473)###-####', cc='GD', name='Grenada', description='', name_ru='Гренада', description_ru=''),
        Region(mask='+995(###)###-###', cc='GE', name='Rep. of Georgia', description='', name_ru='Грузия',
               description_ru=''),
        Region(mask='+594-#####-####', cc='GF', name='Guiana (French)', description='', name_ru='Фр. Гвиана',
               description_ru=''),
        Region(mask='+233(###)###-###', cc='GH', name='Ghana', description='', name_ru='Гана', description_ru=''),
        Region(mask='+350-###-#####', cc='GI', name='Gibraltar', description='', name_ru='Гибралтар',
               description_ru=''),
        Region(mask='+299-##-##-##', cc='GL', name='Greenland', description='', name_ru='Гренландия',
               description_ru=''),
        Region(mask='+220(###)##-##', cc='GM', name='Gambia', description='', name_ru='Гамбия', description_ru=''),
        Region(mask='+224-##-###-###', cc='GN', name='Guinea', description='', name_ru='Гвинея', description_ru=''),
        Region(mask='+240-##-###-####', cc='GQ', name='Equatorial Guinea', description='',
               name_ru='Экваториальная Гвинея', description_ru=''),
        Region(mask='+30(###)###-####', cc='GR', name='Greece', description='', name_ru='Греция', description_ru=''),
        Region(mask='+502-#-###-####', cc='GT', name='Guatemala', description='', name_ru='Гватемала',
               description_ru=''),
        Region(mask='+1(671)###-####', cc='GU', name='Guam', description='', name_ru='Гуам', description_ru=''),
        Region(mask='+245-#-######', cc='GW', name='Guinea-Bissau', description='', name_ru='Гвинея-Бисау',
               description_ru=''),
        Region(mask='+592-###-####', cc='GY', name='Guyana', description='', name_ru='Гайана', description_ru=''),
        Region(mask='+852-####-####', cc='HK', name='Hong Kong', description='', name_ru='Гонконг', description_ru=''),
        Region(mask='+504-####-####', cc='HN', name='Honduras', description='', name_ru='Гондурас', description_ru=''),
        Region(mask='+385-##-###-###', cc='HR', name='Croatia', description='', name_ru='Хорватия', description_ru=''),
        Region(mask='+509-##-##-####', cc='HT', name='Haiti', description='', name_ru='Гаити', description_ru=''),
        Region(mask='+36(###)###-###', cc='HU', name='Hungary', description='', name_ru='Венгрия', description_ru=''),
        Region(mask='+62(8##)###-####', cc='ID', name='Indonesia ', description='mobile', name_ru='Индонезия ',
               description_ru='мобильные'),
        Region(mask='+62-##-###-##', cc='ID', name='Indonesia', description='', name_ru='Индонезия', description_ru=''),
        Region(mask='+62-##-###-###', cc='ID', name='Indonesia', description='', name_ru='Индонезия',
               description_ru=''),
        Region(mask='+62-##-###-####', cc='ID', name='Indonesia', description='', name_ru='Индонезия',
               description_ru=''),
        Region(mask='+62(8##)###-###', cc='ID', name='Indonesia ', description='mobile', name_ru='Индонезия ',
               description_ru='мобильные'),
        Region(mask='+62(8##)###-##-###', cc='ID', name='Indonesia ', description='mobile', name_ru='Индонезия ',
               description_ru='мобильные'),
        Region(mask='+353(###)###-###', cc='IE', name='Ireland', description='', name_ru='Ирландия', description_ru=''),
        Region(mask='+972-5#-###-####', cc='IL', name='Israel ', description='mobile', name_ru='Израиль ',
               description_ru='мобильные'),
        Region(mask='+972-#-###-####', cc='IL', name='Israel', description='', name_ru='Израиль', description_ru=''),
        Region(mask='+91(####)###-###', cc='IN', name='India', description='', name_ru='Индия', description_ru=''),
        Region(mask='+246-###-####', cc='IO', name='Diego Garcia', description='', name_ru='Диего-Гарсия',
               description_ru=''),
        Region(mask='+964(###)###-####', cc='IQ', name='Iraq', description='', name_ru='Ирак', description_ru=''),
        Region(mask='+98(###)###-####', cc='IR', name='Iran', description='', name_ru='Иран', description_ru=''),
        Region(mask='+354-###-####', cc='IS', name='Iceland', description='', name_ru='Исландия', description_ru=''),
        Region(mask='+39(###)####-###', cc='IT', name='Italy', description='', name_ru='Италия', description_ru=''),
        Region(mask='+1(876)###-####', cc='JM', name='Jamaica', description='', name_ru='Ямайка', description_ru=''),
        Region(mask='+962-#-####-####', cc='JO', name='Jordan', description='', name_ru='Иордания', description_ru=''),
        Region(mask='+81-##-####-####', cc='JP', name='Japan ', description='mobile', name_ru='Япония ',
               description_ru='мобильные'),
        Region(mask='+81(###)###-###', cc='JP', name='Japan', description='', name_ru='Япония', description_ru=''),
        Region(mask='+254-###-######', cc='KE', name='Kenya', description='', name_ru='Кения', description_ru=''),
        Region(mask='+996(###)###-###', cc='KG', name='Kyrgyzstan', description='', name_ru='Киргизия',
               description_ru=''),
        Region(mask='+855-##-###-###', cc='KH', name='Cambodia', description='', name_ru='Камбоджа', description_ru=''),
        Region(mask='+686-##-###', cc='KI', name='Kiribati', description='', name_ru='Кирибати', description_ru=''),
        Region(mask='+269-##-#####', cc='KM', name='Comoros', description='', name_ru='Коморы', description_ru=''),
        Region(mask='+1(869)###-####', cc='KN', name='Saint Kitts & Nevis', description='', name_ru='Сент-Китс и Невис',
               description_ru=''),
        Region(mask='+850-191-###-####', cc='KP', name='DPR Korea (North) ', description='mobile',
               name_ru='Корейская НДР ', description_ru='мобильные'),
        Region(mask='+850-##-###-###', cc='KP', name='DPR Korea (North)', description='', name_ru='Корейская НДР',
               description_ru=''),
        Region(mask='+850-###-####-###', cc='KP', name='DPR Korea (North)', description='', name_ru='Корейская НДР',
               description_ru=''),
        Region(mask='+850-###-###', cc='KP', name='DPR Korea (North)', description='', name_ru='Корейская НДР',
               description_ru=''),
        Region(mask='+850-####-####', cc='KP', name='DPR Korea (North)', description='', name_ru='Корейская НДР',
               description_ru=''),
        Region(mask='+850-####-#############', cc='KP', name='DPR Korea (North)', description='',
               name_ru='Корейская НДР', description_ru=''),
        Region(mask='+82-##-###-####', cc='KR', name='Korea (South)', description='', name_ru='Респ. Корея',
               description_ru=''),
        Region(mask='+965-####-####', cc='KW', name='Kuwait', description='', name_ru='Кувейт', description_ru=''),
        Region(mask='+1(345)###-####', cc='KY', name='Cayman Islands', description='', name_ru='Каймановы острова',
               description_ru=''),
        Region(mask='+7(6##)###-##-##', cc='KZ', name='Kazakhstan', description='', name_ru='Казахстан',
               description_ru=''),
        Region(mask='+7(7##)###-##-##', cc='KZ', name='Kazakhstan', description='', name_ru='Казахстан',
               description_ru=''),
        Region(mask='+856(20##)###-###', cc='LA', name='Laos ', description='mobile', name_ru='Лаос ',
               description_ru='мобильные'),
        Region(mask='+856-##-###-###', cc='LA', name='Laos', description='', name_ru='Лаос', description_ru=''),
        Region(mask='+961-##-###-###', cc='LB', name='Lebanon ', description='mobile', name_ru='Ливан ',
               description_ru='мобильные'),
        Region(mask='+961-#-###-###', cc='LB', name='Lebanon', description='', name_ru='Ливан', description_ru=''),
        Region(mask='+1(758)###-####', cc='LC', name='Saint Lucia', description='', name_ru='Сент-Люсия',
               description_ru=''),
        Region(mask='+423(###)###-####', cc='LI', name='Liechtenstein', description='', name_ru='Лихтенштейн',
               description_ru=''),
        Region(mask='+94-##-###-####', cc='LK', name='Sri Lanka', description='', name_ru='Шри-Ланка',
               description_ru=''),
        Region(mask='+231-##-###-###', cc='LR', name='Liberia', description='', name_ru='Либерия', description_ru=''),
        Region(mask='+266-#-###-####', cc='LS', name='Lesotho', description='', name_ru='Лесото', description_ru=''),
        Region(mask='+370(###)##-###', cc='LT', name='Lithuania', description='', name_ru='Литва', description_ru=''),
        Region(mask='+352(###)###-###', cc='LU', name='Luxembourg', description='', name_ru='Люксембург',
               description_ru=''),
        Region(mask='+371-##-###-###', cc='LV', name='Latvia', description='', name_ru='Латвия', description_ru=''),
        Region(mask='+218-##-###-###', cc='LY', name='Libya', description='', name_ru='Ливия', description_ru=''),
        Region(mask='+218-21-###-####', cc='LY', name='Libya', description='Tripoli', name_ru='Ливия',
               description_ru='Триполи'),
        Region(mask='+212-##-####-###', cc='MA', name='Morocco', description='', name_ru='Марокко', description_ru=''),
        Region(mask='+377(###)###-###', cc='MC', name='Monaco', description='', name_ru='Монако', description_ru=''),
        Region(mask='+377-##-###-###', cc='MC', name='Monaco', description='', name_ru='Монако', description_ru=''),
        Region(mask='+373-####-####', cc='MD', name='Moldova', description='', name_ru='Молдова', description_ru=''),
        Region(mask='+382-##-###-###', cc='ME', name='Montenegro', description='', name_ru='Черногория',
               description_ru=''),
        Region(mask='+261-##-##-#####', cc='MG', name='Madagascar', description='', name_ru='Мадагаскар',
               description_ru=''),
        Region(mask='+692-###-####', cc='MH', name='Marshall Islands', description='', name_ru='Маршалловы Острова',
               description_ru=''),
        Region(mask='+389-##-###-###', cc='MK', name='Republic of Macedonia', description='', name_ru='Респ. Македония',
               description_ru=''),
        Region(mask='+223-##-##-####', cc='ML', name='Mali', description='', name_ru='Мали', description_ru=''),
        Region(mask='+95-##-###-###', cc='MM', name='Burma (Myanmar)', description='', name_ru='Бирма (Мьянма)',
               description_ru=''),
        Region(mask='+95-#-###-###', cc='MM', name='Burma (Myanmar)', description='', name_ru='Бирма (Мьянма)',
               description_ru=''),
        Region(mask='+95-###-###', cc='MM', name='Burma (Myanmar)', description='', name_ru='Бирма (Мьянма)',
               description_ru=''),
        Region(mask='+976-##-##-####', cc='MN', name='Mongolia', description='', name_ru='Монголия', description_ru=''),
        Region(mask='+853-####-####', cc='MO', name='Macau', description='', name_ru='Макао', description_ru=''),
        Region(mask='+1(670)###-####', cc='MP', name='Northern Mariana Islands', description='',
               name_ru='Северные Марианские острова Сайпан', description_ru=''),
        Region(mask='+596(###)##-##-##', cc='MQ', name='Martinique', description='', name_ru='Мартиника',
               description_ru=''),
        Region(mask='+222-##-##-####', cc='MR', name='Mauritania', description='', name_ru='Мавритания',
               description_ru=''),
        Region(mask='+1(664)###-####', cc='MS', name='Montserrat', description='', name_ru='Монтсеррат',
               description_ru=''),
        Region(mask='+356-####-####', cc='MT', name='Malta', description='', name_ru='Мальта', description_ru=''),
        Region(mask='+230-###-####', cc='MU', name='Mauritius', description='', name_ru='Маврикий', description_ru=''),
        Region(mask='+960-###-####', cc='MV', name='Maldives', description='', name_ru='Мальдивские острова',
               description_ru=''),
        Region(mask='+265-1-###-###', cc='MW', name='Malawi', description='Telecom Ltd', name_ru='Малави',
               description_ru='Telecom Ltd'),
        Region(mask='+265-#-####-####', cc='MW', name='Malawi', description='', name_ru='Малави', description_ru=''),
        Region(mask='+52(###)###-####', cc='MX', name='Mexico', description='', name_ru='Мексика', description_ru=''),
        Region(mask='+52-##-##-####', cc='MX', name='Mexico', description='', name_ru='Мексика', description_ru=''),
        Region(mask='+60-##-###-####', cc='MY', name='Malaysia ', description='mobile', name_ru='Малайзия ',
               description_ru='мобильные'),
        Region(mask='+60(###)###-###', cc='MY', name='Malaysia', description='', name_ru='Малайзия', description_ru=''),
        Region(mask='+60-##-###-###', cc='MY', name='Malaysia', description='', name_ru='Малайзия', description_ru=''),
        Region(mask='+60-#-###-###', cc='MY', name='Malaysia', description='', name_ru='Малайзия', description_ru=''),
        Region(mask='+258-##-###-###', cc='MZ', name='Mozambique', description='', name_ru='Мозамбик',
               description_ru=''),
        Region(mask='+264-##-###-####', cc='NA', name='Namibia', description='', name_ru='Намибия', description_ru=''),
        Region(mask='+687-##-####', cc='NC', name='New Caledonia', description='', name_ru='Новая Каледония',
               description_ru=''),
        Region(mask='+227-##-##-####', cc='NE', name='Niger', description='', name_ru='Нигер', description_ru=''),
        Region(mask='+672-3##-###', cc='NF', name='Norfolk Island', description='', name_ru='Норфолк (остров)',
               description_ru=''),
        Region(mask='+234(###)###-####', cc='NG', name='Nigeria', description='', name_ru='Нигерия', description_ru=''),
        Region(mask='+234-##-###-###', cc='NG', name='Nigeria', description='', name_ru='Нигерия', description_ru=''),
        Region(mask='+234-##-###-##', cc='NG', name='Nigeria', description='', name_ru='Нигерия', description_ru=''),
        Region(mask='+234(###)###-####', cc='NG', name='Nigeria ', description='mobile', name_ru='Нигерия ',
               description_ru='мобильные'),
        Region(mask='+505-####-####', cc='NI', name='Nicaragua', description='', name_ru='Никарагуа',
               description_ru=''),
        Region(mask='+31-##-###-####', cc='NL', name='Netherlands', description='', name_ru='Нидерланды',
               description_ru=''),
        Region(mask='+47(###)##-###', cc='NO', name='Norway', description='', name_ru='Норвегия', description_ru=''),
        Region(mask='+977-##-###-###', cc='NP', name='Nepal', description='', name_ru='Непал', description_ru=''),
        Region(mask='+674-###-####', cc='NR', name='Nauru', description='', name_ru='Науру', description_ru=''),
        Region(mask='+683-####', cc='NU', name='Niue', description='', name_ru='Ниуэ', description_ru=''),
        Region(mask='+64(###)###-###', cc='NZ', name='New Zealand', description='', name_ru='Новая Зеландия',
               description_ru=''),
        Region(mask='+64-##-###-###', cc='NZ', name='New Zealand', description='', name_ru='Новая Зеландия',
               description_ru=''),
        Region(mask='+64(###)###-####', cc='NZ', name='New Zealand', description='', name_ru='Новая Зеландия',
               description_ru=''),
        Region(mask='+968-##-###-###', cc='OM', name='Oman', description='', name_ru='Оман', description_ru=''),
        Region(mask='+507-###-####', cc='PA', name='Panama', description='', name_ru='Панама', description_ru=''),
        Region(mask='+51(###)###-###', cc='PE', name='Peru', description='', name_ru='Перу', description_ru=''),
        Region(mask='+689-##-##-##', cc='PF', name='French Polynesia', description='',
               name_ru='Французская Полинезия (Таити)', description_ru=''),
        Region(mask='+675(###)##-###', cc='PG', name='Papua New Guinea', description='', name_ru='Папуа-Новая Гвинея',
               description_ru=''),
        Region(mask='+63(###)###-####', cc='PH', name='Philippines', description='', name_ru='Филиппины',
               description_ru=''),
        Region(mask='+92(###)###-####', cc='PK', name='Pakistan', description='', name_ru='Пакистан',
               description_ru=''),
        Region(mask='+48(###)###-###', cc='PL', name='Poland', description='', name_ru='Польша', description_ru=''),
        Region(mask='+970-##-###-####', cc='PS', name='Palestine', description='', name_ru='Палестина',
               description_ru=''),
        Region(mask='+351-##-###-####', cc='PT', name='Portugal', description='', name_ru='Португалия',
               description_ru=''),
        Region(mask='+680-###-####', cc='PW', name='Palau', description='', name_ru='Палау', description_ru=''),
        Region(mask='+595(###)###-###', cc='PY', name='Paraguay', description='', name_ru='Парагвай',
               description_ru=''),
        Region(mask='+974-####-####', cc='QA', name='Qatar', description='', name_ru='Катар', description_ru=''),
        Region(mask='+262-#####-####', cc='RE', name='Reunion', description='', name_ru='Реюньон', description_ru=''),
        Region(mask='+40-##-###-####', cc='RO', name='Romania', description='', name_ru='Румыния', description_ru=''),
        Region(mask='+381-##-###-####', cc='RS', name='Serbia', description='', name_ru='Сербия', description_ru=''),
        Region(mask='+7(###)###-##-##', cc='RU', name='Russia', description='', name_ru='Россия', description_ru=''),
        Region(mask='+250(###)###-###', cc='RW', name='Rwanda', description='', name_ru='Руанда', description_ru=''),
        Region(mask='+966-5-####-####', cc='SA', name='Saudi Arabia ', description='mobile',
               name_ru='Саудовская Аравия ', description_ru='мобильные'),
        Region(mask='+966-#-###-####', cc='SA', name='Saudi Arabia', description='', name_ru='Саудовская Аравия',
               description_ru=''),
        Region(mask='+677-###-####', cc='SB', name='Solomon Islands ', description='mobile',
               name_ru='Соломоновы Острова ', description_ru='мобильные'),
        Region(mask='+677-#####', cc='SB', name='Solomon Islands', description='', name_ru='Соломоновы Острова',
               description_ru=''),
        Region(mask='+248-#-###-###', cc='SC', name='Seychelles', description='', name_ru='Сейшелы', description_ru=''),
        Region(mask='+249-##-###-####', cc='SD', name='Sudan', description='', name_ru='Судан', description_ru=''),
        Region(mask='+46-##-###-####', cc='SE', name='Sweden', description='', name_ru='Швеция', description_ru=''),
        Region(mask='+65-####-####', cc='SG', name='Singapore', description='', name_ru='Сингапур', description_ru=''),
        Region(mask='+290-####', cc='SH', name='Saint Helena', description='', name_ru='Остров Святой Елены',
               description_ru=''),
        Region(mask='+290-####', cc='SH', name='Tristan da Cunha', description='', name_ru='Тристан-да-Кунья',
               description_ru=''),
        Region(mask='+386-##-###-###', cc='SI', name='Slovenia', description='', name_ru='Словения', description_ru=''),
        Region(mask='+421(###)###-###', cc='SK', name='Slovakia', description='', name_ru='Словакия',
               description_ru=''),
        Region(mask='+232-##-######', cc='SL', name='Sierra Leone', description='', name_ru='Сьерра-Леоне',
               description_ru=''),
        Region(mask='+378-####-######', cc='SM', name='San Marino', description='', name_ru='Сан-Марино',
               description_ru=''),
        Region(mask='+221-##-###-####', cc='SN', name='Senegal', description='', name_ru='Сенегал', description_ru=''),
        Region(mask='+252-##-###-###', cc='SO', name='Somalia', description='', name_ru='Сомали', description_ru=''),
        Region(mask='+252-#-###-###', cc='SO', name='Somalia', description='', name_ru='Сомали', description_ru=''),
        Region(mask='+252-#-###-###', cc='SO', name='Somalia ', description='mobile', name_ru='Сомали ',
               description_ru='мобильные'),
        Region(mask='+597-###-####', cc='SR', name='Suriname ', description='mobile', name_ru='Суринам ',
               description_ru='мобильные'),
        Region(mask='+597-###-###', cc='SR', name='Suriname', description='', name_ru='Суринам', description_ru=''),
        Region(mask='+211-##-###-####', cc='SS', name='South Sudan', description='', name_ru='Южный Судан',
               description_ru=''),
        Region(mask='+239-##-#####', cc='ST', name='Sao Tome and Principe', description='',
               name_ru='Сан-Томе и Принсипи', description_ru=''),
        Region(mask='+503-##-##-####', cc='SV', name='El Salvador', description='', name_ru='Сальвадор',
               description_ru=''),
        Region(mask='+1(721)###-####', cc='SX', name='Sint Maarten', description='', name_ru='Синт-Маартен',
               description_ru=''),
        Region(mask='+963-##-####-###', cc='SY', name='Syrian Arab Republic', description='',
               name_ru='Сирийская арабская республика', description_ru=''),
        Region(mask='+268-##-##-####', cc='SZ', name='Swaziland', description='', name_ru='Свазиленд',
               description_ru=''),
        Region(mask='+1(649)###-####', cc='TC', name='Turks & Caicos', description='', name_ru='Тёркс и Кайкос',
               description_ru=''),
        Region(mask='+235-##-##-##-##', cc='TD', name='Chad', description='', name_ru='Чад', description_ru=''),
        Region(mask='+228-##-###-###', cc='TG', name='Togo', description='', name_ru='Того', description_ru=''),
        Region(mask='+66-##-###-####', cc='TH', name='Thailand ', description='mobile', name_ru='Таиланд ',
               description_ru='мобильные'),
        Region(mask='+66-##-###-###', cc='TH', name='Thailand', description='', name_ru='Таиланд', description_ru=''),
        Region(mask='+992-##-###-####', cc='TJ', name='Tajikistan', description='', name_ru='Таджикистан',
               description_ru=''),
        Region(mask='+690-####', cc='TK', name='Tokelau', description='', name_ru='Токелау', description_ru=''),
        Region(mask='+670-###-####', cc='TL', name='East Timor', description='', name_ru='Восточный Тимор',
               description_ru=''),
        Region(mask='+670-77#-#####', cc='TL', name='East Timor', description='Timor Telecom',
               name_ru='Восточный Тимор', description_ru='Timor Telecom'),
        Region(mask='+670-78#-#####', cc='TL', name='East Timor', description='Timor Telecom',
               name_ru='Восточный Тимор', description_ru='Timor Telecom'),
        Region(mask='+993-#-###-####', cc='TM', name='Turkmenistan', description='', name_ru='Туркменистан',
               description_ru=''),
        Region(mask='+216-##-###-###', cc='TN', name='Tunisia', description='', name_ru='Тунис', description_ru=''),
        Region(mask='+676-#####', cc='TO', name='Tonga', description='', name_ru='Тонга', description_ru=''),
        Region(mask='+90(###)###-####', cc='TR', name='Turkey', description='', name_ru='Турция', description_ru=''),
        Region(mask='+1(868)###-####', cc='TT', name='Trinidad & Tobago', description='', name_ru='Тринидад и Тобаго',
               description_ru=''),
        Region(mask='+688-90####', cc='TV', name='Tuvalu ', description='mobile', name_ru='Тувалу ',
               description_ru='мобильные'),
        Region(mask='+688-2####', cc='TV', name='Tuvalu', description='', name_ru='Тувалу', description_ru=''),
        Region(mask='+886-#-####-####', cc='TW', name='Taiwan', description='', name_ru='Тайвань', description_ru=''),
        Region(mask='+886-####-####', cc='TW', name='Taiwan', description='', name_ru='Тайвань', description_ru=''),
        Region(mask='+255-##-###-####', cc='TZ', name='Tanzania', description='', name_ru='Танзания',
               description_ru=''),
        Region(mask='+380(##)###-##-##', cc='UA', name='Ukraine', description='', name_ru='Украина', description_ru=''),
        Region(mask='+256(###)###-###', cc='UG', name='Uganda', description='', name_ru='Уганда', description_ru=''),
        Region(mask='+44-##-####-####', cc='UK', name='United Kingdom', description='', name_ru='Великобритания',
               description_ru=''),
        Region(mask='+598-#-###-##-##', cc='UY', name='Uruguay', description='', name_ru='Уругвай', description_ru=''),
        Region(mask='+998-##-###-####', cc='UZ', name='Uzbekistan', description='', name_ru='Узбекистан',
               description_ru=''),
        Region(mask='+39-6-698-#####', cc='VA', name='Vatican City', description='', name_ru='Ватикан',
               description_ru=''),
        Region(mask='+1(784)###-####', cc='VC', name='Saint Vincent & the Grenadines', description='',
               name_ru='Сент-Винсент и Гренадины', description_ru=''),
        Region(mask='+58(###)###-####', cc='VE', name='Venezuela', description='', name_ru='Венесуэла',
               description_ru=''),
        Region(mask='+1(284)###-####', cc='VG', name='British Virgin Islands', description='',
               name_ru='Британские Виргинские острова', description_ru=''),
        Region(mask='+1(340)###-####', cc='VI', name='US Virgin Islands', description='',
               name_ru='Американские Виргинские острова', description_ru=''),
        Region(mask='+84-##-####-###', cc='VN', name='Vietnam', description='', name_ru='Вьетнам', description_ru=''),
        Region(mask='+84(###)####-###', cc='VN', name='Vietnam', description='', name_ru='Вьетнам', description_ru=''),
        Region(mask='+678-##-#####', cc='VU', name='Vanuatu ', description='mobile', name_ru='Вануату ',
               description_ru='мобильные'),
        Region(mask='+678-#####', cc='VU', name='Vanuatu', description='', name_ru='Вануату', description_ru=''),
        Region(mask='+681-##-####', cc='WF', name='Wallis and Futuna', description='', name_ru='Уоллис и Футуна',
               description_ru=''),
        Region(mask='+685-##-####', cc='WS', name='Samoa', description='', name_ru='Самоа', description_ru=''),
        Region(mask='+967-###-###-###', cc='YE', name='Yemen ', description='mobile', name_ru='Йемен ',
               description_ru='мобильные'),
        Region(mask='+967-#-###-###', cc='YE', name='Yemen', description='', name_ru='Йемен', description_ru=''),
        Region(mask='+967-##-###-###', cc='YE', name='Yemen', description='', name_ru='Йемен', description_ru=''),
        Region(mask='+27-##-###-####', cc='ZA', name='South Africa', description='', name_ru='Южно-Африканская Респ.',
               description_ru=''),
        Region(mask='+260-##-###-####', cc='ZM', name='Zambia', description='', name_ru='Замбия', description_ru=''),
        Region(mask='+263-#-######', cc='ZW', name='Zimbabwe', description='', name_ru='Зимбабве', description_ru=''),
        Region(mask='+1(###)###-####', cc='US', name='USA', description='', name_ru='США', description_ru=''),
        Region(mask='+1(###)###-####', cc='CA', name='Canada', description='', name_ru='Канада', description_ru='')
    ]

    enter_seeds(Region, regions)


def create_references():
    references = [
        Reference(name='Email Newsletter'),
        Reference(name='Partners / Acquaintances'),
        Reference(name='Online advertising'),
        Reference(name='Social network advertising'),
        Reference(name='Advertising mail'),
        Reference(name='Another')
    ]

    enter_seeds(Reference, references)


def create_users():
    users = []

    for x in range(68):
        if x < 3:
            rank = 1
        elif x < 3 + 5:
            rank = 2
        elif x < 3 + 5 + 13:
            rank = 3
        else:
            rank = 0

        users.append(
            User(
                name=Faker().name(),
                description=Faker().paragraph(),
                email=Faker().safe_email(),  # Uncomment email field into Models
                company=Faker().company(),
                position=Faker().job(),
                phone="994" + random.choice(["55", "50", "51", "70", "77"]) + str(random.randint(1234567, 9876532)),
                reference=random.choice(Reference.objects.all()),
                degree=random.choice(Degree.objects.all()),
                region=Region.objects.get(id=20),
                rank=rank
            ),
        )

    enter_seeds(User, users)


def create_topics():
    topics = [
        Topic(name='Культурно-историческое наследие: история и современность', description=Faker().paragraph()),
        Topic(name='Интеграционные процессы и право', description=Faker().paragraph()),
        Topic(name='Экономическая безопасность', description=Faker().paragraph()),
        Topic(name='Агропромышленный комплекс', description=Faker().paragraph()),
        Topic(name='Эколого-биологические вопросы использования природных ресурсов', description=Faker().paragraph()),
        Topic(name='Современная медицина: новые подходы и актуальные исследования', description=Faker().paragraph()),
        Topic(name='Вопросы технических и физико-математических наук в свете современных интеграционных процессов',
              description=Faker().paragraph()),
        Topic(name='Наука и образование', description=Faker().paragraph()),
    ]

    enter_seeds(Topic, topics)
    subtopics = []

    for x in range(10):
        subtopics.append(
            Topic(name=Faker().sentence(), description=Faker().paragraph(),
                  topic=random.choice(Topic.objects.all()))
        )

    enter_seeds(Topic, subtopics)


def create_memberships():
    memberships = [
        Membership(name='Speaker', reporter=1),
        Membership(name='Poster', reporter=1),
        Membership(name='Listener', reporter=0),
        Membership(name='Media', reporter=0),
        Membership(name='Accompanying', reporter=0),
        Membership(name='Guest', reporter=0),
        Membership(name='Poster', reporter=0),
    ]

    enter_seeds(Membership, memberships)


def create_events():
    events = []

    for x in range(10):
        events.append(
            Event(name=Faker().sentence(),
                  description=Faker().paragraph(),
                  address=Faker().address(),
                  date=Faker().date_time_between(start_date='+2d', end_date='+2M'),
                  active=0)
        )

    enter_seeds(Event, events)


def run_seed(self, mode):
    """ Seed database based on mode
        :param self:
        :param mode: refresh / clear
        :return:
        """
    # Clear data from tables
    reset_and_alter_table(Degree)
    reset_and_alter_table(Reference)
    reset_and_alter_table(Region)
    reset_and_alter_table(User)
    reset_and_alter_table(Topic)
    reset_and_alter_table(Membership)
    reset_and_alter_table(Event)

    if mode == MODE_CLEAR:
        return

    create_degrees()
    create_references()
    create_regions()
    create_users()
    create_topics()
    create_memberships()
    create_events()
