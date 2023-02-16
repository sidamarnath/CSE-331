"""
Project 6
CSE 331 S21 (Onsay)
Your Name: Sidharth Amarnath
hashtable.py
"""


from typing import TypeVar, List, Tuple

T = TypeVar("T")
HashNode = TypeVar("HashNode")
HashTable = TypeVar("HashTable")


class HashNode:
    """
    DO NOT EDIT
    """
    __slots__ = ["key", "value", "deleted"]

    def __init__(self, key: str, value: T, deleted: bool = False) -> None:
        self.key = key
        self.value = value
        self.deleted = deleted

    def __str__(self) -> str:
        return f"HashNode({self.key}, {self.value})"

    __repr__ = __str__

    def __eq__(self, other: HashNode) -> bool:
        return self.key == other.key and self.value == other.value

    def __iadd__(self, other: T) -> None:
        self.value += other


class HashTable:
    """
    Hash Table Class
    """
    __slots__ = ['capacity', 'size', 'table', 'prime_index']

    primes = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
        181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
        281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
        397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
        503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
        743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
        863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
        997)

    def __init__(self, capacity: int = 8) -> None:
        """
        DO NOT EDIT
        Initializes hash table
        :param capacity: capacity of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

        i = 0
        while HashTable.primes[i] <= self.capacity:
            i += 1
        self.prime_index = i - 1

    def __eq__(self, other: HashTable) -> bool:
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __str__(self) -> str:
        """
        DO NOT EDIT
        Represents the table as a string
        :return: string representation of the hash table
        """
        represent = ""
        bin_no = 0
        for item in self.table:
            represent += "[" + str(bin_no) + "]: " + str(item) + '\n'
            bin_no += 1
        return represent

    __repr__ = __str__

    def _hash_1(self, key: str) -> int:
        """
        ---DO NOT EDIT---
        Converts a string x into a bin number for our hash table
        :param key: key to be hashed
        :return: bin number to insert hash item at in our table, None if key is an empty string
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)
        return hashed_value % self.capacity

    def _hash_2(self, key: str) -> int:
        """
        ---DO NOT EDIT---
        Converts a string x into a hash
        :param key: key to be hashed
        :return: a hashed value
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)

        prime = HashTable.primes[self.prime_index]

        hashed_value = prime - (hashed_value % prime)
        if hashed_value % 2 == 0:
            hashed_value += 1
        return hashed_value

###############################################################################
#                          Implement the following:                           #
###############################################################################

    def __len__(self) -> int:
        """
        Returns: int that is size of hash table
        """
        return self.size

    def __setitem__(self, key: str, value: T) -> None:
        """
        key: str: The key we are hashing
        value: T: The associated value we are storing
        Returns: None
        """
        self._insert(key, value)

    def __getitem__(self, key: str) -> T:
        """
        key: str: The key we are seraching for the associated value of
        Returns: The value with an associated Key
        """
        bucket = self._get(key)
        if bucket is None:
            raise KeyError
        return bucket.value

    def __delitem__(self, key: str) -> None:
        """
        key: str: The key we are deleting the associated value of
        Returns: None
        """
        bucket = self._get(key)
        if bucket is None:
            raise KeyError
        return self._delete(key)

    def __contains__(self, key: str) -> bool:
        """
        key: str: The key we are checking to be a part of the hash table
        Returns: Whether or not the key exists
        """
        bucket = self._get(key)
        if bucket is not None:
            return True
        return False

    def _hash(self, key: str, inserting: bool = False) -> int:
        """
        key: str: The key being used in our hash function
        inserting: bool: Whether or not we are doing an insertion. Important for the reasons described above.
        Returns: int that is the bin we hashed into
        """
        if self.table is None:
            return self._hash_1(key)
        for i in range(len(self.table)):
            result = (self._hash_1(key) + i * self._hash_2(key)) % self.capacity
            if self.table[result] is None or self.table[result].deleted and inserting:
                break
            if self.table[result].key == key:
                break
        return result

    def _insert(self, key: str, value: T) -> None:
        """
        key: str: The key associated with the value we are storing
        value: T: The associated value we are storing
        Returns: None
        """
        idx = self._hash(key)
        if self.table[idx] is None:
            self.size += 1
            self.table[idx] = HashNode(key, value)
        self.table[idx] = HashNode(key, value)
        self._grow()

    def _get(self, key: str) -> HashNode:
        """
        key: str: The key we looking up
        Returns: HashNode with the key we looked up
        """
        idx = self._hash(key)
        if self.table[idx] is None:
            return

        return self.table[idx]

    def _delete(self, key: str) -> None:
        """
        key: str: The key of the Node we are looking to delete
        Returns: None
        """
        idx = self._hash(key)
        if self.table[idx].key == key:
            self.table[idx] = HashNode(None, None, deleted=True)
            self.size -= 1

    def _grow(self) -> None:
        """
        Doubles the capacity of the existing hash table
        Returns: None
        """
        if self.size / self.capacity >= 0.5:
            self.capacity *= 2
            cpy_table = self.table
            self.table = self.capacity * [None]
            i = 0
            while HashTable.primes[i] <= self.capacity:
                i += 1
            self.prime_index = i - 1
            for item in cpy_table:
                if item is not None and item.key is not None:
                    idx = self._hash(item.key)
                    node = HashNode(item.key, item.value)
                    self.table[idx] = node

    def update(self, pairs: List[Tuple[str, T]] = []) -> None:
        """
        pairs: List[Tuple[str, T]]: list of tuples (key, value) being updated
        Returns: None
        """
        for key, value in pairs:
            self._insert(key, value)

    def keys(self) -> List[str]:
        """
        Makes a list that contains all of the keys in the table
        Returns: List of the keys
        """
        result = []
        for idx in self.table:
            if idx is not None:
                result.append(idx.key)
        return result

    def values(self) -> List[T]:
        """
        Makes a list that contains all of the values in the table
        Returns: List of the values
        """
        result = []
        for idx in self.table:
            if idx is not None:
                result.append(idx.value)
        return result

    def items(self) -> List[Tuple[str, T]]:
        """
        Makes a list that contains all of the key value pairs in the table
        Returns: List of Tuples of the form (key, value)
        """
        result = []
        for idx in self.table:
            if idx is not None:
                result.append((idx.key, idx.value))
        return result

    def clear(self) -> None:
        """
        Clears the table of HashNodes completely, in essence a reset of the table
        Returns: None
        """
        self.table = [None] * self.capacity
        self.size = 0


class ExecuteOnlyOnce:
    """
    Represents a request handler.
    """

    def __init__(self, max_time) -> None:
        """
        Design of data structure
        """
        pass

    def handle_request(self, time: int, request_id: str, client_id: str) -> int:
        """
        Return the number of times this request has been seen already
        """
        pass
