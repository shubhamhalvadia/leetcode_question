def pairSum(self, head: Optional[ListNode]) -> int:
        # max_sum = 0
        # start, twin = head, head
        # while start:
        #     twin = start
        #     while twin.next:
        #         if twin.next.next:
        #             twin = twin.next
        #         else:
        #             b = twin.next.val
        #             twin.next = None
        #             break
        #     a = start.val
        #     start = start.next
        #     max_sum = max(a+b, max_sum)
        
        # return max_sum
        slow = head
        fast = head
        res = 0
        i = 0
        arr = []

        while fast:
            arr.append(slow.val)
            i += 1
            slow = slow.next
            fast = fast.next.next

        i -= 1
        while slow:
            res = max(res, arr[i] + slow.val)
            slow = slow.next
            i -= 1
        return res