#Visualizer om een galgje te printen. Wordt aangeroepen vanuit het interactieve gedeelte
class GalgjeVisualizer:
    def __init__(self):
        self.galgjeLijst = ["""
                               __________
                                |/   |     
                                |   (_)    
                                |   /|\           
                                |    |        
                                |   / \        
                                |               
                                |___

                            """,
                            """
                               __________
                                |/   |     
                                |   (_)    
                                |   /|\           
                                |    |        
                                |   /         
                                |               
                                |___

                            """,
                            """
                                __________
                                |/   |     
                                |   (_)    
                                |   /|\           
                                |    |        
                                |           
                                |               
                                |___

                            """,
                            """                                                         
                               __________
                                |/   |     
                                |   (_)    
                                |   /|\           
                                |            
                                |           
                                |               
                                |___

                            """,
                            """
                               __________
                                |/   |     
                                |   (_)    
                                |   / \           
                                |            
                                |           
                                |               
                                |___

                            """,
                            """
                               __________
                                |/   |     
                                |   (_)    
                                |   /           
                                |            
                                |           
                                |               
                                |___
                            
                            """,
                            """
                               __________
                                |/   |     
                                |   (_)    
                                |              
                                |           
                                |           
                                |               
                                |___

                            """,
                            """                            
                               __________
                                |/   |     
                                |   (_    
                                |              
                                |           
                                |           
                                |               
                                |___

                            """,
                            """
                               __________
                                |/   |     
                                |   (    
                                |              
                                |           
                                |           
                                |               
                                |___

                            """,
                            """
                               __________
                                |/   |     
                                |       
                                |              
                                |           
                                |           
                                |               
                                |___
                        
                            """,
                           """
                               __________
                                |/         
                                |       
                                |              
                                |           
                                |           
                                |               
                                |___
                        
                            """                            
                            ]
    #Deze functie geeft een string terug met het galgje dat hoort bij het aantal pogingen
    # De waarde 10 betekent dat alleen de galg er staat.
    # De waarde 0 betekent dat er geen pogingen meer over zijn en dat je 'hangt'    
    def PrintGalgje(self, aantalPogingen): 
        return "\n" + self.galgjeLijst[aantalPogingen]