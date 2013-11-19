class PhoneContact(object):

	def __init__(self, first_name="", last_name="", phone_number=""):
		self.first_name = first_name
		self.last_name = last_name
		self.phone_number = phone_number

	def get_display_name(self):
		return self.first_name + " " + self.last_name

pc1 = PhoneContact("Paul", "Pham", "123-456-7890")
print(pc1.get_display_name())
print(pc1.first_name)
print(pc1.last_name)
print(pc1.phone_number)

pc2 = PhoneContact(first_name = "Flobot", last_name = "Flobotomy", phone_number = "111-222-3333")
pc3 = PhoneContact("Bender", "Rodriguez", "444-555-6666")

phone_contacts = {"Paul":pc1, "Flobot":pc2, "Bender":pc3}