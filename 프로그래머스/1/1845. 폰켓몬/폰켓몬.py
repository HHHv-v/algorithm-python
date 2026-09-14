def solution(nums):
    answer = 0
    pokemon_number=len(nums)//2
    pokemon_type=len(set(nums))
    
    answer=min(pokemon_number,pokemon_type)
    
    
    return answer