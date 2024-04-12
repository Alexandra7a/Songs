
from domain.validators import Validate
from repository.melody_repository import MelodyRepo
from service.melody_service import Melody_service
from ui.console import Consola



def main():
    repository=MelodyRepo('data/melody.txt')
    service=Melody_service(repository,valid=Validate())
    console=Consola(service)
    console.ui()

main()



