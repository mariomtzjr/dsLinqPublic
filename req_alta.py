def alta(row, rcontratos):

    rc = ""
    for c in rcontratos:
        if c is None:
            rc = ""
        else:
            rc += c + "|"

    xml = """
        <movimiento>

            <clavereferencia>{}</clavereferencia>
            <tipoop>ALTA</tipoop>
            <deudor>{}</deudor>
            <RFC>{}</RFC>
            <contrato>{}</contrato>
            <anexo>N</anexo>

            <nutipocontrato>{}</nutipocontrato>
            <grupo>{}</grupo>

            <tipopersona>{}</tipopersona>
            <paternodeudor>{}</paternodeudor>
            <maternodeudor>{}</maternodeudor>
            <nombredeudor>{}</nombredeudor>
            <razonsocial>{}</razonsocial>

            <direccion>{}</direccion>
            <ciudad>{}</ciudad>
            <nucp>{}</nucp>
            <estado>{}</estado>
            <rama></rama>
            <sector></sector>
            <subsector></subsector>
            <contacto>{}</contacto>
            <email>{}</email>
            <telefono>{}</telefono>
            <ffirmacontrato>{}</ffirmacontrato>
            <fvencimientocontrato>{}</fvencimientocontrato>
            <nuplazo>{}</nuplazo>
            <numontocontrato>{}</numontocontrato>
            <nurentasdeposito>0</nurentasdeposito>
            <nudepositogarantia>0</nudepositogarantia>
            <nuimportecontratocv>0</nuimportecontratocv>
            <nuflujosrestantes>{}</nuflujosrestantes>
            <numontoflujosrestantes>{}</numontoflujosrestantes>
            <referencia1></referencia1>
            <referencia2>{}</referencia2>
            <poliza></poliza>
            <nusumasegurada></nusumasegurada>
            <fvencimientopoliza></fvencimientopoliza>
            <nudependenciaid></nudependenciaid>
            <pagofrecuencia>{}</pagofrecuencia>
            <variable2></variable2>
            <variable3></variable3>
            <motor></motor>
            <serie></serie>
            <nofactura></nofactura>
            <nuvalorfactura></nuvalorfactura>
            <numontopagare>{}</numontopagare>
            <nupagomensual>{}</nupagomensual>
            <tasa>{}</tasa>
            <nuresidual></nuresidual>
            <fnacimientodeudor>{}</fnacimientodeudor>
            <aval></aval>
            <fnacimientoaval></fnacimientoaval>
            <tproducto></tproducto>
            <rcontrato>{}</rcontrato>
    """.format(row[0], row[3], row[10], row[30], row[1], row[4], row[9], row[5],
               row[6], row[7], row[8], row[11], row[12], row[13], row[14],
               row[15], row[16], row[17], row[18], row[19], row[20], row[21],
               row[22], row[23], row[24], row[25], row[26], row[27], row[28],
               row[29], rc[:-1])

    return xml
