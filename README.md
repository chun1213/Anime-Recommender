<h1 align="center"> Anime Recommendation Engine </h1>

Sometimes after watching a good show or movie, you will want to get recommendations for what you want next, this is a very common feature on most streaming services. However, since anime cannot often be found all on one service, most people will decide there next anime based on word of mouth or what they see online. The closest thing that tries to encompass all anime is myanimelist, which has a page for almost every anime ever created alongside ratings. Think of it as the imdb of anime. Myanimelist (MAL) also has a feature which allows users to keep records of all their watched anime in one place alongside their rating. Even with this information about the user, I found that MAL does not give meaningfull suggestions for new anime to the user based on their list. Seeing this, I decided to work on a recommendation engine using MAL data.


<h1> Recommendation Engine Use: </h1>

You can simply follow along the train_bert notebook included in this repo to use or train the engine. This works on Google colab aswell if your PC does not have enough RAM or a CUDA device.

<b> You will also need to download the dataset I pickeled in order to use the engine, here is a google drive link:  </b>
https://drive.google.com/drive/folders/1moBHlNl0zJYJZw5OhGqyd2-hbZxa1vz0?usp=sharing

<h1> Tech Used: </h1>
This project uses this version of BERT4REC to train the Engine along with some modifications: https://github.com/FeiSun/BERT4Rec
All the libraries used in this engine are also requirements of the BERT4REC. 

<h1> Data </h1>

The dataset I pickeled above came from this: https://www.kaggle.com/azathoth42/myanimelist
This was one of the cleanest MAl datasets I could find at the time so I used this. I then converted it to a valid file for BERT4REC to process using convert.py in this repo.
The pickleing is done inside BERT4REC

<h1> Testing </h1>
The trained model will output 10 anime to the user based on the inputed anime.
 
<b> First Test: </b>
The first set of anime I input involved slice of life, drama heavy teen anime such as: <br />
  - Your lie in April <br />
  - Your Name <br />
  - A Silent Voice <br />
<img src="https://github.com/chun1213/Anime-Recommender/blob/main/images/Screenshot_1.png" width="300" />
Based on the tags of the recommended Anime, It recommended a lot of similar anime such as: <br /> 
  - The Pet Girl of Sakurasou: https://myanimelist.net/anime/13759 <br />
  - Orange: https://myanimelist.net/anime/32729 <br />
  - The Garden of Words: https://myanimelist.net/anime/16782 <br />
  - When Marnie Was There: https://myanimelist.net/anime/21557 <br />
<br />
It also recommended some general popular teen anime such as: <br />
  - Re zero: https://myanimelist.net/anime/31240 <br />
  - One punch man: https://myanimelist.net/anime/30276 <br />
  - Tokyo Ghoul: https://myanimelist.net/anime/22319 <br />
<br />
<b> Second Test: </b>
The second set of anime I input involved action, adventure and fantasy: <br />
  - Tokyo Ghoul (22319) <br />
  - Re Zero (31240) <br />
  - Konosuba (30831) <br />
  - No Game No Life (19815) <br />
<img src="https://github.com/chun1213/Anime-Recommender/blob/main/images/Screenshot_2.png" width="300" />
This time, the engine impressively recommended a direct sequel, (Konosuba Season 2): <br />
  - KonoSuba: God's Blessing on This Wonderful World! 2: https://myanimelist.net/anime/32937 <br />
<br />
Based on the tags of the recommended Anime, It also recommended a lot of similar anime such as: <br />
  - The Devil is a Part-Timer!: https://myanimelist.net/anime/15809 <br />
  - One Punch Man: https://myanimelist.net/anime/30276 <br />
  - Sword Art Online II: https://myanimelist.net/anime/21881 <br />
  - Akame ga Kill!: https://myanimelist.net/anime/22199 <br />
  - Kill la Kill: https://myanimelist.net/anime/18679 <br />
  - Noragami: https://myanimelist.net/anime/20507 <br />
  - Guilty Crown: https://myanimelist.net/anime/10793 <br />
<br />
It also recommended some general popular teen anime such as: <br />
  Your Lie in April: https://myanimelist.net/anime/23273 <br />
  
<h1> Limitations </h1>

With the project explained, I need to get to the limitations of the engine. The main issue is that the dataset I used is dated and does not actually include ratings for many popular anime these days. It also strangely does not include user ratings for some older anime aswell. For example, the dataset does not have any ratings for Sword Art Online 1 but does have ratings for Sword Art Online 2. For this reason, if the user inputs an unreconized anime into the predictions, the engine will simply ignore the users request. In addition, the Engine will also never recommend an anime not in this dataset. The engine would have to be trained on a much larger and more recent dataset for this to work.
<br />
<br />
The second main issue right now is the inability to easily enter in anime to be predicted on, The user must manually go to MAL and find the ID for the anime before feeding it into the engine. If I could write a program to take a user's anime list from MAL and use that as input, it would be much more convenient.
