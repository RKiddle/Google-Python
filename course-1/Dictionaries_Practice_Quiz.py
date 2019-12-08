#1

def email_list(domains):
	emails = []
	for keys in domains:
	  for values in domains[keys]:
		  emails.append(values+'@'+keys)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
#2

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for groups in group_dictionary:
		# Now go through the users in the group
		for users in group_dictionary[groups]:
		  user_groups.update({users:groups})
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))


