class RomanNumerals:
    VALORES_A_ROMANO = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
]
    
    ROMANO_A_VALORES = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

    def to_roman(self, n):
        result = ""
        for clave, valor in self.VALORES_A_ROMANO:
            while n >= clave:
                  result += valor
                  n -= clave
        return result

    def from_roman(self, s):
        total = 0
        for i in range (len(s)):
            numero = self.ROMANO_A_VALORES[s[i]]
            if i + 1 < len(s) and numero < self.ROMANO_A_VALORES[s[i + 1]]:
                total -= numero
            else:
                total += numero
        return total

# --- Prueba ---
convertidor = RomanConverter()
print(convertidor.to_roman(1))  # Debe imprimir MCMXC
print(convertidor.from_roman("MMVIII")) # Debe imprimir 2008
