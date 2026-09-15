# 💼 Crazy Tax Tools (Pro Tax & GST Suite)

> An all-in-one Indian Tax, GST, and Accounting computation workstation. Built for Chartered Accountants, Tax Practitioners, Small Business Owners, and Salaried Individuals.

![Crazy Tax Tools](https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&w=1200&q=80)

---

## 🌟 Key Features

### 💰 1. Income Tax Calculator (Old vs New Regime)
- **FY 2025-26 & FY 2026-27 Slabs**: Complete side-by-side comparison.
- **Deductions**: Automatically factors in standard deduction (₹75,000 New / ₹50,000 Old), Section 80C (up to ₹1,50,000), Section 80D (Health insurance), Section 24(b) (Home loan interest up to ₹2,00,000), and HRA.
- **Section 87A Rebate**: Full rebate on taxable income up to ₹7,00,000 with marginal relief calculations.
- **Automatic Recommendation**: Instantly shows whether Old or New Regime saves more tax and highlights exact savings.

### 🏷️ 2. GST Calculator & Tax Splitter
- **Modes**: Both GST Exclusive (Tax added to base) and GST Inclusive (Tax extracted from gross).
- **Slabs**: 0%, 5%, 12%, 18%, 28%, and customizable rates.
- **Supply Breakdown**: Intra-State (CGST 50% + SGST 50%) and Inter-State (IGST 100%).
- **Quick Copy**: One-click copy of the complete calculation summary for WhatsApp or email.

### ⚖️ 3. GST ITC vs Liability Reconciler (Rule 88A)
- Reconciles GSTR-3B Outward Tax Liability against GSTR-2B Available Input Tax Credit.
- Implements statutory set-off hierarchy:
  1. IGST credit utilized first against IGST, then CGST/SGST.
  2. CGST credit utilized against CGST then IGST (never SGST).
  3. SGST credit utilized against SGST then IGST (never CGST).
- Displays exact **Net Cash Payable (Challan PMT-06)** and **ITC Balance Carried Forward**.

### ⏱️ 4. GST Interest (Sec 50) & Late Fee Engine
- Calculates **Section 50(1) interest @ 18% per annum** strictly on net cash liability.
- Automatically calculates daily late fees for Normal (₹50/day) vs Nil returns (₹20/day) with statutory turnover caps (₹2,000 / ₹5,000 / ₹10,000).

### 📋 5. TDS / TCS Master Rate Directory
- Instant, live-searchable database of all key Indian TDS/TCS sections:
  - `194C` (Contractors)
  - `194J` (Technical & Professional)
  - `194I` (Rent on Plant & Land)
  - `194H` (Commission)
  - `194Q` & `206C(1H)` (Purchase & Sale of Goods)
  - `194A` (Interest)
  - Higher rate under Section 206AA without PAN.

### 🧾 6. GST Compliant Tax Invoice Generator
- Full Tax Invoice builder with Supplier details, Buyer details, GSTIN, and State codes.
- Dynamic line items with HSN/SAC code, quantity, rate, and GST rate.
- **Print / PDF Ready**: Styled for clean A4 printing without headers or menus.

### 📈 7. Reports, History & Offline Scratchpad
- Stores all session calculations in your browser's private storage.
- Export history to CSV at any time.
- Integrated tax planning notes scratchpad with automatic saving.

---

## 🚀 How to Run Locally

### Method 1: Instant Zero-Install (Recommended)
Because **Crazy Tax Tools** is designed with standard web technologies:
1. Open the project folder:
   ```
   C:\Users\MOJB-D085-Shashidhar\.gemini\antigravity\scratch\Crazy-Tax-Tools
   ```
2. Simply double-click **`index.html`** in File Explorer! It will immediately open in Google Chrome, Microsoft Edge, or Firefox with 100% functionality.

### Method 2: Run with Python Flask
If you have Python installed:
```bash
pip install -r requirements.txt
python app.py
```
Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🌐 How to Publish for FREE on GitHub Pages (Step-by-Step)

You can host this entire site for **100% free forever** on GitHub Pages under your account:
`https://shashikl7022.github.io/Crazy-Tax-Tools/`

### Step 1: Upload Files to GitHub
1. Open your repository on GitHub: [https://github.com/shashikl7022/Crazy-Tax-Tools](https://github.com/shashikl7022/Crazy-Tax-Tools)
2. Click **Add file** &rarr; **Upload files**.
3. Drag and drop the contents of this folder (`index.html`, `app.py`, `requirements.txt`, `Procfile`, `README.md`, `templates`, and `static`).
4. Click **Commit changes**.

### Step 2: Enable GitHub Pages
1. Go to **Settings** (top tab of your repository).
2. On the left sidebar, click **Pages**.
3. Under **Build and deployment** &rarr; **Branch**:
   - Select **`main`** branch and folder **`/ (root)`**.
4. Click **Save**.
5. Wait ~30-60 seconds, and refresh the page.
6. Your website will be live at:
   👉 **`https://shashikl7022.github.io/Crazy-Tax-Tools/`**

---

## 📁 Repository Structure

```
Crazy-Tax-Tools/
├── index.html              # Standalone web app for 100% Free GitHub Pages
├── app.py                  # Python Flask server with all specified routes
├── requirements.txt        # Flask & gunicorn dependencies
├── Procfile                # Heroku/Render deployment configuration
├── README.md               # Documentation & usage guide
├── templates/
│   ├── base.html           # Master layout
│   ├── dashboard.html      # Overview & compliance calendar
│   ├── tax_tools.html      # All tax & GST calculation engines
│   ├── documents.html      # GST Invoice builder & print module
│   ├── reports.html        # Calculation history & notes scratchpad
│   └── settings.html       # Preferences & theme setup
└── static/
    ├── css/
    │   └── style.css       # FinTech dark/light design & print stylesheets
    └── js/
        └── app.js          # Tax calculation engines & local storage
```

---

## 📄 License
MIT License. Free to use, adapt, and distribute for all accounting and tax professionals.
