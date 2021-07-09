import re
import random
from operator import sub, mul, add, truediv
from discord.ext import commands
from util.lists import split_list
from util.Config import load_config


def roll_dice(dice):
    amount, sides = dice.split('d')
    return sum([random.randint(1, int(sides)) for _ in range(int(amount))])


reg = re.compile(r'([+\-\/*])')
dice_re = re.compile(r'\d{1,2}d\d{1,2}')


def is_die(die):
    if dice_re.fullmatch(die) is not None:
        return True
    else:
        return False


def parse_exp(exp):
    exp = reg.split(exp.replace(' ', ''))
    for index, i in enumerate(exp):
        if i == None or '':
            del exp[index]
    return exp


def is_num(term):
    r = re.fullmatch(r'(\d?\.\d+)|\d+', term.strip())
    return False if r is None else True


def calculate(terms, level=0):
    if type(terms) != list:
        terms = parse_exp(terms)
    elif len(terms) == 1:
        terms = terms[0]
    op = ['-', '+', '/', '*']
    operators = {
        '-': sub,
        '+': add,
        '/': truediv,
        '*': mul
    }
    if type(terms) == str:
        if is_num(terms):
            return float(terms)
        elif is_die(terms):
            return roll_dice(terms)
    elif type(terms) == float:
        return terms
    elif type(terms) == int:
        return float(int)

    operator = op[level]
    if operator in terms:
        l = split_list(terms, operator)
        t1 = calculate(l[0])
        t2 = calculate(l[1])
        return operators[operator](t1, t2)
    else:
        return calculate(terms, level + 1)


class Roll(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.config = load_config()

    @commands.command()
    async def roll(self, ctx, *, roll: str = None):
        await ctx.send(calculate(roll))


def setup(bot):
    bot.add_cog(Roll(bot))
