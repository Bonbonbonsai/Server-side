function addStaff(pro_id, csrf_token){
    const emp = document.getElementById('input-add-staff');
    const emp_id = emp.value;

    fetch(`/project/detail/${pro_id}/add-user/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        },
        body: JSON.stringify({ emp_id })
    })
    .then(data => {
        console.log('Item updated successfully')
        window.location.reload()
    })
    .catch(error => console.error('Error:', error));
}


async function removeStaff(pro_id, emp_id, csrf_token){
    // กำหนด path ให้ถูกต้อง
    fetch(`/project/detail/${pro_id}/remove-user/${emp_id}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        },
    })
    .then(data => {
        console.log('Item updated successfully')
        window.location.reload()
    })
    .catch(error => console.error('Error:', error));
}