def username_generator(first_name, last_name):
  user_name=""
  if len(first_name) >=3:
    user_name= first_name[:3]
  else:
    user_name= first_name
  if len(last_name) >=4:
    user_name += last_name[:4]
  else:
    user_name += last_name
  return user_name
print(username_generator("Azu","Lopez"))

username = username_generator("Azu","Lopez")
def password_generator(username):
  password=""
  for i in range(0,len(username)):
    password += username[i-1]
  return password

print(password_generator(username)) 

print(range(0,len(username)))





poem_title = "el árbol caído"
poem_author = "Inventado"

poem_title_fixed = poem_title.title()

print(poem_title + " " + poem_title_fixed)

poem_author_fixed = poem_author.upper()

print(poem_author + " " + poem_author_fixed)

favorite_song = 'AhorA'
favorite_song_lowercase = favorite_song.lower()
print(favorite_song_lowercase)


line_one = "Voy a separar todas las líneas"

line_one_words = line_one.split()
print(line_one_words)


azu_text = \
"""Primer línea
Esta es la sgunda línea
ahora va la tercer línea
y por último la cuarta."""

azu_lines = azu_text.split('\n')

print(azu_lines)

azu_line_one = ' '.join(azu_lines)
azu_space = '\n'.join(azu_lines)

print(azu_line_one)
print(azu_space)

azu_replace = azu_space.replace('cuarta', '4ta')

print(azu_replace)



def title_card(title, artist):
  return "The movie \"{}\" is written by {}.".format(title,artist)
print( title_card("Pinocho", "Walt Disney"))