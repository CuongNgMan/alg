### POST ORDER USING SINGLE STACK

def post_traversal(root):
    L = []
    R = []
    curr = root
    while curr != None or any(L):
        if curr:
            L.append(curr)
            curr = curr.left
        else:
            peekRight = L[len(L) - 1].right
            if peekRight == None:
                out = L.pop()
                R.append(out.data)
                while any(L) and out == L[len(L) - 1].right:
                    out = L.pop()
                    R.append(out.data)
            else:
                curr = peekRight
    return R                