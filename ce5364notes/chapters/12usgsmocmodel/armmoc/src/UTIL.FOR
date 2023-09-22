
C
C                                                               
                                                               
                                                              
                                                               
                                                               
                                                            
      SUBROUTINE CNCON                                                  
      DOUBLE PRECISION TMRX,VPRM,HI,HR,HC,HK,WT,REC,RECH,TIM,AOPT,TITLE 
      DOUBLE PRECISION XDEL,YDEL,S,AREA,SUMT,RHO,PARAM,TEST,TOL,PINT,   
     1                 HMIN,PYR,ANFCTR                                  
      DOUBLE PRECISION DXINV,DYINV,ARINV,PORINV                         
      DOUBLE PRECISION FLW                                              
      DOUBLE PRECISION DCYFCT,DCYT,DCYT2                                
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
      COMMON /XINV/ DXINV,DYINV,ARINV,PORINV                            
      COMMON /CHMA/ PART(3,06400),CONC(020,020),TMCN(05,50),VX(040,040),
     1              VY(040,040),CONINT(020,020),CNRECH(020,020),POROS,  
     2              SUMTCH,BETA,TIMV,STORM,STORMI,CMSIN,CMSOUT,FLMIN,   
     3              FLMOT,SUMIO,CELDIS,DLTRAT,CSTORM                    
      COMMON /DIFUS/ DISP(020,020,4)                                    
      COMMON /CHMC/ SUMC(020,020),VXBDY(040,040),VYBDY(040,040)         
      COMMON /CHMR/ RF,DK,RHOB,THALF,DECAY,ADSORB,SORBI,DMASS1,CSTM2    
      DIMENSION CNCNC(020,020),CNOLD(020,020),CAVG(020,020)             
C     ***************************************************************   
      DO 10 IX=1,NMX                                                    
      DO 10 IY=1,NMY                                                    
      CNOLD(IX,IY)=CONC(IX,IY)                                          
      CAVG(IX,IY)=CONC(IX,IY)                                           
   10 CNCNC(IX,IY)=0.0                                                  
      APC=0.0                                                           
      NZERO=0                                                           
      TVA=AREA*TIMV                                                     
      TVA2=TVA*0.5                                                      
      TMCHK=TIMV*10.0                                                   
      SRCDCY=0.0                                                        
      RFAREA=RF*AREA                                                    
C     ***************************************************************   
C     ---CONC. CHANGE DUE TO:                                           
C           MIXING AT SOURCE CELLS...                                   
C           ...WITH DECAY OF RECHARGE DURING TIME INCREMENT             
      CONST=TIMV                                                        
      DCYFCT=TIMV*DECAY                                                 
      RFFCT=CONST/RF                                                    
      DCYT=1.D0                                                         
      DCYT2=1.D0                                                        
      IF(DECAY.NE.0.0) THEN                                             
       DCYT=DEXP(-DCYFCT)                                               
       DCYT2=DEXP(-DCYFCT*0.5D0)                                        
      END IF                                                            
      GO TO 70                                                          
   20 DO 60 IX=1,NMX                                                    
      DO 60 IY=1,NMY                                                    
      JX=IX+MX-1                                                        
      JY=IY+MY-1                                                        
      IF (THCK(JX,JY).EQ.0.0) GO TO 60                                  
      EQFCT=RFFCT/THCK(JX,JY)                                           
      C1=CAVG(IX,IY)                                                    
      IF (ABS(C1).LT.1.0E-20) C1=0.0                                    
      C2=C1                                                             
      CLKCN=C1                                                          
      SLEAK=(HK(JX,JY)-WT(JX,JY))*VPRM(JX,JY)                           
      IF (SLEAK.GE.0.0) GO TO 25                                        
      CLKCN=CNRECH(IX,IY)*DCYT2                                         
      SRCDCY=SRCDCY+(CNRECH(IX,IY)-CLKCN)*SLEAK*TVA                     
   25 CONTINUE                                                          
      CNREC=C1                                                          
      CNREC2=C1                                                         
      RATE=REC(JX,JY)*ARINV                                             
      IF (RATE.GE.0.0) GO TO 27                                         
      CNREC=CNRECH(IX,IY)*DCYT2                                         
      SRCDCY=SRCDCY+(CNRECH(IX,IY)-CNREC)*RATE*TVA                      
   27 IF (RECH(JX,JY).GE.0.0) GO TO 29                                  
      CNREC2=CNRECH(IX,IY)*DCYT2                                        
      SRCDCY=SRCDCY+(CNRECH(IX,IY)-CNREC2)*RECH(JX,JY)*TVA              
   29 CONTINUE                                                          
      DIV=RATE+SLEAK+RECH(JX,JY)                                        
      IF (THALF.GT.TMCHK.OR.THALF.EQ.0.0) GO TO 37                      
      IF (DIV.GE.0.0) GO TO 37                                          
      IF (CNOLD(IX,IY).LE.0.0.OR.CONC(IX,IY).LE.0.0) GO TO 37           
      C1=EXP((ALOG(CNOLD(IX,IY))+ALOG(CONC(IX,IY)))*0.5)                
C     IF (NPCELL(IX,IY).LE.0) C1=CNOLD(IX,IY)*DCYT2                     
   37 CONTINUE                                                          
      DELC=EQFCT*(C1*DIV-RATE*CNREC-SLEAK*CLKCN-RECH(JX,JY)*CNREC2)     
   40 CNCNC(IX,IY)=CNCNC(IX,IY)+DELC                                    
C     ---CONC. CHANGE DUE TO DISPERSION FOR TIMV---                     
C        ---DISPERSION WITH TENSOR COEFFICIENTS---                      
      IF (BETA.EQ.0.0) GO TO 60                                         
      IF (MCHK.EQ.1) GO TO 39                                           
      X1=DISP(IX,IY,1)*(CAVG(IX+1,IY)-C2)                               
      X2=DISP(IX-1,IY,1)*(CAVG(IX-1,IY)-C2)                             
      Y1=DISP(IX,IY,2)*(CAVG(IX,IY+1)-C2)                               
      Y2=DISP(IX,IY-1,2)*(CAVG(IX,IY-1)-C2)                             
      XX1=DISP(IX,IY,3)*(CAVG(IX,IY+1)+CAVG(IX+1,IY+1)-CAVG(IX,IY-1)-CAV
     1G(IX+1,IY-1))                                                     
      XX2=DISP(IX-1,IY,3)*(CAVG(IX,IY+1)+CAVG(IX-1,IY+1)-CAVG(IX,IY-1)-C
     1AVG(IX-1,IY-1))                                                   
      YY1=DISP(IX,IY,4)*(CAVG(IX+1,IY)+CAVG(IX+1,IY+1)-CAVG(IX-1,IY)-CAV
     1G(IX-1,IY+1))                                                     
      YY2=DISP(IX,IY-1,4)*(CAVG(IX+1,IY)+CAVG(IX+1,IY-1)-CAVG(IX-1,IY)-C
     1AVG(IX-1,IY-1))                                                   
      GO TO 48                                                          
   39 X1=0.0                                                            
      X2=0.0                                                            
      Y1=0.0                                                            
      Y2=0.0                                                            
      XX1=0.0                                                           
      XX2=0.0                                                           
      YY1=0.0                                                           
      YY2=0.0                                                           
      IF (IX.GE.NMX) GO TO 41                                           
      X1=DISP(IX,IY,1)*(CAVG(IX+1,IY)-C2)                               
   41 IF (IX.LE.1) GO TO 42                                             
      X2=DISP(IX-1,IY,1)*(CAVG(IX-1,IY)-C2)                             
   42 IF (IY.GE.NMY) GO TO 43                                           
      Y1=DISP(IX,IY,2)*(CAVG(IX,IY+1)-C2)                               
   43 IF (IY.LE.1) GO TO 46                                             
      Y2=DISP(IX,IY-1,2)*(CAVG(IX,IY-1)-C2)                             
   44 IF (IY.GE.NMY) GO TO 47                                           
      IF (IX.GE.NMX) GO TO 45                                           
      XX1=DISP(IX,IY,3)*(CAVG(IX,IY+1)+CAVG(IX+1,IY+1)-CAVG(IX,IY-1)-CAV
     1G(IX+1,IY-1))                                                     
   45 IF (IX.LE.1) GO TO 48                                             
      XX2=DISP(IX-1,IY,3)*(CAVG(IX,IY+1)+CAVG(IX-1,IY+1)-CAVG(IX,IY-1)-C
     1AVG(IX-1,IY-1))                                                   
   46 IF (IX.LE.1) GO TO 48                                             
      IF (IY.GE.NMY) GO TO 47                                           
      IF (IX.GE.NMX) GO TO 48                                           
      YY1=DISP(IX,IY,4)*(CAVG(IX+1,IY)+CAVG(IX+1,IY+1)-CAVG(IX-1,IY)-CAV
     1G(IX-1,IY+1))                                                     
   47 IF (IY.LE.1) GO TO 48                                             
      IF (IX.LE.1.OR.IX.GE.NMX) GO TO 48                                
      YY2=DISP(IX,IY-1,4)*(CAVG(IX+1,IY)+CAVG(IX+1,IY-1)-CAVG(IX-1,IY)-C
     1AVG(IX-1,IY-1))                                                   
   48 CONTINUE                                                          
      CNCNC(IX,IY)=CNCNC(IX,IY)+EQFCT*(X1+X2+Y1+Y2+XX1-XX2+YY1-YY2)     
   60 CONTINUE                                                          
C     ****************************************************************  
      GO TO 110                                                         
C     ****************************************************************  
C     ---CONC. CHANGE AT NODES DUE TO CONVECTION---                     
C                                  ... AND DECAY---                     
   70 DO 90 IX=1,NMX                                                    
      DO 90 IY=1,NMY                                                    
      JX=IX+MX-1                                                        
      JY=IY+MY-1                                                        
      IF (THCK(JX,JY).EQ.0.0) GO TO 90                                  
      APC=NPCELL(IX,IY)                                                 
      IF (APC.GT.0.0) GO TO 80                                          
      IF (REC(JX,JY).NE.0.0.OR.VPRM(JX,JY).GT.0.09) GO TO 90            
      NZERO=NZERO+1                                                     
      GO TO 90                                                          
   80 CONC(IX,IY)=SUMC(IX,IY)/APC                                       
      CAVG(IX,IY)=(CONC(IX,IY)+CNOLD(IX,IY))*0.5                        
   90 CONTINUE                                                          
C        ---CHECK NUMBER OF CELLS VOID OF PTS.---                       
      IF (NZERO.GT.0) WRITE (6,290) NZERO,IMOV                          
      IF (NZERO.LE.NZCRIT) GO TO 20                                     
      TEST=99.0                                                         
      WRITE (6,300)                                                     
      WRITE (6,320)                                                     
      DO 100 IY=1,NMY                                                   
  100 WRITE (6,330) (NPCELL(IX,IY),IX=1,NMX)                            
      GO TO 20                                                          
C     ****************************************************************  
C     ---CHANGE CONCENTRATIONS AT NODES---                              
  110 DO 130 IX=1,NMX                                                   
      DO 130 IY=1,NMY                                                   
      JX=IX+MX-1                                                        
      JY=IY+MY-1                                                        
      IF (THCK(JX,JY).EQ.0.0) GO TO 120                                 
      CNCPCT=0.0                                                        
      IF (CONC(IX,IY).GT.0.0) CNCPCT=CNCNC(IX,IY)/CONC(IX,IY)           
      CONC(IX,IY)=CONC(IX,IY)+CNCNC(IX,IY)                              
      SUMC(IX,IY)=0.0                                                   
      IF (CNCPCT.LT.0.0) SUMC(IX,IY)=CNCPCT                             
      GO TO 130                                                         
  120 IF (CONC(IX,IY).GT.0.0) WRITE (6,310) JX,JY,CONC(IX,IY)           
      CONC(IX,IY)=0.0                                                   
  130 CONTINUE                                                          
C     ****************************************************************  
C     ---CHANGE CONCENTRATION OF PARTICLES---                           
      DO 180 IN=1,NP                                                    
      IF (PART(1,IN).EQ.0.0) GO TO 180                                  
      INX=ABS(PART(1,IN))+0.5                                           
      INY=ABS(PART(2,IN))+0.5                                           
      JNX=INX-MX+1                                                      
      JNY=INY-MY+1                                                      
C     ---UPDATE CONC. OF PTS. IN SINK/SOURCE CELLS---                   
      IF (REC(INX,INY).NE.0.0) GO TO 140                                
      IF (VPRM(INX,INY).LE.0.09) GO TO 150                              
  140 PART(3,IN)=CONC(JNX,JNY)                                          
      GO TO 180                                                         
  150 IF (CNCNC(JNX,JNY).LT.0.0) GO TO 170                              
  160 PART(3,IN)=PART(3,IN)+CNCNC(JNX,JNY)                              
      GO TO 180                                                         
  170 IF (CONC(JNX,JNY).LE.0.0) GO TO 160                               
      IF (SUMC(JNX,JNY).LT.-1.0) GO TO 160                              
      PART(3,IN)=PART(3,IN)+PART(3,IN)*SUMC(JNX,JNY)                    
  180 CONTINUE                                                          
      WRITE (6,280) TIM(N),TIMV,SUMTCH                                  
C     ****************************************************************  
C     ---COMPUTE MASS BALANCE FOR SOLUTE---                             
      CSTORM=0.0                                                        
      STORM=0.0                                                         
      ADSORB=0.0                                                        
      DO 270 IX=1,NMX                                                   
      DO 270 IY=1,NMY                                                   
      JX=IX+MX-1                                                        
      JY=IY+MY-1                                                        
      IF (THCK(JX,JY).EQ.0.0) GO TO 270                                 
      C1=CONC(IX,IY)                                                    
      C1B=C1*THCK(JX,JY)                                                
      DELDCY=CNOLD(IX,IY)-CNOLD(IX,IY)*DCYT                             
      DMASS1=DMASS1-DELDCY*THCK(JX,JY)*RFAREA                           
      SUMC(IX,IY)=0.0                                                   
      WTFCT=0.0                                                         
C        ---COMPUTE MASS OF SOLUTE IN STORAGE---                        
      STORM=STORM+C1B                                                   
C        ---COMPUTE MASS ADSORBED---                                    
      ADSORB=C1B+ADSORB                                                 
C        ---ACCOUNT FOR MASS PUMPED IN, OUT, RECHARGED, & DISCHARGED--- 
      IF (REC(JX,JY)) 200,210,190                                       
  190 FCT1=NPOLD(IX,IY)                                                 
      FCT2=NPCELL(IX,IY)                                                
      IF (FCT2.GT.0.0) WTFCT=FCT1/FCT2                                  
      CMSOUT=CMSOUT+REC(JX,JY)*TIMV*((1.0-WTFCT)*CNOLD(IX,IY)+WTFCT*C1) 
      GO TO 210                                                         
  200 CMSIN=CMSIN+REC(JX,JY)*CNRECH(IX,IY)*TIMV                         
  210 IF (RECH(JX,JY)) 230,240,220                                      
  220 CMSOUT=CMSOUT+RECH(JX,JY)*TVA2*(CNOLD(IX,IY)+C1)                  
      GO TO 240                                                         
  230 CMSIN=CMSIN+RECH(JX,JY)*CNRECH(IX,IY)*TVA                         
C     ****************************************************************  
C        ---ACCOUNT FOR BOUNDARY FLOW---                                
  240 IF (VPRM(JX,JY).EQ.0.0) GO TO 265                                 
      FLW=VPRM(JX,JY)*(WT(JX,JY)-HK(JX,JY))                             
      IF (FLW.GT.0.0) GO TO 250                                         
      IF (FLW.LT.0.0) GO TO 260                                         
      GO TO 265                                                         
C           ---MASS IN BOUNDARY DURING TIME STEP---                     
  250 FLMIN=FLMIN+FLW*CNRECH(IX,IY)*TVA                                 
      GO TO 265                                                         
C           ---MASS OUT DURING TIME STEP---                             
  260 FCT1=NPOLD(IX,IY)                                                 
      FCT2=NPCELL(IX,IY)                                                
      IF (FCT2.GT.0.0) WTFCT=FCT1/FCT2                                  
      FLMOT=FLMOT+FLW*TVA*((1.0-WTFCT)*CNOLD(IX,IY)+WTFCT*C1)           
  265 NPOLD(IX,IY)=NPCELL(IX,IY)                                        
      NPCELL(IX,IY)=0                                                   
  270 CONTINUE                                                          
C           ---SUBGRID BOUNDARIES---                                    
      IF (MCHK.EQ.0) GO TO 275                                          
      YT=YDEL*TIMV                                                      
      XT=XDEL*TIMV                                                      
      DO 272 IY=MY,MMY                                                  
      IX=MX                                                             
      JY=IY-MY+1                                                        
      FLW=TMRX(IX-1,IY,1)*(HK(IX-1,IY)-HK(IX,IY))                       
      IF (FLW.GT.0.0) FLMIN=FLMIN+FLW*YT*CNOLD(1,JY)*DCYT               
      IF (FLW.LT.0.0) FLMOT=FLMOT+FLW*YT*CNOLD(1,JY)*DCYT               
      IX=MMX                                                            
      FLW=TMRX(IX,IY,1)*(HK(IX+1,IY)-HK(IX,IY))                         
      IF (FLW.GT.0.0) FLMIN=FLMIN+FLW*YT*CNOLD(NMX,JY)*DCYT             
  272 IF (FLW.LT.0.0) FLMOT=FLMOT+FLW*YT*CNOLD(NMX,JY)*DCYT             
      DO 274 IX=MX,MMX                                                  
      IY=MY                                                             
      JX=IX-MX+1                                                        
      FLW=TMRX(IX,IY-1,2)*(HK(IX,IY-1)-HK(IX,IY))                       
      IF (FLW.GT.0.0) FLMIN=FLMIN+FLW*XT*CNOLD(JX,1)*DCYT               
      IF (FLW.LT.0.0) FLMOT=FLMOT+FLW*XT*CNOLD(JX,1)*DCYT               
      IY=MMY                                                            
      FLW=TMRX(IX,IY,2)*(HK(IX,IY+1)-HK(IX,IY))                         
      IF (FLW.GT.0.0) FLMIN=FLMIN+FLW*XT*CNOLD(JX,NMY)*DCYT             
  274 IF (FLW.LT.0.0) FLMOT=FLMOT+FLW*XT*CNOLD(JX,NMY)*DCYT             
  275 CONTINUE                                                          
C     ****************************************************************  
C        ---COMPUTE CHANGE IN MASS OF SOLUTE STORED---                  
C        ---COMPUTE MASS LOST BY DECAY---                               
      STORM=STORM*AREA                                                  
      ADSORB=ADSORB*DK*RHOB/POROS*AREA                                  
      CSTORM=STORM-STORMI                                               
      CSTM2=CSTORM+ADSORB-SORBI                                         
      DMASS1=DMASS1+SRCDCY                                              
      SUMIO=FLMIN+FLMOT-CMSIN-CMSOUT                                    
C     ****************************************************************  
C     ---REGENERATE PARTICLES IF 'NZCRIT' EXCEEDED---                   
      IF (TEST.GT.98.0) CALL GENPT                                      
      TEST=0.0                                                          
C     ****************************************************************  
      RETURN                                                            
C     ****************************************************************  
C                                                                       
C                                                                       
C                                                                       
  280 FORMAT (3H   ,11HTIM(N)   = ,1G12.5,10X,11HTIMV     = ,1G12.5,10X,
     19HSUMTCH = ,G12.5)                                                
  290 FORMAT (1H0,5X,40HNUMBER OF CELLS WITH ZERO PARTICLES  =  ,I4,5X,9
     1HIMOV  =  ,I4/)                                                   
  300 FORMAT (1H0,5X,44H***   NZCRIT EXCEEDED  ---  CALL GENPT   ***/)  
  310 FORMAT (1H ,5X,37H***CONC.GT.0.AND.THCK.EQ.0 AT NODE = ,2I4,4X,7HC
     1ONC = ,G10.4,4H ***)                                              
  320 FORMAT (1H0,2X,6HNPCELL/)                                         
  330 FORMAT (1H ,4X,20I3)                                              
      END                                                               
      SUBROUTINE OUTPT                                                  
      DOUBLE PRECISION TMRX,VPRM,HI,HR,HC,HK,WT,REC,RECH,TIM,AOPT,TITLE 
      DOUBLE PRECISION XDEL,YDEL,S,AREA,SUMT,RHO,PARAM,TEST,TOL,PINT,   
     1                 HMIN,PYR,ANFCTR                                  
      DOUBLE PRECISION TOTLQ,TOTLQI,TPIN,TPOUT,PQIN,PQOUT,DELQ,QOUT,QIN,
     1                 QNET,DDRW                                        
      DOUBLE PRECISION QSTR,TPUM,PUMP,TOTLQN,SRCS,SINKS,ERRMB,DENOM,    
     1                 PCTERR                                           
      COMMON /PRMJ/ NTIM,NPMP,NPNT,NITP,N,NX,NY,NP,NREC,INT,NNX,NNY,NUMO
     1BS,NMOV,IMOV,NPMAX,ITMAX,NZCRIT,IPRNT,NPTPND,NPNTMV,NPNTVL,NPNTD,N
     2PNCHV,NPDELC,ICHK                                                 
      COMMON /HEDA/ THCK(040,040),TMWL(05,50),TMOBS(50)                 
      COMMON /HEDB/ TMRX(040,040,2),VPRM(040,040),HI(040,040),          
     1              HR(040,040),HC(040,040),HK(040,040),WT(040,040),    
     2 REC(040,040),RECH(040,040),TIM(100),AOPT(20),TITLE(10),XDEL,YDEL,
     3              S,AREA,SUMT,RHO,PARAM,TEST,TOL,PINT,HMIN,PYR,ANFCTR 
      COMMON /BALM/ TOTLQ,TOTLQI,TPIN,TPOUT                             
      DIMENSION IH(040)                                                 
C     ***************************************************************   
      TIMD=SUMT/86400.                                                  
      TIMY=SUMT/(86400.0*365.25)                                        
C     ---PRINT HEAD VALUES---                                           
      WRITE (6,120)                                                     
      WRITE (6,130) N                                                   
      WRITE (6,140) SUMT                                                
      WRITE (6,150) TIMD                                                
      WRITE (6,160) TIMY                                                
      WRITE (6,170)                                                     
      DO 10 IY=1,NY                                                     
   10 WRITE (6,180) (HK(IX,IY),IX=1,NX)                                 
      IF (N.EQ.0) GO TO 110                                             
C     ***************************************************************   
C     ---PRINT HEAD MAP---                                              
      WRITE (6,120)                                                     
      WRITE (6,130) N                                                   
      WRITE (6,140) SUMT                                                
      WRITE (6,150) TIMD                                                
      WRITE (6,160) TIMY                                                
      WRITE (6,170)                                                     
      DO 30 IY=1,NY                                                     
      DO 20 IX=1,NX                                                     
   20 IH(IX)=NINT(HK(IX,IY))                                            
   30 WRITE (6,190) (IH(ID),ID=1,NX)                                    
C     ***************************************************************   
C     ---COMPUTE WATER BALANCE AND DRAWDOWN---                          
      QSTR=0.D0                                                         
      PUMP=0.D0                                                         
      PQIN=0.D0                                                         
      PQOUT=0.D0                                                        
      TPUM=0.D0                                                         
      QIN=0.D0                                                          
      QOUT=0.D0                                                         
      QNET=0.D0                                                         
      DELQ=0.D0                                                         
      PCTERR=0.D0                                                       
      WRITE (6,290)                                                     
C                                                                       
      DO 80 IY=1,NY                                                     
      DO 70 IX=1,NX                                                     
      IH(IX)=0                                                          
      IF (THCK(IX,IY).EQ.0.0) GO TO 70                                  
      IF (REC(IX,IY).GT.0.0) GO TO 32                                   
      PQIN=PQIN+REC(IX,IY)                                              
      GO TO 34                                                          
   32 PQOUT=PQOUT+REC(IX,IY)                                            
   34 IF (RECH(IX,IY).GT.0.0) GO TO 36                                  
      PQIN=PQIN+RECH(IX,IY)*AREA                                        
      GO TO 38                                                          
   36 PQOUT=PQOUT+RECH(IX,IY)*AREA                                      
   38 IF (VPRM(IX,IY).EQ.0.0) GO TO 60                                  
      DELQ=VPRM(IX,IY)*AREA*(WT(IX,IY)-HK(IX,IY))                       
      IF (DELQ.GT.0.0) GO TO 40                                         
      QOUT=QOUT+DELQ                                                    
      GO TO 50                                                          
   40 QIN=QIN+DELQ                                                      
   50 QNET=QNET+DELQ                                                    
   60 DDRW=HI(IX,IY)-HK(IX,IY)                                          
      IH(IX)=NINT(DDRW)                                                 
      QSTR=QSTR+DDRW*AREA*S                                             
   70 CONTINUE                                                          
C        ---PRINT DRAWDOWN MAP---                                       
      WRITE (6,300) (IH(IX),IX=1,NX)                                    
   80 CONTINUE                                                          
      TPUM=PQIN+PQOUT                                                   
      PUMP=TPIN+TPOUT                                                   
      TOTLQN=TOTLQ+TOTLQI                                               
      SRCS=QSTR-TPIN+TOTLQI                                             
      SINKS=TPOUT-TOTLQ                                                 
      ERRMB=SRCS-SINKS                                                  
      DENOM=(SRCS+SINKS)*0.5D0                                          
      IF (DENOM.EQ.0.0) GO TO 100                                       
      PCTERR=ERRMB*100.D0/DENOM                                         
C        ---PRINT MASS BALANCE DATA FOR FLOW MODEL---                   
  100 WRITE (6,240)                                                     
      WRITE (6,211) TPIN                                                
      WRITE (6,212) TPOUT                                               
      WRITE (6,250) PUMP                                                
      WRITE (6,230) QSTR                                                
      WRITE (6,202) TOTLQI                                              
      WRITE (6,203) TOTLQ                                               
      WRITE (6,260) TOTLQN                                              
      WRITE (6,270) ERRMB                                               
      WRITE (6,280) PCTERR                                              
      WRITE (6,201)                                                     
      WRITE (6,202) QIN                                                 
      WRITE (6,203) QOUT                                                
      WRITE (6,204) QNET                                                
      WRITE (6,211) PQIN                                                
      WRITE (6,212) PQOUT                                               
      WRITE (6,210) TPUM                                                
C     ***************************************************************   
  110 RETURN                                                            
C     ***************************************************************   
C                                                                       
C                                                                       
C                                                                       
  120 FORMAT (1H1,23HHEAD DISTRIBUTION - ROW)                           
  130 FORMAT (1X,23HNUMBER OF TIME STEPS = ,1I5)                        
  140 FORMAT (8X,16HTIME(SECONDS) = ,1G12.5)                            
  150 FORMAT (8X,16HTIME(DAYS)    = ,1E12.5)                            
  160 FORMAT (8X,16HTIME(YEARS)   = ,1E12.5)                            
  170 FORMAT (1H )                                                      
  180 FORMAT (1H0,10F12.7)                                              
  190 FORMAT (1H0,30I4)                                                 
  201 FORMAT (1H0,2X,33HRATE MASS BALANCE -- (IN C.F.S.) //)            
  202 FORMAT (4X,29HLEAKAGE INTO AQUIFER       = ,E12.5)                
  203 FORMAT (4X,29HLEAKAGE OUT OF AQUIFER     = ,E12.5)                
  204 FORMAT (4X,29HNET LEAKAGE    (QNET)      = ,E12.5)                
  210 FORMAT (4X,29HNET WITHDRAWAL   (TPUM)    = ,E12.5)                
  211 FORMAT (4X,29HRECHARGE AND INJECTION     = ,E12.5)                
  212 FORMAT (4X,29HPUMPAGE AND E-T WITHDRAWAL = ,E12.5)                
  230 FORMAT (4X,29HWATER RELEASE FROM STORAGE = ,1E12.5)               
  240 FORMAT (1H0,2X,38HCUMULATIVE MASS BALANCE -- (IN FT**3) //)       
  250 FORMAT (4X,29HCUMULATIVE  NET  PUMPAGE   = ,1E12.5)               
  260 FORMAT (4X,29HCUMULATIVE  NET  LEAKAGE   = ,1E12.5)               
  270 FORMAT (1H0,7X,25HMASS BALANCE RESIDUAL  = ,G12.5)                
  280 FORMAT (1H ,7X,25HERROR  (AS PERCENT)    = ,G12.5/)               
  290 FORMAT (1H1,8HDRAWDOWN)                                           
  300 FORMAT (3H   ,25I5)                                               
      END                                                               
      SUBROUTINE CHMOT                                                  
      DOUBLE PRECISION TMRX,VPRM,HI,HR,HC,HK,WT,REC,RECH,TIM,AOPT,TITLE 
      DOUBLE PRECISION XDEL,YDEL,S,AREA,SUMT,RHO,PARAM,TEST,TOL,PINT,   
     1                 HMIN,PYR,ANFCTR                                  
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
      COMMON /CHMR/ RF,DK,RHOB,THALF,DECAY,ADSORB,SORBI,DMASS1,CSTM2    
      DIMENSION IC(020)                                                 
C     ***************************************************************   
      TMFY=86400.0*365.25                                               
      TMYR=SUMT/TMFY                                                    
      TCHD=SUMTCH/86400.0                                               
      TCHYR=SUMTCH/TMFY                                                 
      ERR1=0.0                                                          
      ERR3=0.0                                                          
      IF (MOD(IMOV,NPNTMV).NE.0.AND.(IMOV.NE.NMOV.OR.                   
     1   (MOD(N,NPNT).NE.0.AND.N.NE.NTIM.AND.IPRNT.EQ.0)))              
     2                 GO TO 100                                        
C     ***************************************************************   
C     ---PRINT CONCENTRATIONS---                                        
      WRITE (6,160)                                                     
      WRITE (6,170) N                                                   
      IF (N.GT.0) WRITE (6,180) TIM(N)                                  
      WRITE (6,190) SUMT                                                
      WRITE (6,450) SUMTCH                                              
      WRITE (6,200) TCHD                                                
      WRITE (6,210) TMYR                                                
      WRITE (6,460) TCHYR                                               
      WRITE (6,380) IMOV                                                
      WRITE (6,220) 
      DO 20 IY=1,NMY                                                    
      DO 10 IX=1,NMX                                                    
   10 IC(IX)=NINT(CONC(IX,IY)) 
CTGC
CTGC WRITE CONCENTRATION ARRAY TO SEPARATE 
CTGC FILE FOR CHEMICAL REACTION
CTGC COMPUTATIONS    
CTGC COMPILE WITH -ccx DIRECTIVE  
CTGC 2019-0419 -ccx DIRECTIVE NOT GFORTRAN                                                 
C     WRITE(11,*)(CONC(IX,IY),IX=1,NMX)   
CTGC                                     
   20 WRITE (6,240) (IC(IX),IX=1,NMX)                              
C     ***************************************************************   
      IF (N.EQ.0) GO TO 150                                             
      IF (NPDELC.EQ.0) GO TO 50                                         
C                                                                       
C     ---PRINT CHANGES IN CONCENTRATION---                              
      WRITE (6,230)                                                     
      WRITE (6,170) N                                                   
      WRITE (6,180) TIM(N)                                              
      WRITE (6,190) SUMT                                                
      WRITE (6,450) SUMTCH                                              
      WRITE (6,200) TCHD                                                
      WRITE (6,210) TMYR                                                
      WRITE (6,460) TCHYR                                               
      WRITE (6,380) IMOV                                                
      WRITE (6,220)                                                     
      DO 40 IY=1,NMY                                                    
      DO 30 IX=1,NMX                                                    
   30 IC(IX)=NINT(CONC(IX,IY)-CONINT(IX,IY))                            
   40 WRITE (6,240) (IC(IX),IX=1,NMX)                                   
C     ***************************************************************   
C     ---PRINT MASS BALANCE DATA FOR SOLUTE---                          
   50 RESID=SUMIO-CSTM2+DMASS1                                          
      SUMIN=FLMIN-CMSIN                                                 
      IF (SUMIN.EQ.0.0) GO TO 60                                        
      ERR1=RESID*100.0/SUMIN                                            
      IF (SUMIO.GT.(STORMI+SORBI)) GO TO 70                             
   60 IF (STORMI.EQ.0.0) GO TO 70                                       
      ERR3=-100.0*(RESID)/(STORMI+SORBI-SUMIO)                          
   70 WRITE (6,220)                                                     
      WRITE (6,250)                                                     
      WRITE (6,220)                                                     
      WRITE (6,260) FLMIN                                               
      WRITE (6,270) FLMOT                                               
      RECIN=-CMSIN                                                      
      RECOUT=-CMSOUT                                                    
      WRITE (6,290) RECIN                                               
      WRITE (6,280) RECOUT                                              
      WRITE (6,295) DMASS1                                              
      WRITE (6,296) ADSORB                                              
      WRITE (6,298) SORBI                                               
      WRITE (6,300) SUMIO                                               
      WRITE (6,310) STORMI                                              
      WRITE (6,320) STORM                                               
      WRITE (6,330) CSTORM                                              
      WRITE (6,332) CSTM2                                               
      WRITE (6,340)                                                     
      WRITE (6,350) RESID                                               
      WRITE (6,360) ERR1                                                
   80 IF (STORMI.EQ.0.0) GO TO 100                                      
      IF (SUMIN.NE.0.0.AND.SUMIO.GT.(STORMI+SORBI)) GO TO 100           
      WRITE (6,370)                                                     
      WRITE (6,360) ERR3                                                
C     ***************************************************************   
C     ---PRINT HYDROGRAPHS AFTER 50 STEPS OR END OF SIMULATION---       
  100 IF (NUMOBS.LE.0) GO TO 150                                        
      IF (S.GT.0.0) THEN                                                
       IF (IMOV.NE.NMOV.OR.                                             
     1    (MOD(N,50).NE.0.AND.N.NE.NTIM.AND.IPRNT.EQ.0)) GO TO 150      
      ELSE                                                              
       IF (MOD(IMOV,50).NE.0.AND.IMOV.NE.NMOV) GO TO 150                
      END IF                                                            
      WRITE (6,390) TITLE                                               
      WRITE (6,400) INT                                                 
      IF (S.GT.0.0) WRITE (6,410)                                       
      IF (S.EQ.0.0) WRITE (6,420)                                       
C        ---TABULATE HYDROGRAPH DATA---                                 
      MOZ=0                                                             
      IF (S.GT.0.0) GO TO 110                                           
      NTO=NMOV                                                          
      IF (NMOV.GT.50) NTO=MOD(IMOV,50)                                  
      GO TO 120                                                         
  110 NTO=N                                                             
      IF (N.GT.50) NTO=MOD(N,50)                                        
  120 IF (NTO.EQ.0) NTO=50                                              
      DO 140 J=1,NUMOBS                                                 
      TMYR=0.0                                                          
      JX=IXOBS(J)                                                       
      JY=IYOBS(J)                                                       
      WRITE (6,430) J,IXOBS(J),IYOBS(J)                                 
      C1INT=0.0                                                         
      IX=JX-MX+1                                                        
      IY=JY-MY+1                                                        
      IF (JX.LT.MX.OR.JY.LT.MY.OR.JX.GT.MMX.OR.JY.GT.MMY) GO TO 125     
      C1INT=CONINT(IX,IY)                                               
      GO TO 127                                                         
  125 WRITE (6,435)                                                     
  127 WRITE (6,440) MOZ,WT(JX,JY),C1INT,                                
     1TMYR                                                              
      DO 130 M=1,NTO                                                    
      TMYR=TMOBS(M)/TMFY                                                
  130 WRITE (6,440) M,TMWL(J,M),TMCN(J,M),TMYR                          
  140 CONTINUE                                                          
C     ****************************************************************  
  150 RETURN                                                            
C     ****************************************************************  
C                                                                       
C                                                                       
C                                                                       
  160 FORMAT (1H1,13HCONCENTRATION/)                                    
  170 FORMAT (1X,23HNUMBER OF TIME STEPS = ,1I5)                        
  180 FORMAT (8X,16HDELTA T       = ,1G12.5)                            
  190 FORMAT (8X,16HTIME(SECONDS) = ,1G12.5)                            
  200 FORMAT (3X,21HCHEM.TIME(DAYS)    = ,1E12.5)                       
  210 FORMAT (8X,16HTIME(YEARS)   = ,1E12.5)                            
  220 FORMAT (1H )                                                      
  230 FORMAT (1H1,23HCHANGE IN CONCENTRATION/)                          
  240 FORMAT (1H0,20I5)                                                 
  250 FORMAT (1H ,21HCHEMICAL MASS BALANCE)                             
  260 FORMAT (8X,25HMASS IN BOUNDARIES     = ,1E12.5)                   
  270 FORMAT (8X,25HMASS OUT BOUNDARIES    = ,1E12.5)                   
  280 FORMAT (8X,25HMASS PUMPED OUT        = ,1E12.5)                   
  290 FORMAT (8X,25HMASS PUMPED IN         = ,1E12.5)                   
  295 FORMAT (8X,25HMASS LOST BY DECAY     = ,1E12.5)                   
  296 FORMAT (8X,25HMASS ADSORBED ON SOLIDS= ,1E12.5)                   
  298 FORMAT (8X,25HINITIAL MASS ADSORBED  = ,1E12.5)                   
  300 FORMAT (8X,25HINFLOW MINUS OUTFLOW   = ,1E12.5)                   
  310 FORMAT (8X,25HINITIAL MASS DISSOLVED = ,1E12.5)                   
  320 FORMAT (8X,25HPRESENT MASS DISSOLVED = ,1E12.5)                   
  330 FORMAT (8X,25HCHANGE MASS DISSOLVED  = ,1E12.5)                   
  332 FORMAT (8X,25HCHANGE TOTL.MASS STORED= ,1E12.5)                   
  340 FORMAT (1H ,5X,53HCOMPARE RESIDUAL WITH NET FLUX AND MASS ACCUMULA
     1TION:)                                                            
  350 FORMAT (8X,25HMASS BALANCE RESIDUAL  = ,1E12.5)                   
  360 FORMAT (8X,25HERROR  (AS PERCENT)    = ,1E12.5)                   
  370 FORMAT (1H ,5X,55HCOMPARE INITIAL MASS STORED WITH CHANGE IN MASS 
     1STORED:)                                                          
  380 FORMAT (1X,23H NO. MOVES COMPLETED = ,1I5)                        
  390 FORMAT (1H1,10A8//)                                               
  400 FORMAT (1H0,5X,65HTIME VERSUS HEAD AND CONCENTRATION AT SELECTED O
     1BSERVATION POINTS//15X,19HPUMPING PERIOD NO. ,I4////)             
  410 FORMAT (1H0,16X,19HTRANSIENT  SOLUTION////)                       
  420 FORMAT (1H0,15X,21HSTEADY-STATE SOLUTION////)                     
  430 FORMAT (1H0,20X,22HOBS.WELL NO.    X    Y,17X,1HN,6X,40HHEAD (FT) 
     1   CONC.(MG/L)    TIME (YEARS)//24X,I3,9X,I2,3X,I2//)             
  435 FORMAT (1H ,3X,45H** NOTE **  THIS OBS. WELL IS LOCATED OUTSIDE/16
     1X,24HOF THE TRANSPORT SUBGRID)                                    
  440 FORMAT (1H ,58X,I2,6X,F7.1,8X,F7.1,8X,F7.3)                       
  450 FORMAT (1H ,2X,21HCHEM.TIME(SECONDS) = ,E12.5)                    
  460 FORMAT (1H ,2X,21HCHEM.TIME(YEARS)   = ,E12.5)                    
      END                                                               
