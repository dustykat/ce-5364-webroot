      PROGRAM USGSMOC
C     ****************************************************************  
C     *                                                              *  
C     *     SOLUTE TRANSPORT AND DISPERSION IN A POROUS MEDIUM       *  
C     *      NUMERICAL SOLUTION --- METHOD OF CHARACTERISTICS        *  
C     *      PROGRAMMED BY J. D. BREDEHOEFT AND L. F. KONIKOW        *  
C     *               REVISED APRIL 1979, MARCH 1980                 *  
C     *               REVISED DECEMBER 1980                          *  
C     *               REVISED AUGUST 1981, JUNE 1982                 *  
C     *               REVISED OCTOBER 1983                           *  
C     * REV. JUNE-AUG. 1984 BY W. SANFORD TO ALLOW 16 PTS. PER NODE  *  
C     *  REV. MAY-AUG. 1985 BY L. KONIKOW AND M. PERSON TO INCLUDE:  *  
C     *       DECAY AND EQUILIBRIUM SORPTION-DESORPTION REACTIONS    *  
C     *                                                              *  
C     * REV. JULY-DEC.1985 TO ALLOW SECONDARY SUBGRID FOR TRANSPORT  *  
C     *               REVISED JULY 1986                              *  
C     *               REVISED MARCH 1987 BY D.J. GOODE               *  
C     *               REVISED MAY 1987 BY D.J. GOODE                 *  
C     *               REVISED JANUARY 1988                           *  
C     *               REVISED NOVEMBER 1988                          *
C     *                                                              *
C     * MODIFIED FOR MACII-SI AND FREE FORMAT INPUT FOR CE7397       *
C     *               MODIFIED FEBRUARY 1992 BY T.G. CLEVELAND       *    
C     * MODIFIED FOR INTEL-486 AND FREE FORMAT INPUT FOR CE7332      *
C     *               MODIFIED MARCH 1995 BY T.G. CLEVELAND          *
C     * MODIFIED FOR WINDOWS APPLICATIONS                            *
C     *               MODIFIED MARCH 1995 BY T.G. CLEVELAND          *
C     *                                                              *
C     * MODIFIED FOR 32-BIT WINDOWS APPLICATIONS                     *
C     *               APRIL 1997 BY T.G. CLEVELAND                   *
C     *                                                              * 
C     * MODIFIED FOR ARM/AARCH-64 JUPYTER HUB WINDOWS APPLICATIONS   *
C     *               SEPTEMBER 2023 BY T.G. CLEVELAND               *
C     ****************************************************************  
C      DOUBLE PRECISION DMIN1,DEXP,DLOG,DABS                             
      DOUBLE PRECISION TMRX,VPRM,HI,HR,HC,HK,WT,REC,RECH,TIM,AOPT,TITLE 
      DOUBLE PRECISION XDEL,YDEL,S,AREA,SUMT,RHO,PARAM,TEST,TOL,PINT,   
     1                 HMIN,PYR,ANFCTR                                  
      DOUBLE PRECISION TINIT,TIMX                                       
      DOUBLE PRECISION TINT                                             
      DOUBLE PRECISION TMSUM,TDEL                                       
      DOUBLE PRECISION TOTLQ,TOTLQI,TPIN,TPOUT                          
      DOUBLE PRECISION DXINV,DYINV,ARINV,PORINV                         
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
      COMMON /HEDD/ TINIT,TIMX                                          
      COMMON /XINV/ DXINV,DYINV,ARINV,PORINV                            
      COMMON /BALM/ TOTLQ,TOTLQI,TPIN,TPOUT                             
      COMMON /CHMA/ PART(3,06400),CONC(020,020),TMCN(05,50),VX(040,040),
     1              VY(040,040),CONINT(020,020),CNRECH(020,020),POROS,  
     2              SUMTCH,BETA,TIMV,STORM,STORMI,CMSIN,CMSOUT,FLMIN,   
     3              FLMOT,SUMIO,CELDIS,DLTRAT,CSTORM                    
      COMMON /CHMC/ SUMC(020,020),VXBDY(040,040),VYBDY(040,040)         
      COMMON /CHMP/ PTID(06400)                                         
      COMMON /CHMR/ RF,DK,RHOB,THALF,DECAY,ADSORB,SORBI,DMASS1,CSTM2    
      COMMON /DIFUS/ DISP(020,020,4)                                    
C     ***************************************************************  
CTGC
      CHARACTER*11 FILEIN,FILEOUT 
C      ---LOAD DATA---                                                  
      INT=0                                                             
      TMSUM=0.D0
C
CTGC  ASSIGN STDIO TO A FILE
C
      WRITE(*,*)'ENTER INPUT FILE NAME'
      READ(*,'(A)')FILEIN
      OPEN(UNIT=5,STATUS='UNKNOWN',ACCESS='SEQUENTIAL',
     1     FILE=FILEIN)
	  REWIND(5)
      WRITE(*,*)'ENTER OUTPUT FILE NAME'
      READ(*,'(A)')FILEOUT
      OPEN(UNIT=6,FILE=FILEOUT)
      REWIND(6)
      CALL PARLOD                                                       
      CALL GENPT                                                        
C     ***************************************************************   
C     ---START COMPUTATIONS---                                          
C        ---COMPUTE ONE PUMPING PERIOD---                               
      DO 150 INT=1,NPMP                                                 
      IF (INT.GT.1) TMSUM=TMSUM+PYR                                     
      IF (INT.GT.1) CALL PARLOD                                         
      REMN=1.0                                                          
C        ---COMPUTE ONE TIME STEP---                                    
      DO 130 N=1,NTIM                                                   
      IPRNT=0                                                           
C        ---LOAD NEW DELTA T---                                         
      TINT=SUMT-TMSUM                                                   
      TDEL=DMIN1(TIM(N),PYR-TINT)                                       
      SUMT=SUMT+TDEL                                                    
      TIM(N)=TDEL                                                       
      IF (NPNT.GT.0) REMN=MOD(N,NPNT)                                   
      IF (SUMT.GE.(PYR+TMSUM)) IPRNT=1                                  
C     ***************************************************************   
      CALL ITERAT                                                       
      IF (REMN.EQ.0.0.OR.N.EQ.NTIM.OR.IPRNT.EQ.1) CALL OUTPT            
      CALL VELO                                                         
  101 CALL MOVE                                                         
C     ***************************************************************   
      IF (SUMT.GE.(PYR+TMSUM)) GO TO 140                                
  130 CONTINUE                                                          
C     ***************************************************************   
  140 CONTINUE                                                          
  150 CONTINUE                                                          
C     ***************************************************************   
CTGC      ENDFILE(6)
      WRITE(*,*)'END OF SIMULATION BY USGS MOC'                                                        
      IF (NPNCHV.EQ.0) GO TO 155                                        
CTGC      ENDFILE(7)                                                        
  155 CONTINUE
      CLOSE(5)
C     PAUSE                                                          
      STOP                                                              
C     ***************************************************************   
      END