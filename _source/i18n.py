"""Spanish (es) and Haitian Creole (ht) sections of inspectandprotect.net.

Honesty rule: Nicholas does not speak Spanish or Creole. These pages never say
"Hablamos español" / "Nou pale kreyòl". They say reports are in English and that
clients can text in their language and get replies through translation.
"""
import datetime
from content import *

B = None  # build module, set in build_all()

SVC_ORDER = ["home-inspection", "wind-mitigation", "4-point-inspection",
             "mold-inspection-testing", "pre-listing-inspection", "new-construction-inspection"]
EN_PRICE = {s["slug"]: s["price_from"] for s in SERVICES}
CITY_NAME = {a[0]: a[1] for a in AREAS}
CITY_COUNTY = {a[0]: a[2] for a in AREAS}

SVC_SLUGS = {
    "es": {"home-inspection": "inspeccion-de-viviendas", "wind-mitigation": "mitigacion-de-vientos",
           "4-point-inspection": "inspeccion-4-puntos", "mold-inspection-testing": "inspeccion-y-prueba-de-moho",
           "pre-listing-inspection": "inspeccion-antes-de-vender", "new-construction-inspection": "construccion-nueva"},
    "ht": {"home-inspection": "enspeksyon-kay", "wind-mitigation": "mitigasyon-van",
           "4-point-inspection": "enspeksyon-4-pwen", "mold-inspection-testing": "enspeksyon-ak-tes-mwazi",
           "pre-listing-inspection": "enspeksyon-anvan-vann", "new-construction-inspection": "konstriksyon-nouvo"},
}
BASE = {
    "es": {"root": "/es/", "services": "/es/servicios/", "pricing": "/es/precios/", "contact": "/es/reservar/", "areas": "/es/areas/"},
    "ht": {"root": "/ht/", "services": "/ht/sevis/", "pricing": "/ht/pri/", "contact": "/ht/rezeve/", "areas": "/ht/zon/"},
}
CITIES = {
    "es": ["miami", "kendall", "hialeah", "homestead", "doral", "miami-gardens", "coral-gables",
           "fort-lauderdale", "hollywood", "pembroke-pines", "plantation", "miramar", "west-palm-beach", "boca-raton"],
    "ht": ["miami", "north-miami", "miami-gardens", "homestead", "fort-lauderdale", "lauderhill", "north-lauderdale",
           "pompano-beach", "hollywood", "miramar", "delray-beach", "boynton-beach", "lake-worth-beach", "west-palm-beach"],
}

def svc_path(l, slug): return BASE[l]["services"] + SVC_SLUGS[l][slug] + "/"
def city_path(l, c): return BASE[l]["areas"] + c + "/"

def groups():
    g = [{"en": "/", "es": "/es/", "ht": "/ht/"}]
    for key, en in (("services", "/services/"), ("pricing", "/pricing/"), ("contact", "/contact/"), ("areas", "/areas/")):
        g.append({"en": en, "es": BASE["es"][key], "ht": BASE["ht"][key]})
    for s in SVC_ORDER:
        g.append({"en": f"/services/{s}/", "es": svc_path("es", s), "ht": svc_path("ht", s)})
    for a in AREAS:
        d = {"en": f"/areas/{a[0]}/"}
        for l in ("es", "ht"):
            if a[0] in CITIES[l]:
                d[l] = city_path(l, a[0])
        if len(d) > 1:
            g.append(d)
    return g

# =================================================================== SPANISH
CITY_TEXT_ES = {
    "miami": ("Desde condominios en edificios altos hasta casas antiguas en barrios construidos hace décadas, las viviendas de Miami abarcan todas las épocas de la construcción en la Florida.",
              "Las casas antiguas suelen necesitar una inspección de 4 puntos para el seguro, y los dueños de condominios a menudo necesitan un formulario de mitigación de vientos para su unidad."),
    "kendall": ("Kendall es una de las zonas residenciales más grandes de Miami-Dade, con casas unifamiliares, casas adosadas y condominios.",
                "Muchas casas aquí tienen entre 30 y 50 años, la edad en que las aseguradoras empiezan a pedir inspecciones de 4 puntos."),
    "hialeah": ("Hialeah tiene barrios densos de casas de bloque de concreto, muchas con ampliaciones y conversiones hechas con los años.",
                "Prestamos mucha atención a las ampliaciones, los paneles eléctricos y el estado del techo, que importan tanto a compradores como a aseguradoras."),
    "homestead": ("Homestead combina comunidades nuevas de casas adosadas y unifamiliares con casas más antiguas reconstruidas después del huracán Andrew.",
                  "Las casas reconstruidas después de 1992 suelen tener características resistentes al viento que vale la pena documentar en un formulario de mitigación de vientos."),
    "doral": ("Las comunidades más nuevas de Doral incluyen muchas casas adosadas y condominios, además de casas unifamiliares.",
              "Las casas más nuevas de aquí son ideales para inspecciones de construcción nueva y de garantía de 11 meses."),
    "miami-gardens": ("Miami Gardens es mayormente de casas unifamiliares, muchas construidas en los años 60 y 70.",
                      "Las casas de esa época suelen necesitar una inspección de 4 puntos, y vale la pena revisar con cuidado el techo y la plomería."),
    "coral-gables": ("Coral Gables es conocida por sus casas de estilo mediterráneo, muchas con décadas de antigüedad, junto con construcciones más nuevas.",
                     "Las casas antiguas de Gables suelen tener techos de teja, plomería original y electricidad envejecida, todo importante en una inspección de 4 puntos."),
    "fort-lauderdale": ("Las casas de Fort Lauderdale van desde barrios antiguos de casas unifamiliares hasta propiedades frente al agua y condominios.",
                        "Las propiedades frente al agua y las casas antiguas merecen atención especial a la humedad, la corrosión y el estado del techo."),
    "hollywood": ("Hollywood tiene muchas casas unifamiliares de mediados del siglo pasado y condominios cerca de la playa.",
                  "Las casas de esa época suelen requerir una inspección de 4 puntos y pueden tener componentes originales de plomería o electricidad."),
    "pembroke-pines": ("Pembroke Pines está formada en gran parte por comunidades planificadas, casas adosadas y condominios construidos desde los años 80.",
                       "Los dueños de condominios y casas adosadas de aquí necesitan con frecuencia formularios de mitigación de vientos para renovar su seguro."),
    "plantation": ("Plantation es un suburbio establecido con muchas casas unifamiliares en terrenos grandes.",
                   "Muchas casas tienen edad suficiente para necesitar una inspección de 4 puntos, y un aire acondicionado con años de uso merece una revisión cuidadosa."),
    "miramar": ("Miramar va desde barrios antiguos en el este hasta comunidades planificadas más nuevas en el oeste.",
                "Aquí vemos de todo, desde inspecciones de garantía en casas nuevas hasta inspecciones de 4 puntos en casas antiguas."),
    "west-palm-beach": ("West Palm Beach tiene barrios históricos, condominios nuevos y todo lo que hay entre ellos.",
                        "Las casas históricas suelen tener sistemas antiguos que importan tanto a compradores como a aseguradoras."),
    "boca-raton": ("Las casas de Boca Raton incluyen grandes comunidades planificadas, propiedades en campos de golf y condominios.",
                   "Las casas grandes y las comunidades con techos de teja hacen que la mitigación de vientos y la documentación del techo sean especialmente valiosas."),
}

SVC_ES = {
    "home-inspection": {
        "nav": "Inspección de vivienda",
        "title": "Inspección de viviendas en Miami y el sur de la Florida",
        "meta": "Inspector de viviendas con licencia de la Florida (HI18768) en Miami-Dade, Broward y Palm Beach. Informes el mismo día con fotos. Desde $325.",
        "kicker": "Para compradores y vendedores",
        "h1": "Inspecciones que le dicen exactamente lo que está comprando.",
        "lede": "Una inspección visual completa de la estructura y los sistemas de la vivienda, con un informe el mismo día lleno de fotos y explicaciones claras.",
        "covers": [
            ("Techo y ático", "Cubierta del techo, tapajuntas, entablado visible, estructura del ático, ventilación y aislamiento."),
            ("Estructura", "Cimientos, paredes, techos, pisos, ventanas y puertas, con atención a grietas y filtraciones de agua."),
            ("Electricidad", "Panel principal, breakers, cableado visible, tomacorrientes y protección GFCI y AFCI."),
            ("Plomería", "Tuberías de suministro y desagüe, accesorios, calentador de agua y señales de fugas."),
            ("Aire acondicionado", "Funcionamiento del sistema de A/C, manejadora de aire, línea de condensado y bandeja de drenaje."),
            ("Humedad y termografía", "Lecturas con medidor de humedad e imágenes térmicas en áreas sospechosas, incluidas en cada inspección."),
        ],
        "body": [
            "Las casas del sur de la Florida enfrentan una combinación que no se ve en la mayor parte del país: aire salino, sol intenso, meses de humedad y una temporada de huracanes cada año. Eso se nota en techos que envejecen más rápido, equipos de aire acondicionado que trabajan más y agua que llega a lugares que no se ven a simple vista.",
            "Cada inspección incluye medidor de humedad y cámara térmica sin costo adicional. Los daños por agua son la sorpresa más común y más costosa en las casas de la Florida, así que los buscamos en cada trabajo.",
            "Puede acompañarnos durante la inspección. Le mostramos lo que encontramos, respondemos sus preguntas en el momento y le enviamos el informe completo con fotos el mismo día.",
        ],
        "faq": [
            ("¿Cuánto dura una inspección de vivienda?", "La mayoría toma de 2 a 4 horas, según el tamaño, la edad y el estado de la casa."),
            ("¿Cuándo recibo el informe?", "El informe completo con fotos se entrega el mismo día de la inspección. Los informes están en inglés."),
            ("¿Pueden hacer también la mitigación de vientos o la de 4 puntos?", "Sí. Podemos completar ambos formularios de seguro en la misma visita."),
        ],
    },
    "wind-mitigation": {
        "nav": "Mitigación de vientos",
        "title": "Inspección de mitigación de vientos (OIR-B1-1802) en Miami",
        "meta": "Inspecciones de mitigación de vientos en el formulario OIR-B1-1802 vigente para Miami-Dade, Broward y Palm Beach. $150. Puede bajar el costo de su seguro.",
        "kicker": "Inspección para el seguro",
        "h1": "Un informe de mitigación de vientos puede bajar su seguro.",
        "lede": "Documentamos las características de su casa que resisten el viento en el formulario oficial OIR-B1-1802 de la Florida, para que su aseguradora aplique los descuentos que le corresponden.",
        "covers": [
            ("Código de construcción", "Año de construcción e historial de permisos para determinar bajo qué código se construyó la casa."),
            ("Cubierta del techo", "Tipo de techo y su aprobación de producto o fecha de permiso."),
            ("Fijación del entablado", "Cómo está clavado el entablado del techo a las cerchas o vigas."),
            ("Conexión techo-pared", "Clavos, clips o amarres sencillos o dobles que unen el techo a las paredes."),
            ("Forma del techo", "Techo a cuatro aguas, a dos aguas o plano, y en qué proporción."),
            ("Barrera secundaria contra agua", "Si una membrana sellada evitaría la entrada de agua al perderse tejas o shingles."),
            ("Protección de aberturas", "Ventanas, puertas y puertas de garaje de impacto, o contraventanas, y sus certificaciones."),
        ],
        "body": [
            "La ley de la Florida exige que las aseguradoras ofrezcan descuentos por características de construcción resistentes al viento, pero solo pueden aplicarlos si esas características están documentadas en el formulario oficial.",
            "Completamos la versión vigente del formulario OIR-B1-1802 con fotos que respaldan cada respuesta. Las aseguradoras rechazan formularios en versiones antiguas, por eso nos mantenemos al día.",
            "Por lo general, el formulario es válido por cinco años siempre que la casa no cambie. Si instala un techo nuevo o ventanas de impacto, una nueva inspección puede reflejar la mejora.",
        ],
        "faq": [
            ("¿Cuánto puedo ahorrar?", "Depende de las características de su casa y de su aseguradora, pero muchos propietarios ven reducciones importantes en la parte de vientos de su prima."),
            ("¿Cuánto tiempo toma?", "Normalmente de 30 a 45 minutos en la propiedad."),
            ("¿Tengo que estar en casa?", "Alguien debe darnos acceso al ático y a las ventanas y puertas exteriores."),
        ],
    },
    "4-point-inspection": {
        "nav": "Inspección de 4 puntos",
        "title": "Inspección de 4 puntos para el seguro en Miami y el sur de la Florida",
        "meta": "Inspecciones de 4 puntos (techo, electricidad, plomería y A/C) para casas antiguas en la Florida. $150. Formulario el mismo día para su aseguradora.",
        "kicker": "Inspección para el seguro",
        "h1": "Inspecciones de 4 puntos que su aseguradora acepta.",
        "lede": "Muchas aseguradoras exigen una inspección de 4 puntos en casas antiguas antes de emitir o renovar una póliza. Revisamos los cuatro sistemas que les importan y le entregamos el formulario el mismo día.",
        "covers": [
            ("Techo", "Tipo de cubierta, edad, vida útil restante y señales de filtraciones o daños."),
            ("Electricidad", "Marca y estado del panel, tipo de cableado y riesgos como breakers con doble conexión o tapas faltantes."),
            ("Plomería", "Material de las tuberías, edad y estado del calentador de agua, y fugas visibles."),
            ("Aire acondicionado", "Edad, funcionamiento y estado del sistema."),
        ],
        "body": [
            "Muchas aseguradoras de la Florida piden una inspección de 4 puntos en casas de aproximadamente 25 a 30 años o más, aunque cada compañía tiene sus propias reglas.",
            "Algunos elementos suelen causar problemas con las aseguradoras, como ciertas marcas antiguas de paneles eléctricos, tuberías de polibutileno, techos viejos y fugas activas. Documentamos con fotos exactamente lo que hay para que su agente tenga lo que necesita.",
            "Si primero hace falta una reparación, podemos regresar después del trabajo para actualizar el informe.",
        ],
        "faq": [
            ("¿Cuánto dura una inspección de 4 puntos?", "Entre 45 minutos y una hora en la propiedad."),
            ("¿Pueden hacer la mitigación de vientos al mismo tiempo?", "Sí. La mayoría de los clientes reservan ambas en una sola visita."),
            ("¿Y si algo no pasa?", "El informe documenta lo que hay. Después de las reparaciones, podemos volver a inspeccionar y actualizarlo."),
        ],
    },
    "mold-inspection-testing": {
        "nav": "Inspección y prueba de moho",
        "title": "Inspección y prueba de moho en Miami",
        "meta": "Inspección de moho con pruebas de laboratorio en Miami-Dade y Broward. Mapeo de humedad, termografía y hasta 3 muestras por $375. Hacemos pruebas, no vendemos limpieza.",
        "kicker": "Pruebas ambientales",
        "h1": "Primero encontramos la humedad, luego hacemos las pruebas que importan.",
        "lede": "Un conteo de esporas por sí solo no le dice de dónde viene el agua. Revisamos la casa con medidor de humedad y cámara térmica antes de tomar cualquier muestra.",
        "covers": [
            ("Cada habitación accesible", "Paredes, techos, pisos, zócalos, debajo de los lavamanos, duchas, cocina y lavandería."),
            ("Termografía", "Patrones de temperatura alrededor de ventanas, plomería y el techo que pueden indicar humedad oculta."),
            ("Aire acondicionado y ático", "Manejadora de aire, serpentín, bandeja y línea de drenaje, conexiones de ductos y aislamiento del ático."),
            ("Muestras de laboratorio", "Hasta 3 muestras de aire o superficie con un control exterior, enviadas a un laboratorio acreditado."),
        ],
        "body": [
            "En el sur de la Florida, la manejadora de aire suele estar en un clóset o en el ático, y el serpentín, la bandeja de drenaje y las conexiones de los ductos son donde el moho aparece con más frecuencia. Revisamos el sistema, no solo las habitaciones.",
            "Las muestras se toman donde apuntan los hallazgos. Una muestra de aire interior siempre se compara con una muestra exterior tomada el mismo día.",
            "Solo inspeccionamos y hacemos pruebas. No removemos moho, así que nuestro informe no tiene nada que venderle. Si hace falta limpieza, usted elige al contratista.",
        ],
        "faq": [
            ("¿Cuál es la diferencia entre inspección y prueba de moho?", "La inspección encuentra humedad y crecimiento visible. La prueba envía muestras de aire o superficie a un laboratorio para medir lo que hay. Nuestro servicio incluye ambas."),
            ("¿Cómo me preparo?", "Mantenga ventanas y puertas cerradas 24 horas antes, no haga limpieza profunda, apague los purificadores de aire y deje acceso al clóset del A/C y al ático."),
            ("¿Ustedes remueven moho?", "No. Solo inspeccionamos y hacemos pruebas, así que nuestros resultados nunca vienen con un trabajo de limpieza."),
        ],
        "note": "La inspección y las pruebas de moho se realizan bajo nuestra licencia de inspector de viviendas de la Florida. No realizamos evaluaciones de moho (mold assessment) ni remediación de moho.",
    },
    "pre-listing-inspection": {
        "nav": "Inspección antes de vender",
        "title": "Inspección antes de vender su casa en Miami",
        "meta": "Inspecciones para vendedores en el sur de la Florida. Encuentre los problemas antes que el comprador y fije el precio con confianza. Informe el mismo día.",
        "kicker": "Para vendedores",
        "h1": "Sepa lo que encontrará el inspector del comprador, antes de que lo encuentre.",
        "lede": "Una inspección antes de poner la casa en venta le da tiempo para reparar, ajustar el precio o informar los problemas en sus propios términos.",
        "covers": [
            ("Inspección completa", "El mismo alcance que una inspección para compradores: techo, estructura, electricidad, plomería y A/C."),
            ("Humedad y termografía", "Medidor de humedad e imágenes térmicas incluidos."),
            ("Formularios de seguro", "Una mitigación de vientos y una inspección de 4 puntos recientes ayudan a los compradores a cotizar su seguro más rápido."),
        ],
        "body": [
            "La razón más común por la que las ventas en la Florida se caen o se renegocian es una sorpresa en la inspección. Encontrarla primero le da el control.",
            "Tener listas una mitigación de vientos y una inspección de 4 puntos también ayuda: los compradores pueden cotizar su seguro rápidamente, una ventaja real en el mercado de seguros de la Florida.",
        ],
        "faq": [
            ("¿Tengo que informar lo que encuentren?", "Las reglas de divulgación son una pregunta para su agente o abogado. Nuestro informe es un registro objetivo de lo que observamos."),
        ],
    },
    "new-construction-inspection": {
        "nav": "Construcción nueva y garantía",
        "title": "Inspecciones de construcción nueva y garantía de 11 meses en el sur de la Florida",
        "meta": "Inspecciones de construcción nueva y de garantía de 11 meses en Miami-Dade, Broward y Palm Beach. Documente los defectos antes de que venza su garantía.",
        "kicker": "Casas nuevas",
        "h1": "Nueva no significa perfecta.",
        "lede": "Los constructores trabajan rápido. Una inspección independiente antes del cierre, y otra antes de que venza su garantía de 11 meses, detecta defectos mientras el constructor todavía tiene que repararlos.",
        "covers": [
            ("Antes del cierre", "Una inspección completa antes del recorrido final para que su lista de pendientes esté completa."),
            ("Garantía de 11 meses", "Documenta los defectos que aparecieron después de mudarse, antes de que termine la garantía del constructor."),
            ("Humedad y termografía", "Las imágenes térmicas son muy útiles en casas nuevas para detectar aislamiento faltante y fugas ocultas."),
        ],
        "body": [
            "Hemos inspeccionado casas adosadas y unifamiliares de construcción nueva en todo el sur de la Florida. Los hallazgos más comunes son pequeños pero se suman: aislamiento faltante, aberturas sin sellar, problemas de drenaje y acabados incompletos.",
            "Reserve la inspección de 11 meses aproximadamente un mes antes de la fecha de su garantía para tener tiempo de enviar la lista al constructor.",
        ],
        "faq": [],
    },
}

T_ES = {
    "home": "Inicio", "menu": "Menú", "call": "Llamar", "call_or_text": "Llame o escriba",
    "nav_services": "Servicios", "nav_pricing": "Precios", "nav_mold": "Prueba de moho", "nav_areas": "Áreas", "nav_book": "Reservar",
    "lang_note": "Los informes se entregan en inglés. Escríbanos por texto en español y le responderemos con ayuda de traducción.",
    "hero_kicker": f"Inspector de viviendas con licencia de la Florida · {LICENSE}",
    "hero_h1": "Inspecciones de viviendas certificadas.<br><em>Informes el mismo día.</em>",
    "hero_lede": "Inspecciones de viviendas, mitigación de vientos, 4 puntos y pruebas de moho en Miami-Dade, Broward y Palm Beach, con precios claros desde el principio.",
    "btn_schedule": "Reservar inspección", "btn_prices": "Ver precios",
    "stats": [("5.0 ★", f"{TOTAL_REVIEWS} reseñas · Google + Thumbtack"), ("Mismo día", "Informes con fotos"),
              ("Térmica + humedad", "En cada inspección"), ("InterNACHI", "Inspector certificado")],
    "services_kicker": "Servicios", "services_h2": "Todo lo que una casa del sur de la Florida necesita inspeccionar",
    "pricing_kicker": "Precios", "pricing_h2": "Precios claros. Sin sorpresas.",
    "card_home": "Inspección de vivienda", "card_home_sub": "Según los pies cuadrados",
    "card_ins": "Inspecciones para el seguro", "card_ins_sub": "Formularios de la Florida que su aseguradora acepta",
    "ins_blurb": "La mitigación de vientos puede bajar su prima de vientos. La de 4 puntos cubre techo, electricidad, plomería y A/C en casas antiguas.",
    "card_mold": "Inspección y prueba de moho", "card_mold_sub": "Análisis de laboratorio incluido", "whats_included": "Qué incluye →",
    "pay_title": "Pago sencillo", "pay_text": "Pague el día de la inspección. El informe se entrega una vez recibido el pago.",
    "pay_over": "Divida su inspección en pagos sin intereses con Afterpay o Affirm, sujeto a aprobación.",
    "price_note": "Cada inspección incluye medidor de humedad, cámara térmica, fotos e informe digital completo. Puede aplicar un cargo por distancia fuera de Miami-Dade y Broward.",
    "tiers": [("Condominio / menos de 1,200 pies²", "$325"), ("1,200–1,999 pies²", "$395"), ("2,000–2,999 pies²", "$475"),
              ("3,000–3,999 pies²", "$550"), ("4,000+ pies²", "desde $625")],
    "insurance": [("Mitigación de vientos (OIR-B1-1802)", "$150"), ("Inspección de 4 puntos", "$150")],
    "env": [("Inspección y prueba de moho", "hasta 3 muestras de laboratorio, con control exterior", "$375"), ("Muestra adicional de moho", "", "$75 c/u")],
    "payment": ["Tarjeta de crédito", "Apple Pay", "Zelle", "Venmo", "PayPal", "Efectivo o cheque"],
    "from": "Desde {p}",
    "mold_kicker": "Inspección y prueba de moho", "callout_h": "Hacemos pruebas. No vendemos limpieza.",
    "callout_p": "No removemos moho, así que nuestros resultados nunca vienen con un trabajo de limpieza.", "callout_btn": "Detalles de la prueba de moho",
    "reviews_kicker": "Reseñas", "reviews_h2": "{n} reseñas de cinco estrellas",
    "google_sub": "{n} reseñas · todas de cinco estrellas · léalas en Google", "tt_sub": "{n} reseñas · Top Pro · léalas en Thumbtack",
    "leave_review": "Déjenos una reseña en Google",
    "steps_kicker": "Cómo funciona", "steps_h2": "Reserve en minutos. Informe el mismo día.",
    "steps": [("PASO 1", "Vea su precio", "Los precios aparecen según los pies cuadrados, así sabe el costo antes de llamar."),
              ("PASO 2", "Reserve y firme", "Elija un horario y firme el acuerdo de inspección. Su cita queda confirmada."),
              ("PASO 3", "Día de la inspección", "Puede acompañarnos. Le mostramos lo que encontramos."),
              ("PASO 4", "Informe el mismo día", "Fotos, hallazgos y explicaciones claras, entregados ese mismo día.")],
    "areas_kicker": "Áreas", "areas_h2": "Miami-Dade, Broward y Palm Beach",
    "faq_kicker": "Preguntas frecuentes", "faq_h2": "Preguntas comunes",
    "cta_h": "¿Listo para reservar?", "cta_p": "Llame, escriba o reserve en línea. Confirmamos en menos de 2 horas.",
    "cta_btn": "Reservar inspección", "cta_call": "Llamar al {phone}",
    "what_we_check": "Qué revisamos", "questions": "Preguntas", "other_services": "Otros servicios", "areas_we_serve": "Áreas que servimos",
    "book_from": "Reservar · desde {p}", "full_price_list": "Lista de precios",
    "svc_index_title": "Servicios de inspección de viviendas en Miami y el sur de la Florida",
    "svc_index_meta": "Inspecciones de viviendas, mitigación de vientos, 4 puntos, inspección y prueba de moho, inspecciones antes de vender y de construcción nueva en el sur de la Florida.",
    "svc_index_h1": "Servicios de inspección",
    "svc_index_lede": "Inspecciones de viviendas, inspecciones para el seguro y pruebas de moho en Miami-Dade, Broward y Palm Beach.",
    "pricing_title": "Precios de inspección de viviendas en Miami, Broward y Palm Beach",
    "pricing_meta": "Precios de inspección de viviendas según los pies cuadrados desde $325. Mitigación de vientos y 4 puntos $150 cada una. Inspección y prueba de moho $375 con laboratorio.",
    "pricing_h1": "Precios de inspección", "pricing_lede": "Precios claros antes de reservar. Sin cargos ocultos.", "pricing_faq_h2": "Preguntas sobre precios",
    "contact_title": "Reservar una inspección de vivienda",
    "contact_meta": "Reserve una inspección de vivienda, mitigación de vientos, 4 puntos o prueba de moho en el sur de la Florida. Confirmamos en menos de 2 horas.",
    "contact_h1": "Reservar una inspección", "contact_lede": "Envíe sus datos y le confirmaremos en menos de 2 horas.",
    "f_first": "Nombre", "f_last": "Apellido", "f_phone": "Teléfono", "f_email": "Correo electrónico", "f_address": "Dirección de la propiedad",
    "f_service": "Servicio", "f_sqft": "Pies cuadrados", "f_date": "Fecha preferida", "f_source": "¿Cómo nos encontró?",
    "sources": ["Google", "Thumbtack", "Agente de bienes raíces", "Agente de seguros", "Amigo o familiar", "Otro"],
    "f_notes": "¿Algo que debamos saber?", "f_submit": "Solicitar mi inspección →", "f_multiple": "Varios servicios",
    "f_note": "El acuerdo de inspección se firma antes de la visita; al firmarlo, su fecha y hora quedan confirmadas.",
    "f_subject": "Nueva solicitud (Español) – inspectandprotect.net", "lang_value": "Español",
    "areas_title": "Áreas de servicio: Miami-Dade, Broward y Palm Beach",
    "areas_meta": "Inspect and Protect sirve a Miami, Kendall, Hialeah, Homestead, Doral, Fort Lauderdale, Hollywood, Pembroke Pines, West Palm Beach, Boca Raton y más.",
    "areas_h1": "Áreas que servimos", "areas_lede": "Inspecciones de viviendas, mitigación de vientos, 4 puntos y pruebas de moho en estas ciudades.",
    "county": "Condado de {c}", "all_cities_en": "Ver todas las ciudades (en inglés)", "all_areas": "Todas las áreas",
    "areas_other": "¿Está en otra zona? Llame al {phone}. También aceptamos trabajos en otras partes de la Florida con un cargo por distancia.",
    "city_title": "Inspector de viviendas en {name}, FL – Mitigación de vientos y 4 puntos",
    "city_meta": "Inspector de viviendas con licencia en {name}, FL. Inspecciones desde $325, mitigación de vientos y 4 puntos $150, pruebas de moho $375. Informes el mismo día.",
    "city_h1": "Inspector de viviendas en {name}, FL",
    "city_lede": "Inspecciones de viviendas, mitigación de vientos, 4 puntos y pruebas de moho en {name}, con informes el mismo día.",
    "city_book": "Reservar en {name}", "city_h2": "Inspecciones en {name}",
    "city_std": f"Cada inspección incluye lecturas de humedad e imágenes térmicas, y su informe con fotos llega el mismo día. Tenemos la licencia de inspector de viviendas de la Florida #{LICENSE} y la certificación de InterNACHI.",
    "city_services": "Servicios en {name}", "city_svc_card": "{svc} en {name}", "prices": "Precios",
    "city_faq_h2": "Preguntas sobre {name}", "nearby": "Áreas cercanas", "city_cta": "¿Necesita un inspector en {name}?",
    "city_faq": [("¿Cuánto cuesta una inspección de vivienda en {name}?", "Las inspecciones de viviendas en {name} empiezan en $325 y se calculan según los pies cuadrados. La mitigación de vientos y la inspección de 4 puntos cuestan $150 cada una."),
                 ("¿Qué tan pronto pueden inspeccionar en {name}?", "Programamos inspecciones en {name} los 7 días de la semana, a menudo en uno o dos días. Los informes se entregan el mismo día."),
                 ("¿Cobran por distancia a {name}?", "{travel}")],
    "travel_free": "No hay cargo por distancia dentro de Miami-Dade y Broward.",
    "travel_pb": "Puede aplicar un cargo por distancia en el condado de Palm Beach; se lo diremos antes de reservar.",
    "footer_about": "Inspecciones de viviendas con licencia, inspecciones para el seguro y pruebas de moho en Miami-Dade, Broward y Palm Beach.",
    "company": "Empresa", "reviews_link": "Reseñas",
    "legal": f"Inspector de viviendas con licencia de la Florida #{LICENSE} · Certificado por InterNACHI · Asegurado. La inspección y las pruebas de moho se realizan bajo nuestra licencia de inspector de viviendas de la Florida; no realizamos evaluaciones ni remediación de moho.",
    "home_title": "Inspector de viviendas en Miami y el sur de la Florida | Inspect and Protect",
    "home_meta": "Inspector de viviendas con licencia de la Florida (HI18768) en Miami-Dade, Broward y Palm Beach. Inspecciones desde $325, mitigación de vientos y 4 puntos $150, pruebas de moho $375. Informes el mismo día.",
    "home_faq": [
        ("¿Cuánto cuesta una inspección de vivienda?", "Las inspecciones empiezan en $325 para condominios y casas de menos de 1,200 pies cuadrados y se calculan según el tamaño. La mitigación de vientos y la inspección de 4 puntos cuestan $150 cada una."),
        ("¿Cuánto dura una inspección?", "La mayoría toma de 2 a 4 horas según el tamaño y el estado de la casa. Puede acompañarnos."),
        ("¿Cuándo recibo el informe?", "Los informes y las fotos se entregan el mismo día. Los informes están en inglés."),
        ("¿En qué idioma me atienden?", "Hablamos inglés. Puede escribirnos por texto en español y le responderemos con ayuda de traducción."),
        ("¿Tienen licencia y seguro?", f"Sí. Somos inspectores de viviendas con licencia de la Florida (#{LICENSE}), certificados por InterNACHI, con seguro de errores y omisiones y de responsabilidad civil."),
    ],
    "pricing_faq": [
        ("¿Por qué el precio depende de los pies cuadrados?", "Las casas más grandes toman más tiempo y tienen más sistemas que revisar, así que el precio aumenta con el tamaño."),
        ("¿Cobran por distancia?", "No dentro de Miami-Dade y Broward. Puede aplicar un cargo más lejos; se lo diremos antes de reservar."),
        ("¿Cuándo pago?", "El pago se hace el día de la inspección. El informe se entrega una vez recibido el pago."),
    ],
}

# =================================================================== HAITIAN CREOLE
CITY_TEXT_HT = {
    "miami": ("Soti nan kondo nan gwo bilding rive nan vye kay nan katye yo te bati depi lontan, Miami gen kay ki soti nan tout epòk konstriksyon Florid.",
              "Vye kay yo souvan bezwen yon enspeksyon 4 pwen pou asirans, epi moun ki gen kondo souvan bezwen yon fòm mitigasyon van pou inite yo."),
    "north-miami": ("North Miami gen anpil kay fanmi ki te bati nan mitan syèk pase a, ak kondo toupre bè a.",
                    "Kay ki gen laj sa a souvan gen vye tiyo, vye panèl elektrik ak tèt kay konpayi asirans yo gade byen."),
    "miami-gardens": ("Miami Gardens se sitou kay fanmi, anpil ladan yo te bati nan ane 1960 ak 1970 yo.",
                      "Kay ki gen laj sa a souvan bezwen yon enspeksyon 4 pwen, epi li bon pou tcheke tèt kay la ak plonbri a byen."),
    "homestead": ("Homestead gen nouvo kominote kay ak townhouse, ansanm ak vye kay yo te rebati apre siklòn Andrew.",
                  "Kay yo rebati apre 1992 souvan gen bagay ki fè yo reziste kont van, e sa vo lapenn mete sou yon fòm mitigasyon van."),
    "fort-lauderdale": ("Kay nan Fort Lauderdale soti nan vye katye kay fanmi rive nan kay bò dlo ak kondo.",
                        "Kay bò dlo ak vye kay merite atansyon espesyal pou imidite, rouy ak kondisyon tèt kay la."),
    "lauderhill": ("Lauderhill se sitou kondo, townhouse ak ti kay fanmi.",
                   "Vye bilding kondo ak townhouse yo souvan bezwen enspeksyon pou asirans lè l rive lè pou renouvle polis la."),
    "north-lauderdale": ("North Lauderdale se sitou townhouse, kondo ak kay fanmi ki te bati depi ane 1970 yo.",
                         "Enspeksyon pou asirans se sa moun isit la bezwen pi souvan, sitou lè pou renouvle polis la."),
    "pompano-beach": ("Pompano Beach gen kondo bò lanmè ak vye katye kay fanmi pi lwen nan teren an.",
                      "Lè ki gen sèl bò lanmè a fè metal rouye pi vit, kidonk nou tcheke ekipman AC ak pyès metal yo byen."),
    "hollywood": ("Hollywood gen anpil kay fanmi ki te bati nan mitan syèk pase a, ak kondo toupre plaj la.",
                  "Kay ki gen laj sa a souvan bezwen yon enspeksyon 4 pwen epi yo ka toujou gen tiyo oswa fil elektrik orijinal."),
    "miramar": ("Miramar soti nan vye katye bò lès rive nan nouvo kominote bò lwès.",
                "Nou wè tout kalite travay isit la, soti nan enspeksyon garanti pou kay nouvo rive nan enspeksyon 4 pwen pou vye kay."),
    "delray-beach": ("Delray Beach gen vye kay istorik toupre anba lavil, ak kominote gòlf ak kominote fèmen bò lwès.",
                     "Vye kay yo bezwen atansyon pou ansyen sistèm yo; nouvo kominote yo souvan ka jwenn rabè mitigasyon van."),
    "boynton-beach": ("Boynton Beach gen anpil kominote pou moun 55 an oswa plis, kondo ak kay fanmi.",
                      "Enspeksyon pou asirans lè pou renouvle polis la se yon bezwen ki komen anpil isit la."),
    "lake-worth-beach": ("Lake Worth Beach gen ti kay ak bungalow ki gen anpil laj, kèk ladan yo soti nan kòmansman ak mitan ane 1900 yo.",
                         "Vye kay isit la ka gen vye fil elektrik ak vye tiyo konpayi asirans yo gade byen."),
    "west-palm-beach": ("West Palm Beach gen katye istorik, kondo nouvo ak tout sa ki genyen ant yo.",
                        "Kay istorik yo souvan gen ansyen sistèm ki enpòtan pou achtè ak pou konpayi asirans."),
}

SVC_HT = {
    "home-inspection": {
        "nav": "Enspeksyon kay",
        "title": "Enspeksyon kay nan Miami ak Sid Florid",
        "meta": "Enspektè kay ki gen lisans Florid (HI18768) nan Miami-Dade, Broward ak Palm Beach. Rapò ak foto menm jou a. Apati $325.",
        "kicker": "Pou moun k ap achte ak moun k ap vann",
        "h1": "Yon enspeksyon ki di w egzakteman sa w ap achte.",
        "lede": "Nou egzamine estrikti kay la ak tout sistèm li yo, epi nou voye yon rapò ak foto ak eksplikasyon klè menm jou a.",
        "covers": [
            ("Tèt kay ak galata", "Kouvèti tèt kay la, flachin, bwa ki parèt, chapant galata a, vantilasyon ak izolasyon."),
            ("Estrikti", "Fondasyon, mi, plafon, planche, fenèt ak pòt. Nou chèche fant ak kote dlo antre."),
            ("Elektrisite", "Panèl prensipal la, brekè yo, fil ki parèt, priz ak pwoteksyon GFCI ak AFCI."),
            ("Plonbri", "Tiyo dlo ak tiyo drenaj, aparèy yo, chofe dlo a, ak siy fuit."),
            ("Èkondisyone (AC)", "Jan sistèm AC a mache, èandlè a, liy kondansasyon an ak plato drenaj la."),
            ("Imidite ak kamera tèmik", "Nou mezire imidite epi nou itilize yon kamera tèmik sou zòn ki sispèk. Sa enkli nan chak enspeksyon."),
        ],
        "body": [
            "Kay nan Sid Florid fè fas ak yon melanj ou pa wè nan anpil lòt kote: lè ki gen sèl, gwo solèy, anpil mwa imidite, ak yon sezon siklòn chak ane. Sa fè tèt kay yo vin vye pi vit, AC yo travay pi di, epi dlo rive nan kote ou pa ka wè.",
            "Chak enspeksyon gen yon aparèy pou mezire imidite ak yon kamera tèmik san lajan anplis. Domaj dlo se sipriz ki pi komen e ki koute pi chè nan kay Florid, se poutèt sa nou chèche l nan chak travay.",
            "Ou ka vin avè nou pandan enspeksyon an. N ap montre w sa nou jwenn, n ap reponn kesyon w yo sou plas, epi n ap voye rapò konplè a ak foto menm jou a.",
        ],
        "faq": [
            ("Konbyen tan yon enspeksyon kay pran?", "Pifò pran 2 a 4 èdtan, selon gwosè, laj ak kondisyon kay la."),
            ("Kilè m ap resevwa rapò a?", "Nou voye rapò konplè a ak foto menm jou enspeksyon an. Rapò yo ekri an anglè."),
            ("Èske nou ka fè mitigasyon van ak enspeksyon 4 pwen an tou?", "Wi. Nou ka ranpli de fòm asirans yo pandan menm vizit la."),
        ],
    },
    "wind-mitigation": {
        "nav": "Mitigasyon van",
        "title": "Enspeksyon mitigasyon van (OIR-B1-1802) nan Miami",
        "meta": "Enspeksyon mitigasyon van sou fòm OIR-B1-1802 aktyèl la nan Miami-Dade, Broward ak Palm Beach. $150. Li ka fè asirans ou bese.",
        "kicker": "Enspeksyon pou asirans",
        "h1": "Yon rapò mitigasyon van ka fè asirans ou bese.",
        "lede": "Nou dokimante sa ki fè kay ou reziste kont van sou fòm ofisyèl Florid la, OIR-B1-1802, pou konpayi asirans ou a ka ba w rabè ou merite yo.",
        "covers": [
            ("Kòd konstriksyon", "Ane yo bati kay la ak istwa pèmi yo, pou konnen ki kòd yo te swiv."),
            ("Kouvèti tèt kay", "Ki kalite tèt kay ak dat pèmi oswa apwobasyon pwodwi a."),
            ("Jan bwa tèt kay la kloure", "Ki jan bwa tèt kay la kloure sou chapant lan."),
            ("Koneksyon tèt kay ak mi", "Klou, klip oswa strap ki tache tèt kay la ak mi yo."),
            ("Fòm tèt kay la", "Tèt kay a kat pant (hip), de pant (gable) oswa plat."),
            ("Dezyèm baryè kont dlo", "Si gen yon kouch sele anba tèt kay la ki ta anpeche dlo antre si van an rache shingles oswa tuil yo."),
            ("Pwoteksyon ouvèti yo", "Fenèt, pòt ak pòt garaj anti-enpak, oswa pwoteksyon siklòn (shutters), ak sètifikasyon yo."),
        ],
        "body": [
            "Lalwa Florid mande konpayi asirans yo ofri rabè pou kay ki bati pou reziste kont van, men yo ka bay rabè sa yo sèlman si yo dokimante sou fòm ofisyèl la.",
            "Nou ranpli dènye vèsyon fòm OIR-B1-1802 la ak foto pou chak repons. Konpayi asirans yo refize fòm ki nan vye vèsyon, se pou sa nou toujou itilize vèsyon aktyèl la.",
            "An jeneral, fòm nan bon pou senk ane si anyen pa chanje sou kay la. Si w mete yon nouvo tèt kay oswa fenèt anti-enpak, yon nouvo enspeksyon ka montre amelyorasyon an.",
        ],
        "faq": [
            ("Konbyen m ka ekonomize?", "Sa depann de kay ou ak konpayi asirans ou, men anpil pwopriyetè wè yon bon rediksyon sou pati van nan prim yo."),
            ("Konbyen tan sa pran?", "Anjeneral 30 a 45 minit sou plas."),
            ("Èske m bezwen la?", "Yon moun dwe ban nou aksè nan galata a ak nan fenèt ak pòt deyò yo."),
        ],
    },
    "4-point-inspection": {
        "nav": "Enspeksyon 4 pwen",
        "title": "Enspeksyon 4 pwen pou asirans nan Miami ak Sid Florid",
        "meta": "Enspeksyon 4 pwen (tèt kay, elektrisite, plonbri ak AC) pou kay ki gen laj nan Florid. $150. Fòm nan menm jou a pou konpayi asirans ou.",
        "kicker": "Enspeksyon pou asirans",
        "h1": "Enspeksyon 4 pwen konpayi asirans ou ap aksepte.",
        "lede": "Anpil konpayi asirans mande yon enspeksyon 4 pwen pou kay ki gen laj anvan yo bay oswa renouvle yon polis. Nou enspekte kat sistèm yo enterese ladan yo epi nou ba w fòm nan menm jou a.",
        "covers": [
            ("Tèt kay", "Ki kalite kouvèti, laj li, konbyen tan li rete, ak siy fuit oswa domaj."),
            ("Elektrisite", "Mak ak kondisyon panèl la, kalite fil, ak danje tankou de fil sou yon sèl brekè oswa kouvèti ki manke."),
            ("Plonbri", "Ki materyèl tiyo yo ye, laj ak kondisyon chofe dlo a, ak fuit ki parèt."),
            ("Èkondisyone (AC)", "Laj, fonksyònman ak kondisyon sistèm nan."),
        ],
        "body": [
            "Anpil konpayi asirans nan Florid mande yon enspeksyon 4 pwen pou kay ki gen apeprè 25 a 30 an oswa plis, men chak konpayi gen pwòp règ li.",
            "Gen kèk bagay ki konn bay pwoblèm ak konpayi asirans yo, tankou kèk vye mak panèl elektrik, tiyo polibitilèn, tèt kay ki vye, ak fuit dlo. Nou pran foto egzakteman sa ki la pou ajan w lan gen sa li bezwen.",
            "Si gen yon reparasyon pou fè anvan, nou ka retounen apre travay la pou mete rapò a ajou.",
        ],
        "faq": [
            ("Konbyen tan yon enspeksyon 4 pwen pran?", "Apeprè 45 minit a inèdtan sou plas."),
            ("Èske nou ka fè mitigasyon van an an menm tan?", "Wi. Pifò kliyan rezève tou de nan yon sèl vizit."),
            ("E si yon bagay pa bon?", "Rapò a montre sa ki la. Apre reparasyon yo, nou ka retounen enspekte epi mete l ajou."),
        ],
    },
    "mold-inspection-testing": {
        "nav": "Enspeksyon ak tès mwazi",
        "title": "Enspeksyon ak tès mwazi nan Miami",
        "meta": "Enspeksyon mwazi ak tès laboratwa nan Miami-Dade ak Broward. Nou chèche imidite, nou itilize kamera tèmik, ak jiska 3 echantiyon pou $375. Nou fè tès, nou pa vann netwayaj.",
        "kicker": "Tès anviwònman",
        "h1": "Nou jwenn imidite a anvan, epi nou teste sa ki enpòtan.",
        "lede": "Yon kantite espò pou kont li pa ka di w ki kote dlo a soti. Nou tcheke kay la ak yon aparèy imidite ak yon kamera tèmik anvan nou pran okenn echantiyon.",
        "covers": [
            ("Chak chanm nou ka rive", "Mi, plafon, planche, anba lavabo, douch, kwizin ak kote ou lave rad."),
            ("Kamera tèmik", "Diferans tanperati bò fenèt, tiyo ak tèt kay la ki ka montre imidite kache."),
            ("AC ak galata", "Èandlè a, bobin (coil) la, plato ak liy drenaj la, kanal lè yo ak izolasyon galata a."),
            ("Echantiyon laboratwa", "Jiska 3 echantiyon lè oswa sifas ak yon echantiyon deyò pou konpare, nou voye yo nan yon laboratwa akredite."),
        ],
        "body": [
            "Nan Sid Florid, èandlè a souvan nan yon klozèt oswa nan galata a, e se bobin nan, plato drenaj la ak kanal lè yo ki kote mwazi konn kòmanse. Nou tcheke sistèm nan, pa sèlman chanm yo.",
            "Nou pran echantiyon kote rezilta yo montre. Nou toujou konpare yon echantiyon lè anndan ak yon echantiyon deyò nou pran menm jou a.",
            "Nou sèlman enspekte epi fè tès. Nou pa retire mwazi, kidonk rapò nou an pa gen anyen pou l vann ou. Si gen netwayaj pou fè, se ou ki chwazi kontraktè a.",
        ],
        "faq": [
            ("Ki diferans ant yon enspeksyon mwazi ak yon tès mwazi?", "Enspeksyon an jwenn imidite ak mwazi ki parèt. Tès la voye echantiyon lè oswa sifas nan yon laboratwa pou mezire sa ki la. Sèvis nou an gen tou de."),
            ("Kijan pou m prepare?", "Kenbe fenèt ak pòt fèmen 24 èdtan anvan, pa fè gwo netwayaj, etenn pirifikatè lè yo, epi kite aksè nan klozèt AC a ak galata a."),
            ("Èske nou retire mwazi?", "Non. Nou sèlman enspekte epi fè tès, kidonk rezilta nou yo pa janm vini ak yon travay netwayaj."),
        ],
        "note": "Nou fè enspeksyon ak tès mwazi anba lisans enspektè kay Florid nou an. Nou pa fè evalyasyon mwazi (mold assessment) ni retire mwazi (remediation).",
    },
    "pre-listing-inspection": {
        "nav": "Enspeksyon anvan vann",
        "title": "Enspeksyon anvan w vann kay ou nan Miami",
        "meta": "Enspeksyon pou moun k ap vann kay nan Sid Florid. Jwenn pwoblèm yo anvan achtè a epi fikse pri a avèk konfyans. Rapò menm jou a.",
        "kicker": "Pou moun k ap vann",
        "h1": "Konnen sa enspektè achtè a pral jwenn, anvan li jwenn li.",
        "lede": "Yon enspeksyon anvan w mete kay la an vant ba w tan pou repare, ajiste pri a, oswa di sa ki genyen jan w vle.",
        "covers": [
            ("Enspeksyon konplè", "Menm bagay ak enspeksyon pou achtè: tèt kay, estrikti, elektrisite, plonbri ak AC."),
            ("Imidite ak kamera tèmik", "Aparèy imidite ak kamera tèmik enkli."),
            ("Fòm asirans", "Yon mitigasyon van ak yon enspeksyon 4 pwen resan ede achtè yo jwenn pri asirans pi vit."),
        ],
        "body": [
            "Rezon ki pi komen ki fè yon vant tonbe oswa ki fè moun renegosye nan Florid se yon sipriz nan enspeksyon an. Lè w jwenn li anvan, se ou ki gen kontwòl la.",
            "Lè w gen yon mitigasyon van ak yon enspeksyon 4 pwen pare, achtè yo ka jwenn pri asirans rapid, e sa se yon gwo avantaj nan mache asirans Florid jodi a.",
        ],
        "faq": [
            ("Èske m oblije di sa nou jwenn?", "Règ sou sa w dwe di se yon kesyon pou ajan w oswa avoka w. Rapò nou an se yon dosye sou sa nou te wè."),
        ],
    },
    "new-construction-inspection": {
        "nav": "Konstriksyon nouvo ak garanti",
        "title": "Enspeksyon konstriksyon nouvo ak garanti 11 mwa nan Sid Florid",
        "meta": "Enspeksyon kay nouvo ak garanti 11 mwa nan Miami-Dade, Broward ak Palm Beach. Dokimante defo yo anvan garanti w la fini.",
        "kicker": "Kay nouvo",
        "h1": "Nouvo pa vle di pafè.",
        "lede": "Moun k ap bati yo travay vit. Yon enspeksyon endepandan anvan w siyen, ak yon lòt anvan garanti 11 mwa a fini, jwenn defo yo pandan konstriktè a toujou oblije repare yo.",
        "covers": [
            ("Anvan w fèmen vant lan", "Yon enspeksyon konplè anvan dènye vizit la pou lis reparasyon w lan konplè."),
            ("Garanti 11 mwa", "Nou dokimante defo ki parèt apre w fin rantre, anvan garanti konstriktè a fini."),
            ("Imidite ak kamera tèmik", "Kamera tèmik la itil anpil nan kay nouvo pou jwenn izolasyon ki manke ak fuit kache."),
        ],
        "body": [
            "Nou te enspekte kay nouvo nan tout Sid Florid. Sa nou jwenn pi souvan se ti bagay ki fè gwo pil: izolasyon ki manke, twou ki pa sele, pwoblèm drenaj, ak travay ki pa fini.",
            "Rezève enspeksyon 11 mwa a apeprè yon mwa anvan dat garanti w la pou w gen tan voye lis la bay konstriktè a.",
        ],
        "faq": [],
    },
}

T_HT = {
    "home": "Akèy", "menu": "Meni", "call": "Rele", "call_or_text": "Rele oswa voye tèks",
    "nav_services": "Sèvis", "nav_pricing": "Pri", "nav_mold": "Tès mwazi", "nav_areas": "Zòn", "nav_book": "Rezève",
    "lang_note": "Rapò yo ekri an anglè. Voye yon tèks ban nou an kreyòl, epi n ap reponn ou avèk èd tradiksyon.",
    "hero_kicker": f"Enspektè kay ki gen lisans Florid · {LICENSE}",
    "hero_h1": "Enspeksyon kay sètifye.<br><em>Rapò menm jou a.</em>",
    "hero_lede": "Enspeksyon kay, mitigasyon van, 4 pwen ak tès mwazi nan Miami-Dade, Broward ak Palm Beach, ak pri klè depi okòmansman.",
    "btn_schedule": "Rezève yon enspeksyon", "btn_prices": "Gade pri yo",
    "stats": [("5.0 ★", f"{TOTAL_REVIEWS} revi · Google + Thumbtack"), ("Menm jou", "Rapò ak foto"),
              ("Tèmik + imidite", "Nan chak enspeksyon"), ("InterNACHI", "Enspektè sètifye")],
    "services_kicker": "Sèvis", "services_h2": "Tout sa yon kay nan Sid Florid bezwen enspekte",
    "pricing_kicker": "Pri", "pricing_h2": "Pri klè. Pa gen sipriz.",
    "card_home": "Enspeksyon kay", "card_home_sub": "Pri a depann de gwosè kay la (pye kare)",
    "card_ins": "Enspeksyon pou asirans", "card_ins_sub": "Fòm Florid konpayi asirans ou aksepte",
    "ins_blurb": "Mitigasyon van ka fè prim asirans ou bese. Enspeksyon 4 pwen an kouvri tèt kay, elektrisite, plonbri ak AC pou kay ki gen laj.",
    "card_mold": "Enspeksyon ak tès mwazi", "card_mold_sub": "Analiz laboratwa enkli", "whats_included": "Sa ki enkli →",
    "pay_title": "Peman fasil", "pay_text": "Peye jou enspeksyon an. Nou voye rapò a lè nou resevwa peman an.",
    "pay_over": "Divize peman enspeksyon an an plizyè ti peman san enterè ak Afterpay oswa Affirm, si yo apwouve w.",
    "price_note": "Chak enspeksyon gen aparèy imidite, kamera tèmik, foto ak yon rapò dijital konplè. Ka gen yon frè vwayaj andeyò Miami-Dade ak Broward.",
    "tiers": [("Kondo / mwens pase 1,200 pye kare", "$325"), ("1,200–1,999 pye kare", "$395"), ("2,000–2,999 pye kare", "$475"),
              ("3,000–3,999 pye kare", "$550"), ("4,000+ pye kare", "apati $625")],
    "insurance": [("Mitigasyon van (OIR-B1-1802)", "$150"), ("Enspeksyon 4 pwen", "$150")],
    "env": [("Enspeksyon ak tès mwazi", "jiska 3 echantiyon laboratwa, ak yon echantiyon deyò", "$375"), ("Lòt echantiyon mwazi", "", "$75 chak")],
    "payment": ["Kat kredi", "Apple Pay", "Zelle", "Venmo", "PayPal", "Lajan kach oswa chèk"],
    "from": "Apati {p}",
    "mold_kicker": "Enspeksyon ak tès mwazi", "callout_h": "Nou fè tès. Nou pa vann netwayaj.",
    "callout_p": "Nou pa retire mwazi, kidonk rezilta nou yo pa janm vini ak yon travay netwayaj.", "callout_btn": "Detay tès mwazi",
    "reviews_kicker": "Revi", "reviews_h2": "{n} revi senk zetwal",
    "google_sub": "{n} revi · tout senk zetwal · li yo sou Google", "tt_sub": "{n} revi · Top Pro · li yo sou Thumbtack",
    "leave_review": "Kite yon revi pou nou sou Google",
    "steps_kicker": "Kijan sa mache", "steps_h2": "Rezève nan kèk minit. Rapò menm jou a.",
    "steps": [("ETAP 1", "Konnen pri a", "Pri yo afiche selon gwosè kay la, kidonk ou konnen konbyen sa koute anvan w rele."),
              ("ETAP 2", "Rezève epi siyen", "Chwazi yon lè epi siyen akò enspeksyon an. Randevou w la konfime."),
              ("ETAP 3", "Jou enspeksyon an", "Ou ka vin avè nou. N ap montre w sa nou jwenn."),
              ("ETAP 4", "Rapò menm jou a", "Foto, rezilta ak eksplikasyon klè, menm jou a.")],
    "areas_kicker": "Zòn", "areas_h2": "Miami-Dade, Broward ak Palm Beach",
    "faq_kicker": "Kesyon", "faq_h2": "Kesyon moun poze souvan",
    "cta_h": "Ou pare pou rezève?", "cta_p": "Rele, voye tèks oswa rezève sou entènèt. N ap konfime nan mwens pase 2 èdtan.",
    "cta_btn": "Rezève yon enspeksyon", "cta_call": "Rele {phone}",
    "what_we_check": "Sa nou tcheke", "questions": "Kesyon", "other_services": "Lòt sèvis", "areas_we_serve": "Zòn nou sèvi",
    "book_from": "Rezève · apati {p}", "full_price_list": "Lis pri yo",
    "svc_index_title": "Sèvis enspeksyon kay nan Miami ak Sid Florid",
    "svc_index_meta": "Enspeksyon kay, mitigasyon van, 4 pwen, enspeksyon ak tès mwazi, enspeksyon anvan vann ak konstriksyon nouvo nan Sid Florid.",
    "svc_index_h1": "Sèvis enspeksyon",
    "svc_index_lede": "Enspeksyon kay, enspeksyon pou asirans ak tès mwazi nan Miami-Dade, Broward ak Palm Beach.",
    "pricing_title": "Pri enspeksyon kay nan Miami, Broward ak Palm Beach",
    "pricing_meta": "Pri enspeksyon kay selon pye kare apati $325. Mitigasyon van ak 4 pwen $150 chak. Enspeksyon ak tès mwazi $375 ak laboratwa.",
    "pricing_h1": "Pri enspeksyon yo", "pricing_lede": "Pri klè anvan w rezève. Pa gen frè kache.", "pricing_faq_h2": "Kesyon sou pri",
    "contact_title": "Rezève yon enspeksyon kay",
    "contact_meta": "Rezève yon enspeksyon kay, mitigasyon van, 4 pwen oswa tès mwazi nan Sid Florid. N ap konfime nan mwens pase 2 èdtan.",
    "contact_h1": "Rezève yon enspeksyon", "contact_lede": "Voye enfòmasyon w epi n ap konfime nan mwens pase 2 èdtan.",
    "f_first": "Non", "f_last": "Siyati", "f_phone": "Telefòn", "f_email": "Imèl", "f_address": "Adrès kay la",
    "f_service": "Sèvis", "f_sqft": "Pye kare", "f_date": "Dat ou prefere", "f_source": "Kijan ou jwenn nou?",
    "sources": ["Google", "Thumbtack", "Ajan imobilye", "Ajan asirans", "Zanmi oswa fanmi", "Lòt"],
    "f_notes": "Èske gen yon bagay nou ta dwe konnen?", "f_submit": "Mande enspeksyon mwen →", "f_multiple": "Plizyè sèvis",
    "f_note": "Ou siyen akò enspeksyon an anvan vizit la; lè w siyen, dat ak lè w la konfime.",
    "f_subject": "Nouvo demann (Kreyòl) – inspectandprotect.net", "lang_value": "Kreyòl",
    "areas_title": "Zòn nou sèvi: Miami-Dade, Broward ak Palm Beach",
    "areas_meta": "Inspect and Protect sèvi Miami, North Miami, Miami Gardens, Fort Lauderdale, Lauderhill, Pompano Beach, Delray Beach, West Palm Beach ak plis ankò.",
    "areas_h1": "Zòn nou sèvi", "areas_lede": "Enspeksyon kay, mitigasyon van, 4 pwen ak tès mwazi nan vil sa yo.",
    "county": "Konte {c}", "all_cities_en": "Gade tout vil yo (an anglè)", "all_areas": "Tout zòn yo",
    "areas_other": "Ou nan yon lòt zòn? Rele {phone}. Nou pran travay nan lòt kote nan Florid ak yon frè vwayaj.",
    "city_title": "Enspektè kay nan {name}, FL – Mitigasyon van ak 4 pwen",
    "city_meta": "Enspektè kay ki gen lisans nan {name}, FL. Enspeksyon kay apati $325, mitigasyon van ak 4 pwen $150, tès mwazi $375. Rapò menm jou a.",
    "city_h1": "Enspektè kay nan {name}, FL",
    "city_lede": "Enspeksyon kay, mitigasyon van, 4 pwen ak tès mwazi nan {name}, ak rapò menm jou a.",
    "city_book": "Rezève nan {name}", "city_h2": "Enspeksyon kay nan {name}",
    "city_std": f"Chak enspeksyon gen mezi imidite ak imaj tèmik, epi rapò w la ak foto rive menm jou a. Nou gen lisans enspektè kay Florid #{LICENSE} epi nou sètifye pa InterNACHI.",
    "city_services": "Sèvis nan {name}", "city_svc_card": "{svc} nan {name}", "prices": "Pri",
    "city_faq_h2": "Kesyon sou {name}", "nearby": "Zòn ki toupre", "city_cta": "Ou bezwen yon enspektè nan {name}?",
    "city_faq": [("Konbyen yon enspeksyon kay koute nan {name}?", "Enspeksyon kay nan {name} kòmanse a $325 epi pri a depann de gwosè kay la. Mitigasyon van ak enspeksyon 4 pwen koute $150 chak."),
                 ("Konbyen tan pou nou vin enspekte nan {name}?", "Nou fè enspeksyon nan {name} 7 jou sou 7, souvan nan yon jou oswa de. Nou voye rapò a menm jou a."),
                 ("Èske gen frè vwayaj pou {name}?", "{travel}")],
    "travel_free": "Pa gen frè vwayaj nan Miami-Dade ak Broward.",
    "travel_pb": "Ka gen yon frè vwayaj nan Konte Palm Beach; n ap di w anvan w rezève.",
    "footer_about": "Enspeksyon kay ak lisans, enspeksyon pou asirans ak tès mwazi nan Miami-Dade, Broward ak Palm Beach.",
    "company": "Konpayi", "reviews_link": "Revi",
    "legal": f"Enspektè kay ki gen lisans Florid #{LICENSE} · Sètifye pa InterNACHI · Asire. Nou fè enspeksyon ak tès mwazi anba lisans enspektè kay Florid nou an; nou pa fè evalyasyon mwazi ni retire mwazi.",
    "home_title": "Enspektè kay nan Miami ak Sid Florid | Inspect and Protect",
    "home_meta": "Enspektè kay ki gen lisans Florid (HI18768) nan Miami-Dade, Broward ak Palm Beach. Enspeksyon kay apati $325, mitigasyon van ak 4 pwen $150, tès mwazi $375. Rapò menm jou a.",
    "home_faq": [
        ("Konbyen yon enspeksyon kay koute?", "Enspeksyon kay kòmanse a $325 pou kondo ak kay ki gen mwens pase 1,200 pye kare, epi pri a monte selon gwosè kay la. Mitigasyon van ak enspeksyon 4 pwen koute $150 chak."),
        ("Konbyen tan yon enspeksyon pran?", "Pifò pran 2 a 4 èdtan selon gwosè ak kondisyon kay la. Ou ka vin avè nou."),
        ("Kilè m ap resevwa rapò a?", "Nou voye rapò ak foto yo menm jou a. Rapò yo ekri an anglè."),
        ("Nan ki lang nou pale?", "Nou pale anglè. Ou ka voye tèks ban nou an kreyòl, epi n ap reponn ou avèk èd tradiksyon."),
        ("Èske nou gen lisans ak asirans?", f"Wi. Nou se enspektè kay ki gen lisans Florid (#{LICENSE}), sètifye pa InterNACHI, ak asirans erè ak omisyon ak asirans responsablite sivil."),
    ],
    "pricing_faq": [
        ("Poukisa pri a depann de pye kare?", "Kay ki pi gwo pran plis tan epi yo gen plis sistèm pou tcheke, kidonk pri a monte ak gwosè a."),
        ("Èske gen frè vwayaj?", "Non nan Miami-Dade ak Broward. Ka gen yon frè pi lwen; n ap di w anvan w rezève."),
        ("Kilè pou m peye?", "Ou peye jou enspeksyon an. Nou voye rapò a lè nou resevwa peman an."),
    ],
}

T = {"es": T_ES, "ht": T_HT}
SVC = {"es": SVC_ES, "ht": SVC_HT}
CITY_TEXT = {"es": CITY_TEXT_ES, "ht": CITY_TEXT_HT}

# =================================================================== templates
def excerpt(s, n=140):
    s = B.strip_tags(s)
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + "…"

def _hdr(l):
    t, base = T[l], BASE[l]
    items = [(base["services"], t["nav_services"]), (base["pricing"], t["nav_pricing"]),
             (svc_path(l, "mold-inspection-testing"), t["nav_mold"]), (base["areas"], t["nav_areas"])]
    links = "".join(f'<li><a href="{a}">{b}</a></li>' for a, b in items)
    def h(path):
        return f'''<header class="site-header">{B.topbar(path, l, t["call_or_text"])}<div class="wrap">
<a class="logo" href="{base["root"]}">Inspect <span>&amp;</span> Protect</a>
<ul class="nav">{links}<li><a class="btn btn-gold" href="{base["contact"]}">{t["nav_book"]}</a></li></ul>
<details class="menu"><summary aria-label="{t["menu"]}">{t["menu"]}</summary><ul>{links}<li><a href="{base["contact"]}">{t["nav_book"]}</a></li><li><a href="tel:{PHONE_TEL}">{t["call"]} {PHONE}</a></li></ul></details>
</div></header>'''
    return h

def _ftr(l):
    t, base = T[l], BASE[l]
    def f():
        svc = "".join(f'<li><a href="{svc_path(l, s)}">{SVC[l][s]["nav"]}</a></li>' for s in SVC_ORDER)
        cities = "".join(f'<li><a href="{city_path(l, c)}">{CITY_NAME[c]}</a></li>' for c in CITIES[l][:8])
        return f'''<footer class="site-footer"><div class="wrap"><div class="footer-grid">
<div><a class="logo" href="{base["root"]}">Inspect <span>&amp;</span> Protect</a><p>{t["footer_about"]}</p>
<p><a href="tel:{PHONE_TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p><p>{t["lang_note"]}</p></div>
<div><h4>{t["nav_services"]}</h4><ul>{svc}<li><a href="{base["pricing"]}">{t["nav_pricing"]}</a></li></ul></div>
<div><h4>{t["nav_areas"]}</h4><ul>{cities}<li><a href="{base["areas"]}">{t["all_areas"]}</a></li></ul></div>
<div><h4>{t["company"]}</h4><ul><li><a href="/reviews/">{t["reviews_link"]}</a></li><li><a href="{base["contact"]}">{t["nav_book"]}</a></li><li><a href="/" hreflang="en" lang="en">English</a></li></ul></div>
</div><div class="legal">{t["legal"]} © {datetime.date.today().year} Inspect and Protect.</div></div></footer>'''
    return f

def _page(l, path, title, meta, body, lds=None):
    B.page(path, title, meta, body, lds, lang=l, hdr=_hdr(l), ftr=_ftr(l))

def _crumbs(l, items):
    return B.crumbs(items, home=T[l]["home"], home_href=BASE[l]["root"])

def _bc_ld(l, items):
    return B.breadcrumb_ld(items, home=T[l]["home"], home_href=BASE[l]["root"])

def _cta(l, text=None):
    t = T[l]
    return B.cta_band(text or t["cta_h"], t["cta_p"], btn=t["cta_btn"], call=t["cta_call"].format(phone=PHONE), href=BASE[l]["contact"])

def pricing_block(l):
    t = T[l]
    pay = "".join(f'<span class="chip">{m}</span>' for m in t["payment"])
    ptext = t["pay_text"]
    if PAY_OVER_TIME:
        pay = '<span class="chip chip-solid">Afterpay</span><span class="chip chip-solid">Affirm</span>' + pay
        ptext = t["pay_over"]
    return f'''<div class="grid grid-wide">
<div class="card price-card"><h3>{t["card_home"]}</h3><p class="sub">{t["card_home_sub"]}</p>{B.rows(t["tiers"])}</div>
<div class="card price-card"><h3>{t["card_ins"]}</h3><p class="sub">{t["card_ins_sub"]}</p>{B.rows(t["insurance"])}<p>{t["ins_blurb"]}</p></div>
<div class="card price-card feature"><h3>{t["card_mold"]}</h3><p class="sub">{t["card_mold_sub"]}</p>{B.rows(t["env"])}<p><a href="{svc_path(l, "mold-inspection-testing")}">{t["whats_included"]}</a></p></div>
</div>
<div class="paybar"><div style="flex:1 1 320px"><h3>{t["pay_title"]}</h3><p style="margin:4px 0 0;color:#c9d2dc">{ptext}</p></div><div class="chips">{pay}</div></div>
<p class="note" style="margin-top:12px">{t["price_note"]}</p>'''

def reviews_block(l):
    t = T[l]
    return f'''<div class="grid grid-wide">
<a class="rating" href="{GOOGLE_PROFILE}"><strong>{GOOGLE_RATING}</strong><span><b>Google</b><small>{t["google_sub"].format(n=GOOGLE_COUNT)}</small></span></a>
<a class="rating" href="{THUMBTACK_PROFILE}"><strong>{THUMBTACK_RATING}</strong><span><b>Thumbtack</b><small>{t["tt_sub"].format(n=THUMBTACK_COUNT)}</small></span></a>
</div>
<div class="btn-row"><a class="btn btn-dark" href="{GOOGLE_REVIEW_LINK}">{t["leave_review"]}</a></div>'''

def svc_cards(l, exclude=None):
    t = T[l]
    return '<div class="grid">' + "".join(
        f'<a class="card" href="{svc_path(l, s)}"><h3>{SVC[l][s]["nav"]}</h3><p>{excerpt(SVC[l][s]["lede"])}</p><div class="more">{t["from"].format(p=EN_PRICE[s])} →</div></a>'
        for s in SVC_ORDER if s != exclude) + "</div>"

def city_pills(l, only=None):
    cs = only if only is not None else CITIES[l]
    return '<div class="pills">' + "".join(f'<a class="pill" href="{city_path(l, c)}">{CITY_NAME[c]}</a>' for c in cs) + "</div>"

# =================================================================== pages
def build_home(l):
    t = T[l]
    mold = SVC[l]["mold-inspection-testing"]
    covers = "".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a, b in mold["covers"])
    stats = "".join(f"<div><strong>{a}</strong><span>{b}</span></div>" for a, b in t["stats"])
    steps = "".join(f"<li><b>{a}</b><strong>{b}</strong><p>{c}</p></li>" for a, b, c in t["steps"])
    body = f'''
<section class="hero on-dark"><div class="wrap">
<p class="kicker">{t["hero_kicker"]}</p>
<h1>{t["hero_h1"]}</h1>
<p class="lede">{t["hero_lede"]}</p>
<p class="lang-note">{t["lang_note"]}</p>
<div class="btn-row"><a class="btn btn-gold" href="{BASE[l]["contact"]}">{t["btn_schedule"]}</a><a class="btn btn-line" href="{BASE[l]["pricing"]}">{t["btn_prices"]}</a></div>
<div class="stats">{stats}</div></div></section>

<section class="bg-white"><div class="wrap">
<p class="kicker">{t["services_kicker"]}</p><h2>{t["services_h2"]}</h2>
<div style="margin-top:32px">{svc_cards(l)}</div></div></section>

<section><div class="wrap">
<p class="kicker">{t["pricing_kicker"]}</p><h2>{t["pricing_h2"]}</h2>
<div style="margin-top:32px">{pricing_block(l)}</div></div></section>

<section class="bg-white"><div class="wrap">
<p class="kicker">{t["mold_kicker"]}</p><h2>{mold["h1"]}</h2>
<p class="lede">{mold["lede"]}</p>
<div class="grid" style="margin-top:32px">{covers}</div>
<div class="callout" style="margin-top:28px"><div style="flex:1 1 360px"><h3>{t["callout_h"]}</h3><p style="margin:6px 0 0;color:var(--muted)">{t["callout_p"]}</p></div><a class="btn btn-dark" href="{svc_path(l, "mold-inspection-testing")}">{t["callout_btn"]}</a></div>
</div></section>

<section><div class="wrap">
<p class="kicker">{t["reviews_kicker"]}</p><h2>{t["reviews_h2"].format(n=TOTAL_REVIEWS)}</h2>
<div style="margin-top:28px">{reviews_block(l)}</div></div></section>

<section class="bg-white"><div class="wrap">
<p class="kicker">{t["steps_kicker"]}</p><h2>{t["steps_h2"]}</h2>
<ol class="steps" style="margin-top:28px">{steps}</ol></div></section>

<section><div class="wrap">
<p class="kicker">{t["areas_kicker"]}</p><h2>{t["areas_h2"]}</h2>
<div style="margin-top:24px">{city_pills(l)}</div></div></section>

<section class="bg-white"><div class="wrap narrow">
<p class="kicker">{t["faq_kicker"]}</p><h2>{t["faq_h2"]}</h2>
<div style="margin-top:20px">{B.faq_html(t["home_faq"])}</div></div></section>
{_cta(l)}'''
    _page(l, BASE[l]["root"], t["home_title"], t["home_meta"], body, [B.faq_ld(t["home_faq"])])

def build_services(l):
    t = T[l]
    body = f'''<section class="page-hero on-dark"><div class="wrap">{_crumbs(l, [(None, t["nav_services"])])}
<h1>{t["svc_index_h1"]}</h1><p class="lede">{t["svc_index_lede"]}</p></div></section>
<section class="bg-white"><div class="wrap">{svc_cards(l)}</div></section>{_cta(l)}'''
    _page(l, BASE[l]["services"], t["svc_index_title"], t["svc_index_meta"], body,
          [_bc_ld(l, [(BASE[l]["services"], t["nav_services"])])])
    for slug in SVC_ORDER:
        s = SVC[l][slug]
        price = EN_PRICE[slug]
        covers = "".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a, b in s["covers"])
        paras = "".join(f"<p>{p}</p>" for p in s["body"])
        note = f'<p class="note">{s["note"]}</p>' if s.get("note") else ""
        faq = (f'<section><div class="wrap narrow"><h2>{t["questions"]}</h2><div style="margin-top:16px">{B.faq_html(s["faq"])}</div></div></section>'
               if s["faq"] else "")
        body = f'''<section class="page-hero on-dark"><div class="wrap">{_crumbs(l, [(BASE[l]["services"], t["nav_services"]), (None, s["nav"])])}
<p class="kicker">{s["kicker"]}</p><h1>{s["h1"]}</h1><p class="lede">{s["lede"]}</p>
<div class="btn-row"><a class="btn btn-gold" href="{BASE[l]["contact"]}">{t["book_from"].format(p=price)}</a><a class="btn btn-line" href="{BASE[l]["pricing"]}">{t["full_price_list"]}</a></div></div></section>
<section class="bg-white"><div class="wrap"><h2>{t["what_we_check"]}</h2><div class="grid" style="margin-top:28px">{covers}</div></div></section>
<section><div class="wrap narrow prose">{paras}{note}<p class="note">{t["lang_note"]}</p></div></section>
{faq}
<section class="bg-white"><div class="wrap"><h2>{t["areas_we_serve"]}</h2><div style="margin-top:20px">{city_pills(l)}</div>
<h2 style="margin-top:48px">{t["other_services"]}</h2><div style="margin-top:24px">{svc_cards(l, exclude=slug)}</div></div></section>
{_cta(l)}'''
        svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": B.strip_tags(s["nav"]), "inLanguage": l,
                  "provider": {"@id": DOMAIN + "/#business"},
                  "areaServed": ["Miami-Dade County, FL", "Broward County, FL", "Palm Beach County, FL"],
                  "offers": {"@type": "Offer", "price": price.replace("$", ""), "priceCurrency": "USD"}}
        lds = [svc_ld, _bc_ld(l, [(BASE[l]["services"], t["nav_services"]), (None, s["nav"])])]
        if s["faq"]:
            lds.append(B.faq_ld(s["faq"]))
        _page(l, svc_path(l, slug), s["title"], s["meta"], body, lds)

def build_pricing(l):
    t = T[l]
    body = f'''<section class="page-hero on-dark"><div class="wrap">{_crumbs(l, [(None, t["nav_pricing"])])}
<h1>{t["pricing_h1"]}</h1><p class="lede">{t["pricing_lede"]}</p></div></section>
<section class="bg-white"><div class="wrap">{pricing_block(l)}</div></section>
<section><div class="wrap narrow"><h2>{t["pricing_faq_h2"]}</h2><div style="margin-top:16px">{B.faq_html(t["pricing_faq"])}</div></div></section>{_cta(l)}'''
    _page(l, BASE[l]["pricing"], t["pricing_title"], t["pricing_meta"], body,
          [B.faq_ld(t["pricing_faq"]), _bc_ld(l, [(None, t["nav_pricing"])])])

def build_contact(l):
    t = T[l]
    opts = "".join(f"<option>{B.strip_tags(SVC[l][s]['nav'])}</option>" for s in SVC_ORDER) + f"<option>{t['f_multiple']}</option>"
    src = "".join(f"<option>{o}</option>" for o in t["sources"])
    body = f'''<section class="page-hero on-dark"><div class="wrap">{_crumbs(l, [(None, t["nav_book"])])}
<h1>{t["contact_h1"]}</h1><p class="lede">{t["contact_lede"]}</p><p class="lang-note">{t["lang_note"]}</p></div></section>
<section class="bg-white"><div class="wrap narrow">
<form class="book" action="{FORMSPREE}" method="POST">
<input type="hidden" name="_subject" value="{t["f_subject"]}">
<input type="hidden" name="language" value="{t["lang_value"]}">
<label>{t["f_first"]}<input name="first_name" required autocomplete="given-name"></label>
<label>{t["f_last"]}<input name="last_name" required autocomplete="family-name"></label>
<label>{t["f_phone"]}<input name="phone" type="tel" required autocomplete="tel"></label>
<label>{t["f_email"]}<input name="email" type="email" required autocomplete="email"></label>
<label class="full">{t["f_address"]}<input name="property_address" required autocomplete="street-address"></label>
<label>{t["f_service"]}<select name="service">{opts}</select></label>
<label>{t["f_sqft"]}<input name="square_footage" inputmode="numeric"></label>
<label>{t["f_date"]}<input name="preferred_date" type="date"></label>
<label>{t["f_source"]}<select name="source">{src}</select></label>
<label class="full">{t["f_notes"]}<textarea name="notes"></textarea></label>
<div class="full"><button class="btn btn-gold" type="submit">{t["f_submit"]}</button>
<p class="note">{t["f_note"]}</p></div>
</form></div></section>'''
    _page(l, BASE[l]["contact"], t["contact_title"], t["contact_meta"], body)

def build_areas(l):
    t = T[l]
    body = f'''<section class="page-hero on-dark"><div class="wrap">{_crumbs(l, [(None, t["nav_areas"])])}
<h1>{t["areas_h1"]}</h1><p class="lede">{t["areas_lede"]}</p></div></section>
<section class="bg-white"><div class="wrap">'''
    for county in ("Miami-Dade", "Broward", "Palm Beach"):
        cs = [c for c in CITIES[l] if CITY_COUNTY[c] == county]
        if cs:
            body += f'<h2 style="margin:24px 0 16px">{t["county"].format(c=county)}</h2>{city_pills(l, cs)}'
    body += f'''<p style="margin-top:32px"><a href="/areas/" hreflang="en">{t["all_cities_en"]}</a></p>
<p class="note">{t["areas_other"].format(phone=PHONE)}</p></div></section>{_cta(l)}'''
    _page(l, BASE[l]["areas"], t["areas_title"], t["areas_meta"], body, [_bc_ld(l, [(None, t["nav_areas"])])])

    for c in CITIES[l]:
        name, county = CITY_NAME[c], CITY_COUNTY[c]
        intro, note = CITY_TEXT[l][c]
        travel = t["travel_pb"] if county == "Palm Beach" else t["travel_free"]
        faq = [(q.format(name=name), a.format(name=name, travel=travel)) for q, a in t["city_faq"]]
        svc = "".join(
            f'<a class="card" href="{svc_path(l, s)}"><h3>{t["city_svc_card"].format(svc=SVC[l][s]["nav"], name=name)}</h3><p>{t["from"].format(p=EN_PRICE[s])}</p></a>'
            for s in SVC_ORDER[:4])
        near = [x for x in CITIES[l] if x != c and CITY_COUNTY[x] == county][:6] or [x for x in CITIES[l] if x != c][:6]
        body = f'''<section class="page-hero on-dark"><div class="wrap">{_crumbs(l, [(BASE[l]["areas"], t["nav_areas"]), (None, name)])}
<p class="kicker">{t["county"].format(c=county)}</p><h1>{t["city_h1"].format(name=name)}</h1>
<p class="lede">{t["city_lede"].format(name=name)}</p>
<div class="btn-row"><a class="btn btn-gold" href="{BASE[l]["contact"]}">{t["city_book"].format(name=name)}</a><a class="btn btn-line" href="tel:{PHONE_TEL}">{t["cta_call"].format(phone=PHONE)}</a></div></div></section>
<section class="bg-white"><div class="wrap narrow prose">
<h2>{t["city_h2"].format(name=name)}</h2><p>{intro}</p><p>{note}</p><p>{t["city_std"]}</p><p class="note">{t["lang_note"]}</p>
</div></section>
<section><div class="wrap"><h2>{t["city_services"].format(name=name)}</h2><div class="grid" style="margin-top:24px">{svc}</div>
<h2 style="margin-top:48px">{t["prices"]}</h2><div style="margin-top:24px">{pricing_block(l)}</div></div></section>
<section class="bg-white"><div class="wrap narrow"><h2>{t["city_faq_h2"].format(name=name)}</h2><div style="margin-top:16px">{B.faq_html(faq)}</div>
<h3 style="margin-top:40px">{t["nearby"]}</h3><div style="margin-top:14px">{city_pills(l, near)}</div></div></section>
{_cta(l, t["city_cta"].format(name=name))}'''
        _page(l, city_path(l, c), t["city_title"].format(name=name), t["city_meta"].format(name=name), body,
              [B.faq_ld(faq), _bc_ld(l, [(BASE[l]["areas"], t["nav_areas"]), (None, name)])])

def build_all(build_module):
    global B
    B = build_module
    for l in ("es", "ht"):
        build_home(l); build_services(l); build_pricing(l); build_contact(l); build_areas(l)
