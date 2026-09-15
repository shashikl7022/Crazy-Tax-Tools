const fs = require("fs");
const path = require("path");

const dir = "C:\\Users\\MOJB-D085-Shashidhar\\.gemini\\antigravity\\scratch\\Crazy-Tax-Tools";
let html = fs.readFileSync(path.join(dir, "index.html"), "utf8");
const css = fs.readFileSync(path.join(dir, "static", "css", "style.css"), "utf8");
const js = fs.readFileSync(path.join(dir, "static", "js", "app.js"), "utf8");

// Replace link rel="stylesheet" with inline style
html = html.replace(
  '<link rel="stylesheet" href="static/css/style.css">',
  `<link rel="stylesheet" href="static/css/style.css">\n  <style>\n${css}\n  </style>`
);

// Replace script src with inline script
html = html.replace(
  '<script src="static/js/app.js"></script>',
  `<script src="static/js/app.js"></script>\n  <script>\n${js}\n  </script>`
);

fs.writeFileSync(path.join(dir, "index.html"), html, "utf8");
console.log("Successfully bundled CSS & JS inline into index.html! New size:", html.length);
