class AddCost:
    SHORTCUT = 'ac'
    LABEL = 'Add cost'


class ListCosts:
    SHORTCUT = 'wc'
    LABEL = 'Write costs'


class AddIncome:
    SHORTCUT = 'ai'
    LABEL = 'Add income'


class ListIncomes:
    SHORTCUT = 'wi'
    LABEL = 'Write incomes'


class MainMenu:
    OPTIONS = {
        AddCost.SHORTCUT: AddCost(),
        ListCosts.SHORTCUT : ListCosts(),
        AddIncome.SHORTCUT : AddIncome(),
        ListIncomes.SHORTCUT : ListIncomes()
    }

    def draw(self):
        print('Say what you want to do: ')
        for shortcut, screen in MainMenu.OPTIONS.items():
            print(f'[{shortcut}] - {screen.LABEL}')

        option = None
        while option not in MainMenu.OPTIONS:
            option = input('Select an option: ')

        print(MainMenu.OPTIONS[option])

