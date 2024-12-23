import unittest
from classes import LRUCache

class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(2)

    def test_get_updates_order(self):
        """Test if get operation properly updates access order and preserves the node in map"""
        self.cache.add(1)
        self.cache.add(2)
        self.assertTrue(self.cache.get(1))  # Access 1, should move to most recent
        self.cache.add(3)  # Should evict 2, not 1
        # This will fail because get() creates new node without updating map
        self.assertTrue(self.cache.get(1))  # Will return False in current implementation
        self.assertFalse(self.cache.get(2))
        self.assertTrue(self.cache.get(3))

    def test_repeated_gets(self):
        """Test if multiple get operations maintain correct cache state"""
        self.cache.add(1)
        self.cache.add(2)
        self.assertTrue(self.cache.get(1))
        self.assertTrue(self.cache.get(1))  # Second get should work
        # Will fail because each get creates new node without updating map
        self.assertTrue(self.cache.get(1))  # Will return False in current implementation

    def test_get_before_eviction(self):
        """Test if frequently accessed items are protected from eviction"""
        self.cache.add(1)
        self.cache.add(2)
        for _ in range(3):  # Access 1 multiple times
            self.assertTrue(self.cache.get(1))
        self.cache.add(3)  # Should evict 2, not 1
        # Will fail because get doesn't properly update access order
        self.assertTrue(self.cache.get(1))
        self.assertFalse(self.cache.get(2))
        self.assertTrue(self.cache.get(3))

    def test_node_reuse(self):
        """Test if nodes are properly reused instead of recreated"""
        self.cache.add(1)
        self.cache.add(2)
        initial_node = self.cache.map[1]
        self.assertTrue(self.cache.get(1))
        # Will fail because get creates new node instead of reusing
        self.assertIs(self.cache.map[1], initial_node)

    def test_map_consistency(self):
        """Test if map stays consistent with node list after operations"""
        self.cache.add(1)
        self.cache.add(2)
        self.assertTrue(self.cache.get(1))
        # Will fail because get doesn't maintain map consistency
        self.assertEqual(len(self.cache.map), 2)
        self.assertIn(1, self.cache.map)
        self.assertIn(2, self.cache.map)

    def test_sequential_operations(self):
        """Test a sequence of mixed operations"""
        self.cache.add(1)
        self.cache.add(2)
        self.assertTrue(self.cache.get(1))
        self.cache.add(3)
        # These assertions will fail due to the get() implementation
        self.assertTrue(self.cache.get(1))
        self.assertFalse(self.cache.get(2))
        self.assertTrue(self.cache.get(3))

    def test_complex_sequence(self):
        """Test complex sequence of operations"""
        self.cache.add(1)  # Cache: [1]
        self.cache.add(2)  # Cache: [1, 2]
        self.assertTrue(self.cache.get(1))  # Cache: [2, 1]
        self.cache.add(3)  # Should evict 2, Cache: [1, 3]
        self.cache.add(4)  # Should evict 1, Cache: [3, 4]
        
        # Verify final state
        self.assertFalse(self.cache.get(1))  # 1 was evicted by add(4)
        self.assertFalse(self.cache.get(2))  # 2 was evicted by add(3)
        self.assertTrue(self.cache.get(3))   # 3 is still in cache
        self.assertTrue(self.cache.get(4))   # 4 is still in cache

if __name__ == '__main__':
    unittest.main()