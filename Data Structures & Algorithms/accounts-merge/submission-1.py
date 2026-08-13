class UnionFind:

    def __init__(self, nodes_len):
        self.nodes = [node for node in range(nodes_len)]
    
    def find(self, node):

        if self.nodes[node] == node:
            return node
        
        return self.find(self.nodes[node])
    
    def union(self, node1, node2):

        node1_root = self.find(node1)
        node2_root = self.find(node2)

        if node1_root == node2_root:
            return 

        self.nodes[node1_root] = node2_root

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:


        union_find = UnionFind(len(accounts))
        email_to_name = {}
        email_to_first_index = {}

        for account_index, account in enumerate(accounts):
            for email in account[1:]:

                if email in email_to_first_index:
                    union_find.union(account_index, email_to_first_index[email])
                else:
                    email_to_first_index[email] = account_index

                email_to_name[email] = account[0]
        
        root_to_email_group = defaultdict(list)
        for email, first_index in email_to_first_index.items():

            root = union_find.find(first_index)
            root_to_email_group[root].append(email)
        
        merged_accounts = []
        for _, emails in root_to_email_group.items():
            merged_accounts.append([email_to_name[emails[0]]] + sorted(emails))

        return merged_accounts
        





        """
        account = [] -> []

        [
            ["neet","neet@gmail.com", "bob@gmail.com", "neet_dsa@gmail.com"],
            ["alice","alice@gmail.com"],
            ["neet","neet@gmail.com"]
            ["neet","bob@gmail.com"]
        ]

        {neet@gmail.com: [0, 2], bob@gmail.com: [0, 3], alice@gmail.com: [1], neet_dsa@gmail.com: [0]}

        0<->2<->3 1
        {
            0: [2, 3],
            2: [0, 3],
            3: [0, 2],
            1: [],
        }

        def merge_account(i):

            seen.add(i)

            for account_details in accounts[i]:
                emails = account_details[1:]

                for email in emails:
                    current_group_emails.add(email)

            for connected_index in graph[i]:
                if connected_index in seen:
                    continue

                merge_account(connected_index)
            
        seen = set()
        merged_accounts = []
        for i in range(len(accounts)):
            if i in seen:
                continue

            current_group_emails = set()
            # {neet, bob}
            merge_account(i)
            actual_current_group = [accounts[i][0]]
            sorted_current_group_emails = sorted(current_group_emails)
            for email in sorted_current_group_emails:
                actual_current_group.append(email)
            
            merged_accounts.append(actual_current_group)


        
        return merged_accounts
        """

        # def merge_account(account_index):

        #     seen.add(account_index)

        #     for email in accounts[account_index][1:]:
        #         current_group_emails.add(email)

        #     for connected_index in graph[account_index]:
        #         if connected_index in seen:
        #             continue

        #         merge_account(connected_index)
        
        # def construct_graph():
        #     graph = defaultdict(set)

        #     """
        #     {neet@gmail.com: [0, 2], neet_dsa@gmail.com: [0], alice@gmail.com[1], bob@gmail.com: [2], neetcode@gmail.com: [3]}

        #     [0,1,2,3,4,5] -> {}

        #     n^2 * m
        #     """

        #     for _, indices in email_to_indices.items():

        #         for node1_index in range(len(indices)):
        #             for node2_index in range(node1_index+1, len(indices)):

        #                 node1 = indices[node1_index]
        #                 node2 = indices[node2_index]

        #                 graph[node1].add(node2)
        #                 graph[node2].add(node1)
            
        #     return graph
        
        # def get_email_indices_connections():

        #     email_to_indices = defaultdict(list)
        #     """
        #     {neet@gmail.com: [0, 2], neet_dsa@gmail.com: [0], alice@gmail.com[1], bob@gmail.com: [2], neetcode@gmail.com: [3]}

        #     graph = {
        #         0: {2},
        #         2: {0},
        #         1: {},
        #         3: {}

        #     }

        #     n * m
        #     """

        #     for account_index, account in enumerate(accounts):
        #         emails = account[1:]

        #         for email in emails:
        #             email_to_indices[email].append(account_index)
            
        #     return email_to_indices

        
        # """
        # [
        #     ["neet","neet@gmail.com","neet_dsa@gmail.com"],
        #     ["alice","alice@gmail.com"],
        #     ["neet","bob@gmail.com","neet@gmail.com"],
        #     ["neet","neetcode@gmail.com"]
        # ]

        # emails_to_indices = {neet@gmail.com: [0, 2], neet_dsa@gmail.com: [0], alice@gmail.com[1], bob@gmail.com: [2], neetcode@gmail.com: [3]}


        # """
        # email_to_indices = get_email_indices_connections()
        # graph = construct_graph()

        # seen = set()
        # merged_accounts = []
        # for account_index in range(len(accounts)):
        #     if account_index in seen:
        #         continue

        #     current_group_emails = set()
        #     # {neet, bob}
        #     merge_account(account_index)
        #     actual_current_group = [accounts[account_index][0]]
        #     sorted_current_group_emails = sorted(current_group_emails)
        #     for email in sorted_current_group_emails:
        #         actual_current_group.append(email)
            
        #     merged_accounts.append(actual_current_group)

        # return merged_accounts





        
