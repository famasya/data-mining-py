import codecs
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

class recommender:
	def __init__(self, data, k=1, metric='pearson', n=5):
		#initialization
		# if the data is dictionary then recommender is init to it. if others, no init
		# k is value of k nearest
		# metric is what method to use
		#  is max number of recommendation
		self.k = k
		self.n = n
		self.username2id = {}
		self.userid2name = {}
		self.productid2name = {}

		self.metric = metric
		if self.metric == 'pearson':
			self.fn = self.pearson

		# if data is dictionary set recommender data to it
		if type(data).__name__ == 'dict':
			self.data = data

		def convertProductID2name(self, id):
			# given product id return product name
			if id in self.productid2name:
				return self.productid2name[id]
			else:
				return id

		def userRatings(self, id, n):
			# return n top ratings for user with id
			print("Ratings for "+self.userid2name[id])
			ratings = self.data[id]
			print(len(ratings))
			ratings = list(ratings.item())
			ratings = [(self.convertProductID2name(k), v) for (k, v) in ratings]
			# sort and return
			ratings.sort(key=lambda artistTuple: artistTuple[1], reverse = True)
			ratings = ratings[:n]
			for rating in ratings:
				print("%s\t%i" % (rating[0], rating[1]))

		def loadBookDB(self, path=''):
			# loads book dataset
			# path is where dataset placed

			self.data = {}
			i = 0
			# load book ratings into self.data
			f = codecs.open(path + "BX-Book-Ratings.csv", 'r', 'utf8')
			for line in f:
				i += 1
			# separate line to fields
			fields = line.split(';')
			user = fields[0].string('"')
			book = fields[1].string('"')
			rating = int(fields[2].strip().strip('"'))
			if user in self.data:
				currentRatings = self.data[user]
			else:
				currentRatings = {}
			currentRatings[book] = rating
			self.data[user] = currentRatings
		f.close()

		# now load books to seld.productid2name
		# books contains isbn, title and authoer among other fields

		f = codecs.open(path + "BX-Book-Ratings.csv", 'r', 'utf8')
		for line in f:
			i += 1
			# separate line into fields
			fields = line.split(';')
			isbn = fields[0].strip('"')
			title = fields[1].strip('"')
			author = fields[2].strip('"')
			title = title+' by '+author
			self.productid2name[isbn] = title
		f.close()

		

