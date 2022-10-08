
#include <stdio.h>



//prototipo de funciones
int automata(int[][70], int[],char[], char[]);

int main(){
	//-------IDENTIFICADORES------
	int IdEstadosFinales[7]={2,-1,-1,-1,-1,-1,-1};
	int IdTT[4][70];
	char IdAlfabeto[70]="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
	
	//-------CONSTANTES------
	int ConsEstadosFinales[7]={3,-1,-1,-1,-1,-1,-1};
	int ConsTT[5][70];
	char ConsAlfabeto[70]="0123456789~";
	
	//-------OPERADORES------
	int OpEstadosFinales[7]={1,2,-1,-1,-1,-1,-1};
	int OpTT[3][70];
	char OpAlfabeto[8]={'+','-','*','/','!',173,'=','\0'};
	
	//-------CADENAS LITERALES------
	int CadLitEstadosFinales[7]={3,-1,-1,-1,-1,-1,-1};
	int CadLitTT[5][70];
	char CadLitAlfabeto[80]="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\n{}[]()-";
	
	//-------CARACTERES DE PUNTUACION------
	int PuntuacionEstadosFinales[7]={1,-1,-1,-1,-1,-1,-1};
	int PuntuacionTT[3][70];
	char PuntuacionAlfabeto[8]="\n{}[]()";
	
	//-------PALABRAS RESERVADAS------
	int PalabrasReservEstadosFinales[7]={6,13,18,21,27,31,34};
	int PalabrasReservTT[36][70];
	char PalabrasReservAlfabeto[70]="numeroptalbwhifd";
	
	int j,i;
	

	
	for(j=0;j<10;j++){
		//numeros del 0 al 9
		IdTT[0][j]=3;
		IdTT[1][j]=1;
		IdTT[2][j]=1;
		IdTT[3][j]=3;
		
		ConsTT[0][j]= 4;
		ConsTT[1][j]= 2;
		ConsTT[2][j]= 2;
		ConsTT[3][j]= 4;
		ConsTT[4][j]= 4;
		
		CadLitTT[0][j]=4;
		CadLitTT[1][j]=2;
		CadLitTT[2][j]=2;
		CadLitTT[3][j]=4;
		CadLitTT[4][j]=4;
	}
	
	for(;j<62;j++){
		//letras
		IdTT[0][j]=1;
		IdTT[1][j]=2;
		IdTT[2][j]=2;
		IdTT[3][j]=3;
		
		CadLitTT[0][j]=4;
		CadLitTT[1][j]=2;
		CadLitTT[2][j]=2;
		CadLitTT[3][j]=4;
		CadLitTT[4][j]=4;
	}
	// ---------LLENANDO CONS---------------
	ConsTT[0][10]= 1;
	ConsTT[1][10]= 4;
	ConsTT[2][10]= 3;
	ConsTT[3][10]= 4;
	ConsTT[4][10]= 4;
	
	//----------LLENADO OpTT-----------
	OpTT[0][0]=OpTT[0][1]=OpTT[0][2]=OpTT[0][3]= 1;
	OpTT[0][4]=3;
	OpTT[0][5]=4;
	OpTT[0][6]=2;
	for(j=0;j<7;j++){ OpTT[1][j]=4; OpTT[4][j]; OpTT[3][j];}
	for(j=0;j<6;j++){ OpTT[2][j]=4;}
	OpTT[2][6]=1;
	OpTT[3][5]=1;
	
	
	//------------LLENADO PalabrasReserv------------
	for(j=0;j<17; j++){
		for(i=0; i<36; i++){
			PalabrasReservTT[i][j]=35;
		}
	}
	PalabrasReservTT[0][0]=1;
	PalabrasReservTT[0][4] = 22;
	PalabrasReservTT[0][5] = 30;
	PalabrasReservTT[0][6] = 7;
	PalabrasReservTT[1][1] = 2;
	PalabrasReservTT[2][2] = 3;
	PalabrasReservTT[3][3] = 4;
	PalabrasReservTT[4][4] = 5;
	PalabrasReservTT[5][5] = 6;
	PalabrasReservTT[11][4] = 12;
	PalabrasReservTT[17][3] = 18;
	PalabrasReservTT[19][5] = 20;
	PalabrasReservTT[0][4] = 22;
	PalabrasReservTT[20][4] = 21;
	PalabrasReservTT[22][3] = 23;
	PalabrasReservTT[24][1] = 25;
	PalabrasReservTT[25][4] = 26;
	PalabrasReservTT[26][0] = 27;
	PalabrasReservTT[30][4] = 31;
	PalabrasReservTT[32][0] = 33;
	PalabrasReservTT[0][8] = 32;
	PalabrasReservTT[0][11] = 14;
	PalabrasReservTT[0][13] = 20;
	PalabrasReservTT[0][14] = 19;
	PalabrasReservTT[7][8] = 8;
	PalabrasReservTT[8][9] = 9;
	PalabrasReservTT[9][8] = 10;
	PalabrasReservTT[10][10] = 11;
	PalabrasReservTT[12][8] = 13;
	PalabrasReservTT[16][9] = 17;
	PalabrasReservTT[14][12] = 15;
	PalabrasReservTT[15][13] = 16;
	PalabrasReservTT[28][14] = 29;
	PalabrasReservTT[33][15] = 34;
	
	
	
		
	//------LLENANDO PUNTUACION Y CADENAS LITERALES---------
	for(i=0;i<7;i++)
		{ PuntuacionTT[0][i] = 1;
		PuntuacionTT[1][i] = 2;
		PuntuacionTT[2][i] = 2;
		
		CadLitTT[0][i+62]=4;
		CadLitTT[1][i+62]=2;
		CadLitTT[2][i+62]=2;
		CadLitTT[3][i+62]=4;
		CadLitTT[4][i+62]=4;
		}
		CadLitTT[0][69]=1;
		CadLitTT[1][69]=4;
		CadLitTT[2][69]=3;
		CadLitTT[3][69]=4;
		CadLitTT[4][69]=4;
	
	
	


	
	
	char cadena[10];
	printf("ingresar cadena: ");
    scanf("%s", &cadena);

	//scanf("ingresar cadena: %s \n", &cadena);
	while(cadena[0]!='0')
	{
	printf(" cadena: %s\n\n", cadena);
	printf("valor del automata para identificador: %d \n",automata(IdTT,IdEstadosFinales, IdAlfabeto, cadena));
	printf("valor del automata para constantes: %d \n",automata(ConsTT,ConsEstadosFinales, ConsAlfabeto, cadena));
	printf("valor del automata para palabras reservadas: %d \n", automata(PalabrasReservTT, PalabrasReservEstadosFinales, PalabrasReservAlfabeto, cadena));
	printf("valor del automata para puntuacion: %d \n",automata(PuntuacionTT,PuntuacionEstadosFinales, PuntuacionAlfabeto, cadena));
	printf("valor del automata para operadores: %d \n",automata(OpTT,OpEstadosFinales, OpAlfabeto, cadena));
	printf("valor del automata para cedenas literales: %d \n",automata(CadLitTT,CadLitEstadosFinales, CadLitAlfabeto, cadena));
	
	//scanf("ingresar cadena: %s \n", &cadena);
	printf("ingresar cadena: ");
    scanf("%s", &cadena);
	
	
}return 0;
}

int automata(int TT[][70],int estadosFinales[],char alfabeto[], char cadena[]){
	int i=0, j=0, estadoActual=0, resultado=1;
	int bandera=0;
	while (cadena[i]!= '\0'){
		j=0;
		while((cadena[i] != alfabeto[j] )&& alfabeto[j] != '\0'){
			j++;
			//printf("\ncadena[%d]: %c != alfabeto[%d]: %c ==> %d \n", i, cadena[i], j, alfabeto[j], (cadena[i]!=alfabeto[j]));
		}
		//printf("\nalfabeto[%d]: %c, cadena[%d]: %c \n", j, alfabeto[j], i, cadena[i]);
		if(alfabeto[j]==cadena[i]){//printf("\nestadoActual: %d, TT[%d][%d]: %d\n", estadoActual, estadoActual, j, TT[estadoActual][j]);
			estadoActual = TT[estadoActual][j];
			}
		else {
		resultado=0;
		break;
		}
		i++;
		
	}
	if(resultado==1){
	for(int k=0; k<7;k++){
		//printf("\nestadoActual: %d == estadosFinales[%d]: %d\n", estadoActual, k, estadosFinales[k]);
		if(estadoActual == estadosFinales[k]){
			bandera=1;
		}
	}
	resultado=bandera;}
	
	
	return resultado;
}



