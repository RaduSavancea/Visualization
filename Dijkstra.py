from cProfile import label
from manim import *

##Dijkstra's algorithm##

# Firstly we define the graph for the animation using the mobject in manim "Graph"
def graph():
    vertices = [1, 2, 3, 4, 5, 6]
    edges = [(1, 2),  (2, 3), (3, 4), (4,5), (5,6),(1,6), (2,6),(3,6),(3,4),(3,5)]
    g = Graph(vertices, edges, layout="kamada_kawai", layout_scale=3,
                  vertex_config={'radius': 0.35})
    return g

def labels():
    label0=MathTex(r"B", color=BLACK).scale(1.2)
    label1=MathTex(r"A", color=BLACK).scale(1.2)
    label2=MathTex(r"D", color=BLACK).scale(1.2)
    label3=MathTex(r"F",color=BLACK).scale(1.2)
    label4=MathTex(r"E",color=BLACK).scale(1.2)
    label5=MathTex(r"C",color=BLACK).scale(1.2)
    lab=[label0,label1,label2, label3, label4, label5]
    return lab
def costs():    
    text12=Text("2")
    text18=Text("8")
    text23=Text("5")
    text34=Text("6")
    text45=Text("3")
    text56=Text("2")
    text46=Text("1")
    text36=Text("9")
    text67=Text("3")
    costs=[text12,text18,text23,text34,text45,text56,text46,text36,text67]
    return costs
def pseudocode():
    text1=MathTex(r" Dijkstra(G, s)").scale(0.6)
    text2=MathTex(r"1.\enspace    set \enspace all \enspace vertices \enspace v.prev \gets \emptyset").scale(0.6)
    text3 = MathTex(r"2.\enspace  set \enspace all \enspace vertices \enspace v.key  \gets \infty").scale(0.6)
    text4 = MathTex(r"3.\enspace  UnReach \gets G.V").scale(0.6)
    text5=MathTex(r"4 .\enspace s.key \gets 0 ").scale(0.6)
    text55=MathTex(r"5. \enspace   while \enspace UnReach \neq \emptyset").scale(0.6)
    text6=MathTex(r"6. \quad v \gets ExtractMin(UnReach)").scale(0.6)
    text7=MathTex(r"7. \quad for \enspace each \enspace neighbor \enspace u \enspace of  \enspace v").scale(0.6)
    text8=MathTex(r"8. \qquad  //Relax {(v, u)} ").scale(0.6)
    text9=MathTex(r"9. \quad if \enspace u.key > v.key + wgt(u,v) ").scale(0.6)
    text10=MathTex(r"10. \qquad u.key = v.key + wgt(u,v)  ").scale(0.6)
    text11=MathTex(r"11. \qquad u.previous=v").scale(0.6)
    text55[0][2:7].set_color(YELLOW)
    text7[0][2:5].set_color(YELLOW)
    text9[0][2:4].set_color(RED)
    pseudo=[text1,text2,text3,text4,text5,text55,text6,text7,text8,text9,text10,text11]
    return pseudo

class DijAnim(Scene):
    def construct(self):
        g=graph()
        self.add(g)
        self.play(Create(g))

        title = Text("Dijkstra's algorithm")
        title.scale(1.2)
        
        title.next_to(g, UP)
        self.play(Write(title))
        self.wait(4)

        sh_path = Text(" Dijkstra is a shorthest path algorithm")
        sh_path.next_to(g, DOWN)
        self.play(Write(sh_path))
        self.wait(3)

        problems = Text("Let's see how it works")
        problems.next_to(g, DOWN)
        self.play(ReplacementTransform(sh_path, problems),)

        self.wait(4)
        self.play(
            FadeOut(title),
            FadeOut(problems),
			)
        

        lab=labels()
        #labels
        Write(lab[0].scale(0.65).next_to([-1.24,0.71,0]))
        self.play(Write(lab[0].scale(0.65).next_to([-1.24,0.71,0])))

        Write(lab[1].scale(0.65).next_to([-3.34,0,0]))
		#Write(label11.scale(0.65).next_to([-3.34,0,0]))
        self.play(Write(lab[1].scale(0.65).next_to([-3.34,0,0])))

        Write(lab[2].scale(0.65).next_to([-1.61,-1.46,0]))
        self.play(Write(lab[2].scale(0.65).next_to([-1.61,-1.46,0])))

        Write(lab[3].scale(0.65).next_to([0.56,-0.69,0]))
        self.play(Write(lab[3].scale(0.65).next_to([0.56,-0.69,0])))

        Write(lab[4].scale(0.65).next_to([0.93, 1.41,0]))
        self.play(Write(lab[4].scale(0.65).next_to([0.93, 1.41,0])))

        Write(lab[5].scale(0.65).next_to([2.67, 0,0]))
        self.play(Write(lab[5].scale(0.65).next_to([2.67, 0,0])))

        #costs
        co=costs()
        Write(co[0].scale(0.65).next_to([-2.30,0.58,0]))
        self.play(Write(co[0].scale(0.65).next_to([-2.30,0.58,0])))
        self.add(co[0])

        Write(co[1].scale(0.65).next_to([-2.52,-0.97,0]))
        self.play(Write(co[1].scale(0.65).next_to([-2.52,-0.97,0])))
        self.add(co[1])

        Write(co[2].scale(0.65).next_to([-1.6,-0.3,0]))
        self.play(Write(co[2].scale(0.65).next_to([-1.6,-0.3,0])))
        self.add(co[2])

        Write(co[3].scale(0.65).next_to([-0.1,1.27,0]))
        self.play(Write(co[3].scale(0.65).next_to([-0.1,1.27,0])))
        self.add(co[3])

        Write(co[4].scale(0.65).next_to([-0.48,-0.1,0]))
        self.play(Write(co[4].scale(0.65).next_to([-0.48,-0.1,0])))
        self.add(co[4])

        Write(co[5].scale(0.65).next_to([-0.68,-0.87,0]))
        self.play(Write(co[5].scale(0.65).next_to([-0.68,-0.87,0])))
        self.add(co[5])

        Write(co[6].scale(0.65).next_to([0.64,0.46,0]))
        self.play(Write(co[6].scale(0.65).next_to([0.64,0.46,0])))
        self.add(co[6])

        Write(co[7].scale(0.65).next_to([0.64,0.46,0]))
        self.play(Write(co[7].scale(0.65).next_to([1.93,0.85,0])))
        self.add(co[7])

        Write(co[8].scale(0.65).next_to([0.64,0.46,0]))
        self.play(Write(co[8].scale(0.65).next_to([1.59,-0.58,0])))
        self.add(co[8])

        
        
        
        
        g1=VGroup(g, lab[1], lab[0], lab[2], lab[3], lab[4], lab[5], co[0], co[1], co[2], co[3], co[4], co[5], co[6], co[7], co[8])
        g1.move_to(LEFT)		
        self.play(g1.animate.shift(LEFT))
        self.wait(2)
        
        pcode=pseudocode()
        pcode[0].move_to([3.5,3.5,0])

       # for i in range(1, len(pcode)):
        #    pcode[i].next_to((pcode[i-1],DOWN))
        pcode[1].next_to(pcode[0],DOWN)
        pcode[2].next_to(pcode[1],DOWN)
        
        pcode[3].next_to( pcode[2],DOWN)
        pcode[4].next_to( pcode[3],DOWN)
        pcode[5].next_to( pcode[4],DOWN)
        pcode[6].next_to( pcode[5],DOWN)
        pcode[7].next_to( pcode[6],DOWN)
        pcode[8].next_to( pcode[7],DOWN)
        pcode[9].next_to( pcode[8],DOWN)
        pcode[10].next_to( pcode[9],DOWN)
        pcode[11].next_to(pcode[10],DOWN)
        
        # allignation of the pseudocode and grouping the code blocks in order to highlight them as the algorithm progresses
        gr0 = VGroup(pcode[0], pcode[1],pcode[2],pcode[3],pcode[4],pcode[5] ,pcode[6], pcode[7], pcode[8], pcode[9], pcode[10], pcode[11])
        gr0.arrange(DOWN, center=False, aligned_edge=LEFT) 
        self.play(FadeIn(gr0))
        
        gr1 = VGroup(pcode[0])
        gr2 = VGroup(pcode[1], pcode[2], pcode[3])
        gr4 =  VGroup(pcode[4])
        gr5 =  VGroup(pcode[5])
        gr6 =VGroup(pcode[6])
        gr7 =VGroup(pcode[7])
        gr8 = VGroup( pcode[8])
        gr9 = VGroup( pcode[9])
        gr10 = VGroup(pcode[10])
        gr11 = VGroup(pcode[11])
		
        self.add(gr1,gr2,gr4, gr5, gr6, gr7, gr8, gr9, gr10, gr11)

        self.wait(2)
        self.play(Circumscribe(SurroundingRectangle(gr2, corner_radius=0.2),run_time=2))
        texti1=MathTex(r"\infty", color=BLACK).scale(0.8)
        texti2=MathTex(r"\infty", color=BLACK).scale(0.8)
        texti3=MathTex(r"\infty", color=BLACK).scale(0.8)
        texti4=MathTex(r"\infty", color=BLACK).scale(0.8)
        texti5=MathTex(r"\infty", color=BLACK).scale(0.8)
        texti0=MathTex(r"\infty", color=BLACK).scale(0.8)
        Write(texti1.scale(0.65).next_to(lab[1].get_center()-[0.35,0,0]))
        self.play(ReplacementTransform(lab[1], texti1),)
        Write(texti2.scale(0.65).next_to(lab[2].get_center()-[0.37,0,0]))
        self.play(ReplacementTransform(lab[2], texti2),)
        Write(texti0.scale(0.65).next_to(lab[0].get_center()-[0.35,0.02,0]))
        self.play(ReplacementTransform(lab[0], texti0),)
        Write(texti3.scale(0.65).next_to(lab[3].get_center()-[0.37,0,0]))
        self.play(ReplacementTransform(lab[3], texti3),)
        Write(texti4.scale(0.65).next_to(lab[4].get_center()-[0.35,-0.03,0]))
        self.play(ReplacementTransform(lab[4], texti4),)
        Write(texti5.scale(0.65).next_to(lab[5].get_center()-[0.35,0,0]))
        self.play(ReplacementTransform(lab[5], texti5),)
        

        self.play(Circumscribe(SurroundingRectangle(gr4, corner_radius=0.2),run_time=3))
        text0=Text("0", color=BLACK).scale(0.8)
        text2=Text("2", color=BLACK).scale(0.8)
        text8=Text("8", color=BLACK).scale(0.8)
        Write(text0.scale(0.65).next_to(lab[1].get_center()-[0.35,0,0]))
        self.play(ReplacementTransform(texti1, text0),)
        self.play(Circumscribe(SurroundingRectangle(gr5, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr6, corner_radius=0.2),run_time=2))
        self.play(FadeToColor(g[4], color=RED))
        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=2))
        self.play(Indicate(g[3]),
		         Indicate(g[5]))

        self.play(Circumscribe(SurroundingRectangle(gr8, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr9, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr10, corner_radius=0.2),run_time=2))
        Write(text2.scale(0.65).next_to(lab[0].get_center()-[0.35,0,0]))
        Write(text8.scale(0.65).next_to(lab[2].get_center()-[0.35,0,0]))
        self.play(ReplacementTransform(texti2, text8),)

        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr8, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr9, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr10, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr11, corner_radius=0.2),run_time=2))
        self.play(ReplacementTransform(texti0, text2),)

        self.play(Circumscribe(SurroundingRectangle(gr5, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr6, corner_radius=0.2),run_time=2))
        self.play(FadeToColor(g[3], color=RED))

        text48=Text("8", color=BLACK).scale(0.8)
        Write(text48.scale(0.65).next_to(lab[4].get_center()-[0.35,0,0]))
        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr8, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr9, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr10, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr11, corner_radius=0.2),run_time=2))
        self.play(ReplacementTransform(texti4, text48),)

        text35=Text("5", color=BLACK).scale(0.8)
        Write(text35.scale(0.65).next_to(lab[3].get_center()-[0.35,0,0]))
        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr8, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr9, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr10, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr11, corner_radius=0.2),run_time=2))
        self.play(ReplacementTransform(texti3, text35),)

        text27=Text("7", color=BLACK).scale(0.8)
        Write(text27.scale(0.65).next_to(lab[2].get_center()-[0.35,0,0]))
        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr8, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr9, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr10, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr11, corner_radius=0.2),run_time=2))
        self.play(ReplacementTransform(text8, text27),)

        self.play(Circumscribe(SurroundingRectangle(gr5, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr6, corner_radius=0.2),run_time=2))
        self.play(FadeToColor(g[6], color=RED))

        self.play(Indicate(g[1]),
		         Indicate(g[2]),Indicate(g[5]))

        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr8, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr9, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr10, corner_radius=0.2),run_time=2))
        
        text58=Text("8", color=BLACK).scale(0.8)
        Write(text58.scale(0.65).next_to(lab[5].get_center()-[0.35,0,0]))
        self.play(ReplacementTransform(texti5, text58),)
        self.play(Circumscribe(SurroundingRectangle(gr11, corner_radius=0.2),run_time=2))

        text46=Text("6", color=BLACK).scale(0.8)
        Write(text46.scale(0.65).next_to(lab[4].get_center()-[0.35,0,0]))
        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr8, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr9, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr10, corner_radius=0.2),run_time=2))
        self.play(ReplacementTransform( text48, text46),)
        self.play(Circumscribe(SurroundingRectangle(gr11, corner_radius=0.2),run_time=2))

        self.play(Circumscribe(SurroundingRectangle(gr5, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr6, corner_radius=0.2),run_time=2))
        self.play(FadeToColor(g[2], color=RED))
        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=2))
        self.play(Indicate(g[1]))

        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr8, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr9, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr10, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr11, corner_radius=0.2),run_time=2))

        self.play(Circumscribe(SurroundingRectangle(gr5, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr6, corner_radius=0.2),run_time=2))
        self.play(FadeToColor(g[5], color=RED))
        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr8, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr9, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr10, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr11, corner_radius=0.2),run_time=2))

        self.play(Circumscribe(SurroundingRectangle(gr5, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr6, corner_radius=0.2),run_time=2))
        self.play(FadeToColor(g[1], color=RED))
        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr8, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr9, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr10, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr11, corner_radius=0.2),run_time=2))


        



