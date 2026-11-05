class Node:

  def __init__(self, key: int, val: int):
    self.key = key
    self.val = val
    self.prev = None
    self.next = None


class LRUCache:

  def __init__(self, capacity: int):
    self.cap = capacity
    self.cache = {}  # key -> Node

    # Sentinel nodes for head (LRU) and tail (MRU)
    self.head, self.tail = Node(0, 0), Node(0, 0)
    self.head.next = self.tail
    self.tail.prev = self.head

  def _remove(self, node: Node) -> None:
    """Remove an existing node from the linked list."""
    prev, nxt = node.prev, node.next
    prev.next = nxt
    nxt.prev = prev

  def _add(self, node: Node) -> None:
    """Insert a node right before the tail (Most Recently Used)."""
    prev = self.tail.prev
    prev.next = node
    node.prev = prev
    node.next = self.tail
    self.tail.prev = node

  def get(self, key: int) -> int:
    if key in self.cache:
      node = self.cache[key]
      self._remove(node)
      self._add(node)
      return node.val
    return -1

  def put(self, key: int, value: int) -> None:
    if key in self.cache:
      self._remove(self.cache[key])

    new_node = Node(key, value)
    self.cache[key] = new_node
    self._add(new_node)

    if len(self.cache) > self.cap:
      # Evict the Least Recently Used node (right after head)
      lru = self.head.next
      self._remove(lru)
      del self.cache[lru.key]