import unittest
from Controller import Finder



class MyTestCase(unittest.TestCase):
    # Test all the given Use Cases
    def test_find_1(self):
        """
        Test this Name: Frau Sandra Berger
        """
        person = Finder.find('Frau Sandra Berger')
        self.assertEqual(person.gender, 'weiblich')
        self.assertEqual(person.salutation, 'Frau')
        self.assertEqual(person.titles, [])
        self.assertEqual(person.prename, 'Sandra')
        self.assertEqual(person.name, 'Berger')
        self.assertEqual(person.name_extra, None)

    def test_find_2(self):
        """
        Test this Name: Herr Dr. Sandro Gutmensch
        """
        person = Finder.find('Herr Dr. Sandro Gutmensch')
        self.assertEqual(person.gender, 'männlich')
        self.assertEqual(person.salutation, 'Herr')
        self.assertEqual(person.titles, ['Dr.'])
        self.assertEqual(person.prename, "Sandro")
        self.assertEqual(person.name, "Gutmensch")
        self.assertEqual(person.name_extra, None)

    def test_find_3(self):
        """
        Test this Name: Professor Heinreich Freiherr vom Wald
        """
        person = Finder.find('Professor Heinreich Freiherr vom Wald')
        self.assertEqual(person.gender, None)
        self.assertEqual(person.salutation, None)
        self.assertEqual(person.titles, ['Professor'])
        self.assertEqual(person.prename, 'Heinreich')
        self.assertEqual(person.name, 'Wald')
        self.assertEqual(person.name_extra, 'Freiherr vom')

    def test_find_4(self):
        """
        Test this Name: Mrs. Doreen Faber
        """
        person = Finder.find('Mrs. Doreen Faber')
        self.assertEqual(person.gender, 'weiblich')
        self.assertEqual(person.salutation, 'Mrs.')
        self.assertEqual(person.titles, [])
        self.assertEqual(person.prename, 'Doreen')
        self.assertEqual(person.name, 'Faber')
        self.assertEqual(person.name_extra, None)

    def test_find_5(self):
        """
        Test this Name: Mme. Charlotte Noir
        """
        person = Finder.find('Mme. Charlotte Noir')
        self.assertEqual(person.gender, 'weiblich')
        self.assertEqual(person.salutation, 'Mme.')
        self.assertEqual(person.titles, [])
        self.assertEqual(person.prename, 'Charlotte')
        self.assertEqual(person.name, 'Noir')
        self.assertEqual(person.name_extra, None)

    def test_find_6(self):
        """
        Test this Name: Estobar y Gonzales
        This name is not even correct (y is used only in strict formal when dividing two surnames)
        """
        person = Finder.find('Estobar y Gonzales')
        self.assertEqual(person.gender, None)
        self.assertEqual(person.salutation, None)
        self.assertEqual(person.titles, [])
        self.assertEqual(person.prename, 'y')
        self.assertEqual(person.name, 'Gonzales')
        self.assertEqual(person.name_extra, None)

    def test_find_7(self):
        """
        Test this Name: Frau Prof. Dr. rer. nat. Maria von Leuthäuser-Schnarrenberger
        """
        person = Finder.find('Frau Prof. Dr. rer. nat. Maria von Leuthäuser-Schnarrenberger')
        self.assertEqual(person.gender, 'weiblich')
        self.assertEqual(person.salutation, 'Frau')
        self.assertEqual(person.titles, ['Prof. Dr. rer. nat.'])
        self.assertEqual(person.prename, 'Maria')
        self.assertEqual(person.name, 'Leuthäuser-Schnarrenberger')
        self.assertEqual(person.name_extra, 'von')

    def test_find_8(self):
        """
        Test this Name: Herr Dipl. Ing. Max von Müller
        """
        person = Finder.find('Herr Dipl. Ing. Max von Müller')
        self.assertEqual(person.gender, 'männlich')
        self.assertEqual(person.salutation, 'Herr')
        self.assertEqual(person.titles, ['Dipl. Ing.'])
        self.assertEqual(person.prename, 'Max')
        self.assertEqual(person.name, 'Müller')
        self.assertEqual(person.name_extra, 'von')

    def test_find_9(self):
        """
        Test this Name: Dr. Russwurm, Winfried
        """
        person = Finder.find('Dr. Russwurm, Winfried')
        self.assertEqual(person.gender, None)
        self.assertEqual(person.salutation, None)
        self.assertEqual(person.titles, ['Dr.'])
        self.assertEqual(person.prename, 'Winfried')
        self.assertEqual(person.name, 'Russwurm')
        self.assertEqual(person.name_extra, None)

    def test_find_10(self):
        """
        Test this Name: Dr. von Russwurm, Winfried
        """
        person = Finder.find('Dr. von Russwurm, Winfried')
        self.assertEqual(person.gender, None)
        self.assertEqual(person.salutation, None)
        self.assertEqual(person.titles, ['Dr.'])
        self.assertEqual(person.prename, 'Winfried')
        self.assertEqual(person.name, 'Russwurm')
        self.assertEqual(person.name_extra, 'von')

    def test_find_11(self):
        """
        Test this Name: Herr Dr.-Ing. Dr. rer. nat. Dr. h.c. mult. Paul Steffens
        """
        person = Finder.find('Herr Dr.-Ing. Dr. rer. nat. Dr. h.c. mult. Paul Steffens')
        self.assertEqual(person.gender, 'männlich')
        self.assertEqual(person.salutation, 'Herr')
        self.assertEqual(person.titles, ['Dr. h.c. mult.', ' Dr. rer. nat.', ' Dr.-Ing.'])
        self.assertEqual(person.prename, 'Paul')
        self.assertEqual(person.name, 'Steffens')
        self.assertEqual(person.name_extra, None)


if __name__ == '__main__':
    unittest.main()