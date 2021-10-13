function cuadrados = cu(n)
  
contador = 0

  for i = 2:n
    
    if mod(n,i^2) ~= 0
      
        contador = contador + 1
       
    elseif mod(n,i^2) == 0
        
        disp(0)
        
        break
        
    endif
    
  disp(1)
  
  endfor
endfunction


function simulacion = simulacion(n)
  
contador = 0

  for i = 1:n

    a = randi([1,100])
    resultado = cu(a)
    if numero == 1
      contador = contador + 1
    endif
  disp(contador/n)         #esta es la probabilidad que buscamos
  endfor
endfunction