class Twitter:
    # followerId follows followeeId.
    # getNewsFeed(followerId) -> 10
    # tweets from followerId or followeeId
    def __init__(self):
        self.posts = defaultdict(list)
        self.followers = defaultdict(set)
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        heap = [(time, tweet_id) for time, tweet_id in self.posts[userId]]
        tweet_ids = []

        for followerId in self.followers[userId]:
            for time, tweet_id in self.posts[followerId]:
                heap.append((time, tweet_id))
        
        heapq.heapify(heap)

        while heap and len(tweet_ids) < 10:
            _, tweet_id = heapq.heappop(heap)
            tweet_ids.append(tweet_id)
        
        return tweet_ids

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
