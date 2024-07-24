class Election:
    def __init__(self, candidates):
        self.candidates = {name: 0 for name in candidates}

    def vote(self, name):
        if name in self.candidates:
            self.candidates[name] += 1
            return True
        return False

    def print_winner(self):
        max_votes = max(self.candidates.values())
        winners = [name for name, votes in self.candidates.items() if votes == max_votes]
        
        for winner in winners:
            print(winner)
    
    def get_results(self):
        return dict(sorted(self.candidates.items(), key=lambda x: x[1], reverse=True))


if __name__ == "__main__":

    election = Election(["Alice", "Bob", "Charlie"])


    votes = ["Alice", "Bob", "Charlie", "Alice", "Bob", "Alice", "David"]

    for vote in votes:
        if election.vote(vote):
            print(f"Vote for {vote} recorded successfully.")
        else:
            print(f"Invalid vote for {vote}.")

    print("\nVoting Results:")
    results = election.get_results()
    for candidate, votes in results.items():
        print(f"{candidate}: {votes}")

    print("\nWinner(s):")
    election.print_winner()