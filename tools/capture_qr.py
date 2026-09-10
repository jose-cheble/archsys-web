from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path(r"d:\Projects\Arch\archsys-web\public\assets\screenshots")
BASE = "http://127.0.0.1:4200"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(
        viewport={"width": 390, "height": 844},
        user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        is_mobile=True,
        has_touch=True,
        permissions=["camera"],
    )
    page = context.new_page()
    page.goto(f"{BASE}/login", wait_until="networkidle")
    page.fill('input[name="USUARIO_USERNAME"]', "laura-fernandez")
    page.fill('input[name="USUARIO_PASS"]', "ArchDemo2026!")
    page.click("button.btn-login")
    page.wait_for_url("**/home**", timeout=25000)
    page.wait_for_timeout(1500)
    page.click(".camera-fab")
    page.wait_for_timeout(1000)
    box = page.locator("button.ok-btn-msg-box")
    if box.count():
        box.click(force=True)
        page.wait_for_timeout(400)
    page.wait_for_selector(".qr-scanner-overlay", timeout=8000)
    dest = OUT / "qr-movil.png"
    page.screenshot(path=str(dest), full_page=False)
    print("saved", dest, dest.stat().st_size)
    browser.close()
