### Morris traversal ###


def in_traversal(root) -> list:
    L = []
    curr = root
    while curr!=None:
        if curr.left == None:
            L.append(curr.data)
            curr = curr.right
        else:
            pre = curr.left
            while pre.right != None and pre.right != curr:
                pre = pre.right
            if pre.right == None:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                L.append(curr.data)
                curr=curr.right