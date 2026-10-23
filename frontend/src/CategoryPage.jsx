import { useEffect, useState } from "react";

function CategoryList(){
    const [catgory, setCatgory]= useState([]);

    useEffect(()=>{
        fetch("/api/categories/")
        .then((response) => response.json())
        .then((data) => setCatgory(data))
        .catch((error) => console.error(error));
    },[]);
    return(
        <div>
            <h1>Category Hello</h1>

            {catgory.map((catgory)=>(
                <div key = {catgory.id}>
                    <h2>{catgory.name}</h2>
                    <h2>{catgory.description}</h2>
                    {/* <h2>{product.image}</h2> */}
                    
                    </div>
            ))}
        </div>
    );
}
export default CategoryList