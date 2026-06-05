import pandas as pd
import numpy as np
def prepare_data(df):
    df_clean = df.copy()

    if 'startYear' in df_clean.columns:
        df_clean['startYear'] = pd.to_numeric(df_clean['startYear'], errors='coerce')
        df_clean.loc[(df_clean['startYear'] < 1895) | (df_clean['startYear'] > 2024), 'startYear'] = np.nan
        
    if 'runtimeMinutes' in df_clean.columns:
        df_clean['runtimeMinutes'] = df_clean['runtimeMinutes'].astype(str).str.extract(r'(\d+)')[0]
        df_clean['runtimeMinutes'] = pd.to_numeric(df_clean['runtimeMinutes'], errors='coerce')
        df_clean.loc[(df_clean['runtimeMinutes'] < 60) | (df_clean['runtimeMinutes'] > 300), 'runtimeMinutes'] = np.nan

    cols_to_remove_immediately = ['budget', 'tconst', 'numVotes', 'BoxOffice', 'plot', 'Country']
    df_clean = df_clean.drop(columns=cols_to_remove_immediately, errors='ignore')
    
    if 'averageRating' in df_clean.columns:
        df_clean = df_clean.dropna(subset=['averageRating'])
        
    df_clean = df_clean.drop_duplicates()
    
    if 'startYear' in df_clean.columns:
        df_clean['movie_age'] = 2026 - df_clean['startYear']
        
    if 'primaryTitle' in df_clean.columns:
        df_clean['title_length'] = df_clean['primaryTitle'].astype(str).apply(len)
        
    if 'genres' in df_clean.columns:
        df_clean['genre_count'] = df_clean['genres'].astype(str).apply(lambda x: len(x.split(',')) if x != '\\N' and x != 'nan' else 0)
        
        genres_lower = df_clean['genres'].astype(str).str.lower()
        
        df_clean['is_drama'] = genres_lower.apply(lambda x: 1 if 'drama' in x else 0)
        df_clean['is_documentary'] = genres_lower.apply(lambda x: 1 if 'documentary' in x else 0)
        df_clean['is_comedy'] = genres_lower.apply(lambda x: 1 if 'comedy' in x else 0)
        df_clean['is_action'] = genres_lower.apply(lambda x: 1 if 'action' in x else 0)
        df_clean['is_thriller'] = genres_lower.apply(lambda x: 1 if 'thriller' in x else 0)
        df_clean['is_horror'] = genres_lower.apply(lambda x: 1 if 'horror' in x else 0)
        df_clean['is_romance'] = genres_lower.apply(lambda x: 1 if 'romance' in x else 0)
        df_clean['is_crime'] = genres_lower.apply(lambda x: 1 if 'crime' in x else 0)

    if 'Language' in df_clean.columns or 'language' in df_clean.columns:
        lang_col = 'language' if 'language' in df_clean.columns else 'Language'
        lang_lower = df_clean[lang_col].astype(str).str.lower()
        df_clean['is_english'] = lang_lower.apply(lambda x: 1 if 'english' in x else 0)

    cols_to_drop = ['primaryTitle', 'genres', 'startYear', 'runtime_year_interaction', 'Language', 'language']
    df_clean = df_clean.drop(columns=cols_to_drop, errors='ignore')
    
    df_clean = df_clean.select_dtypes(exclude=['object', 'category'])
    
    return df_clean