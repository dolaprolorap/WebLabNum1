import httpx

from config import PORT

    
def send(HOST: str):
    
    try:
        # req = httpx.get(f"http://{HOST}:{PORT}")
        req = httpx.post(f"http://{HOST}:{PORT}", data={"data1": 123, "data2": "gigigigigiigig"})

        if req.status_code == 200:
            return {"status": "success", "detail": "change success"}
        
        return {"status": "fail", "detail": req.json()}
    
    except:

        return {"status": "fail", "detail": "incorrect host"}