# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):

        bx = ax = xx = None
        ax_start = bx_start = xx_start = None
        while head != None:
          if head.val < x:
            if bx == None:
              bx_start = head
            else:
              bx.next = head
            bx = head
          elif head.val < x:
            if ax == None:
              ax_start = head
            else:
              ax.next = head
            ax = head
          else:
            if xx == None:
              xx_start = head
            else:
              xx.next = head
            xx = head
          head = head.next

        if bx_start != None:
          bx.next = xx_start
        if xx_start != None:
          xx.next = ax_start
        if ax_start != None:
          ax.next = None

        if bx_start != None:
          return bx_start
        if xx_start != None:
          return xx_start
        if ax_start != None:
          return ax_start
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
