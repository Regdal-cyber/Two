# Matplotlib-версия с настраиваемым размером узлов (node_scale)
import random
from dataclasses import dataclass
from typing import List, Tuple

import matplotlib.pyplot as plt
from matplotlib.patches import Circle


@dataclass
class CanvasCfg:
    width: int = 600
    height: int = 400
    margin_x: int = 40
    margin_y: int = 30
    bg: str = "white"


class Neyronka:
    def __init__(
        self,
        layer_in: int,
        layers: List[int],
        count_class: int = 1,
        canvas: CanvasCfg | None = None,
        seed: int | None = 42,
        node_scale: float = 1.35,
    ):
        self.layer_in = layer_in
        self.layers = list(layers)
        self.count_class = count_class
        self.canvas = canvas or CanvasCfg()
        self.node_scale = node_scale

        # геометрия
        self.maxim = max(
            [self.layer_in, self.count_class] + (self.layers if self.layers else [0])
        )
        self.step = (self.canvas.height - 2 * self.canvas.margin_y) / (self.maxim + 1)
        # радиус как доля шага по Y; умножаем на node_scale
        self.radius = max(3, int(self.step * 0.33 * self.node_scale))

        # фигура
        self.fig, self.ax = plt.subplots(
            figsize=(self.canvas.width / 100, self.canvas.height / 100), dpi=100
        )
        self.ax.set_facecolor(self.canvas.bg)
        self.ax.set_xlim(-self.canvas.width / 2, self.canvas.width / 2)
        self.ax.set_ylim(-self.canvas.height / 2, self.canvas.height / 2)
        self.ax.set_aspect("equal", adjustable="box")
        self.ax.axis("off")

        if seed is not None:
            random.seed(seed)

        self.x_y_layer: List[List[Tuple[float, float]]] = []

    # ----- расчёты расположения -----
    def _layer_x(self, idx: int, total_layers: int) -> float:
        if total_layers <= 1:
            return 0.0
        usable = self.canvas.width - 2 * self.canvas.margin_x
        return (
            -self.canvas.width / 2
            + self.canvas.margin_x
            + usable * idx / (total_layers - 1)
        )

    def _neuron_ys(self, n: int) -> List[float]:
        if n <= 0:
            return []
        if n % 2 == 1:
            start = 0 - (n // 2) * self.step
        else:
            start = 0 - (n / 2 - 0.5) * self.step
        return [start + i * self.step for i in range(n)]

    # ----- рисование -----
    def draw_neuron_layer(
        self, x0: float, count_neuron: int
    ) -> List[Tuple[float, float]]:
        coords: List[Tuple[float, float]] = []
        ys = self._neuron_ys(count_neuron)
        palette = [
            (255, 209, 102),
            (244, 162, 97),
            (233, 196, 106),
            (149, 213, 178),
            (138, 180, 248),
        ]
        for y in ys:
            r, g, b = random.choice(palette)
            circ = Circle(
                (x0, y),
                radius=self.radius,
                facecolor=(r / 255, g / 255, b / 255),
                edgecolor="black",
                linewidth=1.2,
            )
            self.ax.add_patch(circ)
            coords.append((x0, y))
        return coords

    def draw_neurons_in(self):
        x0 = self._layer_x(0, len(self.layers) + 2)
        self.x_y_layer.append(self.draw_neuron_layer(x0, self.layer_in))

    def draw_neurons_hidden(self):
        total = len(self.layers) + 2
        for i, n in enumerate(self.layers, start=1):
            x = self._layer_x(i, total)
            self.x_y_layer.append(self.draw_neuron_layer(x, n))

    def draw_neurons_out(self):
        x0 = self._layer_x(len(self.layers) + 1, len(self.layers) + 2)
        self.x_y_layer.append(self.draw_neuron_layer(x0, self.count_class))

    def draw_neurons(self):
        if not self.x_y_layer:
            self.draw_neurons_in()
            self.draw_neurons_hidden()
            self.draw_neurons_out()
        else:
            # перерисовать сверху (оставляем те же координаты)
            layers = self.x_y_layer
            for layer in layers:
                for x, y in layer:
                    circ = Circle(
                        (x, y),
                        radius=self.radius,
                        facecolor="none",
                        edgecolor="black",
                        linewidth=1.2,
                    )
                    self.ax.add_patch(circ)

    def draw_network(self, list_x1_y1, list_x2_y2, color="#777", alpha=0.70, lw=1.0):
        for x1, y1 in list_x1_y1:
            for x2, y2 in list_x2_y2:
                self.ax.plot([x1, x2], [y1, y2], linewidth=lw, alpha=alpha, color=color)

    def network(self):
        for i in range(1, len(self.x_y_layer)):
            self.draw_network(self.x_y_layer[i - 1], self.x_y_layer[i])

    def show(self):
        plt.tight_layout()
        plt.show()


# ===== пример запуска (узлы в 2 раза меньше) =====
neyronka = Neyronka(
    6,
    [2, 3, 4, 3],
    10,
    canvas=CanvasCfg(width=900, height=520, margin_x=70, margin_y=50, bg="white"),
    node_scale=1.35,
)  # <-- ключевая строка

neyronka.draw_neurons()
neyronka.network()
neyronka.draw_neurons()
neyronka.show()
