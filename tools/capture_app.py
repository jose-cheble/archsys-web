from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path(r"d:\Projects\Arch\archsys-web\public\assets\screenshots")
BASE = "http://127.0.0.1:4200"
USER = "laura-fernandez"
PASS = "ArchDemo2026!"


def login(page):
    page.goto(f"{BASE}/login", wait_until="networkidle")
    page.fill('input[name="USUARIO_USERNAME"]', USER)
    page.fill('input[name="USUARIO_PASS"]', PASS)
    page.click("button.btn-login")
    page.wait_for_url("**/home**", timeout=25000)
    page.wait_for_timeout(1800)


def shot(page, name, wait_ms=800):
    page.wait_for_timeout(wait_ms)
    dest = OUT / name
    page.screenshot(path=str(dest), full_page=False)
    print("saved", dest, dest.stat().st_size)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        desktop = browser.new_page(viewport={"width": 1440, "height": 900})
        login(desktop)

        desktop.goto(f"{BASE}/estadisticas/mensuales", wait_until="networkidle")
        desktop.wait_for_timeout(3500)
        shot(desktop, "reportes.png", 800)

        desktop.goto(f"{BASE}/acciones-masivas", wait_until="networkidle")
        desktop.wait_for_selector("text=Carga masiva", timeout=20000)
        shot(desktop, "acciones-masivas.png", 800)

        desktop.goto(f"{BASE}/monitoreos/rutas", wait_until="networkidle")
        desktop.wait_for_selector("text=Carlos Rodriguez", timeout=20000)
        desktop.click("text=Carlos Rodriguez")
        desktop.click("button.btn-buscar-ruta")
        desktop.wait_for_selector(".inspeccion-item, .mensaje-sin-inspecciones", timeout=25000)
        desktop.wait_for_timeout(4000)
        shot(desktop, "monitoreo.png", 800)
        desktop.close()

        context = browser.new_context(
            viewport={"width": 390, "height": 844},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
            is_mobile=True,
            has_touch=True,
        )
        mobile = context.new_page()
        login(mobile)
        mobile.goto(f"{BASE}/equipo-detalles/71", wait_until="networkidle")
        mobile.wait_for_timeout(1500)
        info = mobile.get_by_role("tab", name="Info")
        if info.count():
            info.click()
        else:
            mobile.click("text=Info")
        mobile.wait_for_selector("img[alt='qr-equipo']", timeout=15000)
        shot(mobile, "equipos.png", 800)

        mobile.goto(f"{BASE}/home", wait_until="networkidle")
        mobile.wait_for_selector(".camera-fab", timeout=15000)
        mobile.click(".camera-fab")
        mobile.wait_for_selector(".qr-scanner-overlay", timeout=10000)
        shot(mobile, "qr-movil.png", 600)

        context.close()
        browser.close()


if __name__ == "__main__":
    main()
