def otros(row):
    xml = """
    <movimiento>
        <tipoop>OTROS</tipoop>
        <contrato>{}</contrato>
        <anexo>N</anexo>

    """.format(row[0])

    return xml
