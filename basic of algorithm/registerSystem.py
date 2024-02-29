class CashRegisterSystem:
    def __init__(self):
        self.registers = [[], []]
        self.open_registers = [True, True]
        self.interleaved_queue = []

    # Serve the next customer waiting in line for register register_id.
    # Should return the name of the customer.
    def serve_customer(self, register_id: int) -> str:
        if self.open_registers[register_id]:
            if not self.registers[register_id] and self.interleaved_queue:
                self.registers[register_id].append(self.interleaved_queue.pop(0))
            if self.registers[register_id]:
                return self.registers[register_id].pop(0)
        else:
            if self.interleaved_queue:
                return self.interleaved_queue.pop(0)
        
    # Add a new customer with name customer_name
    # waiting in line for register_id.
    def add_customer(self, register_id: int, customer_name: str):
        if self.open_registers[register_id]:
            self.registers[register_id].append(customer_name)
        else:
            self.interleaved_queue.append(customer_name)

    # Close register register_id.
    def close_register(self, register_id: int):
        self.open_registers[register_id] = False

    # Reopen register register_id.
    def reopen_register(self, register_id: int):
        self.open_registers[register_id] = True
        if self.interleaved_queue:
            self.registers[register_id].append(self.interleaved_queue.pop(0))


system = CashRegisterSystem()
system.add_customer(0, "Carmen")
system.add_customer(1, "Alice")
system.add_customer(0, "Bob")
system.add_customer(0, "Daniel")
print(system.serve_customer(0))  # Output: Carmen
system.close_register(1)
print(system.serve_customer(0))  # Output: Bob
system.reopen_register(1)
print(system.serve_customer(0))  # Output: Daniel


 