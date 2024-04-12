
from domain.entities import Melody

class Melody_service():
    """
    clasa care se ocupa de serviceii ci melodii
    """
    def __init__(self, repo,valid):
        """
        atributele clasei
        :param repo: melody_repo
        :param valid: validator de date
        """
        self.repo=repo
        self.valid=valid

    def update_service(self,title, artist, gen,data):
        """
        Face trimitere la repository pentru a modifica o melodie data
        :param title: titlu
        :param artist: artist
        :param gen: cu ce se modifica genul
        :param data: cu ce se modifica data
        :return:
        """
        if self.valid.melody_validate(title,artist,gen,data)==True:
            entity=Melody(title,artist,gen,data)
            return self.repo.update_repo(title,artist,gen,data,entity)

    def random_service(self,artist_list,titlu_list,nr_mel):
        """
        Se ocupa de validarea melodiilor citite de utilizator si face
        trimitere la repo
        :return:
        """
        artist_list = artist_list.split(",")
        titlu_list = titlu_list.split(",")
        if self.valid.list_validator(artist_list,titlu_list)==True:
            self.repo.random_repo(artist_list,titlu_list,nr_mel)




    def comparator(self,d1,d2):
        """
        compara datele intre ele
        :param d1:
        :param d2:
        :return:
        """
        d1_data=d1.get_data()
        d2_data=d2.get_data()
        if d1.get_an(d1_data)<d2.get_an(d2_data):
            return True
        elif d1.get_an(d1_data)==d2.get_an(d2_data):
            if d1.get_luna(d1_data)<d2.get_luna(d2_data):
                return True
            elif d1.get_luna(d1_data)==d2.get_luna(d2_data):
                if d1.get_zi(d1_data)<d2.get_zi(d2_data):
                    return True
        return False

    def sortare_service(self,file):
        """
        se ocupa de sortare
        :param data:
        :return:
        """
        from utils.MergeSort import MergeSort

        list=self.repo.get_all()
        key = lambda x: (int(x.get_an(x.get_data())),
                         int(x.get_luna(x.get_data())),
                         int(x.get_zi(x.get_data())))
        sorted_list=MergeSort(list,key,self.comparator)
        self.repo.save_to_file_sorted(sorted_list,file)
        return  sorted_list


