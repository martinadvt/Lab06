from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        conn = get_connection() #creo la connessione
        if conn is None:
            raise ConnectionError("Impossibile connettersi al database.")  #controllo nel caso non riesca a connettersi
        try:
            cursore = conn.cursore()
            query = f"""SELECT *
                        FROM strumento s"""  #chiedere se è giusto mettere strumento s o devo scrivere solo strumento
            cursore.execute(query)

            lista_strumenti = [] #creo sempre prima la lista vuota
            for riga in cursore:
                lista_strumenti.append(riga[0], riga[1], riga[2], riga[3], riga[4], riga[5])

            return lista_strumenti

        finally: #chiude il cursore e la connessione a prescindere dal fatto che il try vada a buon fine o meno
            cursore.close()
            conn.close()





    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """

        conn = get_connection()
        if conn is None:
            raise ConnectionError("Impossibile connettersi al database.")
        try:
            cursore = conn.cursore()
            query = f"""SELECT *
                        FROM strumento s
                        WHERE tipo = %s"""  #seleziona gli strumenti per tipo
            cursore.execute(query)

            lista_strumenti_per_tipo = []
            for riga in cursore:
                lista_strumenti_per_tipo.append(riga[0], riga[1], riga[2], riga[3], riga[4], riga[5])
            return lista_strumenti_per_tipo

        finally:
            cursore.close()
            conn.close()

        # TODO
