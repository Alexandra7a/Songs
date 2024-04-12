

class Validate():
    def melody_validate(self,title,artist,gen,data):
        """
        valideaza melodie data
        :param title:
        :param artist:
        :param gen:
        :param data:
        :return:
        """
        err_list=[]
        splited_data=data.split(".")
        if title=='':
            try:
                raise ValueError("Campul TITLU nu poate fi goal!")
            except ValueError as err:
                err_list.append(err)
        if artist=='':
            try:
                raise ValueError("Campul ARTIST nu poate fi goal!")
            except ValueError as err:
                err_list.append(err)
        if gen=='':
            try:
                raise ValueError("Campul GEN nu poate fi goal!")
            except ValueError as err:
                err_list.append(err)
        if data=='':
            try:
               raise ValueError("Campul DATA nu poate fi goal!")
            except ValueError as err:
                err_list.append(err)
        list=['Jazz','Rock','Pop']
        if gen not in list:
            try:
                raise ValueError("Genul poate fi doar: Rock,Pop si Jazz")
            except ValueError as err:
                err_list.append(err)

        if len(splited_data)==3:
            if int(splited_data[0])<1 or int(splited_data[0])>31:
                try:
                   raise ValueError("Ziua nu are structura buna!")
                except ValueError as err:
                    err_list.append(err)
            if int(splited_data[1])<1 or int(splited_data[1])>12:
                try:
                   raise ValueError("Luna nu are structura buna!")
                except ValueError as err:
                    err_list.append(err)
            if int(splited_data[2])<1900 or int(splited_data[2])>2023:
                try:
                   raise ValueError("Anul nu are structura buna!")
                except ValueError as err:
                    err_list.append(err)
        else:
            try:
               raise ValueError("Data nu are structura buna!")
            except ValueError as err:
                err_list.append(err)



        if len(err_list)==0:
            return True
        else:
            for i in err_list:
                print(i)

    def list_validator(self,artist_list,gen_list):
        """
        se vor valida listele
        :param artist_list:
        :param gen_list:
        :return:
        """
        err_list=[]
        if artist_list[0]=='':
            try:
                raise ValueError("Lista de artisti nu poate fi goala!")
            except ValueError as err:
                err_list.append(err)
        if gen_list[0]=='':
            try:
                raise ValueError("Lista de GENURI nu poate fi goala!")
            except ValueError as err:
                err_list.append(err)

        if len(err_list) == 0:
            return True
        else:
            for i in err_list:
                print(i)