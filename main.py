import tkinter as tk
import random
from gtts import gTTS
import os

class WordApp:
    def __init__(self, master):
        self.master = master
        master.title("Flashcards")
        master.geometry("700x700")  # Definindo a largura e altura da janela

        # Cores do tema
        self.background_color = "#0e1017"
        self.text_color = "#ffffff"
        self.button_color = "#3c40c6"

        master.config(bg=self.background_color)

        self.words = {
            "стараться": ("tentar", "стараться", "starat'sya"),
            "дом": ("casa", "дом", "dom"),
            "солнце": ("sol", "солнце", "solntse"),

            # Adicione mais palavras e suas traduções e pronúncias aqui
            
    "стараться": ("tentar", "стараться", "starat'sya"),
    "дом": ("casa", "дом", "dom"),
    "солнце": ("sol", "солнце", "solntse"),
    "быть": ("ser", "быть", "byt'"),
    "иметь": ("ter", "иметь", "imet'"),
    "делать": ("fazer", "делать", "delat'"),
    "говорить": ("falar", "говорить", "govorit'"),
    "идти": ("ir", "идти", "idti'"),
    "есть": ("comer", "есть", "est'"),
    "видеть": ("ver", "видеть", "videt'"),
    "ходить": ("andar", "ходить", "hodit'"),
    "понимать": ("entender", "понимать", "ponimat'"),
    "смотреть": ("assistir", "смотреть", "smotret'"),
    "любить": ("amar", "любить", "lyubit'"),
    "жить": ("viver", "жить", "zhit'"),
    "получать": ("receber", "получать", "poluchat'"),
    "работать": ("trabalhar", "работать", "rabotat'"),
    "спросить": ("perguntar", "спросить", "sprosit'"),
    "думать": ("pensar", "думать", "dumat'"),
    "сказать": ("dizer", "сказать", "skazat'"),
    "ответить": ("responder", "ответить", "otvetit'"),
    "стоять": ("ficar de pé", "стоять", "stoyat'"),
    "ждать": ("esperar", "ждать", "zhdut'"),
    "начинать": ("começar", "начинать", "nachat'"),
    "пойти": ("ir", "пойти", "poyti"),
    "брать": ("pegar", "брать", "brat'"),
    "сидеть": ("sentar", "сидеть", "sidet'"),
    "спать": ("dormir", "спать", "spat'"),
    "вести": ("conduzir", "вести", "vesti'"),
    "писать": ("escrever", "писать", "pisat'"),
    "включать": ("ligar", "включать", "vklyuchat'"),
    "выключать": ("desligar", "выключать", "vыключать"),
    "найти": ("encontrar", "найти", "nayti'"),
    "давать": ("dar", "давать", "davat'"),
    "принимать": ("aceitar", "принимать", "prinimat'"),
    "понять": ("compreender", "понять", "ponyat'"),
    "встречаться": ("encontrar-se", "встречаться", "vstrechat'sya"),
    "спрашивать": ("perguntar", "спрашивать", "sprashivat'"),
    "узнать": ("saber", "узнать", "uznat'"),
    "оставаться": ("permanecer", "оставаться", "ostavat'sya"),
    "остановиться": ("parar", "остановиться", "ostanovit'sya"),
    "показывать": ("mostrar", "показывать", "pokazyvat'"),
    "открывать": ("abrir", "открывать", "otkryvat'"),
    "знать": ("saber", "знать", "znat'"),
    "бежать": ("correr", "бежать", "bezhat'"),
    "делиться": ("compartilhar", "делиться", "delit'sya"),
    "ждать": ("esperar", "ждать", "zhdat'"),
    "встретить": ("encontrar", "встретить", "vstretit'"),
    "взять": ("pegar", "взять", "vzyat'"),
    "дать": ("dar", "дать", "dat'"),
    "пройти": ("passar", "пройти", "projti"),
    "подумать": ("pensar", "подумать", "podumat'"),
    "держать": ("segurar", "держать", "derzhat'"),
    "выходить": ("sair", "выходить", "vykhodit'"),
    "слушать": ("ouvir", "слушать", "slushat'"),
    "считать": ("contar", "считать", "schitat'"),
    "возвращаться": ("voltar", "возвращаться", "vozvrashchat'sya"),
    "закрывать": ("fechar", "закрывать", "zakryvat'"),
    "продолжать": ("continuar", "продолжать", "prodolzhat'"),
    "подходить": ("aproximar", "подходить", "podkhodit'"),
    "помнить": ("lembrar", "помнить", "pomnit'"),
    "видать": ("ver", "видать", "vidat'"),
    "спать": ("dormir", "спать", "spat'"),
    "готовить": ("cozinhar", "готовить", "gotovit'"),
    "просить": ("pedir", "просить", "prosit'"),
    "уходить": ("sair", "уходить", "ukhodit'"),
    "забывать": ("esquecer", "забывать", "zabyvat'"),
    "прийти": ("vir", "прийти", "priyti"),
    "встать": ("levantar-se", "встать", "vstat'"),
    "вести": ("levar", "вести", "vesti'"),
    "подниматься": ("levantar-se", "подниматься", "podnimat'sya"),
    "заниматься": ("envolver-se", "заниматься", "zanimat'sya"),
    "ездить": ("viajar", "ездить", "yezdit'"),
    "отвечать": ("responder", "отвечать", "otvechat'"),
    "обращаться": ("dirigir-se", "обращаться", "obrashchat'sya"),
    "вспоминать": ("lembrar", "вспоминать", "vspominat'"),
    "убивать": ("matar", "убивать", "ubivat'"),
    "верить": ("acreditar", "верить", "verit'"),
    "читать": ("ler", "читать", "chitat'"),
    "рассказывать": ("contar", "рассказывать", "rasskazyvat'"),
    "слышать": ("ouvir", "слышать", "slyshat'"),
    "стоить": ("valer", "стоить", "stoit'"),
    "забирать": ("pegar", "забирать", "zabirat'"),
    "садиться": ("sentar-se", "садиться", "sadit'sya"),
    "звонить": ("ligar", "звонить", "zvonit'"),
    "показать": ("mostrar", "показать", "pokazat'"),
    "попробовать": ("tentar", "попробовать", "poprobovat'"),
    "поддерживать": ("apoiar", "поддерживать", "podderzhat'"),
    "звать": ("chamar", "звать", "zvat'"),
    "следовать": ("seguir", "следовать", "sledovat'"),
    "спасать": ("salvar", "спасать", "spasat'"),
    "помогать": ("ajudar", "помогать", "pomogat'"),
    "смеяться": ("rir", "смеяться", "smeyat'sya"),
    "звучать": ("soar", "звучать", "zvuchat'"),
    "проходить": ("passar", "проходить", "prokhodit'"),
    "пытаться": ("tentar", "пытаться", "pytat'sya"),
    "занимать": ("ocupar", "занимать", "zanimat'"),
    "решать": ("resolver", "решать", "reshat'"),
    "действовать": ("agir", "действовать", "deystvovat'"),
    "поднимать": ("levantar", "поднимать", "podnimat'"),
    "производить": ("produzir", "производить", "proizvodit'"),
    "появляться": ("aparecer", "появляться", "poyavlyat'sya"),
    "возникать": ("surgir", "возникать", "voznikat'"),
    "произносить": ("pronunciar", "произносить", "proiznosit'"),
    "оказываться": ("acabar por ser", "оказываться", "okazyvat'sya"),
    "бегать": ("correr", "бегать", "begat'"),
    "обеспечивать": ("garantir", "обеспечивать", "obespechivat'"),
    "тратить": ("gastar", "тратить", "tratit'"),
    "увидеть": ("ver", "увидеть", "uvidet'"),
    "представлять": ("imaginar", "представлять", "predstavlyat'"),
    "бросать": ("largar", "бросать", "brosat'"),
    "замечать": ("notar", "замечать", "zamechat'"),
    "улыбаться": ("sorrir", "улыбаться", "ulybat'sya"),
    "терять": ("perder", "терять", "teryat'"),
    "собираться": ("pretender", "собираться", "sobirat'sya"),
    "выражать": ("expressar", "выражать", "vyrazhat'"),
    "заключаться": ("resumir-se", "заключаться", "zaklyuchat'sya"),
    "проводить": ("passar", "проводить", "provodit'"),
    "отмечать": ("notar", "отмечать", "otmechat'"),
    "открываться": ("abrir-se", "открываться", "otkryvat'sya"),
    "состоять": ("consistir", "состоять", "sostoyat'"),
    "входить": ("entrar", "входить", "vkhodit'"),
    "выяснять": ("descobrir", "выяснять", "vyasnyat'"),
    "собирать": ("colecionar", "собирать", "sobirat'"),
    "подниматься": ("subir", "подниматься", "podnimat'sya"),
    "подниматься": ("elevar-se", "подниматься", "podnimat'sya"),
    "связываться": ("ligar-se", "связываться", "svyazyvat'sya"),
    "падать": ("cair", "падать", "padat'"),
    "отказываться": ("recusar-se", "отказываться", "otkazyvat'sya"),
    "закрываться": ("fechar-se", "закрываться", "zakryvat'sya"),
    "выполнять": ("realizar", "выполнять", "vypolnyat'"),
    "возможно": ("ser possível", "возможно", "vozmozhno"),
    "оказывать": ("prestar", "оказывать", "okazyvat'"),
    "бороться": ("lutar", "бороться", "borot'sya"),
    "разговаривать": ("conversar", "разговаривать", "razgovarivat'"),
    "появиться": ("aparecer", "появиться", "poyavit'sya"),
    "требовать": ("exigir", "требовать", "trebovat'"),
    "удаваться": ("ser bem-sucedido", "удаваться", "udavat'sya"),
    "смотреться": ("olhar-se", "смотреться", "smotret'sya"),
    "понимать": ("entender", "понимать", "ponimat'"),
    "достигать": ("alcançar", "достигать", "dostigat'"),
    "покупать": ("comprar", "покупать", "pokupat'"),
    "изменяться": ("mudar", "изменяться", "izmenyat'sya"),
    "играть": ("jogar", "играть", "igrat'"),
    "представлять": ("apresentar", "представлять", "predstavlyat'"),
    "составлять": ("constituir", "составлять", "sostavlyat'"),
    "существовать": ("existir", "существовать", "suschestvovat'"),
    "следить": ("seguir", "следить", "sledit'"),
    "включать": ("incluir", "включать", "vklyuchat'"),
    "использовать": ("usar", "использовать", "ispol'zovat'"),
    "бояться": ("temer", "бояться", "boyatsya"),
    "запоминать": ("lembrar", "запоминать", "zapominat'"),
    "снимать": ("remover", "снимать", "snimat'"),
    "предполагать": ("supor", "предполагать", "predpolagat'"),
    "вести": ("conduzir", "вести", "vesti'"),
    "существовать": ("existir", "существовать", "suschestvovat'"),
    "следовать": ("seguir", "следовать", "sledovat'"),
    "вести": ("conduzir", "вести", "vesti'"),
    "составлять": ("constituir", "составлять", "sostavlyat'"),
    "следить": ("seguir", "следить", "sledit'"),
    "включать": ("incluir", "включать", "vklyuchat'"),
    "использовать": ("usar", "использовать", "ispol'zovat'"),
    "бояться": ("temer", "бояться", "boyatsya"),
    "запоминать": ("lembrar", "запоминать", "zapominat'"),
    "снимать": ("remover", "снимать", "snimat'"),
    "предполагать": ("supor", "предполагать", "predpolagat'"),
    "вести": ("conduzir", "вести", "vesti'"),

    
    "стол": ("mesa", "стол", "stol"),
    "молоко": ("leite", "молоко", "moloko"),
    "книга": ("livro", "книга", "kniga"),
    "собака": ("cachorro", "собака", "sobaka"),
    "друг": ("amigo", "друг", "drug"),
    "красивый": ("bonito", "красивый", "krasivyy"),
    "домашний": ("doméstico", "домашний", "domashniy"),
    "синий": ("azul", "синий", "siniy"),
    "дорогой": ("caro", "дорогой", "dorogoy"),
    "сестра": ("irmã", "сестра", "sestra"),
    "компьютер": ("computador", "компьютер", "kompyuter"),
    "время": ("tempo", "время", "vremya"),
    "магазин": ("loja", "магазин", "magazin"),
    "город": ("cidade", "город", "gorod"),
    "новый": ("novo", "новый", "novyy"),
    "простой": ("simples", "простой", "prostoy"),
    "деньги": ("dinheiro", "деньги", "dengi"),
    "человек": ("pessoa", "человек", "chelovek"),
    "красный": ("vermelho", "красный", "krasnyy"),
    "радостный": ("alegre", "радостный", "radostnyy"),
    "девушка": ("garota", "девушка", "devushka"),
    "учитель": ("professor", "учитель", "uchitel"),
    "работа": ("trabalho", "работа", "rabota"),
    "зеленый": ("verde", "зеленый", "zelenyy"),
    "спокойный": ("calmo", "спокойный", "spokojnyj"),
    "мама": ("mãe", "мама", "mama"),
    "крепкий": ("forte", "крепкий", "krepkij"),
    "глаз": ("olho", "глаз", "glaz"),
    "парень": ("garoto", "парень", "paren'"),
    "серый": ("cinza", "серый", "seryj"),
    "дом": ("casa", "дом", "dom"),
    "солнце": ("sol", "солнце", "solntse"),
    "красивая": ("bonita", "красивая", "krasivaya"),
    "маленький": ("pequeno", "маленький", "malen'kij"),
    "большой": ("grande", "большой", "bol'shoj"),
    "счастливый": ("feliz", "счастливый", "schastlivyj"),
    "милый": ("fofo", "милый", "milyj"),
    "комната": ("quarto", "комната", "komnata"),
    "грустный": ("triste", "грустный", "grustnyj"),
    "рука": ("mão", "рука", "ruka"),
    "коричневый": ("marrom", "коричневый", "korichnevyj"),
    "понравиться": ("gostar", "понравиться", "ponravit'sya"),
    "дорога": ("estrada", "дорога", "doroga"),
    "черный": ("preto", "черный", "chernyy"),
    "важный": ("importante", "важный", "vazhnyy"),
    "дети": ("crianças", "дети", "deti"),
    "молодой": ("jovem", "молодой", "molodoj"),
    "прекрасный": ("maravilhoso", "прекрасный", "prekrasnyj"),
    "колоритный": ("pitoresco", "колоритный", "koloritnyj"),
    "вкусный": ("delicioso", "вкусный", "vkusnyj"),
    "интересный": ("interessante", "интересный", "interesnyj"),
    "теплый": ("quente", "теплый", "teplyj"),
    "старый": ("antigo", "старый", "staryj"),
    "холодный": ("frio", "холодный", "holodnyj"),
    "сладкий": ("doce", "сладкий", "sladkij"),
    "большой": ("grande", "большой", "bol'shoj"),
    "веселый": ("alegre", "веселый", "veselyj"),
    "спокойный": ("calmo", "спокойный", "spokojnyj"),
    "веселый": ("alegre", "веселый", "veselyj"),
    "здоровый": ("saudável", "здоровый", "zdorovyj"),
    "плохой": ("ruim", "плохой", "plohoj"),
    "новый": ("novo", "новый", "novyj"),
    "сильный": ("forte", "сильный", "sil'nyj"),
    "простой": ("simples", "простой", "prostoj"),
    "прекрасный": ("maravilhoso", "прекрасный", "prekrasnyj"),
    "замечательный": ("maravilhoso", "замечательный", "zamechatel'nyj"),
    "долгий": ("longo", "долгий", "dolgij"),
    "короткий": ("curto", "короткий", "korotkij"),
    "добрый": ("bom", "добрый", "dobryj"),
    "горячий": ("quente", "горячий", "goryachij"),
    "крепкий": ("forte", "крепкий", "kreplennyj"),
    "мягкий": ("macio", "мягкий", "mjagkij"),
    "последний": ("último", "последний", "poslednij"),
    "первый": ("primeiro", "первый", "pervyj"),
    "трудный": ("difícil", "трудный", "trudnyj"),
    "легкий": ("fácil", "легкий", "legkij"),
    "сложный": ("complicado", "сложный", "slozhnyj"),
    "интересный": ("interessante", "интересный", "interesnyj"),
    "скучный": ("entediante", "скучный", "skuchnyj"),
    "темный": ("escuro", "темный", "temnyj"),
    "светлый": ("claro", "светлый", "svetlyj"),
    "весенний": ("primaveril", "весенний", "vesennyj"),
    "зимний": ("invernal", "зимний", "zimnij"),
    "летний": ("veranil", "летний", "letnij"),
    "осенний": ("outonal", "осенний", "osennij"),
    "жаркий": ("quente", "жаркий", "zharkij"),
    "холодный": ("frio", "холодный", "holodnyj"),
    "солнечный": ("ensolarado", "солнечный", "solnechnyj"),
    "облачный": ("nublado", "облачный", "oblachnyj"),
    "теплый": ("quente", "теплый", "teplyj"),
    "холодный": ("frio", "холодный", "holodnyj"),
    "сухой": ("seco", "сухой", "suhoj"),
    "мокрый": ("molhado", "мокрый", "mokryj"),
    "свежий": ("fresco", "свежий", "svezhij"),
    "старый": ("antigo", "старый", "staryj"),
    "новый": ("novo", "новый", "novyj"),


}


            
        

        self.current_word = None
        self.word_label = tk.Label(master, text="", bg=self.background_color, fg=self.text_color, font=("Helvetica", 36))
        self.word_label.pack(pady=40)

        self.pronunciation_label = tk.Label(master, text="", bg=self.background_color, fg=self.text_color, font=("Helvetica", 24))
        self.pronunciation_label.pack(pady=20)

        self.translation_label = tk.Label(master, text="", bg=self.background_color, fg=self.text_color, font=("Helvetica", 24))
        self.translation_label.pack(pady=20)

        self.show_pronunciation_button = tk.Button(master, text="Revelar Pronúncia", command=self.reveal_pronunciation, bg=self.button_color, fg=self.text_color, font=("Helvetica", 16), padx=20, pady=10, relief=tk.RAISED)
        self.show_pronunciation_button.pack(pady=20)

        self.show_translation_button = tk.Button(master, text="Revelar Tradução", command=self.reveal_translation, bg=self.button_color, fg=self.text_color, font=("Helvetica", 16), padx=20, pady=10, relief=tk.RAISED)
        self.show_translation_button.pack(pady=20)

        self.next_button = tk.Button(master, text="Próxima", command=self.show_word, bg=self.button_color, fg=self.text_color, font=("Helvetica", 16), padx=20, pady=10, relief=tk.RAISED)
        self.next_button.pack(pady=20)

        self.show_word()

    def show_word(self):
        self.current_word = random.choice(list(self.words.items()))
        word = self.current_word[0]
        self.word_label.config(text=word)

        # Limpar as labels de tradução e pronúncia
        self.translation_label.config(text="")
        self.pronunciation_label.config(text="")

    def reveal_translation(self):
        translation = self.current_word[1][0]
        self.translation_label.config(text=translation)

    def reveal_pronunciation(self):
        pronunciation = self.current_word[1][2]
        self.pronunciation_label.config(text=pronunciation)

        # Geração da pronúncia
        tts = gTTS(text=pronunciation, lang='ru')
        tts.save("temp.mp3")
        os.system("mpg321 temp.mp3")

def main():
    root = tk.Tk()
    app = WordApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
