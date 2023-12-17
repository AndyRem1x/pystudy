import random


class Boss:
    def __init__(self, name: str, company: str):
        self.id = random.randint(1, 999)
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        text = f'Workers for {self.name} are:\n'
        for employee in self._workers:
            text += f'{employee["id_"]}, {employee["name"]}\n'

        return text

    @workers.setter
    def workers(self, worker):
        self._workers.append(worker)

    def __repr__(self):
        return f"Boss: {self.id} {self.name}"


class Worker:
    def __init__(self, name: str, boss: Boss):
        self.id_ = random.randint(1, 999)
        self.name = name
        self.boss = boss
        boss.workers = {"id_": self.id_, "name": name}

    def __repr__(self):
        return f"Worker: {self.id_} {self.name}"


boss_1 = Boss("Steve", "Jobs")
boss_2 = Boss("Bill", "Gates")

worker_1 = Worker("Peter", boss_1)
worker_2 = Worker("John", boss_1)
worker_3 = Worker("Bill", boss_2)
worker_4 = Worker("James", boss_2)

print(boss_1.workers)
print(boss_2.workers)

print(boss_1)
print(boss_2)
