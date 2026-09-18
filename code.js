addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  const url = new URL(request.url);
  const key = url.searchParams.get("key") || "FREE";
  const query = url.searchParams.get("query");

  const expiryDate = new Date("2026-09-20");
  const todayDate = new Date();

  // Expiry Check
  if (todayDate > expiryDate) {
    return new Response(JSON.stringify({
      "developer": "@codderpetro",
      "expiry": "2026-09-20",
      "query": query || "",
      "result": "API expired, contact admin @codderpetro"
    }), {
      headers: { "Content-Type": "application/json" },
      status: 200
    });
  }

  if (!query) {
    return new Response(JSON.stringify({
      "developer": "@codderpetro",
      "expiry": "2026-09-20",
      "query": "",
      "result": "No data found"
    }), {
      headers: { "Content-Type": "application/json" },
      status: 200
    });
  }

  const backendKey = (key === "FREE") ? "osintbyabhigyan" : key;
  const targetUrl = `https://paid.originalapis.workers.dev/leak?key=${backendKey}&query=${query}`;

  const headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://paid.originalapis.workers.dev/"
  };

  try {
    const response = await fetch(targetUrl, {
      method: "GET",
      headers: headers
    });

    if (!response.ok) {
      return new Response(JSON.stringify({
        "developer": "@codderpetro",
        "expiry": "2026-09-20",
        "query": query,
        "result": "No data found"
      }), {
        headers: { "Content-Type": "application/json" },
        status: 200
      });
    }

    const backendData = await response.json();

    const finalResponse = {
      "developer": "@codderpetro",
      "expiry": "2026-09-20",
      "query": query,
      "result": backendData
    };

    return new Response(JSON.stringify(finalResponse), {
      headers: { "Content-Type": "application/json" },
      status: 200
    });

  } catch (err) {
    return new Response(JSON.stringify({
      "developer": "@codderpetro",
      "expiry": "2026-09-20",
      "query": query,
      "result": "No data found"
    }), {
      headers: { "Content-Type": "application/json" },
      status: 200
    });
  }
}
