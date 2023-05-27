from manim import *

class Asm3(MovingCameraScene):
    def construct(self):
        # UTILS
        font1 = 'Segoe Print'
        garis_bantu1 = Line(start=[-7,-1.5,0], end=[-7,-3,0], color=WHITE, fill_opacity=0, stroke_opacity=0)
        garis_bantu2 = Line(start=[-7,-3,0], end=[1,-3,0], color=WHITE, fill_opacity=0, stroke_opacity=0)

# -------------------------------------------------------------------------------------------------------------------------------------
        # OBJEK
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
        laut_polos = Rectangle(color=BLUE_B, fill_opacity=1, stroke_opacity=0, width=30, height=2.5).shift([0, -5.3, 0])
        laut_bawah = Rectangle(color=BLUE_D, fill_opacity=1, width=50, height=1).shift([0, -6, 0])
        laut = VGroup(laut_polos, laut_bawah)

        # Tanah
        titik_tanah = [
            [-10, 0, 0],
            [0, 0, 0],
            [1, -0.5, 0],  
            [3, -2, 0],
            [6, -3.5, 0],
            [-10, -3.5, 0]
        ]
        tanah_polos = Polygon(*titik_tanah, color=DARK_BROWN, fill_opacity=1).shift([-6, -0.5, 0]).scale(0.8)
        tanah_bawah = Rectangle(color="#703002", fill_opacity=1, width=50, height=1).shift(DOWN*3)
        endapan_air = Rectangle(color=DARK_BLUE, fill_opacity=1, width=50, height=0.2).shift(DOWN*3)
        tanah_part1 = Intersection(tanah_polos, tanah_bawah, color="#703002", fill_opacity=1)
        tanah_part2 = Intersection(tanah_polos, endapan_air, color=DARK_BLUE, fill_opacity=1)
        danau = Ellipse(color=BLUE_B, fill_opacity=1).shift([-8.7, -1.3, 0]) .scale(0.7)
        p1 = [-1.5, 0, 0] 
        p1b=  p1 + 5 * RIGHT
        p2 = [2.8, -0.9, 0]
        p2b = p2 + 5 * LEFT 
        sungai = CubicBezier(p1,p1b,p2b,p2, color=BLUE_B, stroke_width=20).shift([-6.7, -1.3, 0])
        tanah = VGroup(tanah_polos, tanah_part1, tanah_part2, danau, sungai)

        # Butir Air 
        butir = VGroup(*[
            Circle(color=BLUE, stroke_width=3).scale(0.05).shift(RIGHT*i*0.05 + DOWN*j*0.05)
            for i, j in [(0,2), (5,3), (10,2), (15,3), 
                         (0,12), (5,13), (10,12), (15,13)]
        ]).shift([3, -1, 0])
        butir.save_state()

        butir2 = VGroup(*[
            Circle(color=BLUE, stroke_width=3).scale(0.05).shift(RIGHT*i*0.05 + DOWN*j*0.05)
            for i, j in [(0,2), (5,3), (10,2), (15,3), 
                         (0,12), (5,13), (10,12), (15,13)]
        ]).shift([-7, 1, 0])
        butir2.save_state()

        sebutir = Circle(color=WHITE, stroke_width=3).scale(0.05)

        # Awan
        awan = VGroup(*[Circle(color=LIGHT_GREY, fill_opacity=1).shift(RIGHT*i + UP*j).scale(k)
                        for i, j, k in [(0,0,1), (1,0,1), (2,0,1), (1.5,1,1), (0.5,1,0.8)]
        ]).scale(0.4).shift([2.35,1.2,0])
        awan.save_state()

        # Panah
        panah = Arrow(DOWN*2, UP*2, color=RED).shift([2,0,0]).scale(0.5)
        panah2 = Arrow(RIGHT*2, LEFT*2, color=RED).shift([0,2.5,0]).scale(0.5)
        panah3 = Arrow(DOWN*2, UP*2, color=RED).rotate(180*DEGREES).shift([-5,0.5,0]).scale(0.5)

# -------------------------------------------------------------------------------------------------------------------------------------
        # TEXT
        # Judul
        kanvas = Rectangle(color=WHITE, fill_opacity=0.5, width=1920, height=1080)
        judul = Text('Siklus Air', color=DARK_BLUE, fill_opacity=1, font=font1, font_size=90)
        credit = VGroup(
            RoundedRectangle(color=DARK_BLUE, fill_opacity=1, width=10, height=0.8, corner_radius=0.3).next_to(judul, DOWN),
            Text('Bersama: Muzakki Abdul Aziz', color=WHITE, fill_opacity=1, font=font1, font_size=40).next_to(judul, DOWN*1.5)
            )

        # Subjudul
        text_evaporasi1 = Text('Evaporasi', color=DARK_BLUE, fill_opacity=1, font=font1, font_size=30).shift([6.5,2,0])
        text_evaporasi2 = VGroup(
            RoundedRectangle(color=DARK_BLUE, fill_opacity=1, width=3, height=2, corner_radius=0.3),
            Text('Proses\npenguapan air\noleh\nsinar matahari', color=WHITE, fill_opacity=1, font=font1, font_size=25)
            ).next_to(text_evaporasi1, DOWN)
        
        text_kondensasi1 = Text('Kondensasi', color=DARK_BLUE, fill_opacity=1, font=font1, font_size=30).shift([5.5,2,0]).scale(0.5)
        text_kondensasi2 = VGroup(
            RoundedRectangle(color=DARK_BLUE, fill_opacity=1, width=3, height=2, corner_radius=0.3),
            Text('Proses\npengembunan\nbutiran air\nmenjadi awan', color=WHITE, fill_opacity=1, font=font1, font_size=25)
            ).scale(0.5).next_to(text_kondensasi1, DOWN)
        
        text_adveksi1 = Text('Adveksi', color=DARK_BLUE, fill_opacity=1, font=font1, font_size=30).shift([0,0.5,0])
        text_adveksi2 = VGroup(
            RoundedRectangle(color=DARK_BLUE, fill_opacity=1, width=4, height=2, corner_radius=0.3),
            Text('Pergerakan awan\nakibat penyebaran\npanas secara\nhorizontal', color=WHITE, fill_opacity=1, font=font1, font_size=25)
            ).next_to(text_adveksi1, DOWN)
        
        text_presipitasi1 = Text('Presitipasi', color=DARK_BLUE, fill_opacity=1, font=font1, font_size=30).shift([-3,2,0])
        text_presipitasi2 = VGroup(
            RoundedRectangle(color=DARK_BLUE, fill_opacity=1, width=3, height=2, corner_radius=0.3),
            Text('Proses\njatuhnya materi\ndari atmosfer\ndalam bentuk\ncair (hujan)', color=WHITE, fill_opacity=1, font=font1, font_size=20)
            ).next_to(text_presipitasi1, DOWN)
        
        text_runoff1 = Text('Run Off', color=DARK_BLUE, fill_opacity=1, font=font1, font_size=30).shift([-2,0,0]).scale(0.5)
        text_runoff2 = VGroup(
            RoundedRectangle(color=DARK_BLUE, fill_opacity=1, width=4.5, height=1.5, corner_radius=0.3),
            Text('Mengalirnya air\ndi permukaan tanah\nmelalui sungai', color=WHITE, fill_opacity=1, font=font1, font_size=25)
            ).scale(0.5).next_to(text_runoff1, DOWN)
        
        text_infiltrasi1 = Text('Infiltrasi & Perkolasi', color=WHITE, fill_opacity=1, font=font1, font_size=30).shift([-4.5,-1.8,0]).scale(0.5)
        text_infiltrasi2 = VGroup(
            RoundedRectangle(color=DARK_BLUE, fill_opacity=1, width=4, height=1.5, corner_radius=0.3),
            Text('Meresapnya air\nke dalam tanah\ndan bergerak\nke luar tanah', color=WHITE, fill_opacity=1, font=font1, font_size=25)
            ).scale(0.5).next_to(text_infiltrasi1, DOWN*0.4)

# -------------------------------------------------------------------------------------------------------------------------------------
        # PRESET ANIM
        def anim_butir(preset, arah=UP):
            anim_butir = [butir[i].animate.shift(arah*j)
                        for i,j in zip(range(len(butir)), [2.3, 2.7, 2.3, 2.7, 
                                                            2.3, 2.7, 2.3, 2.7])]
            anim_butir2 = [butir2[i].animate.shift(arah*j)
                        for i,j in zip(range(len(butir2)), [1.3, 1.7, 1.3, 1.7, 
                                                            1.3, 1.7, 1.3, 1.7])]
            if preset ==0:
                self.play(*anim_butir)
            elif preset ==0.5:
                self.play(*anim_butir)
                self.play(FadeOut(*butir), run_time=0.5)
            elif preset == 1:
                self.play(*anim_butir)
                self.play(
                    FadeIn(awan),
                    FadeOut(*butir), run_time=0.5
                    )
            elif preset == 1.5:
                awan.set_color(GREY_C)
                self.play(*anim_butir)
                self.play(
                    FadeIn(awan),
                    FadeOut(*butir), run_time=0.5
                    )
            elif preset ==2:
                self.play(FadeToColor(awan, GREY_C),
                          FadeOut(*butir), run_time=0.5)
            elif preset == 3:
                self.play(FadeOut(*butir), run_time=0.5)
                self.play(awan.animate.shift(LEFT*10))
                self.remove(awan)
                awan.restore()
            elif preset == 3.5:
                self.play(FadeOut(*butir), run_time=0.5)
                self.play(awan.animate.shift(LEFT*10))
                self.play(FadeOut(awan))
                awan.restore()
            elif preset == 4:
                # self.add(awan)
                self.play(awan.animate.shift(LEFT*10))
                for _ in range(10):
                    self.play(*anim_butir2, run_time=0.2)
                    self.remove(butir2)
                    butir2.restore()
                self.play(*anim_butir2)
                self.play(FadeOut(butir2))
                self.play(FadeOut(awan))
                awan.restore()
            elif preset == 4.5:
                self.play(*anim_butir2, run_time=0.5)
                self.play(FadeOut(butir2), run_time=0.2)
            butir.restore()
            butir2.restore()

# -------------------------------------------------------------------------------------------------------------------------------------
        # SCENE
        # Intro
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

        # 1. Evaporasi
        self.play(self.camera.frame.animate.move_to([4, 0.7, 0]).scale(0.7))
        self.wait()
        anim_butir(1)
        for i in range(2):
            anim_butir(0.5)
            if i == 0:
                self.play(GrowFromCenter(text_evaporasi1),
                        GrowArrow(panah))
                self.play(GrowFromEdge(text_evaporasi2, UP))
        anim_butir(0)
        anim_butir(2)
        for _ in range(1):
            anim_butir(0.5)
        self.play(
            FadeOut(text_evaporasi1),
            FadeOut(text_evaporasi2),
            FadeOut(panah)
        )
        anim_butir(3)

        # 2. Kondensasi
        self.play(self.camera.frame.animate.move_to([4,1.5,0]).scale(0.5))
        anim_butir(1)
        self.play(GrowFromCenter(text_kondensasi1))
        self.play(GrowFromEdge(text_kondensasi2, UP))
        anim_butir(0.5)
        anim_butir(2)
        anim_butir(0.5)
        anim_butir(3)
        for _ in range(0):
            anim_butir(1)
            anim_butir(0.5)
            anim_butir(2)
            anim_butir(0.5)
            anim_butir(3)
        self.play(
            FadeOut(text_kondensasi1),
            FadeOut(text_kondensasi2),
        )
        
        # 3. Adveksi     
        self.play(self.camera.frame.animate.scale(3).move_to(ORIGIN))
        self.play(self.camera.frame.animate.move_to(ORIGIN).scale(0.8))
        self.wait()
        for i in range(3):
            anim_butir(1.5)
            anim_butir(3.5)
            if i ==0:
                self.play(GrowFromCenter(text_adveksi1),
                          GrowArrow(panah2))
                self.play(GrowFromEdge(text_adveksi2, UP))
        self.play(
            FadeOut(text_adveksi1),
            FadeOut(text_adveksi2),
            FadeOut(panah2)
        )
        
        # 4. Presipitasi
        self.play(self.camera.frame.animate.scale(1.25).move_to([0,0,0]))
        self.play(self.camera.frame.animate.scale(0.6).move_to([-3.5,0.5,0]))
        self.wait()
        for i in range(2):
            anim_butir(4, DOWN)
            if i == 0:
                self.play(GrowFromCenter(text_presipitasi1),
                        GrowArrow(panah3))
                self.play(GrowFromEdge(text_presipitasi2, UP))
        self.play(
            FadeOut(text_presipitasi1),
            FadeOut(text_presipitasi2),
            FadeOut(panah3)
        )

        # 5. Run Off
        self.play(self.camera.frame.animate.scale(0.8).move_to([-4,-1.5,0]))
        self.wait()
        for i in range(3):
            sebutir.move_to(danau.get_center()).set_color(BLUE_D)
            anim_butir(4.5, DOWN)
            self.play(MoveAlongPath(sebutir, sungai))
            self.play(FadeOut(sebutir), run_tim=0.2)
            if i == 0:
                self.play(GrowFromCenter(text_runoff1))
                self.play(GrowFromEdge(text_runoff2, UP))
        self.play(
            FadeOut(text_runoff1),
            FadeOut(text_runoff2),
        )

        # 6. Infiltrasi
        self.add(garis_bantu1, garis_bantu2)
        for i in range(3):
            sebutir.move_to([-7,-1.5,0]).set_color(BLUE_B)
            anim_butir(4.5, DOWN)
            self.play(MoveAlongPath(sebutir, garis_bantu1))
            self.play(MoveAlongPath(sebutir, garis_bantu2))
            self.play(FadeOut(sebutir), run_tim=0.2)
            if i == 0:
                self.play(GrowFromCenter(text_infiltrasi1))
                self.play(GrowFromEdge(text_infiltrasi2, UP))
        self.play(
            FadeOut(text_infiltrasi1),
            FadeOut(text_infiltrasi2),
        )

        # Outro
        self.play(self.camera.frame.animate.scale(2).move_to([-1,0,0]))
        self.wait()
        judul.shift([-1,0,0])
        self.play(GrowFromCenter(judul), run_time=0.8)

        for _ in range (2):
            anim_butir(1)
            anim_butir(0.5)
            anim_butir(4, DOWN)
            for _ in range(2):
                sebutir.move_to(danau.get_center()).set_color(BLUE_D)
                self.play(MoveAlongPath(sebutir, sungai))
                self.play(FadeOut(sebutir), run_tim=0.2)
            for _ in range(2):
                sebutir.move_to([-7,-1.5,0]).set_color(BLUE_B)
                self.play(MoveAlongPath(sebutir, garis_bantu1))
                self.play(MoveAlongPath(sebutir, garis_bantu2))
                self.play(FadeOut(sebutir), run_tim=0.2)

        self.play(self.camera.frame.animate.move_to([0,3,0]).scale(0.1))
        self.wait()
        





