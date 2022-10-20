from manim import *

##Prim's algorithm##

# Firstly we define the graph for the animation using the mobject in manim "Graph"
def graph():
    vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    edges = [(1, 2), (2, 3),(2,8), (3, 4), (4, 5),(5,6),(4,6),(3,6),(6,7),(7,8),(8,1),(8,9),(3,9),(9,7)]
    g = Graph(vertices, edges, layout="kamada_kawai", layout_scale=3,
                  labels=True)
    return g
# we are writing the costs for each vertices
def costs():    
    text12=Text("4")
    text18=Text("8")
    text23=Text("8")
    text34=Text("7")
    text45=Text("9")
    text56=Text("10")
    text46=Text("14")
    text36=Text("4")
    text67=Text("2")
    text39=Text("2")
    text28=Text("11")
    text78=Text("1")
    text79=Text("6")
    text89=Text("7")
    costs=[text12,text18,text23,text34,text45,text56,text46,text36,text67, text39, text28, text78, text79, text89]
    return costs

def pseudocode():
    text1=MathTex(r" MST-PRIM(g)").scale(0.6)
    text2=MathTex(r"1.\enspace   EDGES \gets \emptyset").scale(0.6)
    text3 = MathTex(r"2.\enspace  Reachset \gets \emptyset").scale(0.6)
    text4 = MathTex(r"3.\enspace  UnReach \gets \emptyset").scale(0.6)
    text5=MathTex(r"4 \enspace  add \enspace an \enspace arbitrary \enspace vertex \enspace ").scale(0.6)
    text55=MathTex(r" \enspace   to \enspace Reachset").scale(0.6)
    text6=MathTex(r"5. \enspace while \enspace Reachset \neq G.V").scale(0.6)
    text7=MathTex(r"6. \quad find \enspace (v, u) \enspace be \enspace the \enspace min \enspace edge").scale(0.6)
    text8=MathTex(r"7. \quad Edges = Edges \cup {(v, u)} ").scale(0.6)
    text9=MathTex(r"8. \quad Reachset = Reachset \cup \{u\} ").scale(0.6)
    text10=MathTex(r"9. \quad UnReach = UnReach \setminus \{v\} ").scale(0.6)
    text11=MathTex(r"10. \enspace return \enspace edges ").scale(0.6)
    text6[0][2:7].set_color(YELLOW)
    text11[0][3:9].set_color(YELLOW)
    pseudo=[text1,text2,text3,text4,text5,text55,text6,text7,text8,text9,text10,text11]
    return pseudo

class PrimAnim(Scene):
    def construct(self):
        #add the graph to the scene
        g=graph()
        self.add(g)
        self.play(Create(g))

        #introduction part
        title = Text("Prim's algorithm")
        title.scale(1.2)
        
        title.next_to(g, UP)
        self.play(Write(title))
        self.wait(5)
        
        why_study = Text(" Why is Prim's algorithm important?")
        why_study.next_to(g, DOWN)
        self.play(Write(why_study))
        self.wait(3)

        definition = Text("It enhances a very intuitive way of finding MSTs")
        definition.next_to(g, DOWN)
        self.play(ReplacementTransform(why_study, definition))
        self.wait(4)

        representation = Text("Where can we apply this greedy method?")
        representation.next_to(g, DOWN)
        self.play(ReplacementTransform(definition, representation),)
        self.wait(3)
     
    #   problems = Text("The optimization problem starts with a graph...")
     #   problems.next_to(g, DOWN)
      #  self.play(ReplacementTransform(representation, problems),)

        self.wait(4)
        self.play(
            FadeOut(title),
            FadeOut(representation),
			)
        
        co = costs()

        
        Write(co[0].scale(0.65).next_to([2.3,0,0]))
        self.play(Write(co[0].scale(0.65).next_to([2.3,0,0])))
        self.add(co[0])

       
        self.play(Write(co[1].scale(0.65).next_to([1.85,-1.45,0])))
        Write(co[1].scale(0.65).next_to([1.85,-1.45,0]))
        self.add(co[1])
        
        
        self.play(Write(co[2].scale(0.65).next_to([0.75,0.95,0])))
        Write(co[2].scale(0.65).next_to([0.75,0.95,0]))
        self.add(co[2])
        
        
        self.play(Write(co[3].scale(0.65).next_to([-0.90,1.55,0])))
        Write(co[3].scale(0.65).next_to([-0.90,1.55,0]))
        self.add(co[3])


        self.play(Write(co[4].scale(0.65).next_to([-2.6,1.5,0])))
        Write(co[4].scale(0.65).next_to([-2.6,1.5,0]))
        self.add(co[4])

    
        self.play(Write(co[5].scale(0.65).next_to([-2.75,0.3,0])))
        Write(co[5].scale(0.65).next_to([-2.75,0.3,0]))
        self.add(co[5])

        
        self.play(Write(co[6].scale(0.65).next_to([-2.05,0.85,0])))
        Write(co[6].scale(0.65).next_to([-2.05,0.85,0]))
        self.add(co[6])

        
        self.play(Write(co[7].scale(0.65).next_to([-1.1,0.37,0])))
        Write(co[7].scale(0.65).next_to([-1.1,0.37,0]))
        self.add(co[7])

        
        self.play(Write(co[8].scale(0.65).next_to([-1.65,-0.7,0])))
        Write(co[8].scale(0.65).next_to([-1.65,-0.7,0]))
        self.add(co[8])
        
        
        self.play(Write(co[9].scale(0.65).next_to([0.05,0.2,0])))
        Write(co[9].scale(0.65).next_to([0.05,0.2,0]))
        self.add(co[9])

        
        self.play(Write(co[10].scale(0.65).next_to([1.00,-0.25,0])))
        Write(co[10].scale(0.65).next_to([1.00,-0.25,0]))
        self.add(co[10])

        
        co[11].next_to(g[1],DOWN)
        self.play(Write(co[11].scale(0.65).next_to([0.15,-1.65,0])))
        Write(co[11].scale(0.65).next_to([0.15,-1.65,0]))
        self.add(co[11])


        self.play(Write(co[12].scale(0.65).next_to([-0.20,-1.10,0])))
        Write(co[12].scale(0.65).next_to([-0.20,-1.10,0]))
        self.add(co[12])

        
        self.play(Write(co[13].scale(0.65).next_to([0.28,-1.10,0])))
        Write(co[13].scale(0.65).next_to([0.28,-1.10,0]))
        self.add(co[13])

        #creating another a new mobject with all costs
        g1=VGroup(g, co[0], co[1], co[2], co[3], co[4], co[5], co[6], co[7], co[8], co[9], co[10], co[11], co[12], co[13])
        g1.move_to(LEFT)		
        self.play(g1.animate.shift(LEFT))  

        #positioning the pseudocode
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
        gr5 =  VGroup(pcode[4], pcode[5])
        gr6 =VGroup(pcode[6])
        gr7 =VGroup(pcode[7])
        gr8 = VGroup( pcode[8], pcode[9], pcode[10])
        gr11 = VGroup(pcode[11])
		
        self.add(gr1,gr2, gr5, gr6, gr7, gr8, gr11)

        self.wait(2)
        self.play(Circumscribe(SurroundingRectangle(gr2, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr5, corner_radius=0.2),run_time=3))
        self.play(FadeToColor(g[1], color=RED))
        self.wait(2)
        self.play(Indicate(Circle().surround(g[1])), run_time=2)
        self.play(Circumscribe(SurroundingRectangle(gr6, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=4))
        self.play(Indicate(g[2]),
		         Indicate(g[8]))
        self.wait(3) 
        self.play(Indicate(Circle().surround(g[2])), run_time=2)
        self.wait(2)
        self.play(FadeToColor(g[2], color=RED))
        self.play(Create(g.add_edges((1,2),edge_config={(1, 2): {"stroke_color": RED}})))
        self.play(Circumscribe(SurroundingRectangle(gr8, corner_radius=0.2),run_time=3))
        
        self.play(Circumscribe(SurroundingRectangle(gr6, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=4))
        self.play(Indicate(g[3]),
		         Indicate(g[8]))
        self.play(Indicate(Circle().surround(g[3])), run_time=2)
        self.play(FadeToColor(g[3], color=RED))
        self.play(Create(g.add_edges((2,3),edge_config={(2, 3): {"stroke_color": RED}},vertex_config={2: {"fill_color": RED}})))
        self.play(Circumscribe(SurroundingRectangle(gr8, corner_radius=0.2),run_time=3)) 
        #
        self.wait(2)
        self.play(Circumscribe(SurroundingRectangle(gr6, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=4))
        self.play(Indicate(g[9]),
		         Indicate(g[8]),Indicate(g[4]),Indicate(g[6]))
        self.wait(2)         
        self.play(Indicate(Circle().surround(g[9])), run_time=2)
        self.wait(2)
        self.play(FadeToColor(g[9], color=RED))
        self.play(Create(g.add_edges((3,9),edge_config={(3, 9): {"stroke_color": RED}})))                  
        self.play(Circumscribe(SurroundingRectangle(gr8, corner_radius=0.2),run_time=3))
        self.wait(2)
        
        self.play(Circumscribe(SurroundingRectangle(gr6, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=4))
        self.play(Indicate(g[7]),
		         Indicate(g[8]),Indicate(g[4]),Indicate(g[6]))
        self.play(Indicate(Circle().surround(g[6])), run_time=2)
        self.wait(2)
        self.play(FadeToColor(g[6], color=RED))
        self.play(Create(g.add_edges((3,6),edge_config={(3, 6): {"stroke_color": RED}})))
        self.play(Circumscribe(SurroundingRectangle(gr8, corner_radius=0.2),run_time=3)) 
        
        self.wait(2)
        self.play(Circumscribe(SurroundingRectangle(gr6, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=4))
        self.play(Indicate(g[7]),
		         Indicate(g[8]),Indicate(g[4]),Indicate(g[5]))
        self.play(Indicate(Circle().surround(g[7])), run_time=2)
        self.wait(2)
        self.play(FadeToColor(g[7], color=RED))
        self.play(Create(g.add_edges((6,7),edge_config={(6, 7): {"stroke_color": RED}})))
        self.play(Circumscribe(SurroundingRectangle(gr8, corner_radius=0.2),run_time=3))
        
        self.play(Circumscribe(SurroundingRectangle(gr6, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=4))
        self.wait(2)
        self.play(Indicate(g[8]),Indicate(g[4]),Indicate(g[5]))
        self.play(Indicate(Circle().surround(g[8])), run_time=2)
        self.wait(2)
        self.play(FadeToColor(g[8], color=RED))
        self.play(Create(g.add_edges((7,8),edge_config={(7, 8): {"stroke_color": RED}})))
        self.play(Circumscribe(SurroundingRectangle(gr8, corner_radius=0.2),run_time=3))
        
        self.play(Circumscribe(SurroundingRectangle(gr6, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=4))
        self.wait(2)
        self.play(Indicate(g[4]),Indicate(g[5]))
        self.play(Indicate(Circle().surround(g[4])), run_time=2)
        self.wait(2)
        self.play(FadeToColor(g[4], color=RED))
        self.play(Create(g.add_edges((3,4),edge_config={(3, 4): {"stroke_color": RED}})))
        self.play(Circumscribe(SurroundingRectangle(gr8, corner_radius=0.2),run_time=3))
        
        self.play(Circumscribe(SurroundingRectangle(gr6, corner_radius=0.2),run_time=2))
        self.play(Circumscribe(SurroundingRectangle(gr7, corner_radius=0.2),run_time=4))
        self.wait(2)
        self.play(Indicate(g[5]))
        self.play(Indicate(Circle().surround(g[5])), run_time=2)
        self.wait(2)
        self.play(FadeToColor(g[5], color=RED))
        self.play(Create(g.add_edges((4,5),edge_config={(4, 5): {"stroke_color": RED}})))
        self.play(Circumscribe(SurroundingRectangle(gr8, corner_radius=0.2),run_time=3))
        self.play(Circumscribe(SurroundingRectangle(gr11, corner_radius=0.2),run_time=3)) 

        self.play(FadeOut( co[1],run_time=1))
        self.play(FadeOut( g.remove_edges((1, 8)),run_time=2))
        self.play(FadeOut( co[10],run_time=1))
        self.play(FadeOut( g.remove_edges((2, 8)),run_time=2))
        self.play(FadeOut( co[12],run_time=1))
        self.play(FadeOut( g.remove_edges((7, 9)),run_time=2))
        self.play(FadeOut( co[13],run_time=1))
        self.play(FadeOut( g.remove_edges((8, 9)),run_time=2))
        self.play(FadeOut( co[5],run_time=1))
        self.play(FadeOut( g.remove_edges((5, 6)),run_time=2))
        self.play(FadeOut( co[6],run_time=1))
        self.play(FadeOut( g.remove_edges((4, 6)),run_time=2))

        self.wait(5)


