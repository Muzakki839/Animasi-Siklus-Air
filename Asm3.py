from manim import *

class Asm3(MovingCameraScene):
    def construct(self):
        # Bakground
        self.camera.background_color=WHITE

        # Bingkai
        bingkai = VGroup(
            Rectangle(color=BLACK, fill_opacity=1, width=20, height=1).shift(DOWN*4),
            Rectangle(color=BLACK, fill_opacity=1, width=20, height=1).shift(UP*4)
        ) 

        # Matahari
        matahari = Circle(color=YELLOW, fill_opacity=1).shift([4, 2, 2]).scale(0.5).shift(UP*5)

        # Laut
        laut = Rectangle(color=BLUE, fill_opacity=0.8, stroke_opacity=0, width=30, height=2.5).shift([0, -5.3, 0])

        # Tanah
        titik_tanah = [
            [-10, 0, 0],
            [0, 0, 0],
            [1, -0.5, 0],  
            [3, -2, 0],
            [6, -3.5, 0],
            [-10, -3.5, 0]
        ]
        tanah = Polygon(*titik_tanah, color=DARK_BROWN, fill_opacity=1).shift([-6, -0.5, 0]).scale(0.8)

        # Judul
        kanvas = Rectangle(color=WHITE, fill_opacity=0.5, width=1920, height=1080)
        judul = Text('Siklus Air', color=DARK_BLUE, fill_opacity=1, font='Segoe Print', font_size=90)
        credit = VGroup(
            RoundedRectangle(color=DARK_BLUE, fill_opacity=1, width=10, height=0.8, corner_radius=0.3).next_to(judul, DOWN),
            Text('Bersama: Muzakki Abdul Aziz', color=WHITE, fill_opacity=1, font='Segoe Print', font_size=40).next_to(judul, DOWN*1.5)
        )

        # Butir Air 
        butir = VGroup(*[
            Circle(color=BLUE, stroke_width=3).scale(0.05).shift(RIGHT*i*0.05 + DOWN*j*0.05)
            for i, j in [(0,2), (5,3), (10,2), (15,3), 
                         (0,12), (5,13), (10,12), (15,13)]
        ]).shift([3, -1, 0])
        butir.save_state()

        def anim_butir():
            anim_butir = [butir[i].animate.shift(UP*j) 
                        for i,j in zip(range(len(butir)), [2.3, 2.7, 2.3, 2.7, 
                                                            2.3, 2.7, 2.3, 2.7])]
            self.play(*anim_butir)
            self.play(
                FadeIn(awan),
                FadeOut(*butir), run_time=0.5
                )
            self.play(awan.animate.shift(LEFT*10))
            self.remove(awan)
            butir.restore()
            awan.restore()

        # Awan
        awan = VGroup(*[Circle(color=LIGHT_GREY, fill_opacity=1).shift(RIGHT*i + UP*j).scale(k)
                        for i, j, k in [(0,0,1), (1,0,1), (2,0,1), (1.5,1,1), (0.5,1,0.8)]
        ]).scale(0.4).shift([2.35,1.2,0])
        awan.save_state()

        # Scene
        self.play(
            FadeIn(bingkai),
            matahari.animate.shift(DOWN*5),
            laut.animate.shift(UP*3),
            tanah.animate.shift(RIGHT*3)
            )
        self.play(
            FadeIn(kanvas),
            GrowFromCenter(judul),
            run_time=0.8
            )
        self.play(Indicate(judul), color=BLACK,)
        self.play(GrowFromEdge(credit, DOWN))
        self.wait()
        self.play(
            FadeOut(kanvas),
            FadeOut(judul),
            FadeOut(credit)
            )
        self.wait(1)
        self.play(self.camera.frame.animate.move_to([4, 0.7, 0]).scale(0.7))
        self.wait()
        for _ in range(10):
            anim_butir()