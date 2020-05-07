import logging

from req_apli import apli
from send_data import sendData


def createXMLA(result_apli, token):

    logging.info({
        "process": "createXMLA",
        "message": "Creating xmls"
    })

    for row in result_apli:
        xml_apli = apli(row)

        xml_apli += """
            <documentos>
                <documento>{}</documento>
                <fvencimiento>{}</fvencimiento>
                <numonto>-{}</numonto>
                <tmovimiento>{}</tmovimiento>
            </documentos>
            """.format(
                    row[1],
                    row[3],
                    str(row[4])[1:] if "-" in str(row[4]) else row[4],
                    row[5]
            )

        xml_apli += """
        </movimiento>
        """

        """
        Envío de xmls a la API de Linq
        """
        sendData(xml_apli, token)
