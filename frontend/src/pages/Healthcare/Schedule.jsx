import * as React from 'react';
import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import { Link } from 'react-router-dom';
import { FaTimes } from 'react-icons/fa';

export default function Schedule() {
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => {
    setOpen(true);
  };
  const handleClose = () => {
    setOpen(false);
  };

  return (
    <div>
      <Link onClick={handleOpen}>Schedule</Link>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="parent-modal-title"
        aria-describedby="parent-modal-description"
      >
        <Box className="mt-32 w-auto flex justify-center bg-white flex-col mx-96 pb-32">
          <div className='flex justify-end'>
            <button onClick={handleClose} className=' rounded-3xl px-5 py-1 text-white '><FaTimes className='text-red-500 text-2xl' /></button>
          </div>
        </Box>
      </Modal>
    </div>
  );
}