import * as React from 'react';
import { useNavigate } from "react-router-dom";
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import MenuItem from '@mui/material/MenuItem';
import InputLabel from '@mui/material/InputLabel';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import FormControl from '@mui/material/FormControl';
import DatePicker from '@mui/lab/DatePicker';
import LocalizationProvider from '@mui/lab/LocalizationProvider';
import AdapterDateFns from '@mui/lab/AdapterDateFns';
import uuid from 'react-uuid';
const axios = require('axios').default;


function Copyright(props) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      {'Copyright © '}
      <Link color="inherit" href="https://mui.com/">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const theme = createTheme();

export default function RegistrationPage() {
  const [date, setDate] = React.useState('');
  const [gender, setGender] = React.useState('non-binary');
  const [userType, setUserType] = React.useState('patient');
  const navigate = useNavigate();
  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const load = {
      id: uuid(),
      firstName: data.get('firstName'),
      lastName: data.get('lastName'),
      email: data.get('email'),
      password: data.get('password'),
      age: document.getElementById("number").value,
      dateOfBirth: date.toLocaleDateString(),
      gender: gender,
      userType: userType, 
      address: ''
    }
    console.log(load);
    // axios({
    //   method: 'post',
    //   url: 'http://localhost:5000/api/1/user/',
    //   headers: {
    //     'Content-Type': 'application/json'
    //   },
    //   body: load
    // })
    axios.post('http://localhost:5000/api/1/user/', load)
    .then((msg)=>{
      console.log(msg.data)
      navigate('/signin')
    }).catch((e)=>{
      console.log(e);
    });
  };

  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign up
          </Typography>
          <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6}>
                <TextField
                  autoComplete="given-name"
                  name="firstName"
                  required
                  fullWidth
                  id="firstName"
                  label="First Name"
                  autoFocus
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  required
                  fullWidth
                  id="lastName"
                  label="Last Name"
                  name="lastName"
                  autoComplete="family-name"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="email"
                  label="Email Address"
                  name="email"
                  autoComplete="email"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  name="password"
                  label="Password"
                  type="password"
                  id="password"
                  autoComplete="new-password"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <FormControl sx={{ minWidth: 190 }}>
                    <InputLabel id="demo-simple-select-helper-label">Gender</InputLabel>
                    <Select
                        defaultValue={''}
                        labelId="demo-simple-select-helper-label"
                        id="gender"
                        label="Gender"
                        onChange={(event) => {
                          setGender(event.target.value);
                        }}
                    >
                        <MenuItem value='male'>Male</MenuItem>
                        <MenuItem value='female'>Female</MenuItem>
                        <MenuItem value='non-binary'>Non-binary</MenuItem>
                    </Select>
                </FormControl>
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                    id="number"
                    label="Age"
                    type="number"
                    InputLabelProps={{
                        shrink: true,
                    }}
                    />
              </Grid>
              <Grid item xs={12} sm={6}>
                <LocalizationProvider dateAdapter={AdapterDateFns}>
                  <DatePicker
                    views={['year', 'month', 'day']}
                    label="Date of Birth"
                    defaultValue={''}
                    onChange={(newValue) => {
                      setDate(newValue);
                    }}
                    renderInput={(params) => <TextField {...params} helperText={null} />}
                  />
                </LocalizationProvider> 
                </Grid>
                <Grid item xs={12} sm={6} >
                <FormControl sx={{ minWidth: 190 }}>
                    <InputLabel id="demo-simple-select-helper-label">User Type</InputLabel>
                    <Select
                        labelId="demo-simple-select-helper-label"
                        id="user-type-selecter"
                        label="user-type"
                        defaultValue={''}
                        onChange={(event) => {
                          setUserType(event.target.value);
                        }}
                    >
                        <MenuItem value='doctor'>Doctor</MenuItem>
                        <MenuItem value='nurse'>Nurse</MenuItem>
                        <MenuItem value='patient'>Patient</MenuItem>
                    </Select>
                </FormControl>
              </Grid>
            </Grid>
        
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Sign Up
            </Button>
            <Grid container justifyContent="flex-end">
              <Grid item>
                <Link href="/signin" variant="body2">
                  Already have an account? Sign in
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
        <Copyright sx={{ mt: 5 }} />
      </Container>
    </ThemeProvider>
  );
}