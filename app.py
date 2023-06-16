import streamlit as st

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def main():
    st.title("Kalkulator Sederhana")
    
    num1 = st.number_input("Masukkan angka pertama:")
    num2 = st.number_input("Masukkan angka kedua:")
    
    operation = st.selectbox("Pilih operasi:", ("Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"))
    
    result = None
    
    if operation == "Penjumlahan":
        result = add(num1, num2)
    elif operation == "Pengurangan":
        result = subtract(num1, num2)
    elif operation == "Perkalian":
        result = multiply(num1, num2)
    elif operation == "Pembagian":
        result = divide(num1, num2)
    
    st.write("Hasil:", result)

if __name__ == '__main__':
    main()
