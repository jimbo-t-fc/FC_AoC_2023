from pathlib import Path
from collections import deque
from math import prod


def solution(input_dir, output_dir, p1):
    input_file = Path(input_dir) / "day_20_input.txt"

    class Module:
        def __init__(self, name, inp_type, state):
            self.name = name
            self.inp_type = inp_type
            self.state = state
            self.out = {}
            self.inp = {}
            self.sent = {0: 0, 1: 0}

        def __repr__(self):
            return f"{self.name} - {self.inp_type} - {self.state}"

        def send_pulse(self, pulse_type: int):
            to_send = []

            for o in self.out.values():
                self.sent[pulse_type] += 1

                o["last"] = pulse_type
                # print(self.name, self.state, o["mod"].name)
                if o["mod"].receive_pulse(pulse_type, self.name):
                    to_send.append(o["mod"])

            return to_send

        def receive_pulse(self, pulse_type: int, source):
            if source != "button":
                self.inp[source]["last"] = pulse_type

            if self.inp_type == "^":
                self.state = pulse_type
            elif self.inp_type == "%":
                if pulse_type:
                    return False
                self.state = not self.state
            elif self.inp_type == "&":
                self.state = not all(i["last"] for i in self.inp.values())
            return True

        def pulse(self):
            return self.send_pulse(self.state)

    modules = {}
    with open(input_file, "r") as f:
        data = f.read().split("\n")
        for d in data:
            inp, out = d.split(" -> ")

            if inp == "broadcaster":
                inp = "^" + inp

            inp_type, inp_name = inp[0], inp[1:]

            if inp_name in modules:
                modules[inp_name].inp_type = inp_type
            else:
                modules[inp_name] = Module(inp_name, inp_type, 0)

            out_names = out.split(", ")
            for out_name in out_names:
                if out_name in modules:
                    op_mod = modules[out_name]
                else:
                    op_mod = Module(out_name, "TBC", 0)

                op_mod.inp[inp_name] = {"last": 0, "mod": modules[inp_name]}
                modules[inp_name].out[out_name] = {"last": 0, "mod": op_mod}
                modules[out_name] = op_mod

    checks = {j["mod"].name: 0 for j in modules["dn"].inp.values()}  # p2
    i = 0
    while True:
        i += 1
        modules["broadcaster"].receive_pulse(0, "button")
        q = deque(modules["broadcaster"].pulse())
        while q:
            n = q.popleft()
            q.extend(n.pulse())
            if n.state and n.name in checks and not checks[n.name]:  # p2
                checks[n.name] = i
        if p1 and i == 1000:
            break
        if not p1 and all(checks.values()):
            break

    if p1:
        low = sum(m.sent[0] for m in modules.values()) + 1000
        high = sum(m.sent[1] for m in modules.values())
        res = low * high
    else:
        res = prod(checks.values())

    return res


def main(input_dir="../input", output_dir="../output"):
    res1 = solution(input_dir, output_dir, True)
    print("Part 1:", res1)
    res2 = solution(input_dir, output_dir, False)
    print("Part 2:", res2)


if __name__ == "__main__":
    main()
