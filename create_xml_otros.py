import logging

from req_otros import otros
from send_data import sendData


def createXMLO(result_otros, token):

    logging.info({
        "process": "createXMLO",
        "message": "Creating xmls"
    })

    for row in result_otros:
        xml_otros = otros(row)

        xml_otros += """
            <documentos>
                <documento>{}</documento>
                <fvencimiento>{}</fvencimiento>
                <numonto>-{}</numonto>
                <nutmovimiento>1</nutmovimiento>
            </documentos>
            """.format(row[1], row[2], row[3])

        xml_otros += """
            <documentos>
                <documento>{}</documento>
                <fvencimiento>{}</fvencimiento>
                <numonto>-{}</numonto>
                <nutmovimiento>2</nutmovimiento>
            </documentos>
        """.format(row[1], row[2], row[4])

        xml_otros += """
    </movimiento>
        """

        """
        Desde aquí se envían a la API de Linq
        """
        sendData(xml_otros, token)
