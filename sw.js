/* Retired 21 Nov 2026: midascfo.com is now the Midas AI CFO site (mining moved to /vaults).
   This worker deletes every old cache, unregisters itself and reloads open tabs so nobody sees a stale page. */
self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", (e) => {
  e.waitUntil((async () => {
    for (const k of await caches.keys()) await caches.delete(k);
    await self.registration.unregister();
    for (const c of await self.clients.matchAll({ type: "window" })) c.navigate(c.url);
  })());
});
self.addEventListener("fetch", () => {});
