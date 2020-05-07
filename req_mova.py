def mova(row):

    xml = """
        <movimiento>
            <tipoop>APLI</tipoop>
            <contrato>{}</contrato>
            <anexo>N</anexo>

    """.format(row[0])

    return xml
