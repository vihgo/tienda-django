
function aumentarCantidad(event){

    const container=event.target.closest(".container");
    const cantidad = container.querySelector('b[name="cantidad"]');
    const precio=container.querySelector('p[name="precio"]');
    const totalItem=container.querySelector('p[name="total-item"]');
    console.log(cantidad)
    console.log(precio.textContent.split('$'))
    console.log(totalItem)

   
 
    let valorCantidad=parseInt(cantidad.textContent)
    valorCantidad++
    if(valorCantidad <1)valorCantidad=1

    
    const valorPrecio=parseInt(precio.textContent.split('$')[1])
    const valorTotal=valorPrecio*valorCantidad
    cantidad.textContent=valorCantidad
    totalItem.textContent=valorTotal
    

}
function reducirCantidad(event){

    const container=event.target.closest(".container");
    const cantidad = container.querySelector('b[name="cantidad"]');
    const precio=container.querySelector('p[name="precio"]');
    const totalItem=container.querySelector('p[name="total-item"]');
    console.log(cantidad)
    console.log(precio.textContent.split('$'))
    console.log(totalItem)

   
 
    let valorCantidad=parseInt(cantidad.textContent)
    valorCantidad--
    if(valorCantidad <1)valorCantidad=1

    
    const valorPrecio=parseInt(precio.textContent.split('$')[1])
    const valorTotal=valorPrecio*valorCantidad
    cantidad.textContent=valorCantidad
    totalItem.textContent=valorTotal


}

function cargarTotalItem(event){
    target=event.target
    console.log(target)
}