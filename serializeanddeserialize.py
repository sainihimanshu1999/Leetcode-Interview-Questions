def sereialize(sel,root):
    def xoxo(node):
        if node:
            result.append(node.val)
            xoxo(node.left)
            xoxo(node.right)
        else:
            result.append('#')
        result = []
        xoxo(root)
        return ''.join(result)

def deserailize(self,data):
    def xoxo():
        val = next(values)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = xoxo()
        node.right = xoxo()
    values = iter(data.split())
    return xoxo()
