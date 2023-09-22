      SUBROUTINE ITERAT                                                 
C      DOUBLE PRECISION DMIN1,DEXP,DLOG,DABS                             
      DOUBLE PRECISION TMRX,VPRM,HI,HR,HC,HK,WT,REC,RECH,TIM,AOPT,TITLE 
      DOUBLE PRECISION XDEL,YDEL,S,AREA,SUMT,RHO,PARAM,TEST,TOL,PINT,   
     1                 HMIN,PYR,ANFCTR                                  
      DOUBLE PRECISION DXINV,DYINV,ARINV,PORINV                         
      DOUBLE PRECISION B,G,W,A,C,E,F,DR,DC,TBAR,TMK,COEF,BLH,BRK,CHK,QL,
     1                 BRH                                              
      DOUBLE PRECISION TOTLQ,TOTLQI,TPIN,TPOUT,PQIN,PQOUT,DELQ          
      COMMON /PRMJ/ NTIM,NPMP,NPNT,NITP,N,NX,NY,NP,NREC,INT,NNX,NNY,    
     1              NUMOBS,NMOV,IMOV,NPMAX,ITMAX,NZCRIT,IPRNT,NPTPND,   
     2              NPNTMV,NPNTVL,NPNTD,NPNCHV,NPDELC,ICHK              
      COMMON /HEDA/ THCK(040,040),TMWL(05,50),TMOBS(50)                 
      COMMON /HEDB/ TMRX(040,040,2),VPRM(040,040),HI(040,040),          
     1              HR(040,040),HC(040,040),HK(040,040),WT(040,040),    
     2 REC(040,040),RECH(040,040),TIM(100),AOPT(20),TITLE(10),XDEL,YDEL,
     3              S,AREA,SUMT,RHO,PARAM,TEST,TOL,PINT,HMIN,PYR,ANFCTR 
      COMMON /BALM/ TOTLQ,TOTLQI,TPIN,TPOUT                             
      COMMON /XINV/ DXINV,DYINV,ARINV,PORINV                            
      DIMENSION W(040), B(040), G(040)                                  
C     ***************************************************************   
      KOUNT=0                                                           
      PQIN=0.D0                                                         
      PQOUT=0.D0                                                        
C      DO NOT REPEAT SOLUTION FOR STEADY-STATE                          
      IREPET=0                                                          
      IF (S.EQ.0.0.AND.(N.GT.1.OR.(INT.GT.1.AND.ICHK.EQ.0))) THEN       
       IREPET=1                                                         
       GO TO 120                                                        
      END IF                                                            
C     ---COMPUTE ROW AND COLUMN---                                      
C        ---CALL NEW ITERATION PARAMETER---                             
   10 REMN=MOD(KOUNT,NITP)                                              
      IF (REMN.EQ.0) NTH=0                                              
      NTH=NTH+1                                                         
      PARAM=AOPT(NTH)                                                   
C     ***************************************************************   
C     ---ROW COMPUTATIONS---                                            
      TEST=0.D0                                                         
      RHO=S/TIM(N)                                                      
      BRK=-RHO                                                          
      DO 50 IY=1,NY                                                     
      DO 20 M=1,NX                                                      
      W(M)=0.D0                                                         
      B(M)=0.D0                                                         
      G(M)=0.D0                                                         
   20 CONTINUE                                                          
      DO 30 IX=1,NX                                                     
      IF (THCK(IX,IY).EQ.0.0) GO TO 30                                  
      COEF=VPRM(IX,IY)                                                  
      QL=-COEF*WT(IX,IY)                                                
      A=TMRX(IX-1,IY,1)*DXINV                                           
      C=TMRX(IX,IY,1)*DXINV                                             
      E=TMRX(IX,IY-1,2)*DYINV                                           
      F=TMRX(IX,IY,2)*DYINV                                             
      TBAR=A+C+E+F                                                      
      TMK=TBAR*PARAM                                                    
      BLH=-A-C-RHO-COEF-TMK                                             
      BRH=E+F-TMK                                                       
      DR=BRH*HC(IX,IY)+BRK*HK(IX,IY)-E*HC(IX,IY-1)-F*HC(IX,IY+1)+QL+RECH
     1(IX,IY)+REC(IX,IY)*ARINV                                          
      W(IX)=BLH-A*B(IX-1)                                               
      B(IX)=C/W(IX)                                                     
      G(IX)=(DR-A*G(IX-1))/W(IX)                                        
   30 CONTINUE                                                          
C                                                                       
C        ---BACK SUBSTITUTION---                                        
      DO 40 J=2,NX                                                      
      IJ=J-1                                                            
      IS=NX-IJ                                                          
   40 HR(IS,IY)=G(IS)-B(IS)*HR(IS+1,IY)                                 
   50 CONTINUE                                                          
C     ***************************************************************   
C     ---COLUMN COMPUTATIONS---                                         
      DO 90 IX=1,NX                                                     
      DO 60 M=1,NY                                                      
      W(M)=0.D0                                                         
      B(M)=0.D0                                                         
   60 G(M)=0.D0                                                         
      DO 70 IY=1,NY                                                     
      IF (THCK(IX,IY).EQ.0.0) GO TO 70                                  
      COEF=VPRM(IX,IY)                                                  
      QL=-COEF*WT(IX,IY)                                                
      A=TMRX(IX,IY-1,2)*DYINV                                           
      C=TMRX(IX,IY,2)*DYINV                                             
      E=TMRX(IX-1,IY,1)*DXINV                                           
      F=TMRX(IX,IY,1)*DXINV                                             
      TBAR=A+C+E+F                                                      
      TMK=TBAR*PARAM                                                    
      BLH=-A-C-RHO-COEF-TMK                                             
      BRH=E+F-TMK                                                       
      DC=BRH*HR(IX,IY)+BRK*HK(IX,IY)-E*HR(IX-1,IY)-F*HR(IX+1,IY)+QL+RECH
     1(IX,IY)+REC(IX,IY)*ARINV                                          
      W(IY)=BLH-A*B(IY-1)                                               
      B(IY)=C/W(IY)                                                     
      G(IY)=(DC-A*G(IY-1))/W(IY)                                        
   70 CONTINUE                                                          
C                                                                       
C        ---BACK SUBSTITUTION---                                        
      DO 80 J=2,NY                                                      
      IJ=J-1                                                            
      IB=NY-IJ                                                          
      HC(IX,IB)=G(IB)-B(IB)*HC(IX,IB+1)                                 
      IF (THCK(IX,IB).EQ.0.0) GO TO 80                                  
      CHK=DABS(HC(IX,IB)-HR(IX,IB))                                     
      IF (CHK.GT.TOL) TEST=1.D0                                         
   80 CONTINUE                                                          
   90 CONTINUE                                                          
C     ***************************************************************   
      KOUNT=KOUNT+1                                                     
      IF (TEST.EQ.0.0) GO TO 120                                        
      IF (KOUNT.GE.ITMAX) GO TO 100                                     
      GO TO 10                                                          
C     ****************************************************************  
C     ---TERMINATE PROGRAM -- ITMAX EXCEEDED---                         
  100 WRITE (6,160)                                                     
      DO 110 IX=1,NX                                                    
      DO 110 IY=1,NY                                                    
  110 HK(IX,IY)=HC(IX,IY)                                               
      CALL OUTPT                                                        
      STOP                                                              
C     ****************************************************************  
C     ---SET NEW HEAD (HK)---                                           
  120 DO 130 IY=1,NY                                                    
      DO 130 IX=1,NX                                                    
      IF (THCK(IX,IY).EQ.0.0) GO TO 130                                 
C      UPDATE THICKNESS*POROSITY FOR TRANSIENT FLOW                     
      IF (IREPET.EQ.0) THEN                                             
      THCK(IX,IY)=THCK(IX,IY)+S*(HC(IX,IY)-HK(IX,IY))                   
      IF (THCK(IX,IY).LE.0.0) THEN                                      
       WRITE (6,2000) IX,IY                                             
 2000  FORMAT(/' **** ERROR **** EFFECTIVE AQUIFER VOLUME IS ZERO ',    
     1         'IN CELL ',I4,' ,',I4//)                                 
       THCK(IX,IY)=0.0                                                  
      END IF                                                            
      HR(IX,IY)=HK(IX,IY)                                               
      HK(IX,IY)=HC(IX,IY)                                               
      END IF                                                            
C                                                                       
C     ---CUMULATE PUMPAGE AND RECHARGE FOR MASS BALANCE---              
      IF (REC(IX,IY).GT.0.0) GO TO 32                                   
      PQIN=PQIN+REC(IX,IY)                                              
      GO TO 34                                                          
   32 PQOUT=PQOUT+REC(IX,IY)                                            
   34 IF (RECH(IX,IY).GT.0.0) GO TO 36                                  
      PQIN=PQIN+RECH(IX,IY)*AREA                                        
      GO TO 38                                                          
   36 PQOUT=PQOUT+RECH(IX,IY)*AREA                                      
C     ---COMPUTE LEAKAGE FOR MASS BALANCE---                            
   38 IF (VPRM(IX,IY).EQ.0.0) GO TO 130                                 
      DELQ=VPRM(IX,IY)*AREA*(WT(IX,IY)-HK(IX,IY))                       
      IF (DELQ.GT.0.0) GO TO 125                                        
      TOTLQ=TOTLQ+DELQ*TIM(N)                                           
      GO TO 130                                                         
  125 TOTLQI=TOTLQI+DELQ*TIM(N)                                         
  130 CONTINUE                                                          
      TPIN=PQIN*TIM(N)+TPIN                                             
      TPOUT=PQOUT*TIM(N)+TPOUT                                          
C                                                                       
      WRITE (6,140) N                                                   
      IF (IREPET.EQ.0) THEN                                             
      WRITE (6,150) KOUNT                                               
      ELSE                                                              
       WRITE (6,151)                                                    
      END IF                                                            
C     ****************************************************************  
      RETURN                                                            
C     ****************************************************************  
C                                                                       
C                                                                       
C                                                                       
  140 FORMAT (1H0//3X,4HN = ,1I4)                                       
  150 FORMAT (1H ,2X,23HNUMBER OF ITERATIONS = ,1I4)                    
  151 FORMAT (1H ,2X,43HNUMBER OF ITERATIONS = 0  (HEADS UNCHANGED))    
  160 FORMAT (1H0,5X,64H***   EXECUTION TERMINATED -- MAX. NO. ITERATION
     1S EXCEEDED   ***/26X,21HFINAL OUTPUT FOLLOWS:)                    
      END 