import locale
from datetime import datetime


# ============================================================
# PAÍSES QUE ATRAVIESAN EL ECUADOR
# ============================================================

PAISES_ECUATORIALES = {
    "BR",  # Brasil
    "CO",  # Colombia
    "EC",  # Ecuador
    "ID",  # Indonesia
    "KI",  # Kiribati
    "CG",  # República del Congo
    "CD",  # República Democrática del Congo
    "GA",  # Gabón
    "UG",  # Uganda
    "KE",  # Kenia
    "SO",  # Somalia
    "ST",  # Santo Tomé y Príncipe
}


# ============================================================
# PAÍSES CON TERRITORIO EN EL HEMISFERIO SUR
# ============================================================

PAISES_HEMISFERIO_SUR = {
    # América del Sur
    "AR",  # Argentina
    "BO",  # Bolivia
    "BR",  # Brasil
    "CL",  # Chile
    "CO",  # Colombia
    "EC",  # Ecuador
    "GY",  # Guyana
    "PY",  # Paraguay
    "PE",  # Perú
    "SR",  # Surinam
    "UY",  # Uruguay
    "VE",  # Venezuela

    # África
    "AO",  # Angola
    "BW",  # Botsuana
    "BI",  # Burundi
    "KM",  # Comoras
    "CD",  # República Democrática del Congo
    "SZ",  # Esuatini
    "GA",  # Gabón
    "LS",  # Lesoto
    "MG",  # Madagascar
    "MW",  # Malaui
    "MU",  # Mauricio
    "MZ",  # Mozambique
    "NA",  # Namibia
    "RW",  # Ruanda
    "SC",  # Seychelles
    "ZA",  # Sudáfrica
    "TZ",  # Tanzania
    "ZM",  # Zambia
    "ZW",  # Zimbabue
    "CG",  # República del Congo
    "KE",  # Kenia
    "UG",  # Uganda
    "SO",  # Somalia
    "ST",  # Santo Tomé y Príncipe

    # Asia
    "ID",  # Indonesia
    "TL",  # Timor-Leste

    # Oceanía
    "AU",  # Australia
    "FJ",  # Fiyi
    "KI",  # Kiribati
    "NR",  # Nauru
    "NZ",  # Nueva Zelanda
    "PG",  # Papúa Nueva Guinea
    "SB",  # Islas Salomón
    "TO",  # Tonga
    "TV",  # Tuvalu
    "VU",  # Vanuatu
    "WS",  # Samoa
}


# ============================================================
# NOMBRES DE PAÍSES USADOS POR WINDOWS
# ============================================================

PAISES_WINDOWS = {
    # América
    "Argentina": "AR",
    "Bolivia": "BO",
    "Brazil": "BR",
    "Brasil": "BR",
    "Chile": "CL",
    "Colombia": "CO",
    "Ecuador": "EC",
    "Guyana": "GY",
    "Paraguay": "PY",
    "Peru": "PE",
    "Perú": "PE",
    "Suriname": "SR",
    "Uruguay": "UY",
    "Venezuela": "VE",

    # África
    "Angola": "AO",
    "Botswana": "BW",
    "Burundi": "BI",
    "Comoros": "KM",
    "Eswatini": "SZ",
    "Gabon": "GA",
    "Lesotho": "LS",
    "Madagascar": "MG",
    "Malawi": "MW",
    "Mauritius": "MU",
    "Mozambique": "MZ",
    "Namibia": "NA",
    "Rwanda": "RW",
    "Seychelles": "SC",
    "South Africa": "ZA",
    "Tanzania": "TZ",
    "Zambia": "ZM",
    "Zimbabwe": "ZW",
    "Kenya": "KE",
    "Uganda": "UG",
    "Somalia": "SO",
    "Congo": "CG",
    "Republic of the Congo": "CG",
    "Democratic Republic of the Congo": "CD",
    "Sao Tome and Principe": "ST",
    "São Tomé and Príncipe": "ST",

    # Asia
    "Indonesia": "ID",
    "Timor-Leste": "TL",

    # Oceanía
    "Australia": "AU",
    "Fiji": "FJ",
    "Kiribati": "KI",
    "Nauru": "NR",
    "New Zealand": "NZ",
    "Papua New Guinea": "PG",
    "Solomon Islands": "SB",
    "Tonga": "TO",
    "Tuvalu": "TV",
    "Vanuatu": "VU",
    "Samoa": "WS",

    # Otros
    "United States": "US",
    "UnitedStates": "US",
    "United Kingdom": "GB",
    "UnitedKingdom": "GB",
    "Spain": "ES",
    "España": "ES",
    "France": "FR",
    "Germany": "DE",
    "Italy": "IT",
    "Portugal": "PT",
    "Canada": "CA",
    "Mexico": "MX",
    "México": "MX",
    "Japan": "JP",
    "China": "CN",
    "India": "IN",
}


# ============================================================
# OBTENER CÓDIGO DE PAÍS
# ============================================================

def obtener_codigo_pais():

    loc = locale.getlocale()[0]

    if not loc:
        return None

    # --------------------------------------------------------
    # Formato estándar:
    #
    # es_AR
    # en_US
    # pt_BR
    # --------------------------------------------------------

    if "_" in loc:

        partes = loc.split("_")
        ultima_parte = partes[-1]

        # Código ISO de dos letras
        if len(ultima_parte) == 2:
            return ultima_parte.upper()

    # --------------------------------------------------------
    # Formato Windows:
    #
    # Spanish_Argentina
    # English_United States
    # Portuguese_Brazil
    # --------------------------------------------------------

    if "_" in loc:

        pais = loc.split("_", 1)[1]

        if pais in PAISES_WINDOWS:
            return PAISES_WINDOWS[pais]

    return None


# ============================================================
# DETERMINAR HEMISFERIO
# ============================================================

def obtener_hemisferio(codigo_pais):

    if not codigo_pais:
        return None

    if codigo_pais in PAISES_ECUATORIALES:
        return "ecuatorial"

    if codigo_pais in PAISES_HEMISFERIO_SUR:
        return "sur"

    # Para los países que no están en las listas,
    # asumimos hemisferio norte.
    return "norte"


# ============================================================
# ESTACIÓN - HEMISFERIO SUR
# ============================================================

def obtener_estacion_sur(fecha):

    mes = fecha.month
    dia = fecha.day

    # 21 de diciembre -> 20 de marzo
    # VERANO
    if (
        (mes == 12 and dia >= 21)
        or mes in (1, 2)
        or (mes == 3 and dia <= 20)
    ):
        return "verano"

    # 21 de marzo -> 20 de junio
    # OTOÑO
    elif (
        (mes == 3 and dia >= 21)
        or mes in (4, 5)
        or (mes == 6 and dia <= 20)
    ):
        return "otoño"

    # 21 de junio -> 20 de septiembre
    # INVIERNO
    elif (
        (mes == 6 and dia >= 21)
        or mes in (7, 8)
        or (mes == 9 and dia <= 20)
    ):
        return "invierno"

    # 21 de septiembre -> 20 de diciembre
    # PRIMAVERA
    else:
        return "primavera"


# ============================================================
# ESTACIÓN - HEMISFERIO NORTE
# ============================================================

def obtener_estacion_norte(fecha):

    mes = fecha.month
    dia = fecha.day

    # 21 de diciembre -> 20 de marzo
    # INVIERNO
    if (
        (mes == 12 and dia >= 21)
        or mes in (1, 2)
        or (mes == 3 and dia <= 20)
    ):
        return "invierno"

    # 21 de marzo -> 20 de junio
    # PRIMAVERA
    elif (
        (mes == 3 and dia >= 21)
        or mes in (4, 5)
        or (mes == 6 and dia <= 20)
    ):
        return "primavera"

    # 21 de junio -> 20 de septiembre
    # VERANO
    elif (
        (mes == 6 and dia >= 21)
        or mes in (7, 8)
        or (mes == 9 and dia <= 20)
    ):
        return "verano"

    # 21 de septiembre -> 20 de diciembre
    # OTOÑO
    else:
        return "otoño"


# ============================================================
# OBTENER ESTACIÓN
# ============================================================

def obtener_estacion():

    codigo_pais = obtener_codigo_pais()

    if not codigo_pais:
        return "desconocida"

    hemisferio = obtener_hemisferio(codigo_pais)

    fecha_actual = datetime.now()

    # País ecuatorial
    if hemisferio == "ecuatorial":
        return "ecuatorial"

    # Hemisferio sur
    if hemisferio == "sur":
        return obtener_estacion_sur(fecha_actual)

    # Hemisferio norte
    if hemisferio == "norte":
        return obtener_estacion_norte(fecha_actual)

    return "desconocida"


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

# Configurar locale según el sistema operativo
locale.setlocale(locale.LC_ALL, "")


# Obtener información
locale_actual = locale.getlocale()[0]

codigo_pais = obtener_codigo_pais()

hemisferio = obtener_hemisferio(codigo_pais)

estacion = obtener_estacion()


# ============================================================
# RESULTADO
# ============================================================

print("Locale:     ", locale_actual)
print("País:       ", codigo_pais)
print("Hemisferio: ", hemisferio)
print("Estación:   ", estacion)
