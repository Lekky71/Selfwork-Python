/**
 * Created by root on 5/8/17.
 */
var target = 100
var xnew, xold =3.5;
while(true) {
    xnew = xold - (Math.pow(xold, xold)-100)/(Math.pow(xold, xold)*(Math.log(xold)+1)); //newton aphson iteration formula
    if(Math.abs(xnew-xold)<0.000001) break;  //test for convergence
    else xold = xnew;
           }
Console.log(xnew);