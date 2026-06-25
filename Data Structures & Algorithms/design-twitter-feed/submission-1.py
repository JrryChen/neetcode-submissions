import heapq

class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set) # user : followed users
        self.tweets = defaultdict(list) # user : their tweets
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follow_map[userId].add(userId)
        self.tweets[userId].append((self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for follow in self.follow_map[userId]:
            followee_tweets = self.tweets[follow]
            for time, t in followee_tweets:
                heapq.heappush(heap, (time, t))
                if len(heap) > 10:
                    heapq.heappop(heap)
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followerId)
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.follow_map[followerId].discard(followeeId)

    def Twitter(self):
        self.__init__()