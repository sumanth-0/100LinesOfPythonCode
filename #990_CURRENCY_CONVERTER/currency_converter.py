import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json

class CurrencyConverter:
    def __init__(self):
        self.rates = {}
        # Load some common currencies as fallback
        self.common_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF', 'CNY', 'INR']
        

    def update_rates(self, base_currency):
        try:
            # Frankfurter API - completely free, no API key needed
            url = f"https://api.frankfurter.app/latest?from={base_currency}"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                self.rates = data.get("rates", {})
                # Add the base currency with rate 1.0
                self.rates[base_currency] = 1.0
                return True
            else:
                return False
                
        except Exception as e:
            print(f"API Error: {e}")
            return False

    def convert(self, from_currency, to_currency, amount):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()
        
        # If we don't have rates for the requested base currency, try to update
        if from_currency not in self.rates or to_currency not in self.rates:
            if not self.update_rates(from_currency):
                raise ValueError(f"Cannot get exchange rates for {from_currency}")
        
        # If still not available after update, use fallback
        if to_currency not in self.rates:
            raise ValueError(f"Unsupported currency: {to_currency}")
            
        rate = self.rates[to_currency]
        return amount * rate

class CurrencyConverterApp(tk.Tk):
    def __init__(self, converter):
        super().__init__()
        self.title("Currency Converter")
        self.geometry("400x300")
        self.resizable(False, False)

        self.converter = converter
        # Use available currencies from rates, fallback to common currencies
        self.currencies = sorted(self.converter.rates.keys() if self.converter.rates else self.converter.common_currencies)

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Amount
        tk.Label(main_frame, text="Amount:").grid(row=0, column=0, sticky="w", pady=5)
        self.amount_entry = tk.Entry(main_frame, width=20, font=("Arial", 12))
        self.amount_entry.grid(row=0, column=1, pady=5, padx=10)
        self.amount_entry.insert(0, "1.00")

        # From Currency
        tk.Label(main_frame, text="From Currency:").grid(row=1, column=0, sticky="w", pady=5)
        self.from_currency = ttk.Combobox(main_frame, values=self.currencies, state="readonly", width=17)
        self.from_currency.grid(row=1, column=1, pady=5, padx=10)
        self.from_currency.set("USD")

        # To Currency
        tk.Label(main_frame, text="To Currency:").grid(row=2, column=0, sticky="w", pady=5)
        self.to_currency = ttk.Combobox(main_frame, values=self.currencies, state="readonly", width=17)
        self.to_currency.grid(row=2, column=1, pady=5, padx=10)
        self.to_currency.set("EUR")

        # Convert button
        self.convert_button = tk.Button(main_frame, text="Convert", command=self.convert_currency, 
                                      bg="#4CAF50", fg="white", font=("Arial", 12), width=15)
        self.convert_button.grid(row=3, column=0, columnspan=2, pady=20)

        # Result label
        self.result_label = tk.Label(main_frame, text="", font=("Arial", 14, "bold"), fg="#2196F3")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

        # Status label
        self.status_label = tk.Label(main_frame, text="Using Frankfurter API", font=("Arial", 8), fg="gray")
        self.status_label.grid(row=5, column=0, columnspan=2, pady=5)

    def convert_currency(self):
        try:
            amount_str = self.amount_entry.get().strip()
            if not amount_str:
                messagebox.showerror("Error", "Please enter an amount")
                return
                
            amount = float(amount_str)
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()

            if not from_curr or not to_curr:
                messagebox.showerror("Error", "Please select both currencies")
                return

            if from_curr == to_curr:
                self.result_label.config(text=f"{amount:.2f} {from_curr} = {amount:.2f} {to_curr}")
                return

            result = self.converter.convert(from_curr, to_curr, amount)
            self.result_label.config(text=f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}")
            
        except ValueError as e:
            if "could not convert string to float" in str(e).lower():
                messagebox.showerror("Error", "Please enter a valid number for amount")
            else:
                messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {e}")

if __name__ == "__main__":
    try:
        app = CurrencyConverterApp(CurrencyConverter())
        app.mainloop()
    except Exception as e:
        print(f"Failed to start application: {e}")
        input("Press Enter to close...")