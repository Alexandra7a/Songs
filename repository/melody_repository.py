from domain.entities import Melody

class MelodyRepo():
    """
    se ocupa de getionarea melodiilor in memorie
    """
    def __init__(self,file):
        """
        ce atribute are entitatea creata
        :param file: fisier de tip txt
        """
        self.file=file

    def get_all(self):
        """
        da toate melodiile din file
        :return:
        """
        try:
            f=open(self.file,"r")
        except IOError:
            return
        lines=f.readlines()
        lines=[token.strip() for token in lines]
        lines=[token.split(";") for token in lines]
        transformed_string=[]
        for me in lines:
            title, artist,gen,data=me
            melody=Melody(title,artist,gen,data)
            transformed_string.append(melody)
        f.close()
        return transformed_string

    def save_to_file(self,list_to_save):
        """
        salveaza in fisier o lista de melodi data
        :param list_to_save:
        :return:
        """
        with open(self.file,"w") as f:
            for i in list_to_save:
                string=str(i.get_title())+";"+str(i.get_artist())+\
               ";"+ str(i.get_gen())+";"+str(i.get_data())+'\n'
                f.write(string)

    def save_to_file_sorted(self,list_to_save,file):
        """
        salveaza in fisier o lista de melodi data
        :param list_to_save:
        :return:
        """
        with open(file,"w") as f:
            for i in list_to_save:
                string=str(i.get_title())+";"+str(i.get_artist())+\
               ";"+ str(i.get_gen())+";"+str(i.get_data())+'\n'
                f.write(string)

    def add_to_file(self,what):
        """
        adauga in fisier o entitate de tip melody
        :param what:
        :return:
        """
        with open(self.file, "a") as f:
            string = str(what.get_title())+";"+str(what.get_artist())+\
               ";"+ str(what.get_gen())+";"+str(what.get_data())+'\n'
            f.write(string)

    def update_repo(self,title,artist,gen,data,given_entity):
        """
        va modifica in file entitatea existenta cu entitatea data
        :param given_entity: cu ce se modifica
        :return:
        """
        melody_list=self.get_all()
        poz=0
        for i in range(len(melody_list)):
            if melody_list[i].get_title()==title and melody_list[i].get_artist()==artist:
                poz=i

        if poz ==0:
            return False
        else:
            melody_list.pop(poz)
            print("ok")
            self.save_to_file(melody_list)
            self.add_to_file(given_entity)

    def random_repo(self,artist_list,titlu_list,nr_mel):
        """
        Adauga in fisier melodii random
        :param artist_list: lista din care se vor lua artistii
        :param gen_list: lista din care se vor lua genurile
        :param nr_mel nr de melodii adaugate
        :return:
        """
        import random
        data='03.02.2023'
        list=['Jazz','Rock','Pop']
        for i in range(nr_mel):
            artist=random.choice(artist_list)
            titlu=random.choice(titlu_list)
            gen=random.choice(list)

            entitate=Melody(titlu,artist,gen,data)
            self.add_to_file(entitate)



