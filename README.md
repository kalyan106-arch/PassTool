# 🔐 PassTool

**PassTool** is a lightweight, interactive command-line utility that helps you:

- ✅ Generate strong and secure passwords  
- 🔍 Evaluate password strength  
- 🔒 Check if a password has been compromised in known data breaches (via the [Have I Been Pwned API](https://haveibeenpwned.com/))

---

## 📦 Features

- 🎲 Secure password generator (includes uppercase, lowercase, digits, symbols)  
- 📊 Password strength evaluation with visual feedback  
- 🚨 Password breach check using the k-Anonymity model  
- 🎨 Enhanced terminal visuals with `colorama` and `rich`  
- 🔐 Hidden password input using `stdiomask`  

---

## 🚀 Setup

### 1. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install required dependencies

```bash
pip install -r requirements.txt
```

---

## 🛠️ Usage

```bash
python project.py
```

You'll be presented with an interactive menu:

```
1. Generate a strong password
2. Check password strength
3. Check if password is compromised
4. Exit
```

Follow the prompts to generate or evaluate passwords securely.

---

## 📷 Example

```bash
Welcome to your personal password utility tool! 🔧

Choose an option:
1. Generate a strong password
2. Check password strength
3. Check if password is compromised
4. Exit

Enter your choice (1-4): 1
Password length: 12
Generated password: kD$9wA&2gLp#
```

---

## 🔐 Security

- Passwords are never stored or logged.  
- Passwords are checked securely via the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3#SearchingPwnedPasswords) using SHA-1 hash prefix (k-Anonymity), ensuring privacy during lookups.

---

## 👤 Author

**Kalyan Koushik**
