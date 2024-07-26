###### Define Classes and Functions ######
class Flashcard:
    def __init__(self, front, back):
        self.front = front
        self.back = back

    # Print the front and back of the flashcard
    def print(self):
        print("Front: " + self.front + "\n" + "Back: " + self.back)
    
    def GetFront(self):
        return self.front
    
    def GetBack(self):
        return self.back
    
class Flashcards:
    def __init__(self):
        self.flashcard_list = []
        # Start list index w/the current index equal to 0.
        self.curr_idx = 0
    
    # Incomplete constructor idea
    # def Flashcards(self, flashcard_list):
        # self.flashcard_list = flashcard_list

    # Print the entire flashcard list
    def print(self):
        print_idx = 1
        for flashcard in self.flashcard_list:
            print(f"Flashcard #{print_idx}" + "\n" + "Front: " + flashcard.GetFront() + "\n" + "Back: " + flashcard.GetBack())
            print_idx = print_idx + 1

    # Increment the curr idx by 1 or, if at the curr_idx is equal to the index of the last element in flashcard_list set the curr_idx equal to 0
    def Next(self):
        #if the array is empty, throw a runtime error
        if (len(self.flashcard_list) == 0):
            raise RuntimeError("No Flashcards")
        else:
            if (len(self.flashcard_list) - 1 == self.curr_idx):
                self.curr_idx = 0
            else:
                self.curr_idx += 1
    
    # Add a new flashcard to the end of the list
    def AddFlashcard(self, front, back):
        new_flashcard = Flashcard(front, back)
        self.flashcard_list.append(new_flashcard)
    
    def GetFlashCardList(self):
        return self.flashcard_list

    def GetCurrFlashCard(self):
        return self.flashcard_list[self.curr_idx]


# test_flashcards = Flashcards()
# test_flashcards.AddFlashcard("Hello", "World")
# test_flashcards.AddFlashcard("Goodbye", "World")
# test_flashcards.print()

###### Driver Function ######
def main():
    initial_user_input = input("Type \"start\" to start flashcard program, Type \"exit\" or anything else to exit flashcard program: ")
    if initial_user_input == "start":
        print("\n" + "Type in what should go on the front of the flashcard, then type what should go on the back of the flashcard." + "\n" + "When all flashcards you desire are added, type \"exit\" to begin displaying flashcards." + "\n")
        flashcards = Flashcards()
        add_flashcard_user_input = ""
        front_bool = True
        front = ""
        back = ""
        while (add_flashcard_user_input != "exit"):
            if front_bool == True:
                add_flashcard_user_input = input()
                front = add_flashcard_user_input
                front_bool = False
            elif front_bool == False:
                add_flashcard_user_input = input()
                back = add_flashcard_user_input
                flashcards.AddFlashcard(front, back)
                print("\n" + "Flashcard added." + "\n")
                front_bool = True
        print("Type \"flip\" to flip over the flashcard you are currently on. Type \"next\" to move on to the next flashcard. Type \"stop\" or anything else to stop the program." + "\n")
        curr_flashcard = flashcards.GetCurrFlashCard()
        flip_bool = False
        print("Front: " + curr_flashcard.GetFront() + "\n")
        main_user_input = input()
        while (main_user_input == "flip" or main_user_input == "next"):
            if (main_user_input == "flip"):
                if flip_bool == False:
                    print("Back: " + curr_flashcard.GetBack() + "\n")
                    flip_bool = True
                else:
                    print("Front: " + curr_flashcard.GetFront() + "\n")
                    flip_bool = False
                main_user_input = input()
            else:
                flashcards.Next()
                curr_flashcard = flashcards.GetCurrFlashCard()
                flip_bool = False
                print("Front: " + curr_flashcard.GetFront() + "\n")
                main_user_input = input()
                
        return
    else:
        print("Goodbye.")
        return

main()