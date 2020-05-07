import logging

from req_mova import mova
from send_data import sendData


def createXMLM(result_mova, token):

    logging.info({
        "process": "createXMLM",
        "message": "Creating xmls"
    })

    for row in result_mova:
        xml_mova = mova(row)

        xml_mova += """
            <documentos>
                <documento>{}</documento>
                <fvencimiento>{}</fvencimiento>
                <numonto>{}</numonto>
                <nuinteres>{}</nuinteres>
                <nuiva>{}</nuiva>
                <tmovimiento>FAC</tmovimiento>
            </documentos>
            """.format(
                row[1],
                row[3],
                0 if row[4] <= 0 else row[4],
                row[5],
                row[6]
            )

        xml_mova += """
        </movimiento>
        """

        """
        Envío de xmls a la API de Linq
        """
        sendData(xml_mova, token)
