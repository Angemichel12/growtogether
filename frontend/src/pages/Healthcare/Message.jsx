import * as React from 'react';
import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import { Link } from 'react-router-dom';
import prof from '../../img/profile.png'

const Message = () => {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => {
        setOpen(true);
    };
    const handleClose = () => {
        setOpen(false);
    };

    return (
        <div>
            <Link onClick={handleOpen}>Message</Link>
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="parent-modal-title"
                aria-describedby="parent-modal-description"
            >
                <Box className="mt-32 w-auto ">

                <div className="flex  pt-8 h-auto justify-center">
                    <content className="flex  bg-white h-auto w-11/12 mb-8 py-6">
                        <aside className='w-4/12'>
                            <div className='bg-gray-300 m-4 rounded-lg flex gap-4'>
                                <img src={prof} alt='profile' className='rounded-full w-20 h-20 p-4' />
                                <content className='pt-4 pb-6'>
                                    <h1 className='text-xl font-bold'>Parent 1</h1>
                                    <p className='text-lg pt-2'>Good Evening Doctor</p>
                                    <p className='pt-2'>I am 14 weeks pregnent </p>
                                </content>
                            </div>

                            <div className='bg-gray-300 m-4 rounded-lg flex gap-4'>
                                <img src={prof} alt='profile' className='rounded-full w-20 h-20 p-4' />
                                <content className='pt-4 pb-6'>
                                    <h1 className='text-xl font-bold'>Parent 2</h1>
                                    <p className='text-lg pt-2'>Good Evening Doctor</p>
                                    <p className='pt-2'>I am 14 weeks pregnent </p>
                                </content>
                            </div>
                        </aside>
                        <content></content>
                    </content>
                </div>
                </Box>
            </Modal>
        </div>
    );
}
export default  Message;