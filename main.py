import execute
import queries
import logging
import get_token

from create_xml import createXML
from create_xml_apli import createXMLA
from create_xml_otros import createXMLO
from create_xml_saldo import createXMLS
from create_xml_cacre import createXMLC
from create_xml_mova import createXMLM


def main():
    """Alta de créditos
        Instrucción:
        Comentar/Descomentar líneas para dar de alta en el sistema
        de Linq los créditos nuevos
        - qalta, qmova, qcare : Queries
        - result_alta, result_mova, result_cacre: Resultado de ejecutar query
        - createXML, createXMLM, createXMLC: Creación de xml
    """

    logging.info({
        "process": "main",
        "message": "Getting token"
    })
    token = get_token.getToken()

    # Envío normal de cobranza (pagos, saldos, refinanciamientos)
    qalta = queries.QueryL.queryD()  # DEU - ALTA - Créditos nuevos
    qmova = queries.QueryL.queryM()  # MOVA - FAC - Cobranza futura
    qcacre = queries.QueryL.queryD()  # CACRE - Acreedores

    qapli = queries.QueryL.queryApli()  # APLI - PAG
    qotros = queries.QueryL.queryOtros()  # APLI - OTROS
    # qaplir = queries.QueryL.queryApliRe()  # APLI - NCR - Refinanciados
    qsaldo = queries.QueryL.querySaldo()  # Saldos

    result_alta = execute.queryExecute(qalta)
    result_mova = execute.queryExecute(qmova)
    result_cacre = execute.queryExecute(qcacre)

    result_apli = execute.queryExecute(qapli)
    result_otros = execute.queryExecute(qotros)
    # result_aplir = execute.queryExecute(qaplir)
    result_saldo = execute.queryExecute(qsaldo)

    createXML(result_alta, token)
    createXMLM(result_mova, token)
    createXMLC(result_cacre, token)

    createXMLA(result_apli, token)
    createXMLO(result_otros, token)
    # createXMLA(result_aplir, token)
    createXMLS(result_saldo, token)

if __name__ == "__main__":
    logging.basicConfig(filename='linq_process.log',
                        format='%(asctime)s %(levelname)s:%(message)s',
                        level=logging.INFO)
    logging.info({
        "process": "main",
        "message": "Started Process"
    })

    main()
