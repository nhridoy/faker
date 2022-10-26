from collections import OrderedDict
from typing import Dict, Tuple

from ... import ElementsType
from ..es import Provider as AddressProvider


class Provider(AddressProvider):
    # Source for regions, provinces and communes
    # https://www.subdere.gov.cl/documentacion/c%C3%B3digos-%C3%BAnicos-
    # territoriales-actualizados-al-06-de-septiembre-2018
    regions: Dict[str, str] = {
        "TA": "Región de Tarapacá",
        "AN": "Región de Antofagasta",
        "AT": "Región de Atacama",
        "CO": "Región de Coquimbo",
        "VA": "Región de Valparaíso",
        "LI": "Región del Libertador General Bernardo O'Higgins",
        "ML": "Región del Maule",
        "BI": "Región del Biobío",
        "AR": "Región de La Araucanía",
        "LL": "Región de Los Lagos",
        "AI": "Región de Aysén del General Carlos Ibáñez del Campo",
        "MA": "Región de Magallanes y de la Antártica Chilena",
        "RM": "Región Metropolitana",
        "LR": "Región de Los Ríos",
        "AP": "Región de Arica y Parinacota",
        "NB": "Región de Ñuble",
    }

    provinces: Dict[str, str] = {
        "011": "Iquique",
        "014": "Tamarugal",
        "021": "Antofagasta",
        "022": "El Loa",
        "023": "Tocopilla",
        "031": "Copiapó",
        "032": "Chañaral",
        "033": "Huasco",
        "041": "Elqui",
        "042": "Choapa",
        "043": "Limarí",
        "051": "Valparaíso",
        "052": "Isla de Pascua",
        "053": "Los Andes",
        "054": "Petorca",
        "055": "Quillota",
        "056": "San Antonio",
        "057": "San Felipe de Aconcagua",
        "058": "Marga Marga",
        "061": "Cachapoal",
        "062": "Cardenal Caro",
        "063": "Colchagua",
        "071": "Talca",
        "072": "Cauquenes",
        "073": "Curicó",
        "074": "Linares",
        "081": "Concepción",
        "082": "Arauco",
        "083": "Biobío",
        "091": "Cautín",
        "092": "Malleco",
        "101": "Llanquihue",
        "102": "Chiloé",
        "103": "Osorno",
        "104": "Palena",
        "111": "Coyhaique",
        "112": "Aysén",
        "113": "Capitán Prat",
        "114": "General Carrera",
        "121": "Magallanes",
        "122": "Antártica Chilena",
        "123": "Tierra del Fuego",
        "124": "Última Esperanza",
        "131": "Santiago",
        "132": "Cordillera",
        "133": "Chacabuco",
        "134": "Maipo",
        "135": "Melipilla",
        "136": "Talagante",
        "141": "Valdivia",
        "142": "Ranco",
        "151": "Arica",
        "152": "Parinacota",
        "161": "Diguillín",
        "162": "Itata",
        "163": "Punilla",
    }

    communes: Dict[str, str] = {
        "15101": "Arica",
        "15102": "Camarones",
        "15201": "Putre",
        "15202": "General Lagos",
        "01101": "Iquique",
        "01402": "Camiña",
        "01403": "Colchane",
        "01404": "Huara",
        "01405": "Pica",
        "01401": "Pozo Almonte",
        "01107": "Alto Hospicio",
        "02101": "Antofagasta",
        "02102": "Mejillones",
        "02103": "Sierra Gorda",
        "02104": "Taltal",
        "02201": "Calama",
        "02202": "Ollagüe",
        "02203": "San Pedro de Atacama",
        "02301": "Tocopilla",
        "02302": "María Elena",
        "03101": "Copiapó",
        "03102": "Caldera",
        "03103": "Tierra Amarilla",
        "03201": "Chañaral",
        "03202": "Diego de Almagro",
        "03301": "Vallenar",
        "03302": "Alto del Carmen",
        "03303": "Freirina",
        "03304": "Huasco",
        "04101": "La Serena",
        "04102": "Coquimbo",
        "04103": "Andacollo",
        "04104": "La Higuera",
        "04105": "Paiguano",
        "04106": "Vicuña",
        "04201": "Illapel",
        "04202": "Canela",
        "04203": "Los Vilos",
        "04204": "Salamanca",
        "04301": "Ovalle",
        "04302": "Combarbalá",
        "04303": "Monte Patria",
        "04304": "Punitaqui",
        "04305": "Río Hurtado",
        "05101": "Valparaíso",
        "05102": "Casablanca",
        "05103": "Concón",
        "05104": "Juan Fernández",
        "05105": "Puchuncaví",
        "05801": "Quilpué",
        "05107": "Quintero",
        "05804": "Villa Alemana",
        "05109": "Viña del Mar",
        "05201": "Isla  de Pascua",
        "05301": "Los Andes",
        "05302": "Calle Larga",
        "05303": "Rinconada",
        "05304": "San Esteban",
        "05401": "La Ligua",
        "05402": "Cabildo",
        "05403": "Papudo",
        "05404": "Petorca",
        "05405": "Zapallar",
        "05501": "Quillota",
        "05502": "Calera",
        "05503": "Hijuelas",
        "05504": "La Cruz",
        "05802": "Limache",
        "05506": "Nogales",
        "05803": "Olmué",
        "05601": "San Antonio",
        "05602": "Algarrobo",
        "05603": "Cartagena",
        "05604": "El Quisco",
        "05605": "El Tabo",
        "05606": "Santo Domingo",
        "05701": "San Felipe",
        "05702": "Catemu",
        "05703": "Llaillay",
        "05704": "Panquehue",
        "05705": "Putaendo",
        "05706": "Santa María",
        "06101": "Rancagua",
        "06102": "Codegua",
        "06103": "Coinco",
        "06104": "Coltauco",
        "06105": "Doñihue",
        "06106": "Graneros",
        "06107": "Las Cabras",
        "06108": "Machalí",
        "06109": "Malloa",
        "06110": "Mostazal",
        "06111": "Olivar",
        "06112": "Peumo",
        "06113": "Pichidegua",
        "06114": "Quinta de Tilcoco",
        "06115": "Rengo",
        "06116": "Requínoa",
        "06117": "San Vicente",
        "06201": "Pichilemu",
        "06202": "La Estrella",
        "06203": "Litueche",
        "06204": "Marchihue",
        "06205": "Navidad",
        "06206": "Paredones",
        "06301": "San Fernando",
        "06302": "Chépica",
        "06303": "Chimbarongo",
        "06304": "Lolol",
        "06305": "Nancagua",
        "06306": "Palmilla",
        "06307": "Peralillo",
        "06308": "Placilla",
        "06309": "Pumanque",
        "06310": "Santa Cruz",
        "07101": "Talca",
        "07102": "Constitución",
        "07103": "Curepto",
        "07104": "Empedrado",
        "07105": "Maule",
        "07106": "Pelarco",
        "07107": "Pencahue",
        "07108": "Río Claro",
        "07109": "San Clemente",
        "07110": "San Rafael",
        "07201": "Cauquenes",
        "07202": "Chanco",
        "07203": "Pelluhue",
        "07301": "Curicó",
        "07302": "Hualañé",
        "07303": "Licantén",
        "07304": "Molina",
        "07305": "Rauco",
        "07306": "Romeral",
        "07307": "Sagrada Familia",
        "07308": "Teno",
        "07309": "Vichuquén",
        "07401": "Linares",
        "07402": "Colbún",
        "07403": "Longaví",
        "07404": "Parral",
        "07405": "Retiro",
        "07406": "San Javier",
        "07407": "Villa Alegre",
        "07408": "Yerbas Buenas",
        "08101": "Concepción",
        "08102": "Coronel",
        "08103": "Chiguayante",
        "08104": "Florida",
        "08105": "Hualqui",
        "08106": "Lota",
        "08107": "Penco",
        "08108": "San Pedro de la Paz",
        "08109": "Santa Juana",
        "08110": "Talcahuano",
        "08111": "Tomé",
        "08112": "Hualpén",
        "08201": "Lebu",
        "08202": "Arauco",
        "08203": "Cañete",
        "08204": "Contulmo",
        "08205": "Curanilahue",
        "08206": "Los Álamos",
        "08207": "Tirúa",
        "08301": "Los Ángeles",
        "08302": "Antuco",
        "08303": "Cabrero",
        "08304": "Laja",
        "08305": "Mulchén",
        "08306": "Nacimiento",
        "08307": "Negrete",
        "08308": "Quilaco",
        "08309": "Quilleco",
        "08310": "San Rosendo",
        "08311": "Santa Bárbara",
        "08312": "Tucapel",
        "08313": "Yumbel",
        "08314": "Alto Biobío",
        "16101": "Chillán",
        "16102": "Bulnes",
        "16202": "Cobquecura",
        "16203": "Coelemu",
        "16302": "Coihueco",
        "16103": "Chillán Viejo",
        "16104": "El Carmen",
        "16204": "Ninhue",
        "16303": "Ñiquén",
        "16105": "Pemuco",
        "16106": "Pinto",
        "16205": "Portezuelo",
        "16107": "Quillón",
        "16201": "Quirihue",
        "16206": "Ránquil",
        "16301": "San Carlos",
        "16304": "San Fabián",
        "16108": "San Ignacio",
        "16305": "San Nicolás",
        "16207": "Treguaco",
        "16109": "Yungay",
        "09101": "Temuco",
        "09102": "Carahue",
        "09103": "Cunco",
        "09104": "Curarrehue",
        "09105": "Freire",
        "09106": "Galvarino",
        "09107": "Gorbea",
        "09108": "Lautaro",
        "09109": "Loncoche",
        "09110": "Melipeuco",
        "09111": "Nueva Imperial",
        "09112": "Padre Las Casas",
        "09113": "Perquenco",
        "09114": "Pitrufquén",
        "09115": "Pucón",
        "09116": "Saavedra",
        "09117": "Teodoro Schmidt",
        "09118": "Toltén",
        "09119": "Vilcún",
        "09120": "Villarrica",
        "09121": "Cholchol",
        "09201": "Angol",
        "09202": "Collipulli",
        "09203": "Curacautín",
        "09204": "Ercilla",
        "09205": "Lonquimay",
        "09206": "Los Sauces",
        "09207": "Lumaco",
        "09208": "Purén",
        "09209": "Renaico",
        "09210": "Traiguén",
        "09211": "Victoria",
        "14101": "Valdivia",
        "14102": "Corral",
        "14202": "Futrono",
        "14201": "La Unión",
        "14203": "Lago Ranco",
        "14103": "Lanco",
        "14104": "Los Lagos",
        "14105": "Máfil",
        "14106": "Mariquina",
        "14107": "Paillaco",
        "14108": "Panguipulli",
        "14204": "Río Bueno",
        "10101": "Puerto Montt",
        "10102": "Calbuco",
        "10103": "Cochamó",
        "10104": "Fresia",
        "10105": "Frutillar",
        "10106": "Los Muermos",
        "10107": "Llanquihue",
        "10108": "Maullín",
        "10109": "Puerto Varas",
        "10201": "Castro",
        "10202": "Ancud",
        "10203": "Chonchi",
        "10204": "Curaco de Vélez",
        "10205": "Dalcahue",
        "10206": "Puqueldón",
        "10207": "Queilén",
        "10208": "Quellón",
        "10209": "Quemchi",
        "10210": "Quinchao",
        "10301": "Osorno",
        "10302": "Puerto Octay",
        "10303": "Purranque",
        "10304": "Puyehue",
        "10305": "Río Negro",
        "10306": "San Juan de la Costa",
        "10307": "San Pablo",
        "10401": "Chaitén",
        "10402": "Futaleufú",
        "10403": "Hualaihué",
        "10404": "Palena",
        "11101": "Coihaique",
        "11102": "Lago Verde",
        "11201": "Aisén",
        "11202": "Cisnes",
        "11203": "Guaitecas",
        "11301": "Cochrane",
        "11302": "O'Higgins",
        "11303": "Tortel",
        "11401": "Chile Chico",
        "11402": "Río Ibáñez",
        "12101": "Punta Arenas",
        "12102": "Laguna Blanca",
        "12103": "Río Verde",
        "12104": "San Gregorio",
        "12201": "Cabo de Hornos",
        "12202": "Antártica",
        "12301": "Porvenir",
        "12302": "Primavera",
        "12303": "Timaukel",
        "12401": "Natales",
        "12402": "Torres del Paine",
        "13101": "Santiago",
        "13102": "Cerrillos",
        "13103": "Cerro Navia",
        "13104": "Conchalí",
        "13105": "El Bosque",
        "13106": "Estación Central",
        "13107": "Huechuraba",
        "13108": "Independencia",
        "13109": "La Cisterna",
        "13110": "La Florida",
        "13111": "La Granja",
        "13112": "La Pintana",
        "13113": "La Reina",
        "13114": "Las Condes",
        "13115": "Lo Barnechea",
        "13116": "Lo Espejo",
        "13117": "Lo Prado",
        "13118": "Macul",
        "13119": "Maipú",
        "13120": "Ñuñoa",
        "13121": "Pedro Aguirre Cerda",
        "13122": "Peñalolén",
        "13123": "Providencia",
        "13124": "Pudahuel",
        "13125": "Quilicura",
        "13126": "Quinta Normal",
        "13127": "Recoleta",
        "13128": "Renca",
        "13129": "San Joaquín",
        "13130": "San Miguel",
        "13131": "San Ramón",
        "13132": "Vitacura",
        "13201": "Puente Alto",
        "13202": "Pirque",
        "13203": "San José de Maipo",
        "13301": "Colina",
        "13302": "Lampa",
        "13303": "Tiltil",
        "13401": "San Bernardo",
        "13402": "Buin",
        "13403": "Calera de Tango",
        "13404": "Paine",
        "13501": "Melipilla",
        "13502": "Alhué",
        "13503": "Curacaví",
        "13504": "María Pinto",
        "13505": "San Pedro",
        "13601": "Talagante",
        "13602": "El Monte",
        "13603": "Isla de Maipo",
        "13604": "Padre Hurtado",
        "13605": "Peñaflor",
    }

    street_prefixes = OrderedDict(
        [
            ("Calle", 0.6),
            ("Avenida", 0.1),
            ("Avda.", 0.1),
            ("Av.", 0.1),
            ("Pasaje", 0.04),
            ("Psje.", 0.04),
            ("Camino", 0.02),
        ]
    )

    street_suffixes = (
        "Norte",
        "Sur",
    )

    city_formats = ("{{city}}",)

    street_name_formats = (
        "{{street_prefix}} {{common_street_name}}",
        "{{street_prefix}} {{historic_people_street_name}}",
        "{{street_prefix}} {{first_name_male}} {{last_name}}",
        "{{street_prefix}} {{first_name_female}} {{last_name}}",
        "{{street_prefix}} {{plant_street_name}}",
        "{{common_street_name}}",
        "{{historic_people_street_name}}",
        "{{plant_street_name}}",
        "{{first_name_male}} {{last_name}}",
        "{{first_name_female}} {{last_name}}",
    )

    building_number_formats = OrderedDict(
        [
            ("%###", 0.35),
            ("%##", 0.35),
            ("%#", 0.25),
            ("%", 0.05),
        ]
    )

    street_address_formats = (
        "{{street_name}} {{building_number}}",
        "{{street_name}} {{building_number}} {{secondary_address}}",
    )

    address_formats = OrderedDict(
        [
            ("{{street_address}}\n{{commune_and_region}}, {{postcode}}", 0.4),
            ("{{street_address}}\n{{commune_and_region}}", 0.4),
            ("{{highway_name}}, km {{random_int:big_kilometer}}", 0.1),
            ("{{road_name}}, km {{random_int:kilometer}}, {{region}}", 0.1),
        ]
    )

    secondary_address_formats = ("Dpto. @@##", "Piso @#", "Of. %##@")

    common_street_names = OrderedDict(
        [
            ("Arturo Prat", 0.118812),
            ("Esmeralda", 0.107261),
            ("Manuel Rodríguez", 0.105611),
            ("Gabriela Mistral", 0.104785),
            ("Los Aromos", 0.104785),
            ("Las Rosas", 0.098185),
            ("Caupolicán", 0.094884),
            ("Lautaro", 0.094059),
            ("Los Alerces", 0.086634),
            ("Los Copihues", 0.084983),
        ]
    )

    # Some chilean historic people. Full names come first, then its variants
    historic_people_street_names = (
        ("Alonso de Ercilla",),
        ("Alonso de Ribera",),
        ("Álvaro Casanova", "Casanova"),
        ("Aníbal Pinto Garmendia", "Aníbal Pinto"),
        ("Antonio Varas",),
        ("Arturo Alessandri Palma", "Arturo Alessandri"),
        ("Benjamín Vicuña Mackenna", "Vicuña Mackenna", "Mackenna"),
        ("Bernardo O'Higgins", "O'Higgins"),
        ("Camilo Henríquez",),
        ("Caupolicán",),
        ("Colo Colo",),
        ("Diego Barros Arana", "Barros Arana"),
        ("Diego Portales", "Portales"),
        ("Domingo Santa María", "Santa María"),
        ("Eliodoro Yáñez",),
        ("Enrique Mac Iver", "Mac Iver"),
        ("Eusebio Lillo",),
        ("Francisco Bilbao", "Bilbao"),
        ("José de San Martín", "San Martín"),
        ("José Manuel Balmaceda", "Balmaceda"),
        ("José Miguel Carrera",),
        ("José Victorino Lastarria", "Lastarria"),
        ("Juan Mackenna",),
        ("Lord Thomas Cochrane", "Lord Cochrane", "Cochrane"),
        ("Los Carrera",),
        ("Manuel Antonio Matta", "Matta"),
        ("Manuel Bulnes", "Bulnes"),
        ("Manuel José Irarrázaval", "Irarrázabal"),
        ("Manuel Montt",),
        ("Manuel Rodríguez",),
        ("Manuel Baquedano", "Baquedano"),
        ("Michimalonco",),
        ("Padre Alberto Hurtado", "Alberto Hurtado"),
        ("Patricio Lynch", "Lynch"),
        ("Paula Jaraquemada",),
        ("Pedro Aguirre Cerda",),
        ("Pedro de Valdivia",),
        ("Pedro Montt",),
        ("Ramón Barros Luco", "Barros Luco"),
        ("Ramón Carnicer",),
        ("Ramón Freire", "Freire"),
        ("Ramón Picarte", "Picarte"),
        ("Salvador Allende Gossens", "Salvador Allende"),
        ("Santa Rosa",),
    )

    # Some streets are named by plants
    plant_street_names: ElementsType = (
        "Los Cactus",
        "Los Laureles",
        "Los Piñones",
        "Los Helechos",
        "Los Higos",
        "Los Abedules",
        "Los Encinos",
        "Los Palmitos",
        "Los Naranjos",
        "Los Robles",
        "Los Pinos",
        "Los Coihues",
        "Los Calafates",
        "Los Digitales",
        "Los Lirios",
        "Los Tilos",
        "Los Girasoles",
        "Las Azucenas",
        "Las Lilas",
        "Las Hortensias",
        "Las Margaritas",
        "Las Maravillas",
        "Las Manzanillas",
        "Las Mandarinas",
        "Las Araucarias",
        "Las Mosquetas",
        "Las Malvas",
        "Las Mosquetas",
    )

    road_names = ("Ruta T-%#", "Ruta U-%##", "Ruta %##-CH")
    highway_names = ("Ruta 5 Norte", "Ruta 5 Sur")

    def commune(self) -> str:
        return self.random_element(self.communes.values())

    def province(self) -> str:
        return self.random_element(self.provinces.values())

    def region(self) -> str:
        return self.random_element(self.regions.values())

    def commune_code(self) -> str:
        return self.random_element(self.communes.keys())

    def province_code(self) -> str:
        return self.random_element(self.provinces.keys())

    def region_code(self) -> str:
        return self.random_element(self.regions.keys())

    def common_street_name(self) -> str:
        return self.random_element(self.common_street_names)

    def plant_street_name(self) -> str:
        return self.random_element(self.plant_street_names)

    def historic_people_street_name(self) -> str:
        person_names: Tuple[str, ...] = self.random_element(self.historic_people_street_names)
        return self.random_element(person_names)

    def street_prefix(self) -> str:
        return self.random_element(self.street_prefixes)

    def secondary_address(self) -> str:
        return self.numerify(self.random_element(self.secondary_address_formats))

    def commune_and_region(self) -> str:
        commune_code = self.commune_code()
        commune_name = self.communes[commune_code]
        region_index = int(commune_code[:2]) - 1
        region_name = tuple(self.regions.values())[region_index]

        return "{:s}, {:s}".format(commune_name, region_name)

    def road_name(self) -> str:
        self.generator.set_arguments("kilometer", {"min": 1, "max": 35})
        return self.numerify(self.generator.parse(self.random_element(self.road_names)))

    def highway_name(self) -> str:
        self.generator.set_arguments("big_kilometer", {"min": 1, "max": 1000})
        return self.numerify(self.generator.parse(self.random_element(self.highway_names)))

    def postcode(self) -> str:
        return self.numerify("######0")

    administrative_unit = region
    city = commune
