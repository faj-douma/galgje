
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
                        
                            """]
        
    def PrintGalgje(self, aantalPogingen): 
        if aantalPogingen > 0:
            aantalPogingen = aantalPogingen -1
        return "\n" + self.galgjeLijst[aantalPogingen]