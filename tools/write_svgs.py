# ASCII-only SVG writer. Spanish via HTML entities.
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "public" / "assets" / "screenshots"


def w(name, svg):
    path = ROOT / name
    path.write_text(svg.strip() + "\n", encoding="utf-8", newline="\n")
    print("wrote", path.name)


menu = """
  <rect x="20" y="54" width="18" height="2" fill="#fff"/>
  <rect x="20" y="60" width="18" height="2" fill="#fff"/>
  <rect x="20" y="66" width="18" height="2" fill="#fff"/>
"""

chrome = """
  <rect width="1280" height="780" rx="12" fill="#e8eef4"/>
  <rect x="0" y="0" width="1280" height="36" fill="#d5dee8"/>
  <circle cx="18" cy="18" r="5" fill="#ed6a5e"/>
  <circle cx="34" cy="18" r="5" fill="#f4bf4f"/>
  <circle cx="50" cy="18" r="5" fill="#61c554"/>
  <rect x="180" y="10" width="920" height="16" rx="8" fill="#fff"/>
"""


def bar(title, url):
    return f"""
  <text x="196" y="22" font-family="Segoe UI, Arial, sans-serif" font-size="10" fill="#7a8694">{url}</text>
  <rect x="0" y="36" width="1280" height="50" fill="#156fb3"/>
  {menu}
  <text x="56" y="67" font-family="Segoe UI, Arial, sans-serif" font-size="15" font-weight="600" fill="#fff">{title}</text>
"""


note = '<text x="640" y="760" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="11" fill="#9aa5b1">Captura ilustrativa - reemplazar por imagen real</text>'

w("inspecciones.svg", f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 780" fill="none">
{chrome}
{bar("Arch - Inspecciones", "app.archsys.com.ar / inspecciones")}
  <text x="1180" y="67" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#e8f2fb">j.garcia</text>
  <rect x="0" y="86" width="1280" height="92" fill="#f4f7f9"/>
  <rect x="24" y="102" width="280" height="36" rx="8" fill="#fff" stroke="#d5dee8"/>
  <text x="40" y="125" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#9aa5b1">Buscar inspecciones...</text>
  <rect x="24" y="148" width="118" height="22" rx="11" fill="#156fb3"/>
  <text x="50" y="163" font-family="Segoe UI, Arial, sans-serif" font-size="11" fill="#fff">Todas</text>
  <rect x="150" y="148" width="148" height="22" rx="11" fill="#ffaf38"/>
  <text x="168" y="163" font-family="Segoe UI, Arial, sans-serif" font-size="11" fill="#3a2a00">Inspecci&#243;n T&#233;cnica</text>
  <rect x="306" y="148" width="136" height="22" rx="11" fill="#ed5034"/>
  <text x="326" y="163" font-family="Segoe UI, Arial, sans-serif" font-size="11" fill="#fff">Reclamo T&#233;cnico</text>
  <rect x="450" y="148" width="118" height="22" rx="11" fill="#38a5ff"/>
  <text x="470" y="163" font-family="Segoe UI, Arial, sans-serif" font-size="11" fill="#fff">Inspecci&#243;n RT</text>
  <rect x="576" y="148" width="156" height="22" rx="11" fill="#06ce9c"/>
  <text x="590" y="163" font-family="Segoe UI, Arial, sans-serif" font-size="11" fill="#083528">Prueba de Seguridad</text>
  <g transform="translate(24,196)">
    <rect width="1232" height="88" rx="10" fill="#fff" stroke="#e4e8ec"/>
    <rect width="8" height="88" rx="4" fill="#ffaf38"/>
    <text x="28" y="28" font-family="Segoe UI, Arial, sans-serif" font-size="16" font-weight="600" fill="#0c1c41">Edificio Nueva C&#243;rdoba (C&#243;rdoba)</text>
    <text x="1080" y="28" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">07/09/2026 09:14</text>
    <text x="28" y="52" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#4a5560">E01: Control de puertas, nivelaci&#243;n y botonera. Sin observaciones.</text>
    <text x="28" y="74" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">Av. Hip&#243;lito Yrigoyen 184 - Juan Garc&#237;a</text>
  </g>
  <g transform="translate(24,296)">
    <rect width="1232" height="88" rx="10" fill="#fff" stroke="#e4e8ec"/>
    <rect width="8" height="88" rx="4" fill="#ed5034"/>
    <text x="28" y="28" font-family="Segoe UI, Arial, sans-serif" font-size="16" font-weight="600" fill="#0c1c41">Torre G&#252;emes (C&#243;rdoba)</text>
    <text x="1080" y="28" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">07/09/2026 08:41</text>
    <text x="28" y="52" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#4a5560">E02: Ruido en cuarto de m&#225;quinas. Se programa visita de reclamo t&#233;cnico.</text>
    <text x="28" y="74" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">Bv. San Juan 650 - Ana P&#233;rez</text>
  </g>
  <g transform="translate(24,396)">
    <rect width="1232" height="88" rx="10" fill="#fff" stroke="#e4e8ec"/>
    <rect width="8" height="88" rx="4" fill="#38a5ff"/>
    <text x="28" y="28" font-family="Segoe UI, Arial, sans-serif" font-size="16" font-weight="600" fill="#0c1c41">Residencial Alberdi (C&#243;rdoba)</text>
    <text x="1080" y="28" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">06/09/2026 16:22</text>
    <text x="28" y="52" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#4a5560">E01: Inspecci&#243;n RT. Documentaci&#243;n y normativa al d&#237;a.</text>
    <text x="28" y="74" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">Av. Col&#243;n 1200 - Luis Romero</text>
  </g>
  <g transform="translate(24,496)">
    <rect width="1232" height="88" rx="10" fill="#fff" stroke="#e4e8ec"/>
    <rect width="8" height="88" rx="4" fill="#06ce9c"/>
    <text x="28" y="28" font-family="Segoe UI, Arial, sans-serif" font-size="16" font-weight="600" fill="#0c1c41">Edificio General Paz (C&#243;rdoba)</text>
    <text x="1080" y="28" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">06/09/2026 11:05</text>
    <text x="28" y="52" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#4a5560">E03: Prueba de seguridad anual aprobada. Freno y limitador OK.</text>
    <text x="28" y="74" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">Av. General Paz 210 - Marta D&#237;az</text>
  </g>
  <g transform="translate(24,596)">
    <rect width="1232" height="88" rx="10" fill="#fff" stroke="#e4e8ec"/>
    <rect width="8" height="88" rx="4" fill="#ffaf38"/>
    <text x="28" y="28" font-family="Segoe UI, Arial, sans-serif" font-size="16" font-weight="600" fill="#0c1c41">Torre Centro (C&#243;rdoba)</text>
    <text x="1080" y="28" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">05/09/2026 15:48</text>
    <text x="28" y="52" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#4a5560">E01: Lubricaci&#243;n de gu&#237;as y revisi&#243;n de cables. Pr&#243;ximo control en 30 d&#237;as.</text>
    <text x="28" y="74" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">25 de Mayo 180 - Juan Garc&#237;a</text>
  </g>
  {note}
</svg>""")

w("edificios.svg", f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 780" fill="none">
{chrome}
{bar("Arch - Edificios", "app.archsys.com.ar / edificios")}
  <rect x="24" y="104" width="160" height="36" rx="8" fill="#10385e"/>
  <text x="44" y="127" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#fff">+ Agregar edificio</text>
  <rect x="480" y="104" width="140" height="36" rx="8" fill="#156fb3"/>
  <text x="504" y="127" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#fff">Servicio activo</text>
  <rect x="628" y="104" width="150" height="36" rx="8" fill="#fff" stroke="#c5d0db"/>
  <text x="650" y="127" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#5a6a7a">Servicio inactivo</text>
  <rect x="980" y="98" width="132" height="52" rx="8" fill="#fff" stroke="#e4e8ec"/>
  <text x="1046" y="118" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="10" fill="#7a8694">EDIFICIOS</text>
  <text x="1012" y="140" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#156fb3">Activos 142</text>
  <rect x="1120" y="98" width="132" height="52" rx="8" fill="#fff" stroke="#e4e8ec"/>
  <text x="1186" y="118" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="10" fill="#7a8694">EQUIPOS</text>
  <text x="1148" y="140" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#156fb3">Activos 318</text>
  <rect x="24" y="168" width="1232" height="560" rx="10" fill="#fff" stroke="#e4e8ec"/>
  <rect x="24" y="168" width="1232" height="48" rx="10" fill="#123e6a"/>
  <text x="48" y="198" font-family="Segoe UI, Arial, sans-serif" font-size="12" font-weight="600" fill="#fff">NOMBRE</text>
  <text x="300" y="198" font-family="Segoe UI, Arial, sans-serif" font-size="12" font-weight="600" fill="#fff">DIRECCI&#211;N</text>
  <text x="620" y="198" font-family="Segoe UI, Arial, sans-serif" font-size="12" font-weight="600" fill="#fff">BARRIO</text>
  <text x="820" y="198" font-family="Segoe UI, Arial, sans-serif" font-size="12" font-weight="600" fill="#fff">CIUDAD</text>
  <text x="1000" y="198" font-family="Segoe UI, Arial, sans-serif" font-size="12" font-weight="600" fill="#fff">EQUIPOS</text>
  <text x="1120" y="198" font-family="Segoe UI, Arial, sans-serif" font-size="12" font-weight="600" fill="#fff">ESTADO</text>
  <g font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#1d2a36">
    <text x="48" y="248">Nueva C&#243;rdoba</text><text x="300" y="248">Av. Hip&#243;lito Yrigoyen 184</text><text x="620" y="248">Nueva C&#243;rdoba</text><text x="820" y="248">C&#243;rdoba</text><text x="1020" y="248">3</text>
    <text x="48" y="298">Torre G&#252;emes</text><text x="300" y="298">Bv. San Juan 650</text><text x="620" y="298">Centro</text><text x="820" y="298">C&#243;rdoba</text><text x="1020" y="298">2</text>
    <text x="48" y="348">Residencial Alberdi</text><text x="300" y="348">Av. Col&#243;n 1200</text><text x="620" y="348">Alberdi</text><text x="820" y="348">C&#243;rdoba</text><text x="1020" y="348">4</text>
    <text x="48" y="398">General Paz</text><text x="300" y="398">Av. General Paz 210</text><text x="620" y="398">General Paz</text><text x="820" y="398">C&#243;rdoba</text><text x="1020" y="398">2</text>
    <text x="48" y="448">Torre Centro</text><text x="300" y="448">25 de Mayo 180</text><text x="620" y="448">Centro</text><text x="820" y="448">C&#243;rdoba</text><text x="1020" y="448">5</text>
    <text x="48" y="498">Edificio Cerro</text><text x="300" y="498">Av. Rafael N&#250;&#241;ez 4600</text><text x="620" y="498">Cerro</text><text x="820" y="498">C&#243;rdoba</text><text x="1020" y="498">2</text>
    <text x="48" y="548">Plaza Espa&#241;a</text><text x="300" y="548">Av. Poeta Lugones 88</text><text x="620" y="548">Nueva C&#243;rdoba</text><text x="820" y="548">C&#243;rdoba</text><text x="1020" y="548">3</text>
    <text x="48" y="598">Alto Verde</text><text x="300" y="598">Recta Martinolli 8500</text><text x="620" y="598">Arg&#252;ello</text><text x="820" y="598">C&#243;rdoba</text><text x="1020" y="598">1</text>
    <text x="48" y="648">Torre R&#237;o</text><text x="300" y="648">Av. Costanera 320</text><text x="620" y="648">San Vicente</text><text x="820" y="648">C&#243;rdoba</text><text x="1020" y="648">2</text>
  </g>
  <g>
    <rect x="1118" y="232" width="72" height="22" rx="11" fill="#e7f8f1"/><text x="1154" y="247" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="11" fill="#0a7a58">Activo</text>
    <rect x="1118" y="282" width="72" height="22" rx="11" fill="#e7f8f1"/><text x="1154" y="297" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="11" fill="#0a7a58">Activo</text>
    <rect x="1118" y="332" width="72" height="22" rx="11" fill="#e7f8f1"/><text x="1154" y="347" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="11" fill="#0a7a58">Activo</text>
    <rect x="1118" y="382" width="72" height="22" rx="11" fill="#e7f8f1"/><text x="1154" y="397" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="11" fill="#0a7a58">Activo</text>
    <rect x="1118" y="432" width="72" height="22" rx="11" fill="#e7f8f1"/><text x="1154" y="447" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="11" fill="#0a7a58">Activo</text>
    <rect x="1118" y="482" width="72" height="22" rx="11" fill="#e7f8f1"/><text x="1154" y="497" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="11" fill="#0a7a58">Activo</text>
    <rect x="1118" y="532" width="72" height="22" rx="11" fill="#e7f8f1"/><text x="1154" y="547" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="11" fill="#0a7a58">Activo</text>
    <rect x="1118" y="582" width="72" height="22" rx="11" fill="#e7f8f1"/><text x="1154" y="597" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="11" fill="#0a7a58">Activo</text>
    <rect x="1118" y="632" width="72" height="22" rx="11" fill="#e7f8f1"/><text x="1154" y="647" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="11" fill="#0a7a58">Activo</text>
  </g>
  <line x1="24" y1="216" x2="1256" y2="216" stroke="#e4e8ec"/>
  <text x="48" y="710" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">Mostrando 1 a 9 de 142 registros</text>
  {note}
</svg>""")

w("monitoreo.svg", f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 780" fill="none">
{chrome}
{bar("Arch - Monitoreo de rutas", "app.archsys.com.ar / monitoreos / rutas")}
  <rect x="0" y="86" width="320" height="694" fill="#fff"/>
  <text x="24" y="122" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#156fb3">Atras</text>
  <text x="24" y="160" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">FECHA</text>
  <rect x="24" y="170" width="272" height="40" rx="8" fill="#f4f7f9" stroke="#d5dee8"/>
  <text x="40" y="195" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#0c1c41">07/09/2026</text>
  <text x="24" y="240" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">TECNICO</text>
  <rect x="24" y="250" width="272" height="36" rx="8" fill="#f4f7f9" stroke="#d5dee8"/>
  <text x="40" y="273" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#9aa5b1">Buscar t&#233;cnico...</text>
  <rect x="24" y="302" width="272" height="40" rx="6" fill="#e8f2fb"/>
  <text x="40" y="327" font-family="Segoe UI, Arial, sans-serif" font-size="14" font-weight="600" fill="#123e6a">Juan Garc&#237;a</text>
  <text x="40" y="372" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#1d2a36">Ana P&#233;rez</text>
  <text x="40" y="412" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#1d2a36">Luis Romero</text>
  <text x="40" y="452" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#1d2a36">Marta D&#237;az</text>
  <rect x="24" y="500" width="272" height="120" rx="10" fill="#f4f7f9"/>
  <text x="40" y="528" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">RESUMEN DEL DIA</text>
  <text x="40" y="556" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#1d2a36">Visitas: 8</text>
  <text x="40" y="578" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#1d2a36">Km estimados: 42</text>
  <text x="40" y="600" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#1d2a36">Pendientes: 1</text>
  <rect x="320" y="86" width="960" height="694" fill="#dce6ef"/>
  <path d="M360 640 C420 520, 480 500, 560 430 C640 360, 700 340, 780 300 C860 260, 920 280, 1020 240 C1100 210, 1160 200, 1220 180" stroke="#156fb3" stroke-width="4" fill="none"/>
  <circle cx="420" cy="560" r="10" fill="#ffaf38" stroke="#fff" stroke-width="3"/>
  <circle cx="560" cy="430" r="10" fill="#06ce9c" stroke="#fff" stroke-width="3"/>
  <circle cx="780" cy="300" r="10" fill="#06ce9c" stroke="#fff" stroke-width="3"/>
  <circle cx="1020" cy="240" r="10" fill="#38a5ff" stroke="#fff" stroke-width="3"/>
  <circle cx="1180" cy="190" r="10" fill="#ed5034" stroke="#fff" stroke-width="3"/>
  <rect x="980" y="120" width="260" height="150" rx="10" fill="#fff" opacity="0.96"/>
  <text x="1000" y="148" font-family="Segoe UI, Arial, sans-serif" font-size="13" font-weight="600" fill="#0c1c41">Leyenda</text>
  <circle cx="1012" cy="176" r="6" fill="#ffaf38"/><text x="1028" y="180" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#1d2a36">Inspecci&#243;n t&#233;cnica</text>
  <circle cx="1012" cy="200" r="6" fill="#ed5034"/><text x="1028" y="204" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#1d2a36">Reclamo t&#233;cnico</text>
  <circle cx="1012" cy="224" r="6" fill="#38a5ff"/><text x="1028" y="228" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#1d2a36">Inspecci&#243;n RT</text>
  <circle cx="1012" cy="248" r="6" fill="#06ce9c"/><text x="1028" y="252" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#1d2a36">Prueba de seguridad</text>
  <rect x="360" y="700" width="220" height="48" rx="8" fill="#fff"/>
  <text x="376" y="720" font-family="Segoe UI, Arial, sans-serif" font-size="11" fill="#7a8694">PROXIMA PARADA</text>
  <text x="376" y="738" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#0c1c41">Torre G&#252;emes - 10:30</text>
  {note}
</svg>""")

w("reportes.svg", f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 780" fill="none">
{chrome}
{bar("Arch - Estad&#237;sticas y reportes", "app.archsys.com.ar / estadisticas / mensuales")}
  <rect x="24" y="106" width="292" height="100" rx="10" fill="#fff" stroke="#e4e8ec"/>
  <text x="44" y="136" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">INSPECCIONES DEL MES</text>
  <text x="44" y="176" font-family="Segoe UI, Arial, sans-serif" font-size="32" font-weight="700" fill="#123e6a">1.248</text>
  <rect x="332" y="106" width="292" height="100" rx="10" fill="#fff" stroke="#e4e8ec"/>
  <text x="352" y="136" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">RECLAMOS CERRADOS</text>
  <text x="352" y="176" font-family="Segoe UI, Arial, sans-serif" font-size="32" font-weight="700" fill="#ed5034">186</text>
  <rect x="640" y="106" width="292" height="100" rx="10" fill="#fff" stroke="#e4e8ec"/>
  <text x="660" y="136" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">PRUEBAS DE SEGURIDAD</text>
  <text x="660" y="176" font-family="Segoe UI, Arial, sans-serif" font-size="32" font-weight="700" fill="#06ce9c">94</text>
  <rect x="948" y="106" width="308" height="100" rx="10" fill="#fff" stroke="#e4e8ec"/>
  <text x="968" y="136" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">CUMPLIMIENTO</text>
  <text x="968" y="176" font-family="Segoe UI, Arial, sans-serif" font-size="32" font-weight="700" fill="#156fb3">98,4%</text>
  <rect x="24" y="226" width="800" height="360" rx="10" fill="#fff" stroke="#e4e8ec"/>
  <text x="44" y="258" font-family="Segoe UI, Arial, sans-serif" font-size="15" font-weight="600" fill="#0c1c41">Inspecciones por semana</text>
  <polyline points="80,520 180,470 280,430 380,390 480,410 580,340 680,300 760,280" fill="none" stroke="#156fb3" stroke-width="3"/>
  <circle cx="80" cy="520" r="5" fill="#156fb3"/>
  <circle cx="180" cy="470" r="5" fill="#156fb3"/>
  <circle cx="280" cy="430" r="5" fill="#156fb3"/>
  <circle cx="380" cy="390" r="5" fill="#156fb3"/>
  <circle cx="480" cy="410" r="5" fill="#156fb3"/>
  <circle cx="580" cy="340" r="5" fill="#156fb3"/>
  <circle cx="680" cy="300" r="5" fill="#156fb3"/>
  <circle cx="760" cy="280" r="5" fill="#156fb3"/>
  <rect x="844" y="226" width="412" height="360" rx="10" fill="#fff" stroke="#e4e8ec"/>
  <text x="864" y="258" font-family="Segoe UI, Arial, sans-serif" font-size="15" font-weight="600" fill="#0c1c41">Distribuci&#243;n por tipo</text>
  <rect x="864" y="290" width="220" height="16" rx="4" fill="#ffaf38"/>
  <text x="1096" y="303" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#1d2a36">T&#233;cnica 62%</text>
  <rect x="864" y="330" width="110" height="16" rx="4" fill="#ed5034"/>
  <text x="986" y="343" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#1d2a36">Reclamo 15%</text>
  <rect x="864" y="370" width="150" height="16" rx="4" fill="#38a5ff"/>
  <text x="1026" y="383" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#1d2a36">RT 15%</text>
  <rect x="864" y="410" width="80" height="16" rx="4" fill="#06ce9c"/>
  <text x="956" y="423" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#1d2a36">Seguridad 8%</text>
  <rect x="864" y="470" width="352" height="86" rx="8" fill="#f4f7f9"/>
  <text x="884" y="504" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#1d2a36">Exportar reporte de edificios</text>
  <rect x="884" y="518" width="140" height="26" rx="6" fill="#10385e"/>
  <text x="954" y="536" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#fff">Generar PDF</text>
  <rect x="24" y="606" width="1232" height="130" rx="10" fill="#fff" stroke="#e4e8ec"/>
  <text x="44" y="638" font-family="Segoe UI, Arial, sans-serif" font-size="15" font-weight="600" fill="#0c1c41">Reportes disponibles</text>
  <rect x="44" y="656" width="240" height="56" rx="8" fill="#f4f7f9"/>
  <text x="64" y="690" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#123e6a">Por edificios</text>
  <rect x="300" y="656" width="240" height="56" rx="8" fill="#f4f7f9"/>
  <text x="320" y="690" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#123e6a">Por administraciones</text>
  <rect x="556" y="656" width="240" height="56" rx="8" fill="#f4f7f9"/>
  <text x="576" y="690" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#123e6a">Por usuarios / t&#233;cnicos</text>
  <rect x="812" y="656" width="240" height="56" rx="8" fill="#f4f7f9"/>
  <text x="832" y="690" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#123e6a">Estad&#237;sticas anuales</text>
  {note}
</svg>""")

w("equipos.svg", f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 780" fill="none">
{chrome}
{bar("Arch - Detalle de equipo", "app.archsys.com.ar / equipo-detalles / E01")}
  <rect x="24" y="106" width="820" height="630" rx="10" fill="#fff" stroke="#e4e8ec"/>
  <text x="48" y="150" font-family="Segoe UI, Arial, sans-serif" font-size="22" font-weight="700" fill="#0c1c41">E01 - Edificio Nueva C&#243;rdoba</text>
  <text x="48" y="178" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#7a8694">Av. Hip&#243;lito Yrigoyen 184 - C&#243;rdoba Capital</text>
  <g font-family="Segoe UI, Arial, sans-serif" font-size="14">
    <text x="48" y="230" fill="#7a8694">Marca</text><text x="220" y="230" fill="#0c1c41">Otis</text>
    <text x="48" y="268" fill="#7a8694">Modelo</text><text x="220" y="268" fill="#0c1c41">Gen2 Comfort</text>
    <text x="48" y="306" fill="#7a8694">Paradas</text><text x="220" y="306" fill="#0c1c41">12</text>
    <text x="48" y="344" fill="#7a8694">Capacidad</text><text x="220" y="344" fill="#0c1c41">8 personas / 630 kg</text>
    <text x="48" y="382" fill="#7a8694">Conservador</text><text x="220" y="382" fill="#0c1c41">Ascensores del Centro S.A.</text>
    <text x="48" y="420" fill="#7a8694">Administraci&#243;n</text><text x="220" y="420" fill="#0c1c41">Adm. Nueva C&#243;rdoba</text>
    <text x="48" y="458" fill="#7a8694">Ultima inspecci&#243;n</text><text x="220" y="458" fill="#0c1c41">07/09/2026 09:14</text>
    <text x="48" y="496" fill="#7a8694">Proxima PS</text><text x="220" y="496" fill="#0c1c41">12/03/2027</text>
    <text x="48" y="534" fill="#7a8694">Estado</text>
  </g>
  <rect x="220" y="516" width="72" height="24" rx="12" fill="#e7f8f1"/>
  <text x="256" y="533" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#0a7a58">Activo</text>
  <rect x="48" y="572" width="200" height="40" rx="8" fill="#10385e"/>
  <text x="148" y="597" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#fff">Historial de visitas</text>
  <rect x="264" y="572" width="180" height="40" rx="8" fill="#fff" stroke="#156fb3"/>
  <text x="354" y="597" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#156fb3">Imprimir QR</text>
  <rect x="864" y="106" width="392" height="630" rx="10" fill="#fff" stroke="#e4e8ec"/>
  <text x="1060" y="150" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="15" font-weight="600" fill="#0c1c41">Identificaci&#243;n QR</text>
  <rect x="944" y="180" width="232" height="232" fill="#fff" stroke="#0c1c41" stroke-width="8"/>
  <g fill="#0c1c41">
    <rect x="968" y="204" width="36" height="36"/>
    <rect x="1116" y="204" width="36" height="36"/>
    <rect x="968" y="352" width="36" height="36"/>
    <rect x="1016" y="220" width="16" height="16"/>
    <rect x="1040" y="244" width="16" height="16"/>
    <rect x="1064" y="220" width="16" height="16"/>
    <rect x="1016" y="268" width="16" height="16"/>
    <rect x="1088" y="268" width="16" height="16"/>
    <rect x="1040" y="292" width="16" height="16"/>
    <rect x="1016" y="316" width="16" height="16"/>
    <rect x="1064" y="316" width="16" height="16"/>
    <rect x="1088" y="340" width="16" height="16"/>
    <rect x="1040" y="364" width="16" height="16"/>
  </g>
  <text x="1060" y="448" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#1d2a36">E01 - Nueva C&#243;rdoba</text>
  <text x="1060" y="476" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">El t&#233;cnico escanea el QR en sitio</text>
  <text x="1060" y="496" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#7a8694">para registrar la inspecci&#243;n.</text>
  <rect x="944" y="530" width="232" height="44" rx="8" fill="#156fb3"/>
  <text x="1060" y="557" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#fff">Descargar etiqueta</text>
  {note}
</svg>""")

w("qr-movil.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 1280" fill="none">
  <rect width="720" height="1280" rx="48" fill="#0a2840"/>
  <rect x="24" y="24" width="672" height="1232" rx="36" fill="#0c1c41"/>
  <rect x="300" y="44" width="120" height="18" rx="9" fill="#1a2a3a"/>
  <text x="360" y="110" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="22" font-weight="600" fill="#fff">Escanea el c&#243;digo QR</text>
  <rect x="70" y="160" width="580" height="720" rx="20" fill="#12263a"/>
  <rect x="110" y="210" width="500" height="500" rx="8" fill="none" stroke="#156fb3" stroke-width="4"/>
  <rect x="110" y="210" width="56" height="8" fill="#2a87c9"/>
  <rect x="110" y="210" width="8" height="56" fill="#2a87c9"/>
  <rect x="554" y="210" width="56" height="8" fill="#2a87c9"/>
  <rect x="602" y="210" width="8" height="56" fill="#2a87c9"/>
  <rect x="110" y="702" width="56" height="8" fill="#2a87c9"/>
  <rect x="110" y="654" width="8" height="56" fill="#2a87c9"/>
  <rect x="554" y="702" width="56" height="8" fill="#2a87c9"/>
  <rect x="602" y="654" width="8" height="56" fill="#2a87c9"/>
  <g fill="#c5d4e2" opacity="0.35">
    <rect x="220" y="330" width="40" height="40"/>
    <rect x="460" y="330" width="40" height="40"/>
    <rect x="220" y="560" width="40" height="40"/>
    <rect x="300" y="400" width="20" height="20"/>
    <rect x="360" y="440" width="20" height="20"/>
    <rect x="400" y="380" width="20" height="20"/>
    <rect x="320" y="500" width="20" height="20"/>
    <rect x="420" y="520" width="20" height="20"/>
  </g>
  <circle cx="580" cy="820" r="28" fill="#156fb3"/>
  <text x="160" y="955" font-family="Segoe UI, Arial, sans-serif" font-size="16" fill="#fff"> </text>
  <rect x="160" y="920" width="400" height="56" rx="12" fill="#123e6a"/>
  <text x="360" y="955" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="16" fill="#fff">Escanear desde foto</text>
  <rect x="160" y="996" width="400" height="56" rx="12" fill="#156fb3"/>
  <text x="360" y="1031" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="16" fill="#fff">Cancelar</text>
  <text x="360" y="1120" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#8aa0b5">El t&#233;cnico registra la visita en el equipo</text>
  <text x="360" y="1144" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#8aa0b5">sin papeles ni planillas.</text>
  <text x="360" y="1220" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#5a7188">Captura ilustrativa - reemplazar por imagen real</text>
</svg>""")

w("acciones-masivas.svg", f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 780" fill="none">
{chrome}
{bar("Arch - Acciones masivas", "app.archsys.com.ar / acciones-masivas")}
  <text x="48" y="130" font-family="Segoe UI, Arial, sans-serif" font-size="22" font-weight="700" fill="#0c1c41">Operaciones en lote</text>
  <text x="48" y="158" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#5a6a7a">Carga, asignaci&#243;n e impresi&#243;n para flotas de edificios y equipos.</text>
  <rect x="48" y="196" width="380" height="200" rx="12" fill="#fff" stroke="#e4e8ec"/>
  <rect x="48" y="196" width="8" height="200" rx="4" fill="#156fb3"/>
  <text x="80" y="240" font-family="Segoe UI, Arial, sans-serif" font-size="18" font-weight="600" fill="#0c1c41">Carga masiva de edificios</text>
  <text x="80" y="272" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#5a6a7a">Importaci&#243;n por planilla con</text>
  <text x="80" y="294" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#5a6a7a">validaci&#243;n previa y confirmaci&#243;n.</text>
  <rect x="80" y="330" width="150" height="36" rx="8" fill="#10385e"/>
  <text x="155" y="353" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#fff">Abrir</text>
  <rect x="452" y="196" width="380" height="200" rx="12" fill="#fff" stroke="#e4e8ec"/>
  <rect x="452" y="196" width="8" height="200" rx="4" fill="#123e6a"/>
  <text x="484" y="240" font-family="Segoe UI, Arial, sans-serif" font-size="18" font-weight="600" fill="#0c1c41">Carga masiva de equipos</text>
  <text x="484" y="272" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#5a6a7a">Alta de ascensores asociados</text>
  <text x="484" y="294" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#5a6a7a">a edificios existentes.</text>
  <rect x="484" y="330" width="150" height="36" rx="8" fill="#10385e"/>
  <text x="559" y="353" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#fff">Abrir</text>
  <rect x="856" y="196" width="380" height="200" rx="12" fill="#fff" stroke="#e4e8ec"/>
  <rect x="856" y="196" width="8" height="200" rx="4" fill="#2a87c9"/>
  <text x="888" y="240" font-family="Segoe UI, Arial, sans-serif" font-size="18" font-weight="600" fill="#0c1c41">Asignaci&#243;n de edificios</text>
  <text x="888" y="272" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#5a6a7a">Asigna t&#233;cnicos, conservadores</text>
  <text x="888" y="294" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#5a6a7a">o administraciones en lote.</text>
  <rect x="888" y="330" width="150" height="36" rx="8" fill="#10385e"/>
  <text x="963" y="353" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#fff">Abrir</text>
  <rect x="48" y="420" width="380" height="200" rx="12" fill="#fff" stroke="#e4e8ec"/>
  <rect x="48" y="420" width="8" height="200" rx="4" fill="#06ce9c"/>
  <text x="80" y="464" font-family="Segoe UI, Arial, sans-serif" font-size="18" font-weight="600" fill="#0c1c41">Impresi&#243;n masiva de QR</text>
  <text x="80" y="496" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#5a6a7a">Hojas listas para imprenta,</text>
  <text x="80" y="518" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#5a6a7a">con logo y datos del equipo.</text>
  <rect x="80" y="554" width="150" height="36" rx="8" fill="#10385e"/>
  <text x="155" y="577" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#fff">Abrir</text>
  <rect x="452" y="420" width="380" height="200" rx="12" fill="#fff" stroke="#e4e8ec"/>
  <rect x="452" y="420" width="8" height="200" rx="4" fill="#ffaf38"/>
  <text x="484" y="464" font-family="Segoe UI, Arial, sans-serif" font-size="18" font-weight="600" fill="#0c1c41">Regeneraci&#243;n de QR</text>
  <text x="484" y="496" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#5a6a7a">Volve a emitir c&#243;digos</text>
  <text x="484" y="518" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#5a6a7a">sin perder el historial.</text>
  <rect x="484" y="554" width="150" height="36" rx="8" fill="#10385e"/>
  <text x="559" y="577" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#fff">Abrir</text>
  <rect x="856" y="420" width="380" height="200" rx="12" fill="#fff" stroke="#e4e8ec"/>
  <rect x="856" y="420" width="8" height="200" rx="4" fill="#38a5ff"/>
  <text x="888" y="464" font-family="Segoe UI, Arial, sans-serif" font-size="18" font-weight="600" fill="#0c1c41">Orden de impresi&#243;n</text>
  <text x="888" y="496" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#5a6a7a">Selecci&#243;n por edificio</text>
  <text x="888" y="518" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#5a6a7a">y preview antes de imprimir.</text>
  <rect x="888" y="554" width="150" height="36" rx="8" fill="#10385e"/>
  <text x="963" y="577" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="13" fill="#fff">Abrir</text>
  {note}
</svg>""")
