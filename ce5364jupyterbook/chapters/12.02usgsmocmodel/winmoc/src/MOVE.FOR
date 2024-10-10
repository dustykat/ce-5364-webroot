      SUBROUTINE MOVE                                                   
      DOUBLE PRECISION TMRX,VPRM,HI,HR,HC,HK,WT,REC,RECH,TIM,AOPT,TITLE 
      DOUBLE PRECISION XDEL,YDEL,S,AREA,SUMT,RHO,PARAM,TEST,TOL,PINT,   
     1                 HMIN,PYR,ANFCTR                                  
      DOUBLE PRECISION DXINV,DYINV,ARINV,PORINV                         
      DOUBLE PRECISION DCYFCT,DCYT,DCYT2                                
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
      COMMON /XINV/ DXINV,DYINV,ARINV,PORINV                            
      COMMON /CHMA/ PART(3,06400),CONC(020,020),TMCN(05,50),VX(040,040),
     1              VY(040,040),CONINT(020,020),CNRECH(020,020),POROS,  
     2              SUMTCH,BETA,TIMV,STORM,STORMI,CMSIN,CMSOUT,FLMIN,   
     3              FLMOT,SUMIO,CELDIS,DLTRAT,CSTORM                    
      COMMON /CHMC/ SUMC(020,020),VXBDY(040,040),VYBDY(040,040)         
      COMMON /CHMR/ RF,DK,RHOB,THALF,DECAY,ADSORB,SORBI,DMASS1,CSTM2    
      COMMON /CHMP/ PTID(06400)                                         
C     ***************************************************************   
      WRITE (6,680) NMOV                                                
      IF (THALF.GT.0.0.AND.THALF.LT.TIMV) WRITE (6,685)                 
      SUMTCH=SUMT-TIM(N)                                                
      IONED=0                                                           
      IF(NX.EQ.3.OR.NY.EQ.3) IONED=1                                    
      F1=0.30                                                           
      F2=1.0/3.0                                                        
      IF (NPTPND.EQ.4) F1=0.25                                          
      IF (NPTPND.EQ.5.AND.IONED.EQ.1) F1=0.25                           
      IF (NPTPND.EQ.9) F1=F2                                            
      IF (NPTPND.EQ.8.AND.IONED.NE.1) F2=0.25                           
      IF (NPTPND.EQ.8.AND.IONED.EQ.1) F1=F2                             
      IF (NPTPND.EQ.16) F1=0.25                                         
      IF (NPTPND.EQ.16) F2=0.125                                        
      CONST1=TIMV*DXINV/RF                                              
      CONST2=TIMV*DYINV/RF                                              
      DCYFCT=TIMV*DECAY                                                 
      DCYT=1.D0                                                         
      DCYT2=1.D0                                                        
      IF(DECAY.NE.0.0) THEN                                             
       DCYT=DEXP(-DCYFCT)                                               
       DCYT2=DEXP(-DCYFCT*0.5D0)                                        
      END IF                                                            
C     ---MOVE PARTICLES 'NMOV' TIMES---                                 
      DO 650 IMOV=1,NMOV                                                
   10 NPTM=NP                                                           
C        ---MOVE EACH PARTICLE---                                       
      DO 590 IN=1,NP                                                    
      IF (PART(1,IN).EQ.0.0) GO TO 590                                  
      KFLAG=0                                                           
      NLOC=0                                                            
C     ***************************************************************   
C           ---COMPUTE OLD LOCATION---                                  
   20 XOLD=PART(1,IN)                                                   
      IX=XOLD+0.5                                                       
      JX=IX-MX+1                                                        
      IFLAG=1                                                           
      IF (PART(2,IN).GE.0.0) GO TO 30                                   
      IFLAG=-1                                                          
      PART(2,IN)=-PART(2,IN)                                            
   30 YOLD=PART(2,IN)                                                   
      IY=YOLD+0.5                                                       
      JY=IY-MY+1                                                        
      IF (THCK(IX,IY).EQ.0.0) GO TO 590                                 
C     ***************************************************************   
C           ---COMPUTE NEW LOCATION AND LOCATE CLOSEST NODE---          
C           ---LOCATE NORTHWEST CORNER---                               
      IVX=XOLD                                                          
      IVY=YOLD                                                          
      IXE=IVX+1                                                         
      IYS=IVY+1                                                         
C     ***************************************************************   
C        ---LOCATE QUADRANT, VEL. AT 4 CORNERS, CHECK FOR BOUNDARIES--- 
      CELDX=XOLD-IX                                                     
      CELDY=YOLD-IY                                                     
      ICD=9                                                             
      IF (CELDX.EQ.0.0.AND.CELDY.EQ.0.0) GO TO 280                      
      IF (CELDX.GE.0.0.OR.CELDY.GE.0.0) GO TO 70                        
C              ---PT. IN NW QUADRANT---                                 
      VXNW=VXBDY(IVX,IVY)                                               
      VXNE=VX(IXE,IVY)                                                  
      VXSW=VXBDY(IVX,IYS)                                               
      VXSE=VX(IXE,IYS)                                                  
      VYNW=VYBDY(IVX,IVY)                                               
      VYNE=VYBDY(IXE,IVY)                                               
      VYSW=VY(IVX,IYS)                                                  
      VYSE=VY(IXE,IYS)                                                  
      ICD=1                                                             
      IF (THCK(IVX,IVY).EQ.0.0) GO TO 50                                
      IF (REC(IXE,IVY).EQ.0.0.AND.VPRM(IXE,IVY).LT.0.09) GO TO 40       
      IF (THCK(IXE+1,IVY).NE.0.0) VXNE=VXNW                             
   40 IF (REC(IVX,IYS).EQ.0.0.AND.VPRM(IVX,IYS).LT.0.09) GO TO 50       
      IF (THCK(IVX,IYS+1).NE.0.0) VYSW=VYNW                             
   50 IF (REC(IXE,IYS).EQ.0.0.AND.VPRM(IXE,IYS).LT.0.09) GO TO 270      
      IF (THCK(IVX,IYS).EQ.0.0) GO TO 60                                
      IF (THCK(IXE+1,IYS).GT.0.0) VXSE=VXSW                             
   60 IF (THCK(IXE,IVY).EQ.0.0) GO TO 270                               
      IF (THCK(IXE,IYS+1).GT.0.0) VYSE=VYNE                             
      GO TO 270                                                         
C                                                                       
   70 IF (CELDX.LE.0.0.OR.CELDY.GE.0.0) GO TO 130                       
C              ---PT. IN NE QUADRANT---                                 
   80 VXNW=VX(IVX,IVY)                                                  
      VXNE=VXBDY(IVX,IVY)                                               
      VXSW=VX(IVX,IYS)                                                  
      VXSE=VXBDY(IVX,IYS)                                               
      VYNW=VYBDY(IVX,IVY)                                               
      VYNE=VYBDY(IXE,IVY)                                               
      VYSW=VY(IVX,IYS)                                                  
      VYSE=VY(IXE,IYS)                                                  
      ICD=2                                                             
      IF (CELDX.EQ.0.0) GO TO 120                                       
      IF (THCK(IXE,IVY).EQ.0.0) GO TO 100                               
      IF (REC(IVX,IVY).EQ.0.0.AND.VPRM(IVX,IVY).LT.0.09) GO TO 90       
      IF (THCK(IVX-1,IVY).NE.0.0) VXNW=VXNE                             
   90 IF (REC(IXE,IYS).EQ.0.0.AND.VPRM(IXE,IYS).LT.0.09) GO TO 100      
      IF (THCK(IXE,IYS+1).NE.0.0) VYSE=VYNE                             
  100 IF (REC(IVX,IYS).EQ.0.0.AND.VPRM(IVX,IYS).LT.0.09) GO TO 270      
      IF (THCK(IXE,IYS).EQ.0.0) GO TO 110                               
      IF (THCK(IVX-1,IYS).GT.0.0) VXSW=VXSE                             
  110 IF (THCK(IVX,IVY).EQ.0.0) GO TO 270                               
      IF (THCK(IVX,IYS+1).GT.0.0) VYSW=VYNW                             
      GO TO 270                                                         
  120 IF (REC(IVX,IYS).EQ.0.0.AND.VPRM(IVX,IYS).LE.0.09) GO TO 270      
      IF (THCK(IVX,IVY).EQ.0.0) GO TO 270                               
      IF (THCK(IVX,IYS+1).GT.0.0) VYSW=VYNW                             
      GO TO 270                                                         
C                                                                       
  130 IF (CELDY.LE.0.0.OR.CELDX.GE.0.0) GO TO 190                       
C              ---PT. IN SW QUADRANT---                                 
  140 VXNW=VXBDY(IVX,IVY)                                               
      VXNE=VX(IXE,IVY)                                                  
      VXSW=VXBDY(IVX,IYS)                                               
      VXSE=VX(IXE,IYS)                                                  
      VYNW=VY(IVX,IVY)                                                  
      VYNE=VY(IXE,IVY)                                                  
      VYSW=VYBDY(IVX,IVY)                                               
      VYSE=VYBDY(IXE,IVY)                                               
      ICD=3                                                             
      IF (CELDY.EQ.0.0) GO TO 180                                       
      IF (THCK(IVX,IYS).EQ.0.0) GO TO 160                               
      IF (REC(IVX,IVY).EQ.0.0.AND.VPRM(IVX,IVY).LT.0.09) GO TO 150      
      IF (THCK(IVX,IVY-1).NE.0.0) VYNW=VYSW                             
  150 IF (REC(IXE,IYS).EQ.0.0.AND.VPRM(IXE,IYS).LT.0.09) GO TO 160      
      IF (THCK(IXE+1,IYS).NE.0.0) VXSE=VXSW                             
  160 IF (REC(IXE,IVY).EQ.0.0.AND.VPRM(IXE,IVY).LT.0.09) GO TO 270      
      IF (THCK(IVX,IVY).EQ.0.0) GO TO 170                               
      IF (THCK(IXE+1,IVY).GT.0.0) VXNE=VXNW                             
  170 IF (THCK(IXE,IYS).EQ.0.0) GO TO 270                               
      IF (THCK(IXE,IVY-1).GT.0.0) VYNE=VYSE                             
      GO TO 270                                                         
  180 IF (REC(IXE,IVY).EQ.0.0.AND.VPRM(IXE,IVY).LE.0.09) GO TO 270      
      IF (THCK(IVX,IVY).EQ.0.0) GO TO 270                               
      IF (THCK(IXE+1,IVY).GT.0.0) VXNE=VXNW                             
      GO TO 270                                                         
C                                                                       
  190 IF (CELDY.LE.0.0.OR.CELDX.LE.0.0) GO TO 260                       
C              ---PT. IN SE QUADRANT---                                 
  200 VXNW=VX(IVX,IVY)                                                  
      VXNE=VXBDY(IVX,IVY)                                               
      VXSW=VX(IVX,IYS)                                                  
      VXSE=VXBDY(IVX,IYS)                                               
      VYNW=VY(IVX,IVY)                                                  
      VYNE=VY(IXE,IVY)                                                  
      VYSW=VYBDY(IVX,IVY)                                               
      VYSE=VYBDY(IXE,IVY)                                               
      ICD=4                                                             
      IF (CELDY.EQ.0.0) GO TO 240                                       
      IF (CELDX.EQ.0.0) GO TO 250                                       
      IF (THCK(IXE,IYS).EQ.0.0) GO TO 220                               
      IF (REC(IXE,IVY).EQ.0.0.AND.VPRM(IXE,IVY).LT.0.09) GO TO 210      
      IF (THCK(IXE,IVY-1).NE.0.0) VYNE=VYSE                             
  210 IF (REC(IVX,IYS).EQ.0.0.AND.VPRM(IVX,IYS).LT.0.09) GO TO 220      
      IF (THCK(IVX-1,IYS).NE.0.0) VXSW=VXSE                             
  220 IF (REC(IVX,IVY).EQ.0.0.AND.VPRM(IVX,IVY).LT.0.09) GO TO 270      
      IF (THCK(IXE,IVY).EQ.0.0) GO TO 230                               
      IF (THCK(IVX-1,IVY).GT.0.0) VXNW=VXNE                             
  230 IF (THCK(IVX,IYS).EQ.0.0) GO TO 270                               
      IF (THCK(IVX,IVY-1).GT.0.0) VYNW=VYSW                             
      GO TO 270                                                         
  240 IF (REC(IVX,IVY).EQ.0.0.AND.VPRM(IVX,IVY).LE.0.09) GO TO 270      
      IF (THCK(IXE,IVY).EQ.0.0) GO TO 270                               
      IF (THCK(IVX-1,IVY).GT.0.0) VXNW=VXNE                             
      GO TO 270                                                         
  250 IF (REC(IVX,IVY).EQ.0.0.AND.VPRM(IVX,IVY).LE.0.09) GO TO 270      
      IF (THCK(IVX,IYS).EQ.0.0) GO TO 270                               
      IF (THCK(IVX,IVY-1).GT.0.0) VYNW=VYSW                             
      GO TO 270                                                         
C                                                                       
  260 IF (CELDX.EQ.0.0.AND.CELDY.LT.0.0) GO TO 80                       
      IF (CELDX.LT.0.0.AND.CELDY.EQ.0.0) GO TO 140                      
      IF (CELDX.GT.0.0.AND.CELDY.EQ.0.0) GO TO 200                      
      IF (CELDX.EQ.0.0.AND.CELDY.GT.0.0) GO TO 200                      
      WRITE (6,690) IN,IX,IY                                            
  270 CONTINUE                                                          
C              --- CHECK FOR ADJACENT NO-FLOW BOUNDARIES---             
      GO TO (1270,1275,1280,1285,1290) ICD                              
      GO TO 1290                                                        
 1270 IF (THCK(IXE,IVY).EQ.0.0) GO TO 1272                              
      IF (THCK(IVX,IYS).EQ.0.0) GO TO 1273                              
      IF (THCK(IVX,IVY).EQ.0.0) GO TO 1274                              
      GO TO 1290                                                        
 1272 VXNE=VXSE                                                         
      IF (THCK(IVX,IYS).GT.0.0) GO TO 1274                              
 1273 VYSW=VYSE                                                         
 1274 VXNW=VXSW                                                         
      VYNW=VYNE                                                         
      GO TO 1290                                                        
 1275 IF (THCK(IVX,IVY).EQ.0.0) GO TO 1277                              
      IF (THCK(IXE,IYS).EQ.0.0) GO TO 1278                              
      IF (THCK(IXE,IVY).EQ.0.0) GO TO 1279                              
      GO TO 1290                                                        
 1277 VXNW=VXSW                                                         
      IF (THCK(IXE,IYS).GT.0.0) GO TO 1279                              
 1278 VYSE=VYSW                                                         
 1279 VXNE=VXSE                                                         
      VYNE=VYNW                                                         
      GO TO 1290                                                        
 1280 IF (THCK(IXE,IYS).EQ.0.0) GO TO 1282                              
      IF (THCK(IVX,IVY).EQ.0.0) GO TO 1283                              
      IF (THCK(IVX,IYS).EQ.0.0) GO TO 1284                              
      GO TO 1290                                                        
 1282 VXSE=VXNE                                                         
      IF (THCK(IVX,IVY).GT.0.0) GO TO 1284                              
 1283 VYNW=VYNE                                                         
 1284 VXSW=VXNW                                                         
      VYSW=VYSE                                                         
      GO TO 1290                                                        
 1285 IF (THCK(IVX,IYS).EQ.0.0) GO TO 1287                              
      IF (THCK(IXE,IVY).EQ.0.0) GO TO 1288                              
      IF (THCK(IXE,IYS).EQ.0.0) GO TO 1289                              
      GO TO 1290                                                        
 1287 VXSW=VXNW                                                         
      IF (THCK(IXE,IVY).GT.0.0) GO TO 1289                              
 1288 VYNE=VYNW                                                         
 1289 VYSE=VYSW                                                         
      VXSE=VXNE                                                         
 1290 CONTINUE                                                          
C     ****************************************************************  
C        ---BILINEAR INTERPOLATION---                                   
      CELXD=XOLD-IVX                                                    
      CELDXH=AMOD(CELXD,0.5)                                            
      CELDX=CELDXH*2.0                                                  
      CELDY=YOLD-IVY                                                    
C     ****************************************************************  
C           ---X VELOCITY---                                            
      VXN=VXNW*(1.0-CELDX)+VXNE*CELDX                                   
      VXS=VXSW*(1.0-CELDX)+VXSE*CELDX                                   
      XVEL=(VXN*(1.0-CELDY)+VXS*CELDY)/THCK(IX,IY)                      
C           ---Y VELOCITY---                                            
      CELDYH=AMOD(CELDY,0.5)                                            
      CELYD=CELDYH*2.0                                                  
      VYW=VYNW*(1.0-CELYD)+VYSW*CELYD                                   
      VYE=VYNE*(1.0-CELYD)+VYSE*CELYD                                   
      YVEL=(VYW*(1.0-CELXD)+VYE*CELXD)/THCK(IX,IY)                      
C                                                                       
      GO TO 290                                                         
  280 XVEL=VX(IX,IY)/THCK(IX,IY)                                        
      YVEL=VY(IX,IY)/THCK(IX,IY)                                        
  290 DISTX=XVEL*CONST1                                                 
      DISTY=YVEL*CONST2                                                 
C     ****************************************************************  
C        ---BOUNDARY CONDITIONS---                                      
      TEMPX=XOLD+DISTX                                                  
      TEMPY=YOLD+DISTY                                                  
      INX=TEMPX+0.5                                                     
      INY=TEMPY+0.5                                                     
      IF (THCK(INX,INY).GT.0.0) GO TO 330                               
C     ****************************************************************  
C           ---X BOUNDARY---                                            
      IF (THCK(INX,IY).EQ.0.0) GO TO 300                                
      PART(1,IN)=TEMPX                                                  
      GO TO 310                                                         
  300 BEYON=TEMPX-IX                                                    
      IF (BEYON.LT.0.0) BEYON=BEYON+0.5                                 
      IF (BEYON.GT.0.0) BEYON=BEYON-0.5                                 
      PART(1,IN)=TEMPX-2.0*BEYON                                        
      INX=PART(1,IN)+0.5                                                
      TEMPX=PART(1,IN)                                                  
C     ****************************************************************  
C           ---Y BOUNDARY---                                            
  310 IF (THCK(INX,INY).EQ.0.0) GO TO 320                               
      PART(2,IN)=TEMPY                                                  
      GO TO 340                                                         
C     ****************************************************************  
  320 BEYON=TEMPY-IY                                                    
      IF (BEYON.LT.0.0) BEYON=BEYON+0.5                                 
      IF (BEYON.GT.0.0) BEYON=BEYON-0.5                                 
      PART(2,IN)=TEMPY-2.0*BEYON                                        
      INY=PART(2,IN)+0.5                                                
      TEMPY=PART(2,IN)                                                  
      GO TO 340                                                         
  330 PART(1,IN)=TEMPX                                                  
      PART(2,IN)=TEMPY                                                  
  340 CONTINUE                                                          
      JNX=INX-MX+1                                                      
      JNY=INY-MY+1                                                      
      IF (MCHK.EQ.0) GO TO 342                                          
      IF (JNX.LT.1.OR.JNX.GT.NMX.OR.JNY.LT.1.OR.JNY.GT.NMY) NLOC=1      
C     ***************************************************************   
      IF (NLOC.GT.0) GO TO 345                                          
  342 CONTINUE                                                          
C        ---SUM CONCENTRATIONS AND COUNT PARTICLES---                   
C           ---DECAY PARTICLES---                                       
      PART(3,IN)=PART(3,IN)*DCYT                                        
      SUMC(JNX,JNY)=SUMC(JNX,JNY)+PART(3,IN)                            
      NPCELL(JNX,JNY)=NPCELL(JNX,JNY)+1                                 
C     ****************************************************************  
  345 CONTINUE                                                          
C        ---CHECK FOR CHANGE IN CELL LOCATION---                        
      IF (IX.EQ.INX.AND.IY.EQ.INY) GO TO 580                            
C           ---CHECK FOR CONST.-HEAD BDY. OR SOURCE AT OLD LOCATION---  
      IBD=0                                                             
C     IF (REC(IX,IY).LT.-0.1) GO TO 350                                 
C     IF (REC(IX,IY).GT.0.1) GO TO 360                                  
      IF (REC(IX,IY).LT.0.0) GO TO 350                                  
      IF (REC(IX,IY).GT.0.0) GO TO 360                                  
      IF (VPRM(IX,IY).LT.0.09) GO TO 348                                
      IF (WT(IX,IY).GT.HK(IX,IY)) GO TO 350                             
      IF (WT(IX,IY).LT.HK(IX,IY)) GO TO 360                             
  348 IF (MCHK.EQ.0) GO TO 540                                          
      IF (JX.EQ.1.AND.VXBDY(IX-1,IY).GT.0.0.AND.JNX.GT.JX) IBD=1        
      IF (JX.EQ.NMX.AND.VXBDY(IX,IY).LT.0.0.AND.JNX.LT.JX) IBD=1        
      IF (JY.EQ.1.AND.VYBDY(IX,IY-1).GT.0.0.AND.JNY.GT.JY) IBD=1        
      IF (JY.EQ.NMY.AND.VYBDY(IX,IY).LT.0.0.AND.JNY.LT.JY) IBD=1        
      IF (IBD.EQ.1) GO TO 350                                           
      GO TO 540                                                         
C     ****************************************************************  
C           ---CREATE NEW PARTICLES AT BOUNDARIES---                    
  350 IF (IFLAG.GT.0) GO TO 550                                         
      KFLAG=1                                                           
  360 CONTINUE                                                          
C     ****************************************************************  
C           ---GENERATE NEW TEMPORARY PARTICLE---                       
      IF (NPTM.EQ.NPMAX) GO TO 600                                      
      NPTM=NPTM+1                                                       
      IP=NPTM                                                           
C                                                                       
  390 IF (KFLAG.EQ.0) GO TO 398                                         
      IF (IBD.EQ.1) GO TO 525                                           
      ITEM=PTID(IN)                                                     
      GO TO 399                                                         
  398 SUMC(JX,JY)=SUMC(JX,JY)+CONC(JX,JY)*DCYT2                         
      NPCELL(JX,JY)=NPCELL(JX,JY)+1                                     
      IF (NPOLD(JX,JY).GT.0) NPOLD(JX,JY)=NPOLD(JX,JY)-1                
      IF (IFLAG.GT.0) GO TO 441                                         
      IF (KFLAG.EQ.0) GO TO 441                                         
  399 IF (NPTPND.EQ.16) GO TO 400                                       
      GO TO (401,411,421,431,441,451,461,471,481),ITEM                  
      GO TO 441                                                         
  400 GO TO (482,483,484,485,486,487,488,489,490,491,492,493,494,495,   
     1       496,497),ITEM                                              
      GO TO 441                                                         
  401 PART(1,IP)=IX-F1                                                  
      PART(2,IP)=IY-F1                                                  
      PTID(IP)=1                                                        
      GO TO 530                                                         
  411 PART(1,IP)=IX-F1                                                  
      PART(2,IP)=IY+F1                                                  
      PTID(IP)=2                                                        
      GO TO 530                                                         
  421 PART(1,IP)=IX+F1                                                  
      PART(2,IP)=IY-F1                                                  
      PTID(IP)=3                                                        
      GO TO 530                                                         
  431 PART(1,IP)=IX+F1                                                  
      PART(2,IP)=IY+F1                                                  
      PTID(IP)=4                                                        
      GO TO 530                                                         
  441 PART(1,IP)=IX                                                     
      PART(2,IP)=IY                                                     
      PTID(IP)=5                                                        
      GO TO 530                                                         
  451 PART(1,IP)=IX-F2                                                  
      PART(2,IP)=IY                                                     
      PTID(IP)=6                                                        
      GO TO 530                                                         
  461 PART(1,IP)=IX                                                     
      PART(2,IP)=IY-F2                                                  
      PTID(IP)=7                                                        
      GO TO 530                                                         
  471 PART(1,IP)=IX+F2                                                  
      PART(2,IP)=IY                                                     
      PTID(IP)=8                                                        
      GO TO 530                                                         
  481 PART(1,IP)=IX                                                     
      PART(2,IP)=IY+F2                                                  
      PTID(IP)=9                                                        
      GO TO 530                                                         
  482 PART(1,IP)=IX-F1-F2                                               
      PART(2,IP)=IY-F1-F2                                               
      PTID(IP)=1                                                        
      GO TO 530                                                         
  483 PART(1,IP)=IX-F1-F2                                               
      PART(2,IP)=IY-F1+F2                                               
      PTID(IP)=2                                                        
      GO TO 530                                                         
  484 PART(1,IP)=IX-F1+F2                                               
      PART(2,IP)=IY-F1-F2                                               
      PTID(IP)=3                                                        
      GO TO 530                                                         
  485 PART(1,IP)=IX-F1+F2                                               
      PART(2,IP)=IY-F1+F2                                               
      PTID(IP)=4                                                        
      GO TO 530                                                         
  486 PART(1,IP)=IX-F1-F2                                               
      PART(2,IP)=IY+F1-F2                                               
      PTID(IP)=5                                                        
      GO TO 530                                                         
  487 PART(1,IP)=IX-F1-F2                                               
      PART(2,IP)=IY+F1+F2                                               
      PTID(IP)=6                                                        
      GO TO 530                                                         
  488 PART(1,IP)=IX-F1+F2                                               
      PART(2,IP)=IY+F1-F2                                               
      PTID(IP)=7                                                        
      GO TO 530                                                         
  489 PART(1,IP)=IX-F1+F2                                               
      PART(2,IP)=IY+F1+F2                                               
      PTID(IP)=8                                                        
      GO TO 530                                                         
  490 PART(1,IP)=IX+F1-F2                                               
      PART(2,IP)=IY-F1-F2                                               
      PTID(IP)=9                                                        
      GO TO 530                                                         
  491 PART(1,IP)=IX+F1-F2                                               
      PART(2,IP)=IY-F1+F2                                               
      PTID(IP)=10                                                       
      GO TO 530                                                         
  492 PART(1,IP)=IX+F1+F2                                               
      PART(2,IP)=IY-F1-F2                                               
      PTID(IP)=11                                                       
      GO TO 530                                                         
  493 PART(1,IP)=IX+F1+F2                                               
      PART(2,IP)=IY-F1+F2                                               
      PTID(IP)=12                                                       
      GO TO 530                                                         
  494 PART(1,IP)=IX+F1-F2                                               
      PART(2,IP)=IY+F1-F2                                               
      PTID(IP)=13                                                       
      GO TO 530                                                         
  495 PART(1,IP)=IX+F1-F2                                               
      PART(2,IP)=IY+F1+F2                                               
      PTID(IP)=14                                                       
      GO TO 530                                                         
  496 PART(1,IP)=IX+F1+F2                                               
      PART(2,IP)=IY+F1-F2                                               
      PTID(IP)=15                                                       
      GO TO 530                                                         
  497 PART(1,IP)=IX+F1+F2                                               
      PART(2,IP)=IY+F1+F2                                               
      PTID(IP)=16                                                       
      GO TO 530                                                         
  525 DLX=INX-IX                                                        
      PART(1,IP)=TEMPX-DLX                                              
      DLY=INY-IY                                                        
      PART(2,IP)=TEMPY-DLY                                              
      PART(2,IP)=-PART(2,IP)                                            
      PART(3,IP)=CONC(JX,JY)*DCYT                                       
      SUMC(JX,JY)=SUMC(JX,JY)+PART(3,IP)                                
      NPCELL(JX,JY)=NPCELL(JX,JY)+1                                     
      GO TO 540                                                         
C                                                                       
  530 PART(2,IP)=-PART(2,IP)                                            
      PART(3,IP)=CONC(JX,JY)                                            
C     ****************************************************************  
C           ---CHECK FOR DISCHARGE BOUNDARY AT NEW LOCATION---          
  540 IFLAG=1                                                           
  550 IF (NLOC.GT.0) GO TO 565                                          
      IF (VPRM(INX,INY).GT.0.09.AND.WT(INX,INY).LT.HK(INX,INY)) GO TO 56
     10                                                                 
C     IF (REC(INX,INY).GT.0.1) GO TO 560                                
      IF (REC(INX,INY).GT.0.0) GO TO 560                                
      GO TO 590                                                         
C     ****************************************************************  
C           ---PUT PT. IN LIMBO IF PT. DENSITY NOT INCREASED---         
  560 IF (NPOLD(JNX,JNY).LE.0) GO TO 590                                
  565 CONTINUE                                                          
      PART(1,IN)=0.0                                                    
      PART(2,IN)=0.0                                                    
      PART(3,IN)=0.0                                                    
      IF (NLOC.GT.0) GO TO 567                                          
      SUMC(JNX,JNY)=SUMC(JNX,JNY)-CONC(JNX,JNY)                         
      NPCELL(JNX,JNY)=NPCELL(JNX,JNY)-1                                 
      NPOLD(JNX,JNY)=NPOLD(JNX,JNY)-1                                   
  567 CONTINUE                                                          
      DO 570 ID=1,500                                                   
      IF (LIMBO(ID).GT.0) GO TO 570                                     
      LIMBO(ID)=IN                                                      
      GO TO 590                                                         
  570 CONTINUE                                                          
C                                                                       
  580 IF (IFLAG.LT.0) PART(2,IN)=-TEMPY                                 
  590 CONTINUE                                                          
C     ---END OF LOOP---                                                 
C     ****************************************************************  
C                                                                       
C        ---INSERT TEMPORARY PARTICLES INTO LIMBO LOCATIONS---          
      IF(NPTM.EQ.NP) GO TO 620                                          
      IN=NPTM                                                           
      DO 595 IL=1,500                                                   
      IP=LIMBO(IL)                                                      
      IF(IP.EQ.0) GO TO 595                                             
      PART(1,IP)=PART(1,IN)                                             
      PART(1,IN)=0.0                                                    
      PART(2,IP)=PART(2,IN)                                             
      PART(2,IN)=0.0                                                    
      PART(3,IP)=PART(3,IN)                                             
      PART(3,IN)=0.0                                                    
      PTID(IP)=PTID(IN)                                                 
      PTID(IN)=0                                                        
      LIMBO(IL)=0                                                       
      IN=IN-1                                                           
      IF(IN.LE.NP) GO TO 596                                            
  595 CONTINUE                                                          
  596 NPTM=IN                                                           
      GO TO 620                                                         
C        ---RESTART MOVE IF PT. LIMIT EXCEEDED---                       
  600 WRITE (6,700) IMOV,IN                                             
      TEST=100.D0                                                       
      CALL GENPT                                                        
      DO 610 IX=1,NMX                                                   
      DO 610 IY=1,NMY                                                   
      SUMC(IX,IY)=0.0                                                   
  610 NPCELL(IX,IY)=0                                                   
      TEST=0.D0                                                         
      GO TO 10                                                          
C     ****************************************************************  
  620 SUMTCH=SUMTCH+TIMV                                                
C        ---ADJUST NUMBER OF PARTICLES---                               
      NP=NPTM                                                           
      WRITE (6,670) NP,IMOV                                             
C     ****************************************************************  
      CALL CNCON                                                        
C     ****************************************************************  
C        ---STORE OBS. WELL DATA---                                     
      IF (NUMOBS.LE.0) GO TO 650                                        
      IF (S.GT.0.0) THEN                                                
       IF (IMOV.NE.NMOV) GO TO 650                                      
       J=MOD(N,50)                                                      
      ELSE                                                              
      J=MOD(IMOV,50)                                                    
      END IF                                                            
      IF (J.EQ.0) J=50                                                  
      TMOBS(J)=SUMTCH                                                   
      DO 630 I=1,NUMOBS                                                 
      TMWL(I,J)=HK(IXOBS(I),IYOBS(I))                                   
      IX=IXOBS(I)-MX+1                                                  
      IF (IXOBS(I).LT.MX.OR.IXOBS(I).GT.MMX) GO TO 630                  
      IY=IYOBS(I)-MY+1                                                  
      IF (IYOBS(I).LT.MY.OR.IYOBS(I).GT.MMY) GO TO 630                  
      TMCN(I,J)=CONC(IX,IY)                                             
  630 CONTINUE                                                          
C        ---PRINT CHEMICAL OUTPUT---                                    
  650 CALL CHMOT                                                        
C     ****************************************************************  
  660 RETURN                                                            
C     ****************************************************************  
C                                                                       
C                                                                       
C                                                                       
  670 FORMAT (1H0,2X,2HNP,7X,2H= ,8X,I4,10X,11HIMOV     = ,8X,I4)       
  680 FORMAT (1H0,10X,61HNO. OF PARTICLE MOVES REQUIRED TO COMPLETE THIS
     1 TIME STEP  = ,I4//)                                              
  685 FORMAT (1H0,5X,51H*** CAUTION ***  DECAY HALF-LIFE IS LESS THAN TI
     1MV;/23X,24HACCURACY MAY BE AFFECTED/23X,34H(REDUCE TIMV BY DECREAS
     2ING CELDIS))                                                      
  690 FORMAT (1H0,5X,53H*** WARNING ***     QUADRANT NOT LOCATED FOR PT.
     1 NO. ,I5,11H , IN CELL ,2I4)                                      
  700 FORMAT (1H0,5X,17H ***   NOTE   ***,10X,23HNPTM.EQ.NPMAX --- IMOV=
     1,I4,5X,8HPT. NO.=,I4,5X,10HCALL GENPT/)                           
      END   