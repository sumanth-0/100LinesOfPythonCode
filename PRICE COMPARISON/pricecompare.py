class Store:
    def __init__(self, name):
        self.name = name
        self.prices = {}

    def add_price(self, item, price):
        self.prices[item] = price

    def get_price(self, item):
        return self.prices.get(item, float('inf'))

class PriceComparison:
    def __init__(self):
        self.stores = []

    def add_store(self, store):
        self.stores.append(store)

    def find_best_price(self, item):
        best_price = float('inf')
        best_store = None
        for store in self.stores:
            price = store.get_price(item)
            if price < best_price:
                best_price = price
                best_store = store.name
        return best_store, best_price

def main():
    # Create stores
    store1 = Store("Store A")
    store2 = Store("Store B")
    store3 = Store("Store C")

    # Add prices to stores
    store1.add_price("Bananas", 0.99)
    store1.add_price("Apples", 1.49)
    store2.add_price("Bananas", 0.89)
    store2.add_price("Apples", 1.59)
    store3.add_price("Bananas", 1.09)
    store3.add_price("Apples", 1.39)

    # Create price comparison object
    price_comparison = PriceComparison()
    price_comparison.add_store(store1)
    price_comparison.add_store(store2)
    price_comparison.add_store(store3)

    # Find best prices
    item = "Bananas"
    best_store, best_price = price_comparison.find_best_price(item)
    print(f"Best price for {item} is ${best_price} at {best_store}")

    item = "Apples"
    best_store, best_price = price_comparison.find_best_price(item)
    print(f"Best price for {item} is ${best_price} at {best_store}")

if __name__ == "__main__":
    main()