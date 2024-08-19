from manim import *

class mySquareScene(Scene):
    def construct(self):
        
        grid = NumberPlane()
        self.play(Write(grid),run_time = 2)

# row 1
        s1 = Square(side_length=1).move_to([-3.5,3.5,0])
        s2 = Square(side_length=1).move_to([-2.5,3.5,0])
        s3 = Square(side_length=1).move_to([-1.5,3.5,0])
        s4 = Square(side_length=1).move_to([-0.5,3.5,0])
    
        s5 = Square(side_length=1).move_to([0.5,3.5,0])
        s6 = Square(side_length=1).move_to([1.5,3.5,0])
        s7 = Square(side_length=1).move_to([2.5,3.5,0])
        s8 = Square(side_length=1).move_to([3.5,3.5,0])
        
        g1 = VGroup(s1,s2,s3,s4,s5,s6,s7,s8)
        self.play((Write(g1)),run_time=0.5)

        self.play(s1.animate.set_fill(BLUE_C, opacity=1),run_time=0.1)
        self.play(s2.animate.set_fill(BLUE_C, opacity=1),run_time=0.1)
        self.play(s3.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s4.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)

        self.play(s5.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s6.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s7.animate.set_fill(BLUE_C, opacity=1),run_time=0.1)
        self.play(s8.animate.set_fill(BLUE_C, opacity=1),run_time=0.1)
# row 2
        s9 = Square(side_length=1).move_to([-3.5,2.5,0])
        s10 = Square(side_length=1).move_to([-2.5,2.5,0])
        s11 = Square(side_length=1).move_to([-1.5,2.5,0])
        s12 = Square(side_length=1).move_to([-0.5,2.5,0])
    
        s13 = Square(side_length=1).move_to([0.5,2.5,0])
        s14 = Square(side_length=1).move_to([1.5,2.5,0])
        s15 = Square(side_length=1).move_to([2.5,2.5,0])
        s16 = Square(side_length=1).move_to([3.5,2.5,0])
        
        g2 = VGroup(s9,s10,s11,s12,s13,s14,s15,s16)
        self.play((Write(g2)),run_time=0.5)

        self.play(s9.animate.set_fill(BLUE_C, opacity=1),run_time=0.1)
        self.play(s10.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s11.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s12.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)

        self.play(s13.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s14.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s15.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s16.animate.set_fill(BLUE_C, opacity=1),run_time=0.1)
# row 3
        s17 = Square(side_length=1).move_to([-3.5,1.5,0])
        s18 = Square(side_length=1).move_to([-2.5,1.5,0])
        s19 = Square(side_length=1).move_to([-1.5,1.5,0])
        s20 = Square(side_length=1).move_to([-0.5,1.5,0])
    
        s21 = Square(side_length=1).move_to([0.5,1.5,0])
        s22 = Square(side_length=1).move_to([1.5,1.5,0])
        s23 = Square(side_length=1).move_to([2.5,1.5,0])
        s24 = Square(side_length=1).move_to([3.5,1.5,0])
        
        g3 = VGroup(s17,s18,s19,s20,s21,s22,s23,s24)
        self.play((Write(g3)),run_time=0.5)

        self.play(s17.animate.set_fill(BLUE_C, opacity=1),run_time=0.1)
        self.play(s18.animate.set_fill(MAROON_B, opacity=1),run_time=0.1)
        self.play(s19.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s20.animate.set_fill(BLACK, opacity=1),run_time=0.1)

        self.play(s21.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s22.animate.set_fill(BLACK, opacity=1),run_time=0.1)
        self.play(s23.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s24.animate.set_fill(BLUE_C, opacity=1),run_time=0.1)
# row 4
        s25 = Square(side_length=1).move_to([-3.5,0.5,0])
        s26 = Square(side_length=1).move_to([-2.5,0.5,0])
        s27 = Square(side_length=1).move_to([-1.5,0.5,0])
        s28 = Square(side_length=1).move_to([-0.5,0.5,0])
    
        s29 = Square(side_length=1).move_to([0.5,0.5,0])
        s30 = Square(side_length=1).move_to([1.5,0.5,0])
        s31 = Square(side_length=1).move_to([2.5,0.5,0])
        s32 = Square(side_length=1).move_to([3.5,0.5,0])
        
        g4 = VGroup(s25,s26,s27,s28,s29,s30,s31,s32)
        self.play((Write(g4)),run_time=0.5)

        self.play(s25.animate.set_fill(MAROON_B, opacity=1),run_time=0.1)
        self.play(s26.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s27.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s28.animate.set_fill(BLUE_E, opacity=1),run_time=0.1)

        self.play(s29.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s30.animate.set_fill(BLUE_E, opacity=1),run_time=0.1)
        self.play(s31.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s32.animate.set_fill(MAROON_B, opacity=1),run_time=0.1)
        
# row 5
        s33 = Square(side_length=1).move_to([-3.5,-0.5,0])
        s34 = Square(side_length=1).move_to([-2.5,-0.5,0])
        s35 = Square(side_length=1).move_to([-1.5,-0.5,0])
        s36 = Square(side_length=1).move_to([-0.5,-0.5,0])
    
        s37 = Square(side_length=1).move_to([0.5,-0.5,0])
        s38 = Square(side_length=1).move_to([1.5,-0.5,0])
        s39 = Square(side_length=1).move_to([2.5,-0.5,0])
        s40 = Square(side_length=1).move_to([3.5,-0.5,0])
        
        g5 = VGroup(s33,s34,s35,s36,s37,s38,s39,s40)
        self.play((Write(g5)),run_time=0.5)

        self.play(s33.animate.set_fill(MAROON_B, opacity=1),run_time=0.1)
        self.play(s34.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s35.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s36.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)

        self.play(s37.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s38.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s39.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s40.animate.set_fill(MAROON_B, opacity=1),run_time=0.1)
# group 6    
        s41 = Square(side_length=1).move_to([-3.5,-1.5,0])
        s42 = Square(side_length=1).move_to([-2.5,-1.5,0])
        s43 = Square(side_length=1).move_to([-1.5,-1.5,0])
        s44 = Square(side_length=1).move_to([-0.5,-1.5,0])
    
        s45 = Square(side_length=1).move_to([0.5,-1.5,0])
        s46 = Square(side_length=1).move_to([1.5,-1.5,0])
        s47 = Square(side_length=1).move_to([2.5,-1.5,0])
        s48 = Square(side_length=1).move_to([3.5,-1.5,0])
        
        g6 = VGroup(s41,s42,s43,s44,s45,s46,s47,s48)
        self.play((Write(g6)),run_time=0.5)

        self.play(s41.animate.set_fill(BLUE_C, opacity=1),run_time=0.1)
        self.play(s42.animate.set_fill(MAROON_B, opacity=1),run_time=0.1)
        self.play(s43.animate.set_fill(MAROON_C, opacity=1),run_time=0.1)
        self.play(s44.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)

        self.play(s45.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s46.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s47.animate.set_fill(MAROON_C, opacity=1),run_time=0.1)
        self.play(s48.animate.set_fill(BLUE_C, opacity=1),run_time=0.1)
# group 7    
        s49 = Square(side_length=1).move_to([-3.5,-2.5,0])
        s50 = Square(side_length=1).move_to([-2.5,-2.5,0])
        s51 = Square(side_length=1).move_to([-1.5,-2.5,0])
        s52 = Square(side_length=1).move_to([-0.5,-2.5,0])
    
        s53 = Square(side_length=1).move_to([0.5,-2.5,0])
        s54 = Square(side_length=1).move_to([1.5,-2.5,0])
        s55 = Square(side_length=1).move_to([2.5,-2.5,0])
        s56 = Square(side_length=1).move_to([3.5,-2.5,0])
        
        g7 = VGroup(s49,s50,s51,s52,s53,s54,s55,s56)
        self.play((Write(g7)),run_time=0.5)

        self.play(s49.animate.set_fill(BLUE_C, opacity=1),run_time=0.1)
        self.play(s50.animate.set_fill(PINK, opacity=1),run_time=0.1)
        self.play(s51.animate.set_fill(MAROON_B, opacity=1),run_time=0.1)
        self.play(s52.animate.set_fill(MAROON_B, opacity=1),run_time=0.1)

        self.play(s53.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s54.animate.set_fill(MAROON_A, opacity=1),run_time=0.1)
        self.play(s55.animate.set_fill(PINK, opacity=1),run_time=0.1)
        self.play(s56.animate.set_fill(BLUE_C, opacity=1),run_time=0.1)

# group 8    
        s57 = Square(side_length=1).move_to([-3.5,-3.5,0])
        s58 = Square(side_length=1).move_to([-2.5,-3.5,0])
        s59 = Square(side_length=1).move_to([-1.5,-3.5,0])
        s60 = Square(side_length=1).move_to([-0.5,-3.5,0])
    
        s61 = Square(side_length=1).move_to([0.5,-3.5,0])
        s62 = Square(side_length=1).move_to([1.5,-3.5,0])
        s63 = Square(side_length=1).move_to([2.5,-3.5,0])
        s64 = Square(side_length=1).move_to([3.5,-3.5,0])
        
        g8 = VGroup(s57,s58,s59,s60,s61,s62,s63,s64)
        self.play((Write(g8)),run_time=0.5)

        self.play(s57.animate.set_fill(GREEN_D, opacity=1),run_time=0.1)
        self.play(s58.animate.set_fill(MAROON_B, opacity=1),run_time=0.1)
        self.play(s59.animate.set_fill(LIGHT_PINK, opacity=1),run_time=0.1)
        self.play(s60.animate.set_fill(LIGHT_PINK, opacity=1),run_time=0.1)

        self.play(s61.animate.set_fill(GREEN_D, opacity=1),run_time=0.1)
        self.play(s62.animate.set_fill(MAROON_B, opacity=1),run_time=0.1)
        self.play(s63.animate.set_fill(LIGHT_PINK, opacity=1),run_time=0.1)
        self.play(s64.animate.set_fill(GREEN_D, opacity=1),run_time=0.1)
    
        fullGroup = VGroup(g1,g2,g3,g4,g5,g6,g7,g8)
        self.play(FadeOut(grid),run_time=1)
        
        self.play(ApplyWave(fullGroup),run_time=2)
        for group in fullGroup:
            for square in group:
                self.play(Indicate(square),run_time=0.02)
                square.set_stroke(width=0)
        
        self.wait(1.0)
        self.play(Unwrite(fullGroup),run_time=1)

        