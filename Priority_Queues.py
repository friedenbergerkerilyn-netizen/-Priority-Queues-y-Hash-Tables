"""
LeetCode 215: Kth Largest Element in an Array
Enlace: https://leetcode.com/problems/kth-largest-element-in-an-array/

Descripción:
Dado un arreglo de enteros `nums` y un entero `k`, devuelve el k-ésimo elemento más grande del arreglo.
Debe resolverse sin ordenar todo el arreglo.
"""

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            
            # Si el tamaño del heap supera 'k', eliminamos el elemento más pequeño.
            # De esta forma, el heap siempre guarda los 'k' elementos más grandes vistos hasta ahora.
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        # El elemento en la cima del min-heap es el k-ésimo más grande global
        return min_heap[0]

# PRUEBA
if __name__ == "__main__":
    sol = Solution()
    print("Test Kth Largest Element:")
    print(sol.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2)) 
 # Output esperado: 5