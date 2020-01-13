def solution(H):
    block_cnt = 0     
    stack = []
     
    for height in H:
        while len(stack) != 0 and stack[-1] > height:
            stack.pop()
         
        if len(stack) != 0 and stack[-1] == height:
            pass
        else:
            block_cnt += 1
            stack.append(height)
             
    return block_cnt

if __name__ == '__main__':
    print(solution([8,8,5,7,9,8,7,4,8]))