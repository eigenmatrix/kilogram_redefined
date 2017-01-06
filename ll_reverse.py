class ll:
	def __init__(self, data, next):
		self.data = data
		self.next = next

def reverse(node):
	p_old = None
	while True:
		p_next = node.next
		node.next = p_old
		if p_next == None:
			return node
		p_old = node
		node = p_next

node = None
for i in range(10):
	node = ll(i, node)
	print i
node_origin = node
while True:
	print node, node.data
	node = node.next
	if node == None:
		break

node = reverse(node_origin)
print
while True:
	print node, node.data
	node = node.next
	if node == None:
		break