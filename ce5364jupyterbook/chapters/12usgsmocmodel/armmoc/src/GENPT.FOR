      SUBROUTINE GENPT                                                  
      DOUBLE PRECISION TMRX,VPRM,HI,HR,HC,HK,WT,REC,RECH,TIM,AOPT,TITLE 
      DOUBLE PRECISION XDEL,YDEL,S,AREA,SUMT,RHO,PARAM,TEST,TOL,PINT,   
     1                 HMIN,PYR,ANFCTR                                  
      INTEGER PTID                                                      
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
      COMMON /CHMA/ PART(3,06400),CONC(020,020),TMCN(05,50),VX(040,040),
     1              VY(040,040),CONINT(020,020),CNRECH(020,020),POROS,  
     2              SUMTCH,BETA,TIMV,STORM,STORMI,CMSIN,CMSOUT,FLMIN,   
     3              FLMOT,SUMIO,CELDIS,DLTRAT,CSTORM                    
      COMMON /CHMP/ PTID(06400)                                         
      DIMENSION RPT(16),RNT(16),RP(16),RN(16),IPT(16)                   
C     ***************************************************************   
      IONED=0                                                           
      IF(NX.EQ.3.OR.NY.EQ.3) IONED=1                                    
      F1=0.30                                                           
      F2=1.0/3.0                                                        
      IF (NPTPND.EQ.4) F1=0.25                                          
      IF (NPTPND.EQ.5.AND.IONED.EQ.1) F1=0.25                           
      IF (NPTPND.EQ.9) F1=1.0/3.0                                       
      IF (NPTPND.EQ.8.AND.IONED.NE.1) F2=0.25                           
      IF (NPTPND.EQ.8.AND.IONED.EQ.1) F1=1.0/3.0                        
      IF (NPTPND.EQ.16) F1=0.25                                         
      IF (NPTPND.EQ.16) F2=0.125                                        
      NCHK=NPTPND                                                       
      IF (NPTPND.EQ.5.OR.NPTPND.EQ.9) NCHK=NPTPND-1                     
      IF (TEST.GT.98.) GO TO 10                                         
C     ***************************************************************   
C     ---INITIALIZE VALUES---                                           
      STORM=0.0                                                         
      CMSIN=0.0                                                         
      CMSOUT=0.0                                                        
      FLMIN=0.0                                                         
      FLMOT=0.0                                                         
      SUMIO=0.0                                                         
C     ***************************************************************   
   10 DO 20 IN=1,NPMAX                                                  
      PTID(IN)=0                                                        
      DO 20 ID=1,3                                                      
   20 PART(ID,IN)=0.0                                                   
      DO 30 IA=1,16                                                     
      RP(IA)=0.0                                                        
      RN(IA)=0.0                                                        
      RPT(IA)=0.0                                                       
      RNT(IA)=0.0                                                       
   30 IPT(IA)=0                                                         
C     ---SET UP LIMBO ARRAY---                                          
      DO 40 IN=1,500                                                    
   40 LIMBO(IN)=0                                                       
      IND=1                                                             
C     ***************************************************************   
C     ---INSERT PARTICLES---                                            
C        ---TRACK PARTICLE LOCATIONS IN COORDINATES OF PRIMARY GRID---  
      DO 410 IX=1,NMX                                                   
      JX=IX+MX-1                                                        
      DO 410 IY=1,NMY                                                   
      JY=IY+MY-1                                                        
      IF (THCK(JX,JY).EQ.0.0) GO TO 410                                 
      KR=0                                                              
      KR2=0                                                             
      TEST2=0.0                                                         
      METH=1                                                            
      NPCELL(IX,IY)=0                                                   
      NPOLD(IX,IY)=NPTPND                                               
      C1=CONC(IX,IY)                                                    
      IF (NPTPND.EQ.1) GO TO 150                                        
      IF (C1.LE.1.0E-05) TEST2=1.0                                      
      IF (IX.EQ.1.OR.IX.EQ.NMX.OR.IY.EQ.1.OR.IY.EQ.NMY) TEST2=1.0       
      IF (VPRM(JX,JY).GT.0.09) TEST2=1.0                                
      IF (REC(JX,JY).NE.0.0) TEST2=1.0                                  
      IF (THCK(JX+1,JY+1).EQ.0.0.OR.THCK(JX+1,JY-1).EQ.0.0.OR.THCK(JX-1,
     1JY+1).EQ.0.0.OR.THCK(JX-1,JY-1).EQ.0.0) TEST2=1.0                 
      IF ((THCK(JX,JY+1).EQ.0.0.OR.THCK(JX,JY-1).EQ.0.0.OR.THCK(JX+1,JY)
     1.EQ.0.0.OR.THCK(JX-1,JY).EQ.0.0).AND.NPTPND.GT.5) TEST2=1.0       
      CNODE=C1*(1.0-F1)                                                 
      IF (TEST.LT.98.0.OR.TEST2.GT.0.0) GO TO 70                        
      SUMC=CONC(IX+1,IY)+CONC(IX-1,IY)+CONC(IX,IY+1)+CONC(IX,IY-1)      
      IF (NCHK.EQ.4) GO TO 60                                           
      SUMC=SUMC+CONC(IX+1,IY+1)+CONC(IX+1,IY-1)+CONC(IX-1,IY+1)+CONC(IX-
     11,IY-1)                                                           
   60 AVC=SUMC/NCHK                                                     
      IF (AVC.GT.C1) METH=2                                             
C                                                                       
C        ---PUT 4 PARTICLES ON CELL DIAGONALS---                        
   70 DO 140 IT=1,2                                                     
      EVET=(-1.0)**IT                                                   
      DO 140 IS=1,2                                                     
      IF(IONED.EQ.1.AND.IT.EQ.1.AND.IS.EQ.2) GO TO 140                  
      IF(IONED.EQ.1.AND.IT.EQ.2.AND.IS.EQ.1) GO TO 140                  
      EVES=(-1.0)**IS                                                   
      KR=KR+1                                                           
      IF (NPTPND.EQ.16) GO TO 72                                        
      PART(1,IND)=JX+F1*EVET                                            
      PART(2,IND)=JY+F1*EVES                                            
      PART(2,IND)=-PART(2,IND)                                          
      PART(3,IND)=C1                                                    
      IPT(KR)=IND                                                       
      PTID(IND)=KR                                                      
      IF(IONED.EQ.1.AND.IS.EQ.2) PTID(IND)=4                            
      GO TO 76                                                          
   72 IF (TEST.LT.98.0.OR.TEST2.GT.0.0) GO TO 135                       
   76 IF (TEST.LT.98.0.OR.TEST2.GT.0.0) GO TO 139                       
      IXD=IX+EVET                                                       
      IYD=IY+EVES                                                       
      IF (METH.EQ.2) GO TO 80                                           
      PARTC=CNODE+CONC(IXD,IYD)*F1                                      
      GO TO 90                                                          
   80 PARTC=2.0*C1*CONC(IXD,IYD)/(C1+CONC(IXD,IYD))                     
   90 IF (C1-CONC(IXD,IYD)) 100,110,120                                 
  100 RPT(KR)=CONC(IXD,IYD)-PARTC                                       
      RNT(KR)=C1-PARTC                                                  
      GO TO 130                                                         
  110 RPT(KR)=0.0                                                       
      RNT(KR)=0.0                                                       
      GO TO 130                                                         
  120 RPT(KR)=C1-PARTC                                                  
      RNT(KR)=CONC(IXD,IYD)-PARTC                                       
  130 IF (NPTPND.EQ.16) GO TO 135                                       
      PART(3,IND)=PARTC                                                 
      RP(KR)=RPT(KR)                                                    
      RN(KR)=RNT(KR)                                                    
      GO TO 139                                                         
  135 DO 138 ITT = 1,2                                                  
      EVET2=(-1.0)**ITT                                                 
      DO 138 ISS = 1,2                                                  
      IF(IONED.EQ.1.AND.ITT.EQ.1.AND.ISS.EQ.2) GO TO 138                
      IF(IONED.EQ.1.AND.ITT.EQ.2.AND.ISS.EQ.1) GO TO 138                
      EVES2=(-1.0)**ISS                                                 
      PART(1,IND)=(JX+F1*EVET)+F2*EVET2                                 
      PART(2,IND)=(JY+F1*EVES)+F2*EVES2                                 
      PART(2,IND)=-PART(2,IND)                                          
      KR2=KR2+1                                                         
      IF (TEST.LT.98.0.OR.TEST2.GT.0.0) GO TO 136                       
      PART(3,IND) = PARTC                                               
      RP(KR2) = RPT(KR)                                                 
      RN(KR2) = RNT(KR)                                                 
      IPT(KR2) = IND                                                    
      GO TO 137                                                         
  136 PART(3,IND) = C1                                                  
  137 PTID(IND)=KR2                                                     
      IF(IONED.EQ.1) THEN                                               
       IF(IT.EQ.1.AND.ISS.EQ.2) PTID(IND)=4                             
       IF(IT.EQ.2) THEN                                                 
        IF(ISS.EQ.1) PTID(IND)=13                                       
        IF(ISS.EQ.2) PTID(IND)=16                                       
       END IF                                                           
      END IF                                                            
      IND=IND+1                                                         
  138 CONTINUE                                                          
      GO TO 140                                                         
  139 IND=IND+1                                                         
  140 CONTINUE                                                          
      IF (NPTPND.EQ.16) GO TO 290                                       
      IF ((NPTPND.EQ.5.AND.IONED.NE.1).OR.NPTPND.EQ.9) GO TO 150        
      IF (NPTPND.EQ.8.AND.IONED.EQ.1) GO TO 150                         
      GO TO 160                                                         
C        ---PUT ONE PARTICLE AT CENTER OF CELL---                       
  150 PART(1,IND)=JX                                                    
      PART(2,IND)=-JY                                                   
      PART(3,IND)=C1                                                    
      PTID(IND)=5                                                       
      IND=IND+1                                                         
      IF (NPTPND.EQ.1) GO TO 410                                        
C        ---PLACE NORTH, SOUTH, EAST, AND WEST PARTICLES---             
  160 IF (NPTPND.LT.8) GO TO 290                                        
      IF(IONED.EQ.1) GO TO 290                                          
      CNODE=C1*(1.0-F2)                                                 
      DO 280 IT=1,2                                                     
      EVET=(-1.0)**IT                                                   
      PART(1,IND)=JX+F2*EVET                                            
      PART(2,IND)=-JY                                                   
      PART(3,IND)=C1                                                    
      IF (EVET.LT.0) PTID(IND)=6                                        
      IF (EVET.GT.0) PTID(IND)=8                                        
      IF (TEST.LT.98.0.OR.TEST2.GT.0.0) GO TO 220                       
      IXD=IX+EVET                                                       
      KR=KR+1                                                           
      IPT(KR)=IND                                                       
      IF (METH.EQ.2) GO TO 170                                          
      PART(3,IND)=CNODE+CONC(IXD,IY)*F2                                 
      GO TO 180                                                         
  170 PART(3,IND)=2.0*C1*CONC(IXD,IY)/(C1+CONC(IXD,IY))                 
  180 IF (C1-CONC(IXD,IY)) 190,200,210                                  
  190 RP(KR)=CONC(IXD,IY)-PART(3,IND)                                   
      RN(KR)=C1-PART(3,IND)                                             
      GO TO 220                                                         
  200 RP(KR)=0.0                                                        
      RN(KR)=0.0                                                        
      GO TO 220                                                         
  210 RP(KR)=C1-PART(3,IND)                                             
      RN(KR)=CONC(IXD,IY)-PART(3,IND)                                   
  220 IND=IND+1                                                         
      PART(1,IND)=JX                                                    
      PART(2,IND)=JY+F2*EVET                                            
      PART(2,IND)=-PART(2,IND)                                          
      PART(3,IND)=C1                                                    
      IF (EVET.LT.0) PTID(IND)=7                                        
      IF (EVET.GT.0) PTID(IND)=9                                        
      IF (TEST.LT.98.0.OR.TEST2.GT.0.0) GO TO 280                       
      IYD=IY+EVET                                                       
      KR=KR+1                                                           
      IPT(KR)=IND                                                       
      IF (METH.EQ.2) GO TO 230                                          
      PART(3,IND)=CNODE+CONC(IX,IYD)*F2                                 
      GO TO 240                                                         
  230 PART(3,IND)=2.0*C1*CONC(IX,IYD)/(C1+CONC(IX,IYD))                 
  240 IF (C1-CONC(IX,IYD)) 250,260,270                                  
  250 RP(KR)=CONC(IX,IYD)-PART(3,IND)                                   
      RN(KR)=C1-PART(3,IND)                                             
      GO TO 280                                                         
  260 RP(KR)=0.0                                                        
      RN(KR)=0.0                                                        
      GO TO 280                                                         
  270 RP(KR)=C1-PART(3,IND)                                             
      RN(KR)=CONC(IX,IYD)-PART(3,IND)                                   
  280 IND=IND+1                                                         
C                                                                       
  290 IF (TEST.LT.98.0.OR.TEST2.GT.0.0) GO TO 410                       
      SUMPT=0.0                                                         
C        ---COMPUTE CONC. GRADIENT WITHIN CELL---                       
      DO 300 KPT=1,NCHK                                                 
      IK=IPT(KPT)                                                       
  300 SUMPT=PART(3,IK)+SUMPT                                            
      CBAR=SUMPT/NCHK                                                   
C        ---CHECK MASS BALANCE WITHIN CELL AND ADJUST PT. CONCS.---     
      SUMPT=0.0                                                         
      IF (CBAR-C1) 310,410,330                                          
  310 CRCT=1.0-(CBAR/C1)                                                
      IF (METH.EQ.1) CRCT=CBAR/C1                                       
      DO 320 KPT=1,NCHK                                                 
      IK=IPT(KPT)                                                       
      PART(3,IK)=PART(3,IK)+RP(KPT)*CRCT                                
  320 SUMPT=SUMPT+PART(3,IK)                                            
      CBARN=SUMPT/NCHK                                                  
      GO TO 350                                                         
  330 CRCT=1.0-(C1/CBAR)                                                
      IF (METH.EQ.1) CRCT=C1/CBAR                                       
      DO 340 KPT=1,NCHK                                                 
      IK=IPT(KPT)                                                       
      PART(3,IK)=PART(3,IK)+RN(KPT)*CRCT                                
  340 SUMPT=SUMPT+PART(3,IK)                                            
      CBARN=SUMPT/NCHK                                                  
  350 IF (CBARN.EQ.C1) GO TO 410                                        
C        ---CORRECT FOR OVERCOMPENSATION---                             
      CRCT=C1/CBARN                                                     
      DO 380 KPT=1,NCHK                                                 
      IK=IPT(KPT)                                                       
      PART(3,IK)=PART(3,IK)*CRCT                                        
C        ---CHECK CONSTRAINTS---                                        
      IF (PART(3,IK)-C1) 360,380,370                                    
  360 CLIM=C1-RP(KPT)+RN(KPT)                                           
      IF (PART(3,IK).LT.CLIM) GO TO 390                                 
      GO TO 380                                                         
  370 CLIM=C1+RP(KPT)-RN(KPT)                                           
      IF (PART(3,IK).GT.CLIM) GO TO 390                                 
  380 CONTINUE                                                          
      GO TO 410                                                         
  390 TEST2=1.0                                                         
      DO 400 KPT=1,NCHK                                                 
      IK=IPT(KPT)                                                       
  400 PART(3,IK)=C1                                                     
  410 CONTINUE                                                          
      NP=IND-1                                                          
      IF (INT.EQ.0) CALL CHMOT                                          
C     ****************************************************************  
      RETURN                                                            
C     ****************************************************************  
      END