# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
I liked the UI of the game. I thought the concept was very interesting. However, you can't find the bug just by looking at it, you had to play the game several times to find all the bugs. There were several things that were wierd so I noted all of them, incase they were errors.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
The game kept saying only to go Lower and never go Higher, even though my guess was lower than the secret number. Also after I won a game or after I lost the game by running out of attempts, when I clicked New game it didn't allow me to play again. Also I noticed that since the comparision of the numbers is using string comparision, everytime my guess was like a single digit number like "9" and the secret number was "80", it said to go lower even though you clearly need to go higher. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude Code.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
AI said that the string comparision of the user's input and the secret number was wrong, because it only compared the first char of the string. Hence if the secret number was 34 and the user's guess was 9 it would say to go lower. But that's incorrect because even though 9 is greater than 3, 34 is greater than 9. So it's actually supposed to say go higher. To make sure AI's fix suggestion was correct I went to the app and tested the inputs to see if it had an error.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
For one fix I had to fix the process of updating the number of attempts. However AI forgot that I asked it to not include invalid inputs such as out of range numbers as part of the attempt count. So from then on, I had to explicitly mention that attempts did NOT include invalid user inputs. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I ran the app and played the game several times in different modes to check whether that bug was still there. And if there was any other bugs accidentally caused by fixing this one.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
AI ran the test_game_logic.py test on the app.py code. It said it had passed all the test cases, and showed me what that exactly they meant. I thought the description was really helpful because I coud make sure that it passed all the test cases. 

- Did AI help you design or understand any tests? How?
AI helped me design some new pytest cases. These were targeted to test the bugs that I found and fixed. These bugs are not tested in the pytest test_game_logic.py. AI told me all my test cases have passed and showed me how. 
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
I'm not sure if I missed this error, but when I ran the app the secret number did not change every time I clicked submit. It only changed when I got the guess correct after I submitted. 

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Based on my understanding so far, I think the streamlit reruns helped to update the page and its information each time the submit button or any other button was clicked. And I think the session-states kept track of the all the different variables of each game such as the difficulty level, the points, the input range, etc. 

- What change did you make that finally gave the game a stable secret number?
Again, I don't know if i missed this error but after running the app over 30 times through this debugging process I never found any errors about the secret number changing. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I like that even though I was using AI to help me code, I double checked before it added its changes to my code. This made sure that regardless of the changes made to the code, I was still in control and oversaw what it was doing to my code.  And I also like that I learned how to do github commit messages, I've always been confused on that concept. And I'd like to continue these habits in my future projects or labs.

- What is one thing you would do differently next time you work with AI on a coding task?
I think next time I work with AI, I need to utilize it a lot more and make it involved in my brainstorming sessions while I come up with the logic. I also think that some of my prompts might have been too descriptive and unnecessary, so I want to change that as well. 

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project makes me trust AI a lot more, especially if you're prompting is very good. I've always thought that AI wouldn't be able to do much, but today that belief changed. I'm excited to use AI in my future with coding!