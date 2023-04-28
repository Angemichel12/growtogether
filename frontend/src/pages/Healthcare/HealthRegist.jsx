import * as React from 'react';
import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import { Link } from 'react-router-dom';
import { FaTimes } from 'react-icons/fa';
const HealthRegister = () => {
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => {
    setOpen(true);
  };
  const handleClose = () => {
    setOpen(false);
  };

  return (
    <div>
      <Link onClick={handleOpen}>Registering Parent</Link>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="parent-modal-title"
        aria-describedby="parent-modal-description"
      >
        <Box className="mt-32 w-auto mx-96">

          <div className="flex justify-center pt-2">
            <content className="bg-white h-auto w-auto pl-10 py-4">
              <div className='flex justify-end'>
                <button onClick={handleClose} className=' rounded-3xl px-5 py-1 text-white '><FaTimes className='text-red-500 text-2xl' /></button>
              </div>
              <p className='text-4xl mb-16 font-bold py-4'>REGISTER A PARENT</p>
              <form className=''>
                <label className='font-bold text-lg'>Names</label>
                <input type='text' className='border-black border p-2  mb-4 mx-16'></input><br />
                <label className='font-bold text-lg'>Birth Year</label>
                <input type='text' className='border-black border p-2  mb-4 mx-10'></input><br />
                <label className='font-bold text-lg'>Email</label>
                <input type='text' className='border-black border p-2 mb-4 mx-20'></input><br />
                <label className='font-bold text-lg'>Telephone</label>
                <input type='text' className='border-black border p-2 mb-4 mx-10'></input><br />
                <Link to=""><button className='healbtn my-12 mx-32 rounded-3xl text-lg border border-black text-white px-5 py-2 '>Register</button></Link>
              </form>
            </content>
          </div>
        </Box>
      </Modal>
    </div>
  );
}
export default HealthRegister;