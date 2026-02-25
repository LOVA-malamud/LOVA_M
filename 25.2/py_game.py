"""Rock Paper Scissors Pygame Implementation.

A graphical Rock Paper Scissors game using Pygame with animations,
card-based UI, and keyboard controls.
"""

import pygame  # pip install pygame
import random
import math
import sys

# -----------------------
# Config
# -----------------------
WIDTH, HEIGHT = 900, 520
FPS = 60

BG = (18, 18, 24)
WHITE = (240, 240, 245)
GRAY = (155, 155, 165)
GREEN = (90, 235, 150)
RED = (235, 90, 90)
YELLOW = (240, 220, 120)

CHOICES = ["rock", "paper", "scissors"]
KEY_TO_CHOICE = {
    pygame.K_r: "rock",
    pygame.K_p: "paper",
    pygame.K_s: "scissors",
}

# -----------------------
# Animation helpers
# -----------------------
def ease_out_back(t: float) -> float:
    """Easing function for back animation.
    
    Args:
        t: Time value between 0 and 1
        
    Returns:
        Eased value
    """
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2


def clamp01(x: float) -> float:
    """Clamp value between 0 and 1.
    
    Args:
        x: Value to clamp
        
    Returns:
        Clamped value between 0 and 1
    """
    return max(0.0, min(1.0, x))

# -----------------------
# Game logic
# -----------------------
def cpu_pick() -> str:
    """Get random choice for CPU.
    
    Returns:
        Random choice from CHOICES
    """
    return random.choice(CHOICES)


def result(player: str, cpu: str) -> str:
    """Determine game result.
    
    Args:
        player: Player's choice
        cpu: CPU's choice
        
    Returns:
        'WIN', 'LOSE', or 'TIE'
    """
    if player == cpu:
        return "TIE"
    wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    return "WIN" if wins[player] == cpu else "LOSE"

# -----------------------
# Load images
# -----------------------
def load_icons():
    """Load and resize game icons.
    
    Returns:
        Dictionary of loaded and resized icons
    """
    rock = pygame.image.load("rock_1.png").convert_alpha()
    paper = pygame.image.load("paper_1.png").convert_alpha()
    scissors = pygame.image.load("scissors_1.png").convert_alpha()

    # Resize to uniform size
    size = 160
    rock = pygame.transform.smoothscale(rock, (size, size))
    paper = pygame.transform.smoothscale(paper, (size, size))
    scissors = pygame.transform.smoothscale(scissors, (size, size))

    return {
        "rock": rock,
        "paper": paper,
        "scissors": scissors
    }

# -----------------------
# Drawing helpers
# -----------------------
def draw_center_text(surf, text, font, color, center):
    """Draw centered text on surface.
    
    Args:
        surf: Surface to draw on
        text: Text to render
        font: Font to use
        color: Text color
        center: Center position tuple
    """
    img = font.render(text, True, color)
    rect = img.get_rect(center=center)
    surf.blit(img, rect)


def draw_panel(surface, rect, alpha=255):
    """Draw a rounded panel.
    
    Args:
        surface: Surface to draw on
        rect: Panel rectangle
        alpha: Transparency value
    """
    panel = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    pygame.draw.rect(panel, (40, 40, 55, alpha), panel.get_rect(), border_radius=18)
    pygame.draw.rect(panel, (90, 90, 110, alpha), panel.get_rect(), width=2, border_radius=18)
    surface.blit(panel, rect.topleft)


def draw_card(surface, rect, who_text, choice, icons, font_small, alpha=255):
    """Draw a game card.
    
    Args:
        surface: Surface to draw on
        rect: Card rectangle
        who_text: Label text ('YOU' or 'CPU')
        choice: Current choice or None
        icons: Dictionary of icons
        font_small: Small font for labels
        alpha: Transparency value
    """
    draw_panel(surface, rect, alpha=alpha)

    # label (YOU / CPU)
    draw_center_text(surface, who_text, font_small, (200, 200, 210), (rect.centerx, rect.top + 28))

    if choice:
        img = icons[choice]
        img_rect = img.get_rect(center=rect.center)
        surface.blit(img, img_rect)
    else:
        # Draw big question mark
        question_font = pygame.font.SysFont("arial", 100, bold=True)
        draw_center_text(surface, "?", question_font, (180, 180, 200), rect.center)

# -----------------------
# Main
# -----------------------
def main():
    """Main game loop and initialization."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rock Paper Scissors (Icons)")
    clock = pygame.time.Clock()

    title_font = pygame.font.SysFont("arial", 34, bold=True)
    small_font = pygame.font.SysFont("arial", 20)

    icons = load_icons()

    state = "waiting"
    player_choice = None
    cpu_choice = None
    outcome = None

    anim_t = 0.0
    anim_duration = 0.55
    shake_t = 0.0

    def start_round(choice):
        """Start a new game round."""
        nonlocal state, player_choice, cpu_choice, outcome, anim_t, shake_t
        player_choice = choice
        cpu_choice = cpu_pick()
        outcome = result(player_choice, cpu_choice)
        anim_t = 0.0
        shake_t = 0.0
        state = "animating"

    def reset_round():
        """Reset the game round."""
        nonlocal state, player_choice, cpu_choice, outcome
        state = "waiting"
        player_choice = None
        cpu_choice = None
        outcome = None

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if state == "waiting":
                    if event.key in KEY_TO_CHOICE:
                        start_round(KEY_TO_CHOICE[event.key])

                elif state == "result":
                    if event.key == pygame.K_SPACE:
                        reset_round()

        if state == "animating":
            anim_t += dt / anim_duration
            if anim_t >= 1.0:
                anim_t = 1.0
                state = "result"
                if outcome == "LOSE":
                    shake_t = 0.35

        if shake_t > 0:
            shake_t -= dt

        screen.fill(BG)

        draw_center_text(screen, "ROCK  PAPER  SCISSORS", title_font, WHITE, (WIDTH // 2, 50))
        draw_center_text(screen, "Press R / P / S to choose", small_font, GRAY, (WIDTH // 2, 84))

        card_w, card_h = 300, 260
        left_base = pygame.Rect(140, 140, card_w, card_h)
        right_base = pygame.Rect(WIDTH - 140 - card_w, 140, card_w, card_h)

        if state in ("animating", "result"):
            t = clamp01(anim_t)
            e = ease_out_back(t)

            left_x = 140 - int((1 - e) * 260)
            right_x = (WIDTH - 140 - card_w) + int((1 - e) * 260)

            pop = int((1 - t) * 18)

            left_rect = pygame.Rect(left_x, 140 + pop, card_w, card_h)
            right_rect = pygame.Rect(right_x, 140 + pop, card_w, card_h)

            if state == "result" and outcome == "LOSE" and shake_t > 0:
                s = int(6 * math.sin((0.35 - shake_t) * 50))
                left_rect.x += s

            draw_card(screen, left_rect, "YOU", player_choice, icons, small_font)
            draw_card(screen, right_rect, "CPU", cpu_choice, icons, small_font)
        else:
            draw_card(screen, left_base, "YOU", None, icons, small_font, alpha=210)
            draw_card(screen, right_base, "CPU", None, icons, small_font, alpha=210)

        if state == "result":
            if outcome == "WIN":
                c, msg = GREEN, "YOU WIN!"
            elif outcome == "LOSE":
                c, msg = RED, "YOU LOSE!"
            else:
                c, msg = YELLOW, "TIE!"

            draw_center_text(screen, msg, pygame.font.SysFont("arial", 44, bold=True), c, (WIDTH // 2, 430))
            draw_center_text(screen, "Press SPACE to play again", small_font, GRAY, (WIDTH // 2, 468))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()