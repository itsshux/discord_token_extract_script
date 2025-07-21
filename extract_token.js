// paste this in devtools

(function () {
    let found = false;
    const interval = setInterval(() => {
      try {
        window.webpackChunkdiscord_app.push([
          [Math.random()], {},
          (req) => {
            for (const id in req.c) {
              const mod = req.c[id]?.exports;
              const tokenFn = mod?.default?.getToken;
              if (typeof tokenFn === 'function') {
                const token = tokenFn();
                if (typeof token === 'string' && token.length > 20 && !found) {
                  found = true;
                  console.log("token found:", token);
                  alert("token: " + token);
                  clearInterval(interval);
                }
              }
            }
          }
        ]);
      } catch {}
    }, 50);
  })();
  
