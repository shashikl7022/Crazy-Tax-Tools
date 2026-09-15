const http = require("http");
const fs = require("fs");
const path = require("path");

const PORT = 3000;
const BASE_DIR = __dirname;

const MIME_TYPES = {
  ".html": "text/html",
  ".css": "text/css",
  ".js": "application/javascript",
  ".json": "application/json",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".svg": "image/svg+xml",
  ".ico": "image/x-icon",
};

const server = http.createServer((req, res) => {
  let reqUrl = req.url.split("?")[0];
  if (reqUrl === "/" || reqUrl === "/dashboard" || reqUrl === "/tax-tools" || reqUrl === "/documents" || reqUrl === "/reports" || reqUrl === "/settings") {
    reqUrl = "/index.html";
  }

  const filePath = path.join(BASE_DIR, reqUrl);
  const ext = path.extname(filePath).toLowerCase();
  const contentType = MIME_TYPES[ext] || "application/octet-stream";

  fs.readFile(filePath, (err, content) => {
    if (err) {
      if (err.code === "ENOENT") {
        // Fallback to index.html for SPA routes
        fs.readFile(path.join(BASE_DIR, "index.html"), (e, indexContent) => {
          if (e) {
            res.writeHead(404, { "Content-Type": "text/plain" });
            res.end("404 Not Found");
          } else {
            res.writeHead(200, { "Content-Type": "text/html" });
            res.end(indexContent, "utf-8");
          }
        });
      } else {
        res.writeHead(500);
        res.end("Server Error: " + err.code);
      }
    } else {
      res.writeHead(200, { "Content-Type": contentType });
      res.end(content, "utf-8");
    }
  });
});

server.listen(PORT, "0.0.0.0", () => {
  console.log(`Crazy Tax Tools Server running at http://localhost:${PORT}/`);
});
