from .I_FILE_reference import I_FILE_reference


class FILE_reference(I_FILE_reference):
    
    def STR_param(self, file, conf = False, G = 0, P = 0):
         try:
            try:
                R = self.STR_refer()
                VR = self.DIGIT_allow(file.split("R"))
                str_refer = [key for key,value in R.items() if value == int(VR)][0]
            except Exception as e:
                str_refer = self.STR_rntfound(file)
        
            try:
                B = self.STR_bench()
                VB = self.DIGIT_allow(file.split("B"))
                str_bench = [key for key,value in B.items() if value == int(VB)][0]
            except Exception as e:
                str_bench = self.STR_bntfound(file)   

            RB = file[0:file.rfind("G")]
            RB_after = file.split(RB)[1]        
            M = self.DIGIT_allow(RB_after.split("M"))
            K = self.DIGIT_allow(RB_after.split("K"))
            D = self.DIGIT_allow(RB_after.split("D"))
            N = self.DIGIT_allow(RB_after.split("N"))

            try:
                G = self.DIGIT_allow(RB_after.split("G"))
            except Exception as e:
                pass

            try:
                P = self.DIGIT_allow(RB_after.split("P"))
            except Exception as e:
                pass

            return (str_refer,str_bench,M,K,D,N,G,P) if conf == False else (M,K,N,D,str_bench,str_refer,G,P)
         except Exception as er:
            return 0,0,0
         

    def STR_rntfound(self,file):
        STR_DIRTY = str(file)
        STR = STR_DIRTY.split('analysis/')[1]
        BLOCK = STR[1:STR.rfind('G')]
        DIV = BLOCK.split('_B')
        return DIV[0]
    

    def STR_refer(self):
        dict_refer = {
            "IN POF"   : 1,
            "OUT POF"  : 2,
            "NEAR POF" : 3,
            "NSGA-3"   : 10,
            "SPEA-2"   : 11,
            "UNSGA-3"  : 12,
            "MOEAD"    : 13,
            "RVEA"     : 14,
            "NSGA-2"   : 15,
            
        }
        return dict_refer
    

    def STR_bntfound(self,file):
        STR_DIRTY = str(file)
        STR = STR_DIRTY.split('analysis/')[1]
        BLOCK = STR[1:STR.rfind('G')]
        DIV = BLOCK.split('_B')
        return DIV[1]
     

    def STR_bench(self):
        dict_bench = {
             "DTLZ1"   : 10,
             "DTLZ2"   : 20,
             "DTLZ3"   : 30,
             "DTLZ4"   : 40,
             "DTLZ5"   : 50,
             "DTLZ6"   : 60,
             "DTLZ7"   : 70,
             "DTLZ8"   : 80,
             "DTLZ9"   : 90,
             "DPF1"    : 11,
             "DPF2"    : 12,
             "DPF3"    : 13,
             "DPF4"    : 14,
             "DPF5"    : 15,
        }
        return dict_bench
    

    def DIGIT_allow(self,arr_str):
        v_str = ""
        for i in arr_str[1]:
                if i.isdigit():
                    v_str=v_str+i
                else:
                    break
        return v_str
    