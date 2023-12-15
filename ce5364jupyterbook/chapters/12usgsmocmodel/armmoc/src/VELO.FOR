      SUBROUTINE VELO                                                   
C      DOUBLE PRECISION DMIN1,DEXP,DLOG,DABS                             
      DOUBLE PRECISION TMRX,VPRM,HI,HR,HC,HK,WT,REC,RECH,TIM,AOPT,TITLE 
      DOUBLE PRECISION XDEL,YDEL,S,AREA,SUMT,RHO,PARAM,TEST,TOL,PINT,   
     1                 HMIN,PYR,ANFCTR                                  
      DOUBLE PRECISION RATE,SLEAK,DIV                                   
      COMMON /PRMJ/ NTIM,NPMP,NPNT,NITP,N,NX,NY,NP,NREC,INT,NNX,NNY,    
     1              NUMOBS,NMOV,IMOV,NPMAX,ITMAX,NZCRIT,IPRNT,NPTPND,   
     2              NPNTMV,NPNTVL,NPNTD,NPNCHV,NPDELC,ICHK              
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
      COMMON /CHMC/ SUMC(020,020),VXBDY(040,040),VYBDY(040,040)         
      COMMON /DIFUS/ DISP(020,020,4)                                    
      COMMON /CHMR/ RF,DK,RHOB,THALF,DECAY,ADSORB,SORBI,DMASS1,CSTM2    
C     ***************************************************************   
C      DO NOT RECOMPUTE VELOCITY OR DISP.COEFS FOR STEADY-STATE FLOW    
      ISOLV=1                                                           
      IF (S.EQ.0.0.AND.ICHK.EQ.0.AND.(N.GT.1.OR.INT.GT.1)) THEN         
       ISOLV=0                                                          
       GO TO 28                                                         
      END IF                                                            
C     ---COMPUTE VELOCITIES AND STORE---                                
      VMAX=1.0E-10                                                      
      VMAY=1.0E-10                                                      
      VMXBD=1.0E-10                                                     
      VMYBD=1.0E-10                                                     
      TMV=TIM(N)*1.0E5                                                  
      LIM=0                                                             
      MAXX=0                                                            
      MAXY=0                                                            
      MAXVXI=0                                                          
      MAXVXJ=0                                                          
      MAXVYI=0                                                          
      MAXVYJ=0                                                          
C                                                                       
      DO 20 IX=1,NX                                                     
      DO 20 IY=1,NY                                                     
      IF (IX.GT.NMX.OR.IY.GT.NMY) GO TO 12                              
      DO 10 IZ=1,4                                                      
   10 DISP(IX,IY,IZ)=0.0                                                
C                                                                       
   12 JCK=0                                                             
      IF (IX.LT.(MX-1).OR.IY.LT.(MY-1).OR.IX.GT.(MMX+1).OR.IY.GT.(MMY+1)
     1) JCK=1                                                           
      IF (THCK(IX,IY).EQ.0.0) GO TO 20                                  
      RATE=REC(IX,IY)/AREA                                              
      SLEAK=(HK(IX,IY)-WT(IX,IY))*VPRM(IX,IY)                           
      DIV=0.D0                                                          
      IF(RATE.LT.0.0) DIV=RATE                                          
      IF(SLEAK.LT.0.0) DIV=DIV+SLEAK                                    
      IF(RECH(IX,IY).LT.0.0) DIV=DIV+RECH(IX,IY)                        
C                                                                       
C        ---VELOCITIES AT CELL BOUNDARIES---                            
C           TERM SAVED IS VELOCITY*THICKNESS*POROSITY                   
      VXBDY(IX,IY)=TMRX(IX,IY,1)*(HK(IX,IY)-HK(IX+1,IY))                
      VYBDY(IX,IY)=TMRX(IX,IY,2)*(HK(IX,IY)-HK(IX,IY+1))                
C        ---VELOCITIES AT NODES---                                      
C           TEMPORARILY SAVE SEEPAGE VELOCITY FOR PRINTING              
      VX(IX,IY)=(0.5*(VXBDY(IX,IY)+VXBDY(IX-1,IY)))/THCK(IX,IY)         
      VY(IX,IY)=(0.5*(VYBDY(IX,IY)+VYBDY(IX,IY-1)))/THCK(IX,IY)         
      IF (JCK.EQ.0) THEN                                                
       IF (THCK(IX+1,IY).NE.0.0.AND.THCK(IX+1,IY).LT.THCK(IX,IY)) THEN  
        ABVX=ABS(VXBDY(IX,IY))/THCK(IX+1,IY)                            
       ELSE                                                             
        ABVX=ABS(VXBDY(IX,IY))/THCK(IX,IY)                              
       END IF                                                           
       IF (THCK(IX,IY+1).NE.0.0.AND.THCK(IX,IY+1).LT.THCK(IX,IY)) THEN  
        ABVY=ABS(VYBDY(IX,IY))/THCK(IX,IY+1)                            
       ELSE                                                             
        ABVY=ABS(VYBDY(IX,IY))/THCK(IX,IY)                              
       END IF                                                           
       IF (ABVX.GT.VMXBD) THEN                                          
         VMXBD=ABVX                                                     
         MAXVXI=IX                                                      
         MAXVXJ=IY                                                      
       END IF                                                           
       IF (ABVY.GT.VMYBD) THEN                                          
         VMYBD=ABVY                                                     
         MAXVYI=IX                                                      
         MAXVYJ=IY                                                      
       END IF                                                           
      END IF                                                            
C                                                                       
      IF (DIV.GE.0.0) GO TO 20                                          
      IF (JCK.GT.0) GO TO 20                                            
      TDIV=(THCK(IX,IY)*RF)/DABS(DIV)                                   
      IF (TDIV.GE.TMV) GO TO 20                                         
      TMV=TDIV                                                          
      MAXX=IX                                                           
      MAXY=IY                                                           
   20 CONTINUE                                                          
C      IF OUTPUT OF VELOCITIES ON CELL BOUNDARIES IS DESIRED,           
C       SEE LINES E 732, E 795A, E 839, E 909, E 986A, E1027A, AND E2399
C      ACTIVATE NEXT 6 LINES TO COMPUTE BOUNDARY VELOCITIES FOR PRINTING
C     DO 25 IY=2,NNY                                                    
C     DO 25 IX=2,NNX                                                    
C     IF (THCK(IX,IY).EQ.0.0) GO TO 25                                  
C     VXBDY(IX,IY)=VXBDY(IX,IY)/(THCK(IX,IY)+THCK(IX+1,IY))*2.          
C     VYBDY(IX,IY)=VYBDY(IX,IY)/(THCK(IX,IY)+THCK(IX,IY+1))*2.          
C  25 CONTINUE                                                          
C     ***************************************************************   
C     ---PRINT VELOCITIES---                                            
   28 IF (NPNTVL.EQ.0) GO TO 80                                         
      IF (NPNTVL.EQ.-2.AND.(N.EQ.NTIM.OR.IPRNT.EQ.1)) GO TO 30          
      IF (NPNTVL.EQ.-1.AND.N.EQ.1) GO TO 30                             
      IF (MOD(N,NPNTVL).EQ.0) GO TO 30                                  
      GO TO 80                                                          
   30 IF (ISOLV.EQ.0) THEN                                              
       DO 32 IY=2,NNY                                                   
       DO 32 IX=2,NNX                                                   
       IF(THCK(IX,IY).EQ.0.0) GO TO 32                                  
       VX(IX,IY)=VX(IX,IY)/THCK(IX,IY)                                  
       VY(IX,IY)=VY(IX,IY)/THCK(IX,IY)                                  
C       ACTIVATE NEXT 2 LINES IF BOUNDARY VELOCITIES PRINTED            
C      VXBDY(IX,IY)=2.0*VXBDY(IX,IY)/(THCK(IX,IY)+THCK(IX+1,IY))        
C      VYBDY(IX,IY)=2.0*VYBDY(IX,IY)/(THCK(IX,IY)+THCK(IX,IY+1))        
   32  CONTINUE                                                         
       ISOLV=-1                                                         
      END IF                                                            
      WRITE (6,320)                                                     
      WRITE (6,330)                                                     
      DO 40 IY=1,NY                                                     
   40 WRITE (6,350) (VX(IX,IY),IX=1,NX)                                 
C      ACTIVATE NEXT 3 LINES TO PRINT BOUNDARY VELOCITIES               
C     WRITE (6,340)                                                     
C     DO 50 IY=1,NY                                                     
C  50 WRITE (6,350) (VXBDY(IX,IY),IX=1,NX)                              
      WRITE (6,360)                                                     
      WRITE (6,330)                                                     
      DO 60 IY=1,NY                                                     
   60 WRITE (6,350) (VY(IX,IY),IX=1,NX)                                 
C      ACTIVATE NEXT 3 LINES TO PRINT BOUNDARY VELOCITIES               
C     WRITE (6,340)                                                     
C     DO 70 IY=1,NY                                                     
C  70 WRITE (6,350) (VYBDY(IX,IY),IX=1,NX)                              
C     ---WRITE VELOCITIES TO FILE UNIT 7---                             
   80 IF (NPNCHV.EQ.0) GO TO 110                                        
      IF (NPNCHV.EQ.-2.AND.(N.EQ.NTIM.OR.IPRNT.EQ.1)) GO TO 90          
      IF (NPNCHV.EQ.-1.AND.N.EQ.1) GO TO 90                             
      IF (MOD(N,NPNCHV).EQ.0) GO TO 90                                  
      GO TO 110                                                         
   90 IF (ISOLV.EQ.0) THEN                                              
       DO 92 IY=2,NNY                                                   
       DO 92 IX=2,NNX                                                   
       IF(THCK(IX,IY).EQ.0.0) GO TO 92                                  
       VX(IX,IY)=VX(IX,IY)/THCK(IX,IY)                                  
       VY(IX,IY)=VY(IX,IY)/THCK(IX,IY)                                  
C       ACTIVATE NEXT 2 LINES IF BOUNDARY VELOCITIES PRINTED            
C      VXBDY(IX,IY)=2.0*VXBDY(IX,IY)/(THCK(IX,IY)+THCK(IX+1,IY))        
C      VYBDY(IX,IY)=2.0*VYBDY(IX,IY)/(THCK(IX,IY)+THCK(IX,IY+1))        
   92  CONTINUE                                                         
       ISOLV=-1                                                         
      END IF                                                            
      WRITE (7,510) NX,NY,XDEL,YDEL,VMAX,VMAY                           
      DO 100 IY=1,NY                                                    
      WRITE (7,520) (VX(IX,IY),IX=1,NX)                                 
  100 WRITE (7,520) (VY(IX,IY),IX=1,NX)                                 
C      SAVE VELOCITY*THICKNESS*POROSITY                                 
  110 IF (ISOLV.EQ.0) GO TO 240                                         
      DO 112 IY=2,NNY                                                   
      DO 112 IX=2,NNX                                                   
      IF (THCK(IX,IY).EQ.0.0) GO TO 112                                 
      VX(IX,IY)=VX(IX,IY)*THCK(IX,IY)                                   
      VY(IX,IY)=VY(IX,IY)*THCK(IX,IY)                                   
C      ACTIVATE NEXT 2 LINES IF BOUNDARY VELOCITIES PRINTED             
C     VXBDY(IX,IY)=VXBDY(IX,IY)*0.5*(THCK(IX,IY)+THCK(IX+1,IY))         
C     VYBDY(IX,IY)=VYBDY(IX,IY)*0.5*(THCK(IX,IY)+THCK(IX,IY+1))         
  112 CONTINUE                                                          
      IF(ISOLV.NE.1) GO TO 240                                          
C     ****************************************************************  
C     ---COMPUTE NEXT TIME STEP---                                      
      WRITE (6,390)                                                     
      WRITE (6,410) VMXBD,VMYBD                                         
      IF (RF.LE.1.0) GO TO 115                                          
      VMXBD=VMXBD/RF                                                    
      VMYBD=VMYBD/RF                                                    
      WRITE (6,394) VMXBD,VMYBD                                         
  115 TDELXB=CELDIS*XDEL/VMXBD                                          
      TDELYB=CELDIS*YDEL/VMYBD                                          
      ITCD=0                                                            
      IF (TDELYB.LT.TDELXB) ITCD=1                                      
      TIMV=AMIN1(TDELXB,TDELYB)                                         
      IF (AMAX1(VMXBD,VMYBD).LE.1.0E-10) WRITE(6,570)                   
      WRITE (6,310) TMV,TIMV                                            
      IF (TMV.LT.TIMV) GO TO 120                                        
      LIM=-1                                                            
      GO TO 130                                                         
  120 TIMV=TMV                                                          
      LIM=1                                                             
  130 NTIMV=TIM(N)/TIMV                                                 
      NMOV=NTIMV+1                                                      
      WRITE (6,420) TIMV,NTIMV,NMOV                                     
      TIMV=TIM(N)/NMOV                                                  
      WRITE (6,370) TIM(N)                                              
      WRITE (6,380) TIMV                                                
C                                                                       
      IF (BETA.EQ.0.0) GO TO 200                                        
C     ****************************************************************  
C     ---COMPUTE DISPERSION COEFFICIENTS---                             
      ALPHA=BETA                                                        
      ALNG=ALPHA                                                        
      TRAN=DLTRAT*ALPHA                                                 
      XX2=XDEL*XDEL                                                     
      YY2=YDEL*YDEL                                                     
      XY2=4.0*XDEL*YDEL                                                 
      DO 150 IX=2,MMX                                                   
      DO 150 IY=2,MMY                                                   
      IF (THCK(IX,IY).EQ.0.0) GO TO 150                                 
      JX=IX-MX+1                                                        
      JY=IY-MY+1                                                        
      IF (JX.LT.1.OR.JY.LT.1) GO TO 150                                 
      VXE=VXBDY(IX,IY)                                                  
      VYS=VYBDY(IX,IY)                                                  
      IF (THCK(IX+1,IY).EQ.0.0) GO TO 140                               
      IF ((IX+1).GT.MMX) GO TO 140                                      
C        ---FORWARD COEFFICIENTS: X-DIRECTION---                        
      VYE=(VYBDY(IX,IY-1)+VYBDY(IX+1,IY-1)+VYS+VYBDY(IX+1,IY))/4.0      
      VXE2=VXE*VXE                                                      
      VYE2=VYE*VYE                                                      
      VMGE=SQRT(VXE2+VYE2)                                              
      IF (VMGE.LT.1.0E-20) GO TO 140                                    
      DALN=ALNG*VMGE                                                    
      DTRN=TRAN*VMGE                                                    
      VMGE2=VMGE*VMGE                                                   
C           ---XX COEFFICIENT---                                        
      DISP(JX,JY,1)=(DALN*VXE2+DTRN*VYE2)/(VMGE2*XX2)                   
C           ---XY COEFFICIENT---                                        
      IF ((IY-1).LT.MY.OR.(IY+1).GT.MMY) GO TO 140                      
      DISP(JX,JY,3)=(DALN-DTRN)*VXE*VYE/(VMGE2*XY2)                     
C        ---FORWARD COEFFICIENTS: Y-DIRECTION---                        
  140 IF (THCK(IX,IY+1).EQ.0.0) GO TO 150                               
      IF ((IY+1).GT.MMY) GO TO 150                                      
      VXS=(VXBDY(IX-1,IY)+VXE+VXBDY(IX-1,IY+1)+VXBDY(IX,IY+1))/4.0      
      VYS2=VYS*VYS                                                      
      VXS2=VXS*VXS                                                      
      VMGS=SQRT(VXS2+VYS2)                                              
      IF (VMGS.LT.1.0E-20) GO TO 150                                    
      DALN=ALNG*VMGS                                                    
      DTRN=TRAN*VMGS                                                    
      VMGS2=VMGS*VMGS                                                   
C           ---YY COEFFICIENT---                                        
      DISP(JX,JY,2)=(DALN*VYS2+DTRN*VXS2)/(VMGS2*YY2)                   
C           ---YX COEFFICIENT---                                        
      IF ((IX-1).LT.MX.OR.(IX+1).GT.MMX) GO TO 150                      
      DISP(JX,JY,4)=(DALN-DTRN)*VXS*VYS/(VMGS2*XY2)                     
  150 CONTINUE                                                          
C     ****************************************************************  
C     ---ADJUST CROSS-PRODUCT TERMS FOR ZERO THICKNESS---               
      DO 160 IX=2,MMX                                                   
      DO 160 IY=2,MMY                                                   
      JX=IX-MX+1                                                        
      JY=IY-MY+1                                                        
      IF (JX.LT.1.OR.JY.LT.1) GO TO 160                                 
      IF (THCK(IX,IY+1).EQ.0.0.OR.THCK(IX+1,IY+1).EQ.0.0.OR.THCK(IX,IY-1
     1).EQ.0.0.OR.THCK(IX+1,IY-1).EQ.0.0) DISP(JX,JY,3)=0.0             
      IF (THCK(IX+1,IY).EQ.0.0.OR.THCK(IX+1,IY+1).EQ.0.0.OR.THCK(IX-1,IY
     1).EQ.0.0.OR.THCK(IX-1,IY+1).EQ.0.0) DISP(JX,JY,4)=0.0             
  160 CONTINUE                                                          
C     ****************************************************************  
C     ---CHECK FOR STABILITY OF EXPLICIT METHOD---                      
      TIMDIS=0.0                                                        
      DO 170 IX=1,NMX                                                   
      DO 170 IY=1,NMY                                                   
      JX=IX+MX-1                                                        
      JY=IY+MY-1                                                        
      IF (THCK(JX,JY).LE.0.0) GO TO 170                                 
      IF (IX.EQ.1) THEN                                                 
       DISPX=DISP(IX,IY,1)                                              
      ELSE                                                              
       DISPX=AMAX1(DISP(IX,IY,1),DISP(IX-1,IY,1))                       
      END IF                                                            
      IF (IY.EQ.1) THEN                                                 
       DISPY=DISP(IX,IY,2)                                              
      ELSE                                                              
       DISPY=AMAX1(DISP(IX,IY,2),DISP(IX,IY-1,2))                       
      END IF                                                            
      TDCO=(DISPX+DISPY)/THCK(JX,JY)                                    
      IF (TDCO.GT.TIMDIS) TIMDIS=TDCO                                   
  170 CONTINUE                                                          
      TIMDC=0.5*RF/TIMDIS                                               
      WRITE (6,440) TIMDC                                               
      NTIMD=TIM(N)/TIMDC                                                
      NDISP=NTIMD+1                                                     
      IF (NDISP.LE.NMOV) GO TO 180                                      
      NMOV=NDISP                                                        
      TIMV=TIM(N)/NMOV                                                  
      LIM=0                                                             
  180 WRITE (6,430) TIMV,NTIMD,NMOV                                     
C     ****************************************************************  
  200 IF (NMOV.EQ.1) GO TO 235                                          
      IF (LIM) 210,220,230                                              
  210 WRITE (6,530)                                                     
      IF (ITCD.GT.0) THEN                                               
         MJ=MAXVYJ+1                                                    
         WRITE (6,534) MAXVYI,MAXVYJ,MAXVYI,MJ                          
       ELSE                                                             
         MI=MAXVXI+1                                                    
         WRITE (6,535) MAXVXI,MAXVXJ,MI,MAXVXJ                          
      END IF                                                            
      GO TO 240                                                         
  220 WRITE (6,540)                                                     
      GO TO 240                                                         
  230 WRITE (6,550)                                                     
      WRITE (6,560) MAXX,MAXY                                           
      GO TO 240                                                         
  235 WRITE (6,580)                                                     
C     ****************************************************************  
C     ---PRINT DISPERSION EQUATION COEFFICIENTS---                      
  240 IF (NPNTD.EQ.0) GO TO 300                                         
      IF (NPNTD.EQ.2) GO TO 250                                         
      IF (NPNTD.EQ.1.AND.N.EQ.1) GO TO 250                              
      GO TO 300                                                         
  250 WRITE (6,450)                                                     
      WRITE (6,460)                                                     
      DO 260 IY=1,NMY                                                   
  260 WRITE (6,500) (DISP(IX,IY,1),IX=1,NMX)                            
      WRITE (6,470)                                                     
      DO 270 IY=1,NMY                                                   
  270 WRITE (6,500) (DISP(IX,IY,2),IX=1,NMX)                            
      WRITE (6,480)                                                     
      DO 280 IY=1,NMY                                                   
  280 WRITE (6,500) (DISP(IX,IY,3),IX=1,NMX)                            
      WRITE (6,490)                                                     
      DO 290 IY=1,NMY                                                   
  290 WRITE (6,500) (DISP(IX,IY,4),IX=1,NMX)                            
C     ****************************************************************  
  300 RETURN                                                            
C     ****************************************************************  
C                                                                       
C                                                                       
C                                                                       
  310 FORMAT (1H0,19H TMV (MAX. INJ.) = ,G12.5/20H  TIMV (CELDIS)   = ,G
     112.5)                                                             
  320 FORMAT (1H1,12HX VELOCITIES)                                      
  330 FORMAT (1H ,25X,8HAT NODES/)                                      
C      ACTIVATE NEXT LINE IF BOUNDARY VELOCITIES PRINTED                
C 340 FORMAT (1H0,25X,41HON BOUNDARIES (USING INTERFACE THICKNESS)/)    
  350 FORMAT (1H ,1P10E12.3)                                            
  360 FORMAT (1H1,12HY VELOCITIES)                                      
  370 FORMAT (3H   ,11HTIM (N)  = ,1G12.5)                              
  380 FORMAT (3H   ,11HTIMEVELO = ,1G12.5)                              
  390 FORMAT (1H1,10X,29HSTABILITY CRITERIA --- M.O.C.//)               
  394 FORMAT (1H0,5X,46HMAXIMUM EFFECTIVE SOLUTE VELOCITIES:  X-VEL = , 
     1  1PE9.2,5X,8HY-VEL = ,1PE9.2)                                    
  410 FORMAT (1H0,5X,35HMAXIMUM FLUID VELOCITIES:  X-VEL = ,1PE9.2,5X,  
     1  8HY-VEL = ,1PE9.2)                                              
  420 FORMAT (1H0,8H TIMV = ,1PE9.2,5X,8HNTIMV = ,I5,5X,7HNMOV = ,I5/)  
  430 FORMAT (1H0,8H TIMV = ,1PE9.2,5X,8HNTIMD = ,I5,5X,7HNMOV = ,I5)   
  440 FORMAT (3H   ,11HTIMEDISP = ,1E12.5)                              
  450 FORMAT (1H1,32HDISPERSION EQUATION COEFFICIENTS,10X,33H=(D-IJ)*(B)
     1*(POROS)/(GRID FACTOR))                                           
  460 FORMAT (1H0,35X,14HXX COEFFICIENT/)                               
  470 FORMAT (1H0,35X,14HYY COEFFICIENT/)                               
  480 FORMAT (1H0,35X,14HXY COEFFICIENT/)                               
  490 FORMAT (1H0,35X,14HYX COEFFICIENT/)                               
  500 FORMAT (1H ,1P10E11.2)                                            
  510 FORMAT (2I4,2F10.1,2F10.7)                                        
  520 FORMAT (8F10.7)                                                   
  530 FORMAT (1H0,10X,42HTHE LIMITING STABILITY CRITERION IS CELDIS)    
  534 FORMAT (1H ,4X,52HMAX. Y-VEL. IS CONSTRAINT AND OCCURS BETWEEN NOD
     1ES (,I2,1H,,I2,7H) AND (,I2,1H,,I2,1H))                           
  535 FORMAT (1H ,4X,52HMAX. X-VEL. IS CONSTRAINT AND OCCURS BETWEEN NOD
     1ES (,I2,1H,,I2,7H) AND (,I2,1H,,I2,1H))                           
  540 FORMAT (1H0,10X,40HTHE LIMITING STABILITY CRITERION IS BETA)      
  550 FORMAT (1H0,10X,58HTHE LIMITING STABILITY CRITERION IS MAXIMUM INJ
     1ECTION RATE)                                                      
  560 FORMAT (1H ,15X,35HMAX. INJECTION OCCURS AT CELL IX = ,I3,7H  IY =
     1 ,I3)                                                             
  570 FORMAT (1H0,5X,47H*** WARNING ***  DECREASE CRITERIA IN E 230-260)
  580 FORMAT (1H0,10X,63H*TIME INCREMENT FOR SOLUTE TRANSPORT EQUALS TIM
     1E STEP FOR FLOW*)                                                 
      END