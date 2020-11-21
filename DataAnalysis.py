import pandas as pd
import matplotlib.pyplot as plt
import sqlite3


conn = sqlite3.connect("PoliticalPartyWebScraper.db")

# Read all democracy related words from the database
afd_query_demo = pd.read_sql_query("""
        SELECT word, page_title 
        FROM democracy_words_from_afd
        """, conn)
cdu_query_demo = pd.read_sql_query("""
        SELECT word, page_title 
        FROM democracy_words_from_cdu
        """, conn)
spd_query_demo = pd.read_sql_query("""
        SELECT word, page_title 
        FROM democracy_words_from_spd
        """, conn)

afd_query_demo_specific = pd.read_sql_query("""
        SELECT word, page_title 
        FROM democracy_words_from_afd
        WHERE word LIKE '%emokr%'
        """, conn)
cdu_query_demo_specific = pd.read_sql_query("""
        SELECT word, page_title 
        FROM democracy_words_from_cdu
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

# Read all immigration-related words from the database
afd_query_immigration = pd.read_sql_query("""
        SELECT word, page_title
        FROM immigration_words_from_afd
        """, conn)

# democracy-related words as dataframes
df_afd_demo = pd.DataFrame(afd_query_demo, columns=['word'])
df_cdu_demo = pd.DataFrame(cdu_query_demo, columns=['word'])
df_spd_demo = pd.DataFrame(spd_query_demo, columns=['word'])

# democracy-related words that have 'democracy' as the root as dataframes
df_afd_demo_specific = pd.DataFrame(afd_query_demo_specific, columns=['word'])
df_cdu_demo_specific = pd.DataFrame(cdu_query_demo_specific, columns=['word'])

# populism-related words as dataframes
df_afd_pop = pd.DataFrame(afd_query_pop, columns=['word'])
df_cdu_pop = pd.DataFrame(cdu_query_pop, columns=['word'])
df_spd_pop = pd.DataFrame(spd_query_pop, columns=['word'])

# immigration-related words as a dataframe
df_afd_immigration = pd.DataFrame(afd_query_immigration, columns=['word'])


plt.figure(figsize=(8, 4))

# Graph for comparison of all key words
'''labels_all = ['AfD Democracy', 'AfD Populism', 'CDU Democracy', 'CDU Populism', 'SPD Democracy', 'SPD Populism']
values_all = [len(df_afd_demo), len(df_afd_pop), len(df_cdu_demo), len(df_cdu_pop), len(df_spd_demo), len(df_spd_pop)]
plt.bar(labels_all, values_all, color='#10009e', label='All words', zorder=2)

labels_demo_specific = ['AfD Democracy', 'CDU Democracy']
values_demo_specific = [len(df_afd_demo_specific), len(df_cdu_demo_specific)]
plt.bar(labels_demo_specific, values_demo_specific, color='#00cf41', label='Demokratie/isch', zorder=2)

labels_immigration = ['AfD Populism', 'CDU Populism']
values_immigration = [len(df_afd_immigration), 0]
plt.bar(labels_immigration, values_immigration, color='#bd0000', label='Immigration words', zorder=2)'''

# Graph for democracy-related key words
'''labels_demo = ['AfD', 'CDU', 'SPD']
values_demo = [len(df_afd_demo), len(df_cdu_demo), len(df_spd_demo)]
plt.bar(labels_demo, values_demo, color='#10009e', label='Democracy words', zorder=2)'''

'''labels_demo_specific = ['AfD', 'CDU']
values_demo_specific = [len(df_afd_demo_specific), len(df_cdu_demo_specific)]
plt.bar(labels_demo_specific, values_demo_specific, color='#00cf41', label='Demokratie/isch', zorder=2)'''

# Graph for populism-related key words
labels_pop = ['AfD', 'CDU', 'SPD']
values_pop = [len(df_afd_pop), len(df_cdu_pop), len(df_spd_pop)]
plt.bar(labels_pop, values_pop, color='#8900c4', label='Populism words', zorder=2)

# Graph for immigration-related key words
labels_immigration = ['AfD', 'CDU', 'SPD']
values_immigration = [len(df_afd_immigration), 0, 0]
plt.bar(labels_immigration, values_immigration, color='#bd0000', label='Immigration words', zorder=2)


plt.yticks(range(len(df_afd_demo))[::3])
plt.grid(axis='y', color='black', linestyle='--', linewidth=0.5, zorder=1)
plt.xlabel('Political Parties', fontdict={'fontname': 'Arial', 'fontsize': 12})
plt.ylabel('Word Count', fontdict={'fontname': 'Arial', 'fontsize': 12})

'''plt.title("Occurrence of Key Words Related to Democracy Among German Political Parties",
          fontdict={'fontname': 'Arial', 'fontweight': 'bold', 'fontsize': 14})'''

'''plt.title("Occurrence of Key Words Related to Populism Among German Political Parties",
          fontdict={'fontname': 'Arial', 'fontweight': 'bold', 'fontsize': 14})'''

'''plt.title("Occurrence of Key Words Related to Immigration Among German Political Parties",
          fontdict={'fontname': 'Arial', 'fontweight': 'bold', 'fontsize': 14})'''

'''plt.title("Comparison of Democracy- and Populism-Related Key Words",
          fontdict={'fontname': 'Arial', 'fontweight': 'bold', 'fontsize': 14})'''

'''plt.title("Comparison of Democracy- and Immigration-Related Key Words",
          fontdict={'fontname': 'Arial', 'fontweight': 'bold', 'fontsize': 14})'''

plt.title("Comparison of Populism- and Immigration-Related Key Words",
          fontdict={'fontname': 'Arial', 'fontweight': 'bold', 'fontsize': 14})

plt.legend()
plt.show()

print("Democracy related words in AfD:", len(df_afd_demo), '\n')
print("Democracy related words in CDU:", len(df_cdu_demo), '\n')
print("Democracy related words in SPD:", len(df_spd_demo), '\n')

print("Democracy-specific related words in AfD:", len(df_afd_demo_specific), '\n')
print("Democracy-specific related words in CDU:", len(df_cdu_demo_specific), '\n')

print("Populism related words in AfD:", len(df_afd_pop), '\n')
print("Populism related words in CDU:", len(df_cdu_pop), '\n')
print("Populism related words in SPD:", len(df_spd_pop), '\n')

print("Immigration related words in AfD:", len(df_afd_immigration))

conn.close()
