from handlers.menu import router as menu_router
from handlers.cards_handler.skills import router as skills_router
from handlers.cards_handler.members import router as members_router
from handlers.cards_handler.cards_member import router as cards_member_router
from handlers.cards_handler.cards_skill import router as cards_skill_router
from handlers.roulette import router as roulette_router
from handlers.admin.admin_GG import router as admin_router
from handlers.admin.add_edit_card import router as add_edit_card_router
from handlers.admin.users_command import router as users_command_router
from datebase.stats import router as stats_router
from handlers.keyboard import router as keyboard_router
from handlers.support import router as support_router

routers = [
    menu_router,
    skills_router,
    members_router,
    cards_member_router,
    cards_skill_router,
    admin_router,
    roulette_router,
    add_edit_card_router,
    users_command_router,
    stats_router,
    keyboard_router,
    support_router
]