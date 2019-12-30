password = facebook_hash(input_password)
if password == hash_facebook:
   print('Login successful.')
else:
   print('Login failed. Incorrect password.')
