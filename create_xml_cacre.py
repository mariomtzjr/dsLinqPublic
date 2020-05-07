import logging

from req_cacre import cacre
from send_data import sendData


def createXMLC(result_cacre, token):

    logging.info({
        "process": "createXMLC",
        "message": "Creating xmls"
    })

    for row in result_cacre:
        xml_cacre = cacre(row)

        """
        Envío de xmls a la API de Linq
        """
        sendData(xml_cacre, token)
