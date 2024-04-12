


class Consola():
    def __init__(self,service):
        """
        atribuie atributul service entitatii create
        :param service:
        """
        self.service=service


    def update(self):
        """
        Ia inputurile necesare pentru modificarea unei melodii si face trimitere la service
        :return:
        """
        print("Ce se va modifica:")
        titlu=input("Titlu: ")
        artist=input("Artist: ")
        print("Cu ce se vor modifica genul si data:")
        gen=input("Gen: ")
        data=input("Data: ")
        #trimitere la service
        verdict=self.service.update_service(titlu,artist,gen,data)

        if verdict == False:
            print("Melodia nu se afla in lista!!!")


    def random(self):
        """
        Utilizatorul citeste de la tastatura si se face trimitere la service
        :return:
        """
        print("Se vor adauga melodii random...")
        try:
            nr_mel=int(input("Cate melodii? "))
            if nr_mel<=0:
                print("Numarul de melodii trebuie sa fie mai mare ca 0")
            else:

                print("introdu o lista de artisti...")
                artist_list = input("Artisti: ")

                print("introdu o lista de titluri de melodii....")
                titlu_list=input("Titluri: ")
                self.service.random_service(artist_list,titlu_list,nr_mel)


        except ValueError:
            print("Numarul de melodii trebuie sa fie numar!!!")

    def sortare(self):
        """
        citeste numele fisierului
        sorteaza
        :return:
        """

        file_name=input("Nume fisier:")
        file_name="data/" + file_name
        sorted_list=self.service.sortare_service(file_name)
        for i in sorted_list:
            print("TITLU:",i.get_title(),
                  "   ARTIST: ", i.get_artist(),
                  "   GEN: ",i.get_gen(),
                  "   DATA: ",i.get_data()
            )

        #trimitere la service

    def ui(self):
        ok=True
        #afisare automata aici
        while ok==True:
            print("""
                    MENIU:
                    1.Modificare melodie
                    2. Melodii Random
                    3.Export                    
                """)
            opt=input("Optiune: ")
            if opt=='1':
                self.update()
            elif opt=='2':
                self.random()
            elif opt=='3':
                self.sortare()

            else:
                print("Comanda invalida!!!")
