import logging
import collections

from collections import defaultdict

from req_alta import alta
from send_data import sendData


def createXML(result_alta, token):
    logging.info({
        "process": "createXML",
        "message": "Creating xmls"
    })
    rc = [((row[30], row[32] if row[32] != "" else "")) for row in result_alta]

    diccionario_contratos = collections.defaultdict(list)
    for k, v in rc:
        diccionario_contratos[k].append(v)

    diccionario_contratos = dict(diccionario_contratos)

    for c in result_alta:
        xml_deu = alta(c, diccionario_contratos[c[30]])
        xml_deu += """
        </movimiento>
        """

        """
        Envío de xmls a la API de Linq
        """
        sendData(xml_deu, token)
