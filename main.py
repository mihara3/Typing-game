import pygame
import random
import time
import webbrowser
import subprocess
from question_loader import load_questions
from speech import speak
from sound_effects import play_correct_sound, play_wrong_sound
from result_logger import log_result
from generate_html import generate_html



pygame.init()
pygame.mixer.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 149, 237)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Game")

font_path = "/home/s1310064/Typing-game/data/NotoSansJP-VariableFont_wght.ttf"
font = pygame.font.Font(font_path, 36)
# font = pygame.font.SysFont("Arial", 36)

def draw_start_screen():
    screen.fill(WHITE)
    title = font.render("タイピングゲーム", True, BLACK)
    start_text = font.render("▶ スタート", True, WHITE)
    
    title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 60)

    pygame.draw.rect(screen, BLUE, button_rect, border_radius=15)
    screen.blit(title, title_rect)
    screen.blit(start_text, start_text.get_rect(center=button_rect.center))

    pygame.display.flip()
    return button_rect

def wait_for_start(button_rect):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return  # スタートが押されたらループを抜ける


def draw_text_lines(line1, line2=None):
    """2行分のテキストを描画"""
    screen.fill((255, 255, 255))
    render1 = font.render(line1, True, (0, 0, 0))
    rect1 = render1.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(render1, rect1)

    if line2:
        render2 = font.render(line2, True, (0, 0, 255))
        rect2 = render2.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(render2, rect2)

    pygame.display.flip()

def main():
    button_rect = draw_start_screen()  # 開始画面を描画
    wait_for_start(button_rect)        # スタートボタンが押されるまで待つ

    questions = load_questions("words.json")
    selected = random.sample(questions, 15)
    correct = 0
    total_start = time.time()

    for word in selected:
        user_input = ""
        draw_text_lines(f"問題: {word}")  # 先に問題を表示
        speak(word)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if user_input == word:
                            play_correct_sound()
                            correct += 1
                        else:
                            play_wrong_sound()
                        break
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode

                    draw_text_lines(f"問題: {word}", f"入力: {user_input}")
            else:
                continue
            break

    total_time = round(time.time() - total_start, 2)
    accuracy = round(correct / 15 * 100, 1)
    log_result(accuracy, total_time)
    show_result_screen(accuracy, total_time)
    generate_html("/home/s1310064/Typing-game/results.csv", "/home/s1310064/Typing-game/docs/index.html")
    subprocess.run(["git", "add", "/home/s1310064/Typing-game/docs/index.html"])
    subprocess.run(["git", "commit", "-m", "Update ranking automatically"])
    subprocess.run(["git", "push"])

    pygame.quit()

    
def show_result_screen(accuracy, total_time):
    screen.fill((255, 255, 255))

    # 結果表示
    result_text = font.render(f"正答率: {accuracy}%   時間: {total_time}s", True, (0, 0, 0))
    result_rect = result_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(result_text, result_rect)

    # ランキングボタン
    button_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2, 300, 60)
    pygame.draw.rect(screen, BLUE, button_rect, border_radius=15)
    button_text = font.render("▶ ランキングを表示", True, (255, 255, 255))
    button_rect_text = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_rect_text)

    pygame.display.flip()

    # ボタンクリック待ち（またはウィンドウを閉じる）
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    webbrowser.open("http://localhost:5000")
                    return


if __name__ == "__main__":
    main()


