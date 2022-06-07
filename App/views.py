from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from .models import *
import datetime
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from django.conf import settings
from App.models import Cargo
from django.core.mail import EmailMessage
import requests
import os
import codecs
from datetime import datetime
from django.core.files.storage import FileSystemStorage
import time
import mimetypes
import logging
import logging.handlers as handlers
import socket


def home(request):
    '''
    img=Image.objects.all()  
    context={'img':img}
    '''
    return render(request, 'App/home.html', {})


def gracias(request):
    context = {}
    return render(request, 'App/gracias.html', context)


def vacantes(request, filtro):
    cargos = Cargo.objects.all()

    if filtro == '1':
        cargos = cargos.order_by('nombre')
    elif filtro == '2':
        cargos = cargos.order_by('-nombre')

    fechaActual = datetime.now().date

    context = {'cargos': cargos, 'fechaActual': fechaActual}

    return render(request, 'App/vacantes.html', context)


def cargos(request, idCargos):
    cargos = Cargo.objects.get(id=idCargos)
    splitObjetivo = cargos.objetivo.split("*")
    splitContrato = cargos.contrato.split("*")
    splitFormacion = cargos.formacion.split("*")
    splitResponsabilidades = cargos.responsabilidades.split("*")
    splitExperiencia = cargos.experiencia.split("*")
    splitIdiomas = cargos.idiomas.split("*")
    splitJornada = cargos.jornada.split("*")
    splitUbicacion = cargos.ubicacion.split("*")
    splitConocimientos = cargos.conocimientos.split("*")
    splitSistemasPH = cargos.sistemas_programas_herramientas.split("*")
    context = {'cargos': cargos, 'splitResponsabilidades': splitResponsabilidades, 'splitJornada': splitJornada,
               'splitSistemasPH': splitSistemasPH, 'splitObjetivo': splitObjetivo, 'splitFormacion': splitFormacion,
               'splitExperiencia': splitExperiencia, 'splitIdiomas': splitIdiomas, 'splitUbicacion': splitUbicacion,
               'splitConocimientos': splitConocimientos, 'splitContrato': splitContrato}
    return render(request, 'App/cargos.html', context)


def generate_decoded(url):
    with open(url, 'r', encoding='utf-8') as archivo:
        datos = archivo.read()

    objeto = json.loads(datos)
    return objeto


def depNacim(request):
    pais = int(request.GET.get('paisNac'))
    resultPais = generate_decoded('App/json/paises.json')
    resultDepart = generate_decoded('App/json/departamentos.json')

    context = {'resultDepart': resultDepart, 'resultPais': resultPais, 'pais': pais}

    return render(request, 'App/depNacim.html', context)


def ciudadNacim(request):
    depNacim = int(request.GET.get('depNacim'))
    resultDepart = generate_decoded('App/json/departamentos.json')
    resultCiudades = generate_decoded('App/json/ciudades.json')

    context = {'resultDepart': resultDepart, 'resultCiudades': resultCiudades, 'depNacim': depNacim}

    return render(request, 'App/ciudadNacim.html', context)


def ciudadResi(request):
    depResi = int(request.GET.get('depResi'))
    resultDepart = generate_decoded('App/json/departamentos.json')
    resultCiudades = generate_decoded('App/json/ciudades.json')

    context = {'resultDepart': resultDepart, 'resultCiudades': resultCiudades, 'depResi': depResi}

    return render(request, 'App/ciudadResi.html', context)


def estudios(request):
    formacion = int(request.GET.get('formacion'))
    form = generate_decoded('App/json/formacion.json')
    areas = generate_decoded('App/json/areasEstu.json')
    dict_area = [x['grupoArea'] for x in form if x['codigo'] == formacion]
    print(dict_area)
    output_dict = [x for x in areas if x['grupoArea'] == dict_area[0]]
    print(output_dict)
    context = {'areas': output_dict}

    return render(request, 'App/estudios.html', context)


def formulario(request, idCargos):
    dias = {
        '01': '01',
        '02': '02',
        '03': '03',
        '04': '04',
        '05': '05',
        '06': '06',
        '07': '07',
        '08': '08',
        '09': '09',
        '10': '10',
        '11': '11',
        '12': '12',
        '13': '13',
        '14': '14',
        '15': '15',
        '16': '16',
        '17': '17',
        '18': '18',
        '19': '19',
        '20': '20',
        '21': '21',
        '22': '22',
        '23': '23',
        '24': '24',
        '25': '25',
        '26': '26',
        '27': '27',
        '28': '28',
        '29': '29',
        '30': '30',
        '31': '31'
    }

    meses = [
        {'id': "01", "mes": 'Enero'},
        {'id': "02", "mes": 'Febrero'},
        {'id': "03", "mes": 'Marzo'},
        {'id': "04", "mes": 'Abril'},
        {'id': "05", "mes": 'Mayo'},
        {'id': "06", "mes": 'Junio'},
        {'id': "07", "mes": 'Julio'},
        {'id': "08", "mes": 'Agosto'},
        {'id': "09", "mes": 'Septiembre'},
        {'id': "10", "mes": 'Octubre'},
        {'id': "11", "mes": 'Noviembre'},
        {'id': "12", "mes": 'Diciembre'},
    ]

    anioMenor = 1950
    anioActual = datetime.now().year
    anios = []
    while anioMenor <= anioActual:
        anios.append(anioMenor)
        anioMenor = anioMenor + 1

    documento = generate_decoded('App/json/documento.json')
    formacion = generate_decoded('App/json/formacion.json')
    resultDepart = generate_decoded('App/json/departamentos.json')
    resultPais = generate_decoded('App/json/paises.json')
    idiomas = generate_decoded('App/json/idiomas.json')
    areaInteres = generate_decoded('App/json/areaInteres.json')
    aspSal = generate_decoded('App/json/aspSalarial.json')
    trabajoEnCrystal = generate_decoded('App/json/trabajoCrystal.json')

    nivel = {
        'Alto': 'Alto',
        'Medio': 'Medio',
        'Bajo': 'Bajo'
    }

    tarjetaPro = generate_decoded('App/json/tarjetaPro.json')

    mesEstu = ""
    for m in meses:
        mesEstu = f'{mesEstu}<option value="{m["mes"]}">{m["mes"]}</option>'

    anioEstu = ""
    for a in anios:
        anioEstu = f'{anioEstu}<option value="{str(a)}">{str(a)}</option>'

    tipoVia = {
        'AEROPUERTO': 'AEROPUERTO',
        'APARTADO': 'APARTADO',
        'AUTOPISTA': 'AUTOPISTA',
        'AVENIDA': 'AVENIDA',
        'CALLE': 'CALLE',
        'CARRERA': 'CARRERA',
        'CARRETERA': 'CARRETERA',
        'CENTRO COMERCIAL': 'CENTRO COMERCIAL',
        'CIRCULAR': 'CIRCULAR',
        'CORREGIMIENTO': 'CORREGIMIENTO',
        'FINCA': 'FINCA',
        'GLORIETA': 'GLORIETA',
        'KILÓMETRO': 'KILÓMETRO',
        'LOTE': 'LOTE',
        'MANZANA': 'MANZANA',
        'TERMINAL': 'TERMINAL',
        'TRANSVERSAL': 'TRANSVERSAL',
        'VARIANTE': 'VARIANTE',
        'VEREDA': 'VEREDA'
    }

    letraDire = {
        'A': 'A',
        'AA': 'AA',
        'AAA': 'AAA',
        'AB': 'AB',
        'AC': 'AC',
        'AF': 'AF',
        'B': 'B',
        'BB': 'BB',
        'BBB': 'BBB',
        'BC': 'BC',
        'BD': 'BD',
        'BE': 'BE',
        'C': 'C',
        'CC': 'CC',
        'CCC': 'CCC',
        'D': 'D',
        'DA': 'DA',
        'DB': 'DB',
        'DD': 'DD',
        'DDD': 'DDD',
        'E': 'E',
        'EE': 'EE',
        'EEE': 'EEE',
        'F': 'F',
        'FF': 'FF',
        'FFF': 'FFF',
        'G': 'G',
        'GG': 'GG',
        'GGG': 'GGG',
        'H': 'H',
        'HA': 'HA',
        'HB': 'HB',
        'HC': 'HC',
        'HD': 'HD',
        'HE': 'HE',
        'HF': 'HF',
        'HG': 'HG',
        'I': 'I',
        'IA': 'IA',
        'IB': 'IB',
        'IC': 'IC',
        'ID': 'ID',
        'IE': 'IE',
        'IF': 'IF',
        'IG': 'IG',
        'J': 'J',
        'JA': 'JA',
        'JB': 'JB',
        'JC': 'JC',
        'JD': 'JD',
        'JE': 'JE',
        'JF': 'JF',
        'JG': 'JG',
        'K': 'K',
        'KA': 'KA',
        'KB': 'KB',
        'KC': 'KC',
        'KD': 'KD',
        'KE': 'KE',
        'KF': 'KF',
        'KG': 'KG',
        'L': 'L',
        'LA': 'LA',
        'LB': 'LB',
        'LC': 'LC',
        'LD': 'LD',
        'LE': 'LE',
        'LF': 'LF',
        'LG': 'LG',
        'M': 'M',
        'MA': 'MA',
        'MB': 'MB',
        'MC': 'MC',
        'MD': 'MD',
        'ME': 'ME',
        'MF': 'MF',
        'MG': 'MG',
        'N': 'N',
        'NA': 'NA',
        'NB': 'NB',
        'NC': 'NC',
        'ND': 'ND',
        'NE': 'NE',
        'NF': 'NF',
        'NG': 'NG',
        'O': 'O',
        'OA': 'OA',
        'OB': 'OB',
        'OC': 'OC',
        'OD': 'OD',
        'OE': 'OE',
        'OF': 'OF',
        'OG': 'OG',
        'P': 'P',
        'PA': 'PA',
        'PB': 'PB',
        'PC': 'PC',
        'PD': 'PD',
        'PE': 'PE',
        'PF': 'PF',
        'PG': 'PG',
        'Q': 'Q',
        'QA': 'QA',
        'QB': 'QB',
        'QC': 'QC',
        'QD': 'QD',
        'QE': 'QE',
        'QF': 'QF',
        'QG': 'QG',
        'R': 'R',
        'RA': 'RA',
        'RB': 'RB',
        'RC': 'RC',
        'RD': 'RD',
        'RE': 'RE',
        'RF': 'RF',
        'RG': 'RG',
        'S': 'S',
        'SA': 'SA',
        'SB': 'SB',
        'SC': 'SC',
        'SD': 'SD',
        'SE': 'SE',
        'SF': 'SF',
        'SG': 'SG',
        'T': 'T',
        'TA': 'TA',
        'TB': 'TB',
        'TC': 'TC',
        'TD': 'TD',
        'TE': 'TE',
        'TF': 'TF',
        'TG': 'TG',
        'U': 'U',
        'UA': 'UA',
        'UB': 'UB',
        'UC': 'UC',
        'UD': 'UD',
        'UE': 'UE',
        'UF': 'UF',
        'UG': 'UG',
        'V': 'V',
        'VA': 'VA',
        'VB': 'VB',
        'VC': 'VC',
        'VD': 'VD',
        'VE': 'VE',
        'VF': 'VF',
        'VG': 'VG',
        'W': 'W',
        'WA': 'WA',
        'WB': 'WB',
        'WC': 'WC',
        'WD': 'WD',
        'WE': 'WE',
        'WF': 'WF',
        'WG': 'WG',
        'X': 'X',
        'XA': 'XA',
        'XB': 'XB',
        'XC': 'XC',
        'XD': 'XD',
        'XE': 'XE',
        'XF': 'XF',
        'XG': 'XG',
        'Y': 'Y',
        'YA': 'YA',
        'YB': 'YB',
        'YC': 'YC',
        'YD': 'YD',
        'YE': 'YE',
        'YF': 'YF',
        'YG': 'YG',
        'Z': 'Z',
        'ZA': 'ZA',
        'ZB': 'ZB',
        'ZC': 'ZC',
        'ZD': 'ZD',
        'ZE': 'ZE',
        'ZF': 'ZF',
        'ZG': 'ZG',

    }

    cuadrante = {
        'Sin selección': 'Sin selección',
        'ESTE': 'ESTE',
        'NORTE': 'NORTE',
        'OESTE': 'OESTE',
        'SUR': 'SUR'

    }

    claseVivienda = {
        'APARTAMENTO': 'APARTAMENTO',
        'CASA': 'CASA',
        'CASA - LOTE': 'CASA - LOTE',
        'CUARTO COMPARTIDO': 'CUARTO COMPARTIDO',
        'FINCA': 'FINCA',
        'HABITACIÓN': 'HABITACIÓN',
        'INQUILINATO': 'INQUILINATO',
        'RESIDENCIA': 'RESIDENCIA'

    }

    context = {'idCargos': idCargos, 'resultPais': resultPais, 'formacion': formacion, 'tarProfe': tarjetaPro,
               'mesEstu': mesEstu, 'anioEstu': anioEstu,
               'idiomas': idiomas, 'documento': documento, 'aspSal': aspSal, 'dias': dias, 'meses': meses,
               'areaInteres': areaInteres,
               'trabajoEnCrystal': trabajoEnCrystal, 'resultDepart': resultDepart, 'anios': anios, 'nivel': nivel,
               'tipoVia': tipoVia,
               'letraDire': letraDire, 'cuadrante': cuadrante, 'claseVivienda': claseVivienda}

    return render(request, 'App/formulario.html', context)


def inicializarLog():
    logger = logging.getLogger("crystal.trabajo")
    logHandler = handlers.TimedRotatingFileHandler("logs/app.log", when='d', interval=1)
    logHandler.setLevel(logging.ERROR)
    logger.addHandler(logHandler)

    return logger


def enviarForm(request):
    logger = inicializarLog()

    fecha_creacion = datetime.now()
    fecha_creacion.strftime("%Y-%m-%d")
    logger.error("------ Inicia un nuevo registro " + str(fecha_creacion.strftime("%Y-%m-%d %H:%M:%S")) + " ------")
    logger.error("User agent: " + str(request.META['HTTP_USER_AGENT']))
    direccion_equipo = socket.gethostbyname(socket.gethostname())
    logger.error("IP del equipo: " + direccion_equipo)
    correo = request.POST.get('email', 'default')
    nombres = request.POST.get('nombres', 'default')
    apellidos = request.POST.get('apellidos', 'default')
    logger.error("nombre: " + nombres + " " + apellidos)
    idCargos = request.POST.get('cargo', 'default')
    cargos = int(idCargos)
    print(str(cargos) + " cargos")
    cargo = Cargo.objects.get(id=cargos)
    logger.error("Cargo: " + str(cargo))
    form = generate_decoded('App/json/formacion.json')
    if request.POST.get('formacion1', 'default') != '':
        formacion1 = [x['nombre'] for x in form if x['codigo'] == int(request.POST.get('formacion1', 'default'))]
        formacion1 = str(formacion1[0])
    else:
        formacion1 = ""

    if request.POST.get('formacion2', 'default') != '':
        formacion2 = [x['nombre'] for x in form if x['codigo'] == int(request.POST.get('formacion2', 'default'))]
        formacion2 = str(formacion2[0])
    else:
        formacion2 = ""

    if request.POST.get('formacion3', 'default') != '':
        formacion3 = [x['nombre'] for x in form if x['codigo'] == int(request.POST.get('formacion3', 'default'))]
        formacion3 = str(formacion3[0])
    else:
        formacion3 = ""

    if request.POST.get('formacion4', 'default') != '':
        formacion4 = [x['nombre'] for x in form if x['codigo'] == int(request.POST.get('formacion4', 'default'))]
        formacion4 = str(formacion4[0])
    else:
        formacion4 = ""

    areas = generate_decoded('App/json/areasEstu.json')
    if request.POST.get('areasEst1', 'default') != '':
        areasEst1 = [x['nombre'] for x in areas if x['codigo'] == int(request.POST.get('areasEst1', 'default'))]
        areasEst1 = str(areasEst1[0])
    else:
        areasEst1 = ""

    if request.POST.get('areasEst2', 'default') != '':
        areasEst2 = [x['nombre'] for x in areas if x['codigo'] == int(request.POST.get('areasEst2', 'default'))]
        areasEst2 = str(areasEst2[0])
    else:
        areasEst2 = ""

    if request.POST.get('areasEst3', 'default') != '':
        areasEst3 = [x['nombre'] for x in areas if x['codigo'] == int(request.POST.get('areasEst3', 'default'))]
        areasEst3 = str(areasEst3[0])
    else:
        areasEst3 = ""

    if request.POST.get('areasEst4', 'default') != '':
        areasEst4 = [x['nombre'] for x in areas if x['codigo'] == int(request.POST.get('areasEst4', 'default'))]
        areasEst4 = str(areasEst4[0])
    else:
        areasEst4 = ""
        
    areaInte = generate_decoded('App/json/areaInteres.json')
    areaInteres = [x['nombre'] for x in areaInte if x['codigo'] == int(request.POST.get('areasInte', 'default'))]
    areaInteres = str(areaInteres[0])

    aspSal = generate_decoded('App/json/aspSalarial.json')
    aspSalarial = [x['nombre'] for x in aspSal if x['codigo'] == int(request.POST.get('aspSal', 'default'))]
    aspSalarial = str(aspSalarial[0])

    docu = generate_decoded('App/json/documento.json')
    documento = [x['nombre'] for x in docu if x['codigo'] == int(request.POST.get('documento', 'default'))]
    documento = str(documento[0])

    paises = generate_decoded('App/json/paises.json')
    paisesNac = [x['name'] for x in paises if x['id'] == int(request.POST.get('paisNacim', 'default'))]
    paisesNac = str(paisesNac[0])

    depart = generate_decoded('App/json/departamentos.json')
    departNac = [x['name'] for x in depart if x['id'] == int(request.POST.get('depNac', 'default'))]
    departNac = str(departNac[0])

    ciudad = generate_decoded('App/json/ciudades.json')
    ciudadNac = [x['name'] for x in ciudad if x['id'] == int(request.POST.get('ciudadNac', 'default'))]
    ciudadNac = str(ciudadNac[0])

    depResi = [x['name'] for x in depart if x['id'] == int(request.POST.get('depResi', 'default'))]
    depResi = str(depResi[0])

    ciudadResi = [x['name'] for x in ciudad if x['id'] == int(request.POST.get('ciudadResi', 'default'))]
    ciudadResi = str(ciudadResi[0])

    trabajoEnCry = generate_decoded('App/json/trabajoCrystal.json')
    trabajoEnCrystal = [x['nombre'] for x in trabajoEnCry if x['codigo'] == int(request.POST.get('trabajoEnCrystal', 'default'))]
    trabajoEnCrystal = str(trabajoEnCrystal[0])

    tarjetaPro = generate_decoded('App/json/tarjetaPro.json')
    if request.POST.get('tarProfe1', 'default') != '':
        tarProfe1 = [x['nombre'] for x in tarjetaPro if x['codigo'] == int(request.POST.get('tarProfe1', 'default'))]
        tarProfe1 = str(tarProfe1[0])
    else:
        tarProfe1 = ""

    if request.POST.get('tarProfe2', 'default') != '':
        tarProfe2 = [x['nombre'] for x in tarjetaPro if x['codigo'] == int(request.POST.get('tarProfe2', 'default'))]
        tarProfe2 = str(tarProfe2[0])
    else:
        tarProfe2 = ""

    if request.POST.get('tarProfe3', 'default') != '':
        tarProfe3 = [x['nombre'] for x in tarjetaPro if x['codigo'] == int(request.POST.get('tarProfe3', 'default'))]
        tarProfe3 = str(tarProfe3[0])
    else:
        tarProfe3 = ""

    if request.POST.get('tarProfe4', 'default') != '':
        tarProfe4 = [x['nombre'] for x in tarjetaPro if x['codigo'] == int(request.POST.get('tarProfe4', 'default'))]
        tarProfe4 = str(tarProfe4[0])
    else:
        tarProfe4 = ""

    idiomas = generate_decoded('App/json/idiomas.json')
    if request.POST.get('idioma1', 'default') != '':
        idioma1 = [x['nombre'] for x in idiomas if x['codigo'] == int(request.POST.get('idioma1', 'default'))]
        idioma1 = str(idioma1[0])
    else:
        idioma1 = ""

    if request.POST.get('idioma2', 'default') != '':
        idioma2 = [x['nombre'] for x in idiomas if x['codigo'] == int(request.POST.get('idioma2', 'default'))]
        idioma2 = str(idioma2[0])
    else:
        idioma2 = ""

    if request.POST.get('idioma3', 'default') != '':
        idioma3 = [x['nombre'] for x in idiomas if x['codigo'] == int(request.POST.get('idioma3', 'default'))]
        idioma3 = str(idioma3[0])
    else:
        idioma3 = ""

    ar = request.FILES.get('archivoHV', None)
    archivo = "/media/App/" + str(ar)
    mime = mimetypes.guess_type(archivo, strict=True)[0]
    if mime == "application/pdf" or mime == "application/msword":
        archivoHV = ar
    else:
        archivoHV = None

    logger.error("Archivo: " + str(archivo))
    
    Personas_Postulada.objects.create(
        cargo=cargo,
        correo=correo,
        telefono=request.POST.get('telefono', 'default'),
        telefono_adicional=request.POST.get('telefonoOp', 'default'),
        identificacion=documento,
        numero_identificacion=request.POST.get('identificacion', 'default'),
        nombres=nombres,
        apellidos=apellidos,
        fecha_nacimiento=request.POST.get('fechaNac', 'default'),
        pais_nacimiento=paisesNac,
        departamento_nacimiento=departNac,
        ciudad_nacimiento=ciudadNac,
        genero=request.POST.get('genero', 'default'),
        soy_empleado=trabajoEnCrystal,
        direccion=request.POST.get('address', 'default'),
        departamento_residencia=depResi,
        municipio_residencia=ciudadResi,
        formacion_1=formacion1,
        formacion_2=formacion2,
        formacion_3=formacion3,
        formacion_4=formacion4,
        area_formacion_1=areasEst1,
        area_formacion_2=areasEst2,
        area_formacion_3=areasEst3,
        area_formacion_4=areasEst4,
        institucion_1=request.POST.get('institucion1', 'default'),
        institucion_2=request.POST.get('institucion2', 'default'),
        institucion_3=request.POST.get('institucion3', 'default'),
        institucion_4=request.POST.get('institucion4', 'default'),
        tarjeta_profesional_1=tarProfe1,
        tarjeta_profesional_2=tarProfe2,
        tarjeta_profesional_3=tarProfe3,
        tarjeta_profesional_4=tarProfe4,
        fecha_finalizacion_estudio_1=request.POST.get('fechaEstu1', 'default'),
        fecha_finalizacion_estudio_2=request.POST.get('fechaEstu2', 'default'),
        fecha_finalizacion_estudio_3=request.POST.get('fechaEstu3', 'default'),
        fecha_finalizacion_estudio_4=request.POST.get('fechaEstu4', 'default'),
        fecha_finalizacion_experiencia_1=request.POST.get('fechaExp1', 'default'),
        fecha_finalizacion_experiencia_2=request.POST.get('fechaExp2', 'default'),
        fecha_finalizacion_experiencia_3=request.POST.get('fechaExp3', 'default'),
        fecha_finalizacion_experiencia_4=request.POST.get('fechaExp4', 'default'),
        fecha_finalizacion_experiencia_5=request.POST.get('fechaExp5', 'default'),
        fecha_finalizacion_experiencia_6=request.POST.get('fechaExp6', 'default'),
        fecha_finalizacion_experiencia_7=request.POST.get('fechaExp7', 'default'),
        fecha_finalizacion_experiencia_8=request.POST.get('fechaExp8', 'default'),
        fecha_finalizacion_experiencia_9=request.POST.get('fechaExp9', 'default'),
        fecha_finalizacion_experiencia_10=request.POST.get('fechaExp10', 'default'),
        idioma_1=idioma1,
        nivel_idioma_1=request.POST.get('nivel1', 'default'),
        idioma_2=idioma2,
        nivel_idioma_2=request.POST.get('nivel2', 'default'),
        idioma_3=idioma3,
        nivel_idioma_3=request.POST.get('nivel3', 'default'),
        empresa_1=request.POST.get('empresa1', 'default'),
        cargo_1=request.POST.get('cargo1', 'default'),
        funciones_y_logros_1=request.POST.get('funciones1', 'default'),
        empresa_2=request.POST.get('empresa2', 'default'),
        cargo_2=request.POST.get('cargo2', 'default'),
        funciones_y_logros_2=request.POST.get('funciones2', 'default'),
        empresa_3=request.POST.get('empresa3', 'default'),
        cargo_3=request.POST.get('cargo3', 'default'),
        funciones_y_logros_3=request.POST.get('funciones3', 'default'),
        empresa_4=request.POST.get('empresa4', 'default'),
        cargo_4=request.POST.get('cargo4', 'default'),
        funciones_y_logros_4=request.POST.get('funciones4', 'default'),
        empresa_5=request.POST.get('empresa5', 'default'),
        cargo_5=request.POST.get('cargo5', 'default'),
        funciones_y_logros_5=request.POST.get('funciones5', 'default'),
        empresa_6=request.POST.get('empresa6', 'default'),
        cargo_6=request.POST.get('cargo6', 'default'),
        funciones_y_logros_6=request.POST.get('funciones6', 'default'),
        empresa_7=request.POST.get('empresa7', 'default'),
        cargo_7=request.POST.get('cargo7', 'default'),
        funciones_y_logros_7=request.POST.get('funciones7', 'default'),
        empresa_8=request.POST.get('empresa8', 'default'),
        cargo_8=request.POST.get('cargo8', 'default'),
        funciones_y_logros_8=request.POST.get('funciones8', 'default'),
        empresa_9=request.POST.get('empresa9', 'default'),
        cargo_9=request.POST.get('cargo9', 'default'),
        funciones_y_logros_9=request.POST.get('funciones9', 'default'),
        empresa_10=request.POST.get('empresa10', 'default'),
        cargo_10=request.POST.get('cargo10', 'default'),
        funciones_y_logros_10=request.POST.get('funciones10', 'default'),
        areas_de_interes=areaInteres,
        otras_areas_de_interes=request.POST.get('areaInteOtr', 'default'),
        ultimo_salario=request.POST.get('ultiSal', 'default'),
        aspiracion_salarial=aspSalarial,
        archivo_HV=archivoHV,
        referido_por="N/A",
        comentarios="N/A",
        fecha_creacion=fecha_creacion
    )
    
    logger.error("se guardó en la BD")
    # time.sleep(10)
    if cargos == 1:
        nombreImagen = "AUTORESPUESTASIN"
    else:
        nombreImagen = "AUTORESPUESTA"

    subject = "Hemos recibido tu hoja de vida"
    mensaje = '<html><h1>Hola ' + nombres + ',</h1><body><img src=cid:' + nombreImagen + '></body></html>'
    msg = EmailMessage(subject, mensaje, settings.DEFAULT_FROM_EMAIL, [correo])
    rutaImagen = "App/static/App/images/" + nombreImagen + ".jpg"
    file = open(rutaImagen, "rb").read()
    attach_image = MIMEImage(file, 'jpg')
    attach_image.add_header('Content-ID', '<' + nombreImagen + '>')
    attach_image.add_header('Content-Disposition', 'attachment', filename=nombreImagen)
    msg.attach(attach_image)
    msg.content_subtype = "html"
    msg.send()
    logger.error("se envío el correo")

    logger.handlers[0].flush()

    return HttpResponse('Registro completo!', status=200)
