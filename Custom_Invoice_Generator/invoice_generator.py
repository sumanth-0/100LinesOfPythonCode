import pdfkit

def create_invoice(service, hours, rate, client_name, invoice_number):
    total = hours * rate
    invoice_content = f"""
    Invoice Number: {invoice_number}
    Client Name: {client_name}
    Service: {service}
    Hours Worked: {hours}
    Rate per Hour: ${rate}
    Total Amount: ${total}

    Thank you for your business!
    """
    
    # Create PDF
    pdfkit.from_string(invoice_content, f'invoice_{invoice_number}.pdf')

def main():
    print("Welcome to the Customizable Invoice Generator!")
    
    client_name = input("Enter the client's name: ")
    service = input("Enter the service provided: ")
    hours = float(input("Enter the number of hours worked: "))
    rate = float(input("Enter the hourly rate: "))
    invoice_number = input("Enter the invoice number: ")
    
    create_invoice(service, hours, rate, client_name, invoice_number)
    print(f"Invoice for {client_name} has been created successfully!")

if __name__ == "__main__":
    main()
