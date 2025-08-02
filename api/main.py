from fastapi import FastAPI, Request
from scanner.nmap_wrapper import run_nmap_scan
from ai_module.analyzer import analyze_services

app = FastAPI()

@app.post("/scan")
async def scan_endpoint(request: Request):
    body = await request.json()
    target = body.get("target")

    try:
        xml_output = run_nmap_scan(target)
        analysis = analyze_services(xml_output)
        return {"target": target, "analysis": analysis}
    except Exception as e:
        return {"error": str(e)}
