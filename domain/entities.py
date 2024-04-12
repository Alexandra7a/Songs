class Melody():
    """
    clasa care se ocupa de entitatile de tip melody
    """
    def __init__(self,title, artist, gen,r_data):
        """
        este apelata automat cand se creaza o entitate de tip melody
        atribute:
        title=titlul melodiei
        artist= cine a scris melodia
        gen= in care gen se incadreaza melodia
        r_data= data la care a fost lansata melodia
        """
        self.title=title
        self.artist=artist
        self.gen=gen
        self.r_data=r_data

    def get_title(self):
        """
        :return: se returneaza titlul melodiei
        """
        return  self.title
    def get_artist(self):
        """
        :return: numele artistului
        """
        return self.artist
    def get_gen(self):
        """
        :return: genul melodiei
        """
        return self.gen
    def get_data(self):
        """
        :return: data la care a fost lansata melodia
        """
        return self.r_data
    def get_luna(self,data):
        splited=data.split(".")
        return splited[1]
    def get_zi(self, data):
        splited = data.split(".")
        return splited[0]
    def get_an(self, data):
        splited = data.split(".")
        return splited[2]
    def __str__(self):
        return str(self.get_title())+";"+str(self.get_artist())+\
               ";"+ str(self.get_gen())+";"+str(self.get_data())+'\n'


#tests
def test_get_title():
    entiti=Melody('AAA','Andre','pop','20.12.2022')
    assert entiti.get_title()=='AAA'
def test_get_gen():
    entiti = Melody('AAA', 'Andre', 'pop', '20.12.2022')
    assert entiti.get_gen()=='pop'
def test_get_artist():
    entiti = Melody('AAA', 'Andre', 'pop', '20.12.2022')
    assert entiti.get_artist()=='Andre'
def test_get_data():
    entiti = Melody('AAA', 'Andre', 'pop', '20.12.2022')
    assert entiti.get_data()=='20.12.2022'


test_get_data()
test_get_artist()
test_get_title()
test_get_gen()