from fastapi import FastAPI, Query
import httpx
from datetime import datetime

app = FastAPI()

total_api_counter = 0

@app.get("/leakinfo/api")
@app.get("/numinfo/api")
@app.get("/api/index")
async def num_info(
    key: str = Query("FREE", description="API Key"),
    query: str = Query(..., description="Query / Phone Number")
):
    global total_api_counter
    total_api_counter += 1

    expiry_date = datetime.strptime("2026-09-20", "%Y-%m-%d").date()
    today_date = datetime.now().date()

    if today_date > expiry_date:
        return {
            "developer": "@codderpetro",
            "expiry": "2026-09-20",
            "query": query,
            "result": "API expired, contact admin @codderpetro"
        }

    backend_key = "osintbyabhigyan" if key == "FREE" else key
    target_url = f"https://paid.originalapis.workers.dev/leak?key={backend_key}&query={query}"
    
    # Cloudflare block cheyyathirikkanulla full headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://paid.originalapis.workers.dev/",
        "Origin": "https://paid.originalapis.workers.dev"
    }

    try:
        # Timeout 30 seconds aakki kooti, redirect follow cheyyan set cheythu
        async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
            response = await client.get(target_url, headers=headers)
            
            # Status code 200 allaengil exact error kkaanikkan
            if response.status_code != 200:
                return {
                    "developer": "@codderpetro",
                    "expiry": "2026-09-20",
                    "query": query,
                    "result": f"Upstream Error Status: {response.status_code}",
                    "raw_text": response.text
                }
            
            try:
                backend_data = response.json()
            except Exception:
                backend_data = {"raw_response": response.text}

            if isinstance(backend_data, dict):
                backend_data["API_Developer"] = "@codderpetro"
                if "Today_Used" in backend_data:
                    backend_data["Today_Used"] = total_api_counter

            return {
                "developer": "@codderpetro",
                "expiry": "2026-09-20",
                "query": query,
                "result": backend_data
            }

    except httpx.TimeoutException:
        return {
            "developer": "@codderpetro",
            "expiry": "2026-09-20",
            "query": query,
            "result": "Timeout Error: Upstream API error"
        }
        
    except Exception as e:
        return {
            "developer": "@codderpetro",
            "expiry": "2026-09-20",
            "query": query,
            "result": f"Error: {str(e)}"
        }from fastapi import FastAPI, Query
import httpx
from datetime import datetime

app = FastAPI()

total_api_counter = 0

@app.get("/leakinfo/api")
@app.get("/numinfo/api")
@app.get("/api/index")
async def num_info(
    key: str = Query("FREE", description="API Key"),
    query: str = Query(..., description="Query / Phone Number")
):
    global total_api_counter
    total_api_counter += 1

    expiry_date = datetime.strptime("2026-09-20", "%Y-%m-%d").date()
    today_date = datetime.now().date()

    if today_date > expiry_date:
        return {
            "developer": "@codderpetro",
            "expiry": "2026-09-20",
            "query": query,
            "result": "API expired, contact admin @codderpetro"
        }

    backend_key = "osintbyabhigyan" if key == "FREE" else key
    target_url = f"https://paid.originalapis.workers.dev/leak?key={backend_key}&query={query}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://paid.originalapis.workers.dev/"
    }

    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.get(target_url, headers=headers)
            
            try:
                backend_data = response.json()
            except Exception:
                backend_data = {"raw_response": response.text}

            if isinstance(backend_data, dict):
                backend_data["API_Developer"] = "@codderpetro"
                if "Today_Used" in backend_data:
                    backend_data["Today_Used"] = total_api_counter

            return {
                "developer": "@codderpetro",
                "expiry": "2026-09-20",
                "query": query,
                "result": backend_data
            }

    except Exception as e:
        return {
            "developer": "@codderpetro",
            "expiry": "2026-09-20",
            "query": query,
            "result": "No data found"
        }
