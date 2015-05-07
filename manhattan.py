from math import sqrt

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0,
"Norah Jones": 4.5, "Phoenix": 5.0,
"Slightly Stoopid": 1.5,
"The Strokes": 2.5, "Vampire Weekend": 2.0},
"Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5,
"Deadmau5": 4.0, "Phoenix": 2.0,
"Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
"Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0,
"Deadmau5": 1.0, "Norah Jones": 3.0,
"Phoenix": 5, "Slightly Stoopid": 1.0},
"Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0,
"Deadmau5": 4.5, "Phoenix": 3.0,
"Slightly Stoopid": 4.5, "The Strokes": 4.0,
"Vampire Weekend": 2.0},
"Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0,
"Norah Jones": 4.0, "The Strokes": 4.0,
"Vampire Weekend": 1.0},
"Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0,
"Phoenix": 5.0, "Slightly Stoopid": 4.5,
"The Strokes": 4.0, "Vampire Weekend": 4.0},
"Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0,
"Norah Jones": 3.0, "Phoenix": 5.0,
"Slightly Stoopid": 4.0, "The Strokes": 5.0},
"Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0,
"Phoenix": 4.0, "Slightly Stoopid": 2.5,
"The Strokes": 3.0}}

def manhattan(rating1, rating2):
	"""Compute manhattan distance"""

	distance = 0
	for key in rating1:
		if key in rating2:
			distance += abs(rating1[key]-rating2[key])
	return distance

def computeNearestNeighbor(username, users):
	"""create sorted list based on their distance on username"""
	distances = []
	for user in users:
		if user != username:
			# distance = manhattan(users[user], users[username])
			distance = minkowskiDistance(users[user], users[username], 2.)
			distances.append((distance, user))

	#sort based on closest
	distances.sort()
	return distances

def recommend(username, users):
	#find nearest
	nearest = computeNearestNeighbor(username,users)[0][1];
	recommendations = []
	#find bands neighbor
	neighborRatings = users[nearest]
	userRatings = users[username]
	for artist in neighborRatings:
		if not artist in userRatings:
			recommendations.append((artist, neighborRatings[artist]))
	#sorting
	return sorted(recommendations, key=lambda artistTuple:artistTuple[1], reverse = True)

def euclideanDistance(rating1, rating2):
	distance = 0
	for key in rating1:
		if key in rating2:
			distance += abs(rating1[key]-rating2[key])**2
	return math.sqrt(distance)
	
def minkowskiDistance(user1, user2, r):
	distance = 0
	commonRating = False
	for key in user1:
		if key in user2:
			distance += pow(abs(user1[key]-user2[key]),r)
			commonRating = True
	if commonRating:
		return pow(distance, 1/r)
	else:
		return 0

# pearson
def pearsonDistance(user1, user2):
	distance = 0
	sum_xy = 0
	sum_user1 = 0
	sum_user2 = 0
	sum_user1_sq = 0
	sum_user2_sq = 0
	sum1 = 0
	sum2 = 0
	counter = 0
	for key in user1:
		if key in user2:
			sum_xy += user1[key]*user2[key]
			sum_user1 += user1[key]
			sum_user2 += user2[key]
			sum_user1_sq += user1[key]**2
			sum_user2_sq += user2[key]**2
			counter = counter+1
	sum1 = sum_user1_sq-(sum_user1**2)/counter
	sum2 = sum_user2_sq-(sum_user2**2)/counter
	return (sum_xy-(sum_user1*sum_user2)/counter)/((sqrt(sum1))*(sqrt(sum2)))

def cosineSimilarity(user1, user2):
	sum_x = 0
	sum_y = 0
	bawah = 0
	atas = 0
	for key in user1:
		sum_x += user1[key]**2
	for key in user2:
		sum_y += user2[key]**2
	for key in user1:
		if key in user2:
			atas += user1[key]*user2[key]
	bawah = sqrt(sum_x)*sqrt(sum_y)
	return atas/bawah

# print(manhattan(users["Hailey"],users["Jordyn"]))
# print(computeNearestNeighbor("Hailey",users))
# print(recommend("Sam",users))
# print(euclideanDistance(users["Angelica"], users["Bill"]))
# print(minkowskiDistance(users["Angelica"],users["Bill"],2.))
# print(pearsonDistance(users["Angelica"],users["Jordyn"]))
print(cosineSimilarity(users["Angelica"],users["Veronica"]))