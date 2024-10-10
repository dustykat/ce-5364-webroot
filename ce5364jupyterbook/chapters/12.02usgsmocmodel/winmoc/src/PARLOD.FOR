      SUBROUTINE PARLOD                                                 
C      DOUBLE PRECISION DMIN1,DEXP,DLOG,DABS                             
      DOUBLE PRECISION TMRX,VPRM,HI,HR,HC,HK,WT,REC,RECH,TIM,AOPT,TITLE 
      DOUBLE PRECISION XDEL,YDEL,S,AREA,SUMT,RHO,PARAM,TEST,TOL,PINT,   
     1                 HMIN,PYR,ANFCTR                                  
      DOUBLE PRECISION FCTR,TIMX,TINIT,PIES,YNS,XNS,RAT,HMX,HMY         
      DOUBLE PRECISION ANTIM                                            
      DOUBLE PRECISION DXINV,DYINV,ARINV,PORINV                         
      DOUBLE PRECISION ALPHA1,ANITP                                     
      DOUBLE PRECISION TOTLQ,TOTLQI,TPIN,TPOUT                          
      INTEGER OVERRD                                                    
      COMMON /PRMJ/ NTIM,NPMP,NPNT,NITP,N,NX,NY,NP,NREC,INT,NNX,NNY,    
     1              NUMOBS,NMOV,IMOV,NPMAX,ITMAX,NZCRIT,IPRNT,NPTPND,   
     2              NPNTMV,NPNTVL,NPNTD,NPNCHV,NPDELC,ICHK              
      COMMON /PRMC/ NODEID(040,040),NPCELL(020,020),NPOLD(020,020),     
     1              LIMBO(0500),IXOBS(05),IYOBS(05)                     
      COMMON /HEDA/ THCK(040,040),TMWL(05,50),TMOBS(50)                 
      COMMON /HEDB/ TMRX(040,040,2),VPRM(040,040),HI(040,040),          
     1              HR(040,040),HC(040,040),HK(040,040),WT(040,040),    
     2 REC(040,040),RECH(040,040),TIM(100),AOPT(20),TITLE(10),XDEL,YDEL,
     3              S,AREA,SUMT,RHO,PARAM,TEST,TOL,PINT,HMIN,PYR,ANFCTR 
      COMMON /HEDC/ MX,MY,MMX,MMY,NMX,NMY,MCHK                          
      COMMON /HEDD/ TINIT,TIMX                                          
      COMMON /CHMA/ PART(3,06400),CONC(020,020),TMCN(05,50),VX(040,040),
     1              VY(040,040),CONINT(020,020),CNRECH(020,020),POROS,  
     2              SUMTCH,BETA,TIMV,STORM,STORMI,CMSIN,CMSOUT,FLMIN,   
     3              FLMOT,SUMIO,CELDIS,DLTRAT,CSTORM                    
      COMMON /CHMR/ RF,DK,RHOB,THALF,DECAY,ADSORB,SORBI,DMASS1,CSTM2    
      COMMON /BALM/ TOTLQ,TOTLQI,TPIN,TPOUT                             
      COMMON /XINV/ DXINV,DYINV,ARINV,PORINV                            
      COMMON /CHMC/ SUMC(020,020),VXBDY(040,040),VYBDY(040,040)         
C     ***************************************************************   
      IF (INT.GT.1) GO TO 10                                            
      WRITE (6,750)                                                     
      READ (5,720) TITLE
CTGC      READ (5,'(A)') TITLE                                                
      WRITE (6,730) TITLE                                               
C     ***************************************************************   
C     ---INITIALIZE TEST AND CONTROL VARIABLES---                       
      STORMI=0.0                                                        
      SORBI=0                                                           
      RHOB=0.0                                                          
      DK=0.0                                                            
      TEST=0.D0                                                         
      TOTLQ=0.D0                                                        
      TOTLQI=0.D0                                                       
      TPIN=0.D0                                                         
      TPOUT=0.D0                                                        
      SUMT=0.D0                                                         
      SUMTCH=0.0                                                        
      INT=0                                                             
      IPRNT=0                                                           
      MX=1                                                              
      MY=1                                                              
      MCHK=0                                                            
      NCA2=0                                                            
      NCA=0                                                             
      N=0                                                               
      IMOV=0                                                            
      NMOV=0                                                            
      ICHK=0                                                            
      DMASS1=0.0                                                        
      RF=1.0                                                            
      DECAY=0.0                                                         
      THALF=0.0                                                         
C     ***************************************************************   
C     ---LOAD CONTROL PARAMETERS---                                     
CTGC      READ (5,740) NTIM,NPMP,NX,NY,NPMAX,NPNT,NITP,NUMOBS,ITMAX,NREC,NPT
CTGC     1PND,NCODES,NPNTMV,NPNTVL,NPNTD,NPDELC,NPNCHV,NREACT 
      READ (5,*) NTIM,NPMP,NX,NY,NPMAX,NPNT,NITP,NUMOBS,ITMAX,NREC,NPT
     1PND,NCODES,NPNTMV,NPNTVL,NPNTD,NPDELC,NPNCHV,NREACT              
      NMX=NX                                                            
      NMY=NY                                                            
      MMX=NX-1                                                          
      MMY=NY-1                                                          
C        ---READ UPPER LEFT AND LOWER RIGHT NODAL COORDS. OF            
C           TRANSPORT SUBGRID, IN FREE FORMAT, IF NX.LT.0---            
      IF (NX.GT.0) GO TO 5                                              
      NX=-NX                                                            
      MCHK=1                                                            
      READ (5,*) MX,MY,MMX,MMY                                          
      NMX=MMX-MX+1                                                      
      NMY=MMY-MY+1                                                      
    5 CONTINUE                                                          
CTGC      READ (5,800) PINT,TOL,POROS,BETA,S,TIMX,TINIT,XDEL,YDEL,DLTRAT,CEL
CTGC     1DIS,ANFCTR
      READ (5,*) PINT,TOL,POROS,BETA,S,TIMX,TINIT,XDEL,YDEL,DLTRAT,CEL
     1DIS,ANFCTR                                                        
C        ---READ REACTION TERMS IN FREE FORMAT---                       
      IF (NREACT.EQ.1) READ (5,*) DK,RHOB,THALF                         
      NNX=NX-1                                                          
      NNY=NY-1                                                          
      NP=NPMAX                                                          
      DXINV=1.D0/XDEL                                                   
      DYINV=1.D0/YDEL                                                   
      ARINV=DXINV*DYINV                                                 
      PORINV=1.D0/POROS                                                 
      RF=1.0+(DK*RHOB/POROS)                                            
      IF (THALF.GT.0.0) DECAY=ALOG(2.0)/THALF                           
C     ---PRINT CONTROL PARAMETERS---                                    
      WRITE (6,755)                                                     
      WRITE (6,760)                                                     
      WRITE (6,770) NX,NY,XDEL,YDEL                                     
      IF (MCHK.GT.0) WRITE (6,775) NMX,NMY,MX,MY,MMX,MMY                
      WRITE (6,780) NTIM,NPMP,PINT,TIMX,TINIT                           
      WRITE (6,790) S,POROS,BETA,DLTRAT,ANFCTR                          
      WRITE (6,870) NITP,TOL,ITMAX,CELDIS,NPMAX,NPTPND                  
      IF (NPTPND.NE.4.AND.NPTPND.NE.5.AND.NPTPND.NE.8.AND.NPTPND.NE.9.  
     1.AND.NPTPND.NE.16.AND.NPTPND.NE.1) WRITE(6,880)                   
      IF (NPTPND.EQ.1) WRITE (6,882)                                    
      IF((NX.EQ.3.OR.NY.EQ.3).AND.NPTPND.NE.1) WRITE(6,883)             
      IF (NITP.LE.0) WRITE (6,885)                                      
      WRITE (6,888)                                                     
      WRITE (6,890) NPNT,NPNTMV,NPNTVL,NPNTD,NUMOBS,NREC,NCODES,NPNCHV,N
     1PDELC                                                             
      WRITE (6,895) DK,RHOB,RF,THALF,DECAY                              
      GO TO 20                                                          
C     ***************************************************************   
C     ---READ DATA TO REVISE TIME STEPS AND STRESSES FOR SUBSEQUENT     
C        PUMPING PERIODS---                                             
CTGC   10 READ (5,1060) ICHK
   10 READ (5,*) ICHK                                                
      IF (ICHK.LE.0) WRITE (6,1110) INT                                 
      IF (ICHK.LE.0) GO TO 20                                           
C     ---REINITIALIZE REC AND CNRECH IN REC CELLS---                    
      IF (NREC.GT.0) THEN                                               
       DO 12 IY=2,NNY                                                   
       DO 12 IX=2,NNX                                                   
       IF (REC(IX,IY).EQ.0.0) GO TO 12                                  
        REC(IX,IY)=0.D0                                                 
        JX=IX-MX+1                                                      
        JY=IY-MY+1                                                      
        IF (JX.GT.0.AND.JX.LE.NMX.AND.JY.GT.0.AND.JY.LE.NMY)            
     1      CNRECH(JX,JY)=0.0                                           
   12  CONTINUE                                                         
      END IF                                                            
CTGC      READ (5,1070) NTIM,NPNT,NITP,ITMAX,NREC,NPNTMV,NPNTVL,NPNTD,NPDELC
CTGC     1,NPNCHV,PINT,TIMX,TINIT
      READ (5,*) NTIM,NPNT,NITP,ITMAX,NREC,NPNTMV,NPNTVL,NPNTD,NPDELC
     1,NPNCHV,PINT,TIMX,TINIT                                           
      WRITE (6,1080) INT                                                
      WRITE (6,1090) NTIM,NPNT,NITP,ITMAX,NREC,NPNTMV,NPNTVL,NPNTD,NPDEL
     1C,NPNCHV,PINT,TIMX,TINIT                                          
C     ***************************************************************   
C     ---LIST TIME INCREMENTS---                                        
   20 DO 30 J=1,100                                                     
      TIM(J)=0.D0                                                       
   30 CONTINUE                                                          
      PYR=PINT*86400.D0*365.25D0                                        
      TIM(1)=TINIT                                                      
      IF (NPNTMV.EQ.0) NPNTMV=999                                       
      IF (S.GT.0.0) THEN                                                
      DO 40 K=2,NTIM                                                    
   40 TIM(K)=TIMX*TIM(K-1)                                              
      WRITE (6,470)                                                     
      WRITE (6,490) (TIM(K),K=1,NTIM)                                   
      IF (TINIT.GT.PYR) WRITE (6,475)                                   
      ELSE                                                              
   50 ANTIM=NTIM                                                        
      DO 55 K=1,NTIM                                                    
   55 TIM(K)=PYR/ANTIM                                                  
       WRITE (6,480)                                                    
       WRITE (6,490) (TIM(K),K=1,NTIM)                                  
      END IF                                                            
C     ***************************************************************   
C     ---INITIALIZE MATRICES---                                         
   60 IF (INT.GT.1) GO TO 100                                           
      DO 70 IY=1,NY                                                     
      DO 70 IX=1,NX                                                     
      VPRM(IX,IY)=0.D0                                                  
      THCK(IX,IY)=0.0                                                   
      RECH(IX,IY)=0.D0                                                  
      REC(IX,IY)=0.D0                                                   
      NODEID(IX,IY)=0                                                   
      TMRX(IX,IY,1)=0.D0                                                
      TMRX(IX,IY,2)=0.D0                                                
      HI(IX,IY)=0.D0                                                    
      HR(IX,IY)=0.D0                                                    
      HC(IX,IY)=0.D0                                                    
      HK(IX,IY)=0.D0                                                    
      WT(IX,IY)=0.D0                                                    
      VX(IX,IY)=0.0                                                     
      VY(IX,IY)=0.0                                                     
      VXBDY(IX,IY)=0.0                                                  
      VYBDY(IX,IY)=0.0                                                  
   70 CONTINUE                                                          
      DO 75 IY=1,NMY                                                    
      DO 75 IX=1,NMX                                                    
      CNRECH(IX,IY)=0.0                                                 
      CONC(IX,IY)=0.0                                                   
      CONINT(IX,IY)=0.0                                                 
      SUMC(IX,IY)=0.0                                                   
      NPCELL(IX,IY)=0                                                   
   75 CONTINUE                                                          
C     ****************************************************************  
C     ---READ OBSERVATION WELL LOCATIONS---                             
      IF (NUMOBS.LE.0) GO TO 100                                        
      WRITE (6,755)                                                     
      WRITE (6,900)                                                     
      DO 80 J=1,NUMOBS                                                  
CTGC      READ (5,700) IX,IY
      READ (5,*) IX,IY                                                
      WRITE (6,810) J,IX,IY                                             
      IXOBS(J)=IX                                                       
   80 IYOBS(J)=IY                                                       
      DO 90 I=1,NUMOBS                                                  
      DO 90 J=1,50                                                      
      TMWL(I,J)=0.0                                                     
   90 TMCN(I,J)=0.0                                                     
C     ****************************************************************  
C     ---READ PUMPAGE DATA -- (X-Y COORDINATES AND RATE IN CFS)---      
C        ---SIGNS : WITHDRAWAL = POS.;  INJECTION = NEG.---             
C        ---IF INJ. WELL, ALSO READ CONCENTRATION OF INJECTED WATER---  
  100 IF (NREC.LE.0) GO TO 120                                          
      IF (INT.GT.1.AND.ICHK.LE.0) RETURN                                
      WRITE (6,755)                                                     
      WRITE (6,910)                                                     
      DO 110 I=1,NREC                                                   
CTGC      READ (5,710) IX,IY,FCTR,CNREC 
      READ (5,*) IX,IY,FCTR,CNREC                                    
      JX=IX-MX+1                                                        
      JY=IY-MY+1                                                        
      IF (JX.LT.1.OR.JY.LT.1.OR.JX.GT.NMX.OR.JY.GT.NMY) GO TO 105       
      IF (FCTR.LT.0.0) CNRECH(JX,JY)=CNREC                              
  105 REC(IX,IY)=FCTR                                                   
  110 WRITE (6,820) IX,IY,REC(IX,IY),CNREC                              
C     ****************************************************************  
  120 IF (INT.GT.1) RETURN                                              
      AREA=XDEL*YDEL                                                    
      WRITE (6,755)                                                     
      WRITE (6,690) AREA                                                
      WRITE (6,600)                                                     
      WRITE (6,610) XDEL                                                
      WRITE (6,610) YDEL                                                
C     ****************************************************************  
C     ---READ TRANSMISSIVITY IN FT**2/SEC INTO VPRM ARRAY---            
C        ---FCTR = TRANSMISSIVITY MULTIPLIER  --->  FT**2/SEC---        
      WRITE (6,530)                                                     
      WRITE (6,755)                                                     
CTGC      READ (5,550) INPUT,FCTR 
      READ (5,*) INPUT,FCTR                                          
      DO 160 IY=1,NY                                                    
CTGC      IF (INPUT.EQ.1) READ (5,560) (VPRM(IX,IY),IX=1,NX)
      IF (INPUT.EQ.1) READ (5,*) (VPRM(IX,IY),IX=1,NX)                 
      DO 150 IX=1,NX                                                    
      IF (INPUT.NE.1) GO TO 130                                         
      VPRM(IX,IY)=VPRM(IX,IY)*FCTR                                      
      GO TO 140                                                         
  130 VPRM(IX,IY)=FCTR                                                  
  140 IF (IX.EQ.1.OR.IX.EQ.NX) VPRM(IX,IY)=0.D0                         
      IF (IY.EQ.1.OR.IY.EQ.NY) VPRM(IX,IY)=0.D0                         
  150 CONTINUE                                                          
  160 WRITE (6,840) (VPRM(IX,IY),IX=1,NX)                               
C     ****************************************************************  
C     ---SET UP COEFFICIENT MATRIX --- BLOCK-CENTERED GRID---           
C     ---AVERAGE TRANSMISSIVITY --- HARMONIC MEAN---                    
      IF (ANFCTR.NE.0.0) GO TO 170                                      
      WRITE (6,1050)                                                    
      ANFCTR=1.D0                                                       
  170 PIES=3.1415927D0*3.1415927D0/2.D0                                 
      YNS=NY*NY                                                         
      XNS=NX*NX                                                         
      HMIN=2.D0                                                         
      DO 180 IY=2,NNY                                                   
      DO 180 IX=2,NNX                                                   
      IF (VPRM(IX,IY).EQ.0.0) GO TO 180                                 
      TMRX(IX,IY,1)=2.D0*VPRM(IX,IY)*VPRM(IX+1,IY)/                     
     1                  (VPRM(IX,IY)+VPRM(IX+1,IY))/XDEL                
      TMRX(IX,IY,2)=2.D0*VPRM(IX,IY)*VPRM(IX,IY+1)/                     
     1                  (VPRM(IX,IY)+VPRM(IX,IY+1))/YDEL                
C        ---ADJUST COEFFICIENT FOR ANISOTROPY---                        
      TMRX(IX,IY,2)=TMRX(IX,IY,2)*ANFCTR                                
C        ---COMPUTE MINIMUM ITERATION PARAMETER (HMIN)---               
      IF (TMRX(IX,IY,1).EQ.0.0) GO TO 180                               
      IF (TMRX(IX,IY,2).EQ.0.0) GO TO 180                               
      RAT=TMRX(IX,IY,1)*YDEL/(TMRX(IX,IY,2)*XDEL)                       
      HMX=PIES/(XNS*(1.D0+RAT))                                         
      HMY=PIES/(YNS*(1.D0+(1.D0/RAT)))                                  
      IF (HMX.LT.HMIN) HMIN=HMX                                         
      IF (HMY.LT.HMIN) HMIN=HMY                                         
  180 CONTINUE                                                          
      IF (NX.GT.3.AND.NY.GT.3) GO TO 185                                
      HMX=PIES/XNS                                                      
      HMY=PIES/YNS                                                      
      HMIN=DMIN1(HMIN,HMX,HMY)                                          
  185 CONTINUE                                                          
C     ****************************************************************  
C     ---READ AQUIFER THICKNESS---                                      
      WRITE (6,510)                                                     
      WRITE (6,755)                                                     
CTGC      READ (5,550) INPUT,FCTR
      READ (5,*) INPUT,FCTR                                           
      DO 210 IY=1,NY                                                    
CTGC      IF (INPUT.EQ.1) READ (5,540) (THCK(IX,IY),IX=1,NX) 
      IF (INPUT.EQ.1) READ (5,*) (THCK(IX,IY),IX=1,NX)                
      DO 200 IX=1,NX                                                    
      IF (INPUT.NE.1) GO TO 190                                         
      THCK(IX,IY)=THCK(IX,IY)*FCTR                                      
      GO TO 200                                                         
  190 IF (VPRM(IX,IY).NE.0.0) THCK(IX,IY)=FCTR                          
  200 CONTINUE                                                          
      WRITE (6,500) (THCK(IX,IY),IX=1,NX)                               
      DO 205 IX=1,NX                                                    
  205 THCK(IX,IY)=THCK(IX,IY)*POROS                                     
  210 CONTINUE                                                          
C     ****************************************************************  
C     ---READ DIFFUSE RECHARGE AND DISCHARGE---                         
      WRITE (6,830)                                                     
      WRITE (6,755)                                                     
CTGC      READ (5,550) INPUT,FCTR
      READ (5,*) INPUT,FCTR                                           
      DO 240 IY=1,NY                                                    
CTGC      IF (INPUT.EQ.1) READ (5,560) (RECH(IX,IY),IX=1,NX) 
      IF (INPUT.EQ.1) READ (5,*) (RECH(IX,IY),IX=1,NX)               
      DO 230 IX=1,NX                                                    
      IF (INPUT.NE.1) GO TO 220                                         
      RECH(IX,IY)=RECH(IX,IY)*FCTR                                      
      GO TO 230                                                         
  220 IF (THCK(IX,IY).NE.0.0) RECH(IX,IY)=FCTR                          
  230 CONTINUE                                                          
  240 WRITE (6,840) (RECH(IX,IY),IX=1,NX)                               
C     ****************************************************************  
C     ---COMPUTE PERMEABILITY FROM TRANSMISSIVITY---                    
C     ---COUNT NO. OF CELLS IN AQUIFER---                               
C     ---SET NZCRIT = 2% OF THE NO. OF CELLS IN THE AQUIFER---          
      DO 250 IX=1,NX                                                    
      DO 250 IY=1,NY                                                    
      IF (THCK(IX,IY).EQ.0.0) GO TO 250                                 
      VPRM(IX,IY)=(VPRM(IX,IY)*POROS)/THCK(IX,IY)                       
      NCA=NCA+1                                                         
      IF (MCHK.EQ.0) GO TO 250                                          
      IF (IX.LT.MX.OR.IX.GT.MMX) GO TO 250                              
      IF (IY.LT.MY.OR.IY.GT.MMY) GO TO 250                              
      NCA2=NCA2+1                                                       
  250 CONTINUE                                                          
C                                                                       
      AAQ=NCA*AREA                                                      
      NZCRIT=(NCA+25)/50                                                
      IF (MCHK.GT.0) NZCRIT=(NCA2+25)/50                                
      IF (NZCRIT.EQ.0) NZCRIT=1                                         
      WRITE (6,620)                                                     
      WRITE (6,755)                                                     
      DO 260 IY=1,NY                                                    
      WRITE (6,840) (VPRM(IX,IY),IX=1,NX)                               
      DO 260 IX=1,NX                                                    
  260 VPRM(IX,IY)=0.D0                                                  
      IF (MCHK.EQ.0) GO TO 265                                          
      AAQ2=NCA2*AREA                                                    
      WRITE (6,633)                                                     
      WRITE (6,635) NCA,AAQ                                             
      WRITE (6,634)                                                     
      WRITE (6,630) NCA2,AAQ2,NZCRIT                                    
      GO TO 267                                                         
  265 CONTINUE                                                          
      WRITE (6,630) NCA,AAQ,NZCRIT                                      
  267 CONTINUE                                                          
C     ****************************************************************  
C     ---READ NODE IDENTIFICATION CARDS---                              
C        ---SET VERT. PERM., SOURCE CONC., AND DIFFUSE RECHARGE---      
C           ---SPECIFY CODES TO FIT YOUR NEEDS---                       
      WRITE (6,570)                                                     
CTGC      READ (5,550) INPUT,FCTR
      READ (5,*) INPUT,FCTR                                           
      DO 280 IY=1,NY                                                    
CTGC      IF (INPUT.EQ.1) READ (5,640) (NODEID(IX,IY),IX=1,NX)
      IF (INPUT.EQ.1) READ (5,*) (NODEID(IX,IY),IX=1,NX)              
      DO 270 IX=1,NX                                                    
  270 IF (INPUT.NE.1.AND.THCK(IX,IY).NE.0.0) NODEID(IX,IY)=FCTR         
  280 WRITE (6,580) (NODEID(IX,IY),IX=1,NX)                             
      WRITE (6,920) NCODES                                              
      IF (NCODES.LE.0) GO TO 310                                        
      WRITE (6,930)                                                     
      DO 300 IJ=1,NCODES                                                
CTGC      READ (5,850) ICODE,FCTR1,FCTR2,FCTR3,OVERRD
      READ (5,*) ICODE,FCTR1,FCTR2,FCTR3,OVERRD                       
      DO 290 IX=1,NX                                                    
      DO 290 IY=1,NY                                                    
      IF (NODEID(IX,IY).NE.ICODE) GO TO 290                             
      VPRM(IX,IY)=FCTR1                                                 
      JX=IX-MX+1                                                        
      JY=IY-MY+1                                                        
      IF (JX.LT.1.OR.JY.LT.1.OR.JX.GT.NMX.OR.JY.GT.NMY) GO TO 285       
      CNRECH(JX,JY)=FCTR2                                               
  285 CONTINUE                                                          
      IF (OVERRD.NE.0) RECH(IX,IY)=FCTR3                                
  290 CONTINUE                                                          
      WRITE (6,860) ICODE,FCTR1,FCTR2                                   
  300 IF (OVERRD.NE.0) WRITE (6,1100) FCTR3                             
  310 WRITE (6,590)                                                     
      WRITE (6,755)                                                     
      DO 320 IY=1,NY                                                    
  320 WRITE (6,840) (VPRM(IX,IY),IX=1,NX)                               
C     ***************************************************************   
C     ---READ WATER-TABLE ELEVATION---                                  
      WRITE (6,670)                                                     
      WRITE (6,755)                                                     
CTGC      READ (5,550) INPUT,FCTR
      READ (5,*) INPUT,FCTR                                           
      DO 350 IY=1,NY                                                    
CTGC      IF (INPUT.EQ.1) READ (5,660) (WT(IX,IY),IX=1,NX)
      IF (INPUT.EQ.1) READ (5,*) (WT(IX,IY),IX=1,NX)                 
      DO 340 IX=1,NX                                                    
      IF (INPUT.NE.1) GO TO 330                                         
      WT(IX,IY)=WT(IX,IY)*FCTR                                          
      GO TO 340                                                         
  330 IF (THCK(IX,IY).NE.0.0) WT(IX,IY)=FCTR                            
  340 CONTINUE                                                          
  350 WRITE (6,680) (WT(IX,IY),IX=1,NX)                                 
C     ****************************************************************  
C     ---SET INITIAL HEADS---                                           
      DO 360 IX=1,NX                                                    
      DO 360 IY=1,NY                                                    
      HI(IX,IY)=WT(IX,IY)                                               
      HC(IX,IY)=HI(IX,IY)                                               
      HR(IX,IY)=HI(IX,IY)                                               
  360 HK(IX,IY)=HI(IX,IY)                                               
C                                                                       
      CALL OUTPT                                                        
C     ***************************************************************   
C     ---COMPUTE ITERATION PARAMETERS---                                
      DO 370 ID=1,20                                                    
      AOPT(ID)=0.D0                                                     
  370 CONTINUE                                                          
      ANITP=NITP-1.D0                                                   
      ALPHA1=DEXP(DLOG(1.D0/HMIN)/ANITP)                                
      AOPT(1)=HMIN                                                      
      DO 380 IP=2,NITP                                                  
  380 AOPT(IP)=AOPT(IP-1)*ALPHA1                                        
C                                                                       
      WRITE (6,450)                                                     
      WRITE (6,460) (AOPT(IP),IP=1,NITP)                                
C     ****************************************************************  
C     ---READ INITIAL CONCENTRATIONS AND COMPUTE INITIAL MASS STORED--- 
C        ---IF USING SMALLER SUBGRID FOR TRANSPORT, READ INITIAL        
C           CONCENTRATION ARRAY FOR SUBGRID NODES ONLY---               
CTGC      READ (5,550) INPUT,FCTR
      READ (5,*) INPUT,FCTR                                           
      CFCTR2=DK*RHOB/POROS                                              
      DO 420 IY=1,NMY                                                   
      JY=IY+MY-1                                                        
CTGC      IF (INPUT.EQ.1) READ (5,660) (CONC(IX,IY),IX=1,NMX) 
      IF (INPUT.EQ.1) READ (5,*) (CONC(IX,IY),IX=1,NMX)              
      DO 410 IX=1,NMX                                                   
      JX=IX+MX-1                                                        
      IF (INPUT.NE.1) GO TO 390                                         
      CONC(IX,IY)=CONC(IX,IY)*FCTR                                      
      GO TO 400                                                         
  390 IF (THCK(JX,JY).NE.0.0) CONC(IX,IY)=FCTR                          
  400 CONINT(IX,IY)=CONC(IX,IY)                                         
      CFCTR=CONINT(IX,IY)*THCK(JX,JY)*AREA                              
      SORBI=SORBI+CFCTR*CFCTR2                                          
  410 STORMI=STORMI+CFCTR                                               
  420 CONTINUE                                                          
C     ****************************************************************  
C     ---CHECK DATA SETS FOR INTERNAL CONSISTENCY---                    
      DO 440 IX=1,NX                                                    
      DO 440 IY=1,NY                                                    
      IF (THCK(IX,IY).GT.0.0) THEN                                      
       IF (IX.EQ.1.OR.IY.EQ.1.OR.IX.EQ.NX.OR.IY.EQ.NY)                  
     1     WRITE (6,935) IX,IY                                          
       GO TO 430                                                        
      END IF                                                            
      IF (TMRX(IX,IY,1).GT.0.0) WRITE (6,940) IX,IY                     
      IF (TMRX(IX,IY,2).GT.0.0) WRITE (6,950) IX,IY                     
      IF (IX.NE.1) THEN                                                 
       IF (TMRX(IX-1,IY,1).GT.0.0) WRITE (6,940) IX,IY                  
      END IF                                                            
      IF (IY.NE.1) THEN                                                 
       IF (TMRX(IX,IY-1,2).GT.0.0) WRITE (6,950) IX,IY                  
      END IF                                                            
      IF (NODEID(IX,IY).GT.0) WRITE (6,960) IX,IY                       
      IF (WT(IX,IY).NE.0.0) WRITE (6,970) IX,IY                         
      IF (RECH(IX,IY).NE.0.0) WRITE (6,980) IX,IY                       
      IF (REC(IX,IY).NE.0.0) WRITE (6,990) IX,IY                        
  430 IF (TMRX(IX,IY,1).GT.0.0.OR.TMRX(IX,IY,2).GT.0.0) GO TO 440       
      IF (IX.NE.1) THEN                                                 
       IF (TMRX(IX-1,IY,1).GT.0.0) GO TO 440                            
      END IF                                                            
      IF (IY.NE.1) THEN                                                 
       IF (TMRX(IX,IY-1,2).GT.0.0) GO TO 440                            
      END IF                                                            
      IF (NODEID(IX,IY).GT.0.0) WRITE (6,1000) IX,IY                    
      IF (WT(IX,IY).NE.0.0) WRITE (6,1010) IX,IY                        
      IF (RECH(IX,IY).NE.0.0) WRITE (6,1020) IX,IY                      
      IF (REC(IX,IY).NE.0.0) WRITE (6,1030) IX,IY                       
      IF (THCK(IX,IY).GT.0.0) WRITE (6,1040) IX,IY                      
  440 CONTINUE                                                          
C     ****************************************************************  
      RETURN                                                            
C     ****************************************************************  
C                                                                       
C                                                                       
C                                                                       
  450 FORMAT (1H1,20HITERATION PARAMETERS)                              
  460 FORMAT (3H   ,1G20.6)                                             
  470 FORMAT (1H1,27HTIME INTERVALS (IN SECONDS))                       
  475 FORMAT (1H0,5X,65H*** WARNING ***   INITIAL TIME STEP IS LONGER TH
     1AN PUMPING PERIOD/25X,34H***ADJUST EITHER TINIT OR PINT.***/)     
  480 FORMAT (1H1,15X,17HSTEADY-STATE FLOW//5X,55HTIME INTERVALS (IN SEC
     1) FOR SOLUTE-TRANSPORT SIMULATION)                                
  490 FORMAT (3H   ,10G12.5)                                            
  500 FORMAT (3H   ,25F5.1)                                             
  510 FORMAT (1H1,22HAQUIFER THICKNESS (FT))                            
  530 FORMAT (1H1,30HTRANSMISSIVITY MAP (FT*FT/SEC))                    
  540 FORMAT (20G3.0)                                                   
  550 FORMAT (I1,G10.0)                                                 
  560 FORMAT (20G4.1)                                                   
  570 FORMAT (1H1,23HNODE IDENTIFICATION MAP//)                         
  580 FORMAT (1H ,40I3)                                                 
  590 FORMAT (1H1,45HVERTICAL PERMEABILITY/THICKNESS (FT/(FT*SEC)))     
  600 FORMAT (1H0,10X,12HX-Y SPACING:)                                  
  610 FORMAT (1H ,12X,10G12.5)                                          
  620 FORMAT (1H1,24HPERMEABILTY MAP (FT/SEC))                          
  630 FORMAT (1H0,05X,05X,44HNO. OF FINITE-DIFFERENCE CELLS IN AQUIFER =
     1 ,I4//10X,28HAREA OF AQUIFER IN MODEL  = ,G12.5,10H   SQ. FT.////1
     20X,47HNZCRIT   (MAX. NO. OF CELLS THAT CAN BE VOID OF/20X,56HPARTI
     3CLES;  IF EXCEEDED, PARTICLES ARE REGENERATED)   = ,I4/)          
  633 FORMAT (1H0,////2X,26HFLOW MODEL (PRIMARY GRID):/)                
  634 FORMAT (1H0,///2X,18HTRANSPORT SUBGRID:/)                         
  635 FORMAT (1H0,05X,05X,44HNO. OF FINITE-DIFFERENCE CELLS IN AQUIFER =
     1 ,I4//10X,28HAREA OF AQUIFER IN MODEL  = ,G12.5,10H   SQ. FT./)   
  640 FORMAT (20I1)                                                     
  660 FORMAT (20G4.0)                                                   
  670 FORMAT (1H1,11HWATER TABLE)                                       
  680 FORMAT (1H ,20F5.0)                                               
  690 FORMAT (1H0,10X,19HAREA OF ONE CELL = ,G12.4)                     
  700 FORMAT (2I2)                                                      
  710 FORMAT (2I2,2G8.2)                                                
  720 FORMAT (10A8)                                                     
  730 FORMAT (1H0,10A8)                                                 
  740 FORMAT (18I4)                                                     
  750 FORMAT (1H1,77HU.S.G.S. METHOD-OF-CHARACTERISTICS MODEL FOR SOLUTE
     1 TRANSPORT IN GROUND WATER)                                       
  755 FORMAT (1H )                                                      
  760 FORMAT (1H0,21X,21HI N P U T     D A T A)                         
  770 FORMAT (1H0,23X,16HGRID DESCRIPTORS//13X,30HNX    (NUMBER OF COLUM
     1NS)  =  ,I4/13X,28HNY    (NUMBER OF ROWS)     =,I6/13X,29HXDEL  (X
     2-DISTANCE IN FEET) = ,F7.1/13X,29HYDEL  (Y-DISTANCE IN FEET) = ,F7
     3.1)                                                               
  775 FORMAT (1H0,18X,31HSECONDARY SUBGRID FOR TRANSPORT//16X,30HNMX   (
     1NUMBER OF COLUMNS)  =  ,I4/16X,30HNMY   (NUMBER OF ROWS)     =  ,I
     24//16X,38HCROSS-REF. TO PRIMARY GRID      IX  IY/46X,8H --- ---/18
     3X,28HFIRST NODE (UPPER LEFT) AT: ,2I4/18X,28HLAST NODE (LOWER RIGH
     4T) AT: ,2I4)                                                      
  780 FORMAT (1H0,23X,16HTIME  PARAMETERS//13X,40HNTIM   (MAX. NO. OF TI
     1ME STEPS)       = ,I6/13X,40HNPMP   (NO. OF PUMPING PERIODS)      
     2 = ,I6/13X,39HPINT   (PUMPING PERIOD IN YEARS)      =,F11.3/13X,39
     3HTIMX   (TIME INCREMENT MULTIPLIER)    =,F10.2/13X,39HTINIT  (INIT
     4IAL TIME STEP IN SEC.)    =,F8.0)                                 
  790 FORMAT (1H0,14X,34HHYDROLOGIC AND CHEMICAL PARAMETERS//13X,1HS,7X,
     129H(STORAGE COEFFICIENT)       =,5X,F9.6/13X,28HPOROS   (EFFECTIVE
     2 POROSITY),8X,3H=  ,F9.3/13X,39HBETA    (LONGITUDINAL DISPERSIVITY
     3) =  ,F7.1/13X,31HDLTRAT  (RATIO OF TRANSVERSE TO/21X,30HLONGITUDI
     4NAL DISPERSIVITY)  = ,F9.2/13X,39HANFCTR  (RATIO OF T-YY TO T-XX) 
     5    =  ,F12.6)                                                    
  800 FORMAT (12G5.0)                                                   
  810 FORMAT (1H ,16X,I2,5X,I2,4X,I2)                                   
  820 FORMAT (1H ,7X,2I4,3X,F9.4,3X,F8.2)                               
  830 FORMAT (1H1,39HDIFFUSE RECHARGE AND DISCHARGE (FT/SEC))           
  840 FORMAT (1H ,1P10E10.2)                                            
  850 FORMAT (I2,3G10.2,I2)                                             
  860 FORMAT (1H0,7X,I2,7X,E10.3,5X,F9.2)                               
  870 FORMAT (1H0,21X,20HEXECUTION PARAMETERS//13X,39HNITP   (NO. OF ITE
     1RATION PARAMETERS) = ,I4/13X,39HTOL    (CONVERGENCE CRITERIA - ADI
     2P) = ,E9.2/13X,39HITMAX  (MAX.NO.OF ITERATIONS - ADIP) = ,I4/13X,3
     34HCELDIS (MAX.CELL DISTANCE PER MOVE/24X,28HOF PARTICLES - M.O.C.)
     4    = ,F8.3/13X,30HNPMAX  (MAX. NO. OF PARTICLES),7X,2H= ,I4/12X,3
     52H NPTPND (NO. PARTICLES PER NODE),6X,3H=  ,I4)                   
  880 FORMAT (1H0,5X,47H*** WARNING *** NPTPND MUST =  1,4,5,8,9, OR 16)
  882 FORMAT (1H0,5X,58H*** CAUTION *** USE OF NPTPND=1 MAY CAUSE LOSS O
     1F ACCURACY)                                                       
  883 FORMAT (1H0,5X,56H*** ONE-DIMENSIONAL *** WILL USE ONLY 1 ROW OF P
     1ARTICLES/13X,35HUSE 2 PARTICLES FOR NPTPND = 4 OR 5/13X,35HUSE 3 P
     2ARTICLES FOR NPTPND = 8 OR 9/13X,31HUSE 4 PARTICLES FOR NPTPND = 1
     36)                                                                
  885 FORMAT (1H0,5X,38H*** WARNING ***  NITP MUST BE POSITIVE)         
  888 FORMAT (1H1)                                                      
  890 FORMAT (1H0,23X,15HPROGRAM OPTIONS//13X,30HNPNT   (TIME STEP INTER
     1VAL FOR/21X,18HCOMPLETE PRINTOUT),7X,3H=  ,I4/13X,31HNPNTMV (MOVE 
     2INTERVAL FOR CHEM./21X,28HCONCENTRATION PRINTOUT)  =  ,I4/13X,30HN
     3PNTVL (TIME STEP INTERVAL FOR/21X,'VELOCITY PRINTOUT; 0=NEVER;'/  
     4 21X,'-1=FIRST TIME STEP;'/21X,'-2=LAST TIME STEP)',7X,3H=  ,I4/  
     5 13X,'NPNTD  (PRINT OPTION-DISP.COEF.'/21X,                       
     6 '0=NO; 1=FIRST TIME STEP;'/21X,'2=ALL TIME STEPS)',8X,3H=  ,I4/  
     7 13X,'NUMOBS (NO. OF OBSERVATION WELLS'/                          
     8 21X,'FOR HYDROGRAPH PRINTOUT) =  ',I4/                           
     9 13X,'NREC   (NO. OF PUMPING WELLS)    = ',I5/                    
     $ 13X,'NCODES (FOR NODE IDENT.)',9X,2H= ,I5/                       
     1 13X,'NPNCHV (TIME STEP INTERVAL FOR'/21X,'VELOCITY PRINTOUT ON'/ 
     2 21X,'FILE UNIT 7; 0=NEVER;'/21X,'-1=FIRST TIME STEP;'/           
     3 21X,'-2=LAST TIME STEP)',7X,2H= ,I5/                             
     4 13X,'NPDELC (PRINT OPT.-CONC. CHANGE) =  ',I4)                   
  895 FORMAT (1H0,23X,14HREACTION TERMS//13X,37HDK      (DISTRIBUTION CO
     1EFFICIENT) = ,E12.5/13X,37HRHOB    (BULK DENSITY OF SOLIDS)   = ,E
     212.5/13X,37HRF      (RETARDATION FACTOR)       = ,E12.5/13X,37HTHA
     3LF   (HALF LIFE OF DECAY,IN SEC)= ,E12.5/13X,37HDECAY   (DECAY CON
     4STANT=LN 2/THALF)= ,E12.5)                                        
  900 FORMAT (1H0,10X,29HLOCATION OF OBSERVATION WELLS//17X,3HNO.,5X,1HX
     1,5X,1HY/)                                                         
  910 FORMAT (1H0,10X,28HLOCATION  OF  PUMPING  WELLS//11X,28HX   Y   RA
     1TE(IN CFS)   CONC./)                                              
  920 FORMAT (1H0,5X,37HNO. OF NODE IDENT. CODES SPECIFIED = ,I2)       
  930 FORMAT (1H0,10X,41HTHE FOLLOWING ASSIGNMENTS HAVE BEEN MADE:/5X,51
     1HCODE NO.     LEAKANCE     SOURCE CONC.     RECHARGE)             
  935 FORMAT (1H ,5X,54H*** WARNING ***   THCK.NE.0.0 ON BOUNDARY AT NOD
     1E IX =,I4,6H, IY =,I4)                                            
  940 FORMAT (1H ,5X,61H*** WARNING ***   THCK.EQ.0.0 AND TMRX(X).GT.0.0
     1 AT NODE IX =,I4,6H, IY =,I4)                                     
  950 FORMAT (1H ,5X,61H*** WARNING ***   THCK.EQ.0.0 AND TMRX(Y).GT.0.0
     1 AT NODE IX =,I4,6H, IY =,I4)                                     
  960 FORMAT (1H ,5X,61H*** WARNING ***    THCK.EQ.0.0 AND NODEID.GT.0.0
     1 AT NODE IX =,I4,6H, IY =,I4)                                     
  970 FORMAT (1H ,5X,56H*** WARNING ***   THCK.EQ.0.0 AND WT.NE.0.0 AT N
     1ODE IX =,I4,6H, IY =,I4)                                          
  980 FORMAT (1H ,5X,58H*** WARNING ***   THCK.EQ.0.0 AND RECH.NE.0.0 AT
     1 NODE IX =,I4,6H, IY =,I4)                                        
  990 FORMAT (1H ,5X,58H*** WARNING ***    THCK.EQ.0.0 AND REC.NE.0.0 AT
     1 NODE IX =,I4,6H, IY =,I4)                                        
 1000 FORMAT (1H ,5X,61H*** WARNING ***    TMRX.EQ.0.0 AND NODEID.GT.0.0
     1 AT NODE IX =,I4,6H, IY =,I4)                                     
 1010 FORMAT (1H ,5X,56H*** WARNING ***   TMRX.EQ.0.0 AND WT.NE.0.0 AT N
     1ODE IX =,I4,6H, IY =,I4)                                          
 1020 FORMAT (1H ,5X,58H*** WARNING ***   TMRX.EQ.0.0 AND RECH.NE.0.0 AT
     1 NODE IX =,I4,6H, IY =,I4)                                        
 1030 FORMAT (1H ,5X,58H*** WARNING ***    TMRX.EQ.0.0 AND REC.NE.0.0 AT
     1 NODE IX =,I4,6H, IY =,I4)                                        
 1040 FORMAT (1H ,5X,58H*** WARNING ***   TMRX.EQ.0.0 AND THCK.GT.0.0 AT
     1 NODE IX =,I4,6H, IY =,I4)                                        
 1050 FORMAT (1H0,5X,45H*** WARNING ***   ANFCTR WAS SPECIFIED AS 0.0/23
     1X,34HDEFAULT ACTION: RESET ANFCTR = 1.0)                          
 1060 FORMAT (I1)                                                       
 1070 FORMAT (10I4,3G5.0)                                               
 1080 FORMAT (1H1,5X,25HSTART PUMPING PERIOD NO. ,I2//2X,75HTHE FOLLOWIN
     1G TIME STEP, PUMPAGE, AND PRINT PARAMETERS HAVE BEEN REDEFINED:/) 
 1090 FORMAT (1H0,14X,9HNTIM   = ,I4/15X,9HNPNT   = ,I4/15X,9HNITP   = ,
     1I4/15X,9HITMAX  = ,I4/15X,9HNREC   = ,I4/15X,9HNPNTMV = ,I4/15X,9H
     2NPNTVL = ,I4/15X,9HNPNTD  = ,I4/15X,9HNPDELC = ,I4/15X,9HNPNCHV = 
     3,I4/15X,9HPINT   = ,F10.3/15X,9HTIMX   = ,F10.3/15X,9HTINIT  = ,F1
     40.3/)                                                             
 1100 FORMAT (1H ,46X,E10.3)                                            
 1110 FORMAT (1H1,5X,25HSTART PUMPING PERIOD NO. ,I2//2X,23HNO PARAMETER
     1S REDEFINED/)                                                     
      END