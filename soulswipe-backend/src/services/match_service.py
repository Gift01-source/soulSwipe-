class MatchService:
    def __init__(self, user_data):
        self.user_data = user_data

    def find_matches(self, user_id):
        # Logic to find matches for the user based on compatibility
        matches = []
        user = self.user_data.get(user_id)
        for potential_match in self.user_data.values():
            if potential_match['id'] != user_id and self.calculate_compatibility(user, potential_match) > 0.7:
                matches.append(potential_match)
        return matches

    def calculate_compatibility(self, user1, user2):
        # Simple compatibility calculation based on shared interests
        shared_interests = set(user1['interests']).intersection(set(user2['interests']))
        compatibility_score = len(shared_interests) / max(len(user1['interests']), len(user2['interests']))
        return compatibility_score