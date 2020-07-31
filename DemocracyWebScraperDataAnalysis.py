import pandas as pd
import matplotlib.pyplot as plt
import sqlite3


conn = sqlite3.connect("PoliticalPartyWebScraper.db")

# Read all democracy related words from the database
afd_query_demo = pd.read_sql_query("""
        SELECT word, page_title 
        FROM words_from_afd
        """, conn)
cdu_query_demo = pd.read_sql_query("""
        SELECT word, page_title 
        FROM words_from_cdu
        """, conn)
spd_query_demo = pd.read_sql_query("""
        SELECT word, page_title 
        FROM words_from_spd
        """, conn)

afd_query_demo_word = pd.read_sql_query("""
        SELECT word, page_title 
        FROM words_from_afd
        WHERE word LIKE '%emokr%'
        """, conn)
cdu_query_demo_word = pd.read_sql_query("""
        SELECT word, page_title 
        FROM words_from_cdu
        WHERE word LIKE '%emokr%'
        """, conn)

# Read all populism related words from the database
afd_query_pop = pd.read_sql_query("""
        SELECT word, page_title 
        FROM populist_words_from_afd
        """, conn)
cdu_query_pop = pd.read_sql_query("""
        SELECT word, page_title 
        FROM populist_words_from_cdu
        """, conn)
spd_query_pop = pd.read_sql_query("""
        SELECT word, page_title 
        FROM populist_words_from_spd
        """, conn)


df_afd = pd.DataFrame(afd_query_demo, columns=['word'])
df_cdu = pd.DataFrame(cdu_query_demo, columns=['word'])
df_spd = pd.DataFrame(spd_query_demo, columns=['word'])

df_afd_demo = pd.DataFrame(afd_query_demo_word, columns=['word'])
df_cdu_demo = pd.DataFrame(cdu_query_demo_word, columns=['word'])

df_afd_pop = pd.DataFrame(afd_query_pop, columns=['word'])
df_cdu_pop = pd.DataFrame(cdu_query_pop, columns=['word'])
df_spd_pop = pd.DataFrame(spd_query_pop, columns=['word'])


plt.figure(figsize=(8, 4))

labels_words = ['AfD', 'CDU', 'SPD']
values_words = [len(df_afd), len(df_cdu), len(df_spd)]
plt.bar(labels_words, values_words, color='#10009e', label='All words', zorder=2)

labels_demo = ['AfD', 'CDU']
values_demo = [len(df_afd_demo), len(df_cdu_demo)]
plt.bar(labels_demo, values_demo, color='#00cf41', label='Demokratie/isch', zorder=2)

# Graph for populism-related key words
'''labels_pop = ['AfD', 'CDU', 'SPD']
values_pop = [len(df_afd_pop), len(df_cdu_pop), len(df_spd_pop)]
plt.bar(labels_pop, values_pop, color='#8900c4', label='All words', zorder=2)'''

plt.yticks(range(len(df_afd))[::3])
plt.grid(axis='y', color='black', linestyle='--', linewidth=0.5, zorder=1)
plt.xlabel('Political Parties', fontdict={'fontname': 'Arial', 'fontsize': 12})
plt.ylabel('Word Count', fontdict={'fontname': 'Arial', 'fontsize': 12})

plt.title("Occurrence of Key Words Related to Democracy Among German Political Parties",
          fontdict={'fontname': 'Arial', 'fontweight': 'bold', 'fontsize': 14})

plt.legend()
plt.show()

print("Democracy related words in AfD:", len(df_afd), '\n')
print("Democracy related words in CDU:", len(df_cdu), '\n')
print("Democracy related words in SPD:", len(df_spd), '\n')

print("Populism related words in AfD:", len(df_afd_pop), '\n')
print("Populism related words in CDU:", len(df_cdu_pop), '\n')
print("Populism related words in SPD:", len(df_spd_pop), '\n')

conn.close()
