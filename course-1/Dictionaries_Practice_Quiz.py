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
  for group in group_dictionary:
		# Now go through the users in the group
    users = group_dictionary[group]
    print(1, users)
    for usr in users:
      print(3,user_groups)
      if usr not in user_groups:
        if usr!='usr':
          user_groups.update({usr :[]})
          print (5, user_groups )
      
      user_grp = user_groups[usr]
      user_grp.append(group)
      user_groups.update(usr = user_grp)
      #print(user_groups)
 			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary
  user_groups.pop('usr')
  return(user_groups)

print(7,groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

