from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

UNITS = [
    "zero","one","two","three","four","five","six","seven","eight","nine",
    "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen",
    "seventeen","eighteen","nineteen"
]
TENS = ["","", "twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
SCALES = ["", "thousand", "million", "billion", "trillion"]

# --- Level 2 helpers ---
def normalize_input(s: str) -> Decimal:
    try:
        s = s.replace(",", "").strip()
        return Decimal(s).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    except (InvalidOperation, AttributeError):
        raise ValueError("Invalid amount format.")

def validate(amount: Decimal,
             min_amt: Decimal = Decimal("0.00"),
             max_amt: Decimal = Decimal("999999999999.99")) -> None:
    if not (min_amt <= amount <= max_amt):
        raise ValueError(f"Amount out of supported range ({min_amt}–{max_amt}).")

def split_amount(amount: Decimal) -> tuple[int, int]:
    total_cents = int((amount * 100).to_integral_value(rounding=ROUND_HALF_UP))
    return total_cents // 100, total_cents % 100

def chunk_to_words(n: int, hyphenate: bool = True) -> str:
    """0..999"""
    parts = []
    hundreds, rem = divmod(n, 100)
    if hundreds:
        parts.append(f"{UNITS[hundreds]} hundred")
    if rem:
        if rem < 20:
            parts.append(UNITS[rem])
        else:
            t, u = divmod(rem, 10)
            joiner = "-" if (u and hyphenate) else (" " if u else "")
            parts.append(TENS[t] + (joiner + UNITS[u] if u else ""))
    return " ".join(parts)

def number_to_words(num: int, hyphenate: bool = True) -> str:
    if num == 0:
        return "zero"
    parts = []
    i = 0
    while num:
        num, chunk = divmod(num, 1000)
        if chunk:
            w = chunk_to_words(chunk, hyphenate)
            scale = SCALES[i]
            parts.append((w + (" " + scale if scale else "")).strip())
        i += 1
    return " ".join(reversed(parts))

def compose_phrase(dollars: int, cents: int, hyphenate: bool = True) -> str:
    dwords = number_to_words(dollars, hyphenate)
    cwords = number_to_words(cents, hyphenate) if cents else "zero"
    dsuf = "dollar" if dollars == 1 else "dollars"
    csuf = "cent" if cents == 1 else "cents"
    if cents > 0:
        return f"{dwords.capitalize()} {dsuf} and {cwords} {csuf}"
    else:
        return f"{dwords.capitalize()} {dsuf}"

# --- Level 1 orchestration ---
if __name__ == "__main__":
    user_input = input("Enter dollar amount: ")
    try:
        amt = normalize_input(user_input)
        validate(amt)
        dollars, cents = split_amount(amt)
        print(compose_phrase(dollars, cents))
    except ValueError as e:
        print("Error:", e)
