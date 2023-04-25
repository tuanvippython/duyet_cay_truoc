# Định nghĩa lớp TreeNode
# Tạo hàm __init__ với 3 tham số value, left, right
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
#value là giá trị của nút
#left là cây con bên trái
#right là cây con bên phải
    #Tạo hàm duyệt trước
    def duyet_NLR(self, current_node=None):
        # Nếu không truyền tham số cho current_node thì nút hiện tại sẽ là nút của gốc cây
        if current_node == None:
            current_node = self

        result = []
        result.append(current_node.value)
        # Nếu nút hiện tại có giá trị bên trái thực hiện đệ quy phương thức "duyet_NLR" với nút bên trái
        # và thêm danh sách kết quả vào result
        if current_node.left is not None:
            left_result = self.duyet_NLR(current_node.left)
            result += left_result
        # Nếu nút hiện tại có giá trị bên phải thực hiện đệ quy phương thức "duyet_NLR" với nút bên phải
        # và thêm danh sách kết quả vào result
        if current_node.right is not None:
            right_result = self.duyet_NLR(current_node.right)
            result += right_result
        # Trả về result khi đã duyệt hết các giá trị trong cây
        return result
        
          

# Tạo một cây nhị phân đơn giản
#     1
#    / \
#   2   3
#  / \
# 4   5
node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)

# In kết quả của việc duyệt cây theo thứ tự NLR 
print(node.duyet_NLR())

# Kết quả hiển thị sẽ là: [1,2,4,5,3]

