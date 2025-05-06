import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()
    
    def compute_hash(self):
        content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(content.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.tampered_index = None
    
    def create_genesis_block(self):
        return Block(0, str(datetime.datetime.now()), "Genesis Block", "0")
    
    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), str(datetime.datetime.now()), data, previous_block.hash)
        self.chain.append(new_block)
    
    def edit_block(self, index, new_data):
        if index < len(self.chain) and index != 0:
            # Store the tampered index
            self.tampered_index = index
            # Update the data
            self.chain[index].data = new_data
            # Recalculate the hash of the edited block
            self.chain[index].hash = self.chain[index].compute_hash()
    
    def get_invalid_blocks(self):
        invalid_indices = []
        
        if self.tampered_index is not None:
            # Mark all blocks from the tampered block onwards as invalid
            for i in range(self.tampered_index, len(self.chain)):
                invalid_indices.append(i)
        
        return invalid_indices