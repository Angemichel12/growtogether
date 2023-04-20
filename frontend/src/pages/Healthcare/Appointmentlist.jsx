import * as React from 'react';
import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import { Link } from 'react-router-dom';
import { FaTimes } from 'react-icons/fa';

const Appointmentlist = () => {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => {
        setOpen(true);
    };
    const handleClose = () => {
        setOpen(false);
    };

    return (
        <div>
            <Link onClick={handleOpen}>Appointmentlist</Link>
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="parent-modal-title"
                aria-describedby="parent-modal-description"
            >
                <Box className="mt-32 w-auto ">

                    <div className="flex justify-center pt-8">
                        <content className="flex flex-col bg-white h-auto w-11/12 p-6">
                            <div className='flex justify-end'>
                                <button onClick={handleClose} className=' rounded-3xl   text-white '><FaTimes className='text-red-500 text-2xl' /></button>
                            </div>
                            <div className='w-full flex flex-col items-center justify-center'>
                                <h1 className='text-green-500 text-4xl font-bold '>Today</h1>
                                <content className='flex gap-32 mt-4'>
                                    <h1 className='text-xl font-bold'>Reg Number</h1>
                                    <h1 className='text-xl font-bold'>Full Name</h1>
                                    <h1 className='text-xl font-bold'>Telphone</h1>
                                    <h1 className='text-xl font-bold'>Email</h1>
                                </content>
                            </div>

                            <div className='w-full flex flex-col items-center justify-center mt-4'>
                                <h1 className='text-green-500 text-4xl font-bold '>Tomorrow</h1>
                                <content className='flex gap-32 mt-4'>
                                    <h1 className='text-xl font-bold'>Reg Number</h1>
                                    <h1 className='text-xl font-bold'>Full Name</h1>
                                    <h1 className='text-xl font-bold'>Telphone</h1>
                                    <h1 className='text-xl font-bold'>Email</h1>
                                </content>
                            </div>
                        </content>
                    </div>
                </Box>
            </Modal>
        </div>
    );
}
export default Appointmentlist;