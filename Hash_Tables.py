"""
LeetCode 1: Two Sum
Enlace: https://leetcode.com/problems/two-sum/

Descripción:
Dado un arreglo de números enteros `nums` y un número entero `target`, 
devuelve los índices de los dos números de modo que sumen `target`.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash table para guardar {valor: indice}
        vistos = {}
        
        for i, num in enumerate(nums):
            complemento = target - num
            
            # Si el complemento ya está en la tabla, encontramos la solución
            if complemento in vistos:
                return [vistos[complemento], i]
            
            # Si no, agregamos el número actual a la tabla
            vistos[num] = i
            
        return []

# PRUEBA
if __name__ == "__main__":
    sol = Solution()
    print("Test Two Sum:")
    print(sol.twoSum(nums=[2, 7, 11, 15], target=9)) 
# Output esperado: [0, 1]