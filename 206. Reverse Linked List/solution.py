def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # Initialize prev as None
        curr = head  # Start with curr at the head of the list

        while curr:
            temp = curr.next  # Store the next node
            curr.next = prev  # Reverse the pointer
            prev = curr       # Move prev forward
            curr = temp      # Move curr forward

        return prev  # prev is the new head of the reversed list