import joblib
import re

# Load trained ML model
model = joblib.load("models/ticket_classifier.pkl")


# --------------------------------------------------
# CATEGORY PREDICTION
# --------------------------------------------------

def predict_category(text):

    if not text or not text.strip():
        return "Unknown"

    text = text.lower().strip()

    # Account Access
    account_patterns = [
        r"\blog\s*in\b",
        r"\blogin\b",
        r"\bsign\s*in\b",
        r"\bsignin\b",
        r"\bpassword\b",
        r"\busername\b",
        r"\baccount access\b",
        r"\baccount locked\b",
        r"\bforgot.*password\b",
        r"\binvalid credentials\b",
        r"\bunable to access.*account\b",
        r"\bcannot access.*account\b"
    ]

    if any(re.search(pattern, text) for pattern in account_patterns):
        return "Account Access"


    # Refund Request
    refund_patterns = [
        r"\brefund\b",
        r"\breturn.*product\b",
        r"\breturn.*item\b",
        r"\bmoney back\b",
        r"\breimburse\b",
        r"\bwant.*refund\b",
        r"\bneed.*refund\b",
        r"\brequest.*refund\b"
    ]

    if any(re.search(pattern, text) for pattern in refund_patterns):
        return "Refund Request"


    # Billing
    billing_patterns = [
        r"\bcharged\b",
        r"\bcharge\b",
        r"\bpayment\b",
        r"\bbilling\b",
        r"\binvoice\b",
        r"\bsubscription payment\b",
        r"\bpaid\b",
        r"\bdeducted.*bank\b",
        r"\bpayment.*deducted\b",
        r"\bcharged twice\b",
        r"\bdouble charged\b",
        r"\btransaction\b"
    ]

    if any(re.search(pattern, text) for pattern in billing_patterns):
        return "Billing"


    # Technical Issue
    technical_patterns = [
        r"\berror\b",
        r"\bcrash\b",
        r"\bcrashed\b",
        r"\bcrashing\b",
        r"\bbug\b",
        r"\bsoftware.*crash",
        r"\bsoftware.*error",
        r"\bapplication.*crash",
        r"\bapplication.*error",
        r"\bapp.*crash",
        r"\bapp.*error",
        r"\bnot working\b",
        r"\bdoesn't work\b",
        r"\bdoes not work\b",
        r"\bfailed\b",
        r"\bfailure\b",
        r"\bnetwork\b",
        r"\bwifi\b",
        r"\bwi-fi\b"
    ]

    if any(re.search(pattern, text) for pattern in technical_patterns):
        return "Technical Issue"


    # Product Support
    product_patterns = [
        r"\bsetup\b",
        r"\bset up\b",
        r"\binstall\b",
        r"\binstallation\b",
        r"\bprinter\b",
        r"\bcompatib",
        r"\bhow do i\b",
        r"\bhow can i\b",
        r"\bconfigure\b",
        r"\bconfiguration\b",
        r"\bconnect.*device\b",
        r"\bbattery\b",
        r"\bproduct support\b"
    ]

    if any(re.search(pattern, text) for pattern in product_patterns):
        return "Product Support"


    # ML fallback for unknown cases
    return model.predict([text])[0]


# --------------------------------------------------
# URGENCY PREDICTION
# --------------------------------------------------

def predict_urgency(text):

    if not text or not text.strip():
        return "Low"

    text = text.lower().strip()

    # HIGH PRIORITY
    high_keywords = [
        "urgent",
        "immediately",
        "asap",
        "critical",
        "crash",
        "crashed",
        "crashing",          # added
        "failed",
        "failure",
        "error",
        "not working",
        "doesn't work",
        "does not work",
        "unable",
        "cannot",
        "can't",
        "charged twice",
        "double charged",
        "payment deducted",
        "deducted from my bank",
        "order not confirmed",
        "account locked"
    ]

    for word in high_keywords:
        if word in text:
            return "High"

    # MEDIUM PRIORITY
    medium_keywords = [
        "issue",
        "problem",
        "slow",
        "delay",
        "damaged",
        "defective",
        "refund",
        "return"
    ]

    for word in medium_keywords:
        if word in text:
            return "Medium"

    # LOW PRIORITY
    return "Low"