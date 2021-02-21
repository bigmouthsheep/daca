class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            cur = trie
            for ch in word:
                if not ch in cur:
                    cur[ch] = {}
                cur = cur[ch]
            cur['leaf'] = word
        print (trie)
        res = []
        
        def search(board, i, j, curDic):
            
            if 'leaf' in curDic:
                word = curDic['leaf']
                del curDic['leaf']
                res.append(word)
            
            if i >= 0 and i < len(board) and j >= 0 and j < len(board[i]) and  board[i][j] in curDic:
                ch = board[i][j]
                board[i][j] = '*'
                for ni, nj in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                    search(board, ni, nj, curDic[ch])
                board[i][j] = ch
            return 

    
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in trie:
                    search(board, i, j, trie)
        return res
