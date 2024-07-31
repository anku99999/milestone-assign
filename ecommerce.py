class Order:
    def __init__(self, order_id, product, quantity):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.is_processed = False

    def process_order(self):
        if self.product.stock >= self.quantity:
            self.product.update_stock(-self.quantity)
            self.is_processed = True
            return True
        return False

    def __str__(self):
        return f"Order(id={self.order_id}, product={self.product.name}, quantity={self.quantity}, processed={self.is_processed})"

def create_order(order_list, order):
    if order.process_order():
        order_list.append(order)
        return True
    return False


