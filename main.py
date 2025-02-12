from src.get_img import imgArr
from const import *
import time

from src.MemAlgorithms.best_fit import bestFit
from src.MemAlgorithms.first_fit import firstFit

if __name__ == '__main__':
  
  # Main Loop to get to every Image
  tic = time.perf_counter()
  for i in range(1, 1168):
    file_name = f'imagesData/kirmizi {i}.jpg'
    arr = imgArr(file_name)
    val = firstFit(arr, memory_blocks)
  toc = time.perf_counter()
  print(f'First fit completion: {toc - tic:0.4f} seconds')

  tic = time.perf_counter()
  for i in range(1, 1168):
    file_name = f'imagesData/kirmizi {i}.jpg'
    arr = imgArr(file_name)
    val = bestFit(arr, memory_blocks)
  toc = time.perf_counter()
  print(f'Best fit completion: {toc - tic:0.4f} seconds')

