import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

describe('Calculator App', () => {
  test('renders calculator title', () => {
    render(<App />);
    const titleElement = screen.getByText(/Simple React Calculator/i);
    expect(titleElement).toBeInTheDocument();
  });

  test('renders input fields', () => {
    render(<App />);
    const firstInput = screen.getByPlaceholderText(/first number/i);
    const secondInput = screen.getByPlaceholderText(/second number/i);
    expect(firstInput).toBeInTheDocument();
    expect(secondInput).toBeInTheDocument();
  });

  test('renders all operation buttons', () => {
    render(<App />);
    expect(screen.getByText(/Add \(\+\)/i)).toBeInTheDocument();
    expect(screen.getByText(/Multiply \(×\)/i)).toBeInTheDocument();
    expect(screen.getByText(/Divide \(÷\)/i)).toBeInTheDocument();
    expect(screen.getByText(/Power \(\^\)/i)).toBeInTheDocument();
  });

  test('performs basic addition', () => {
    render(<App />);
    
    const firstInput = screen.getByPlaceholderText(/first number/i);
    const secondInput = screen.getByPlaceholderText(/second number/i);
    const addButton = screen.getByText(/Add \(\+\)/i);

    fireEvent.change(firstInput, { target: { value: '5' } });
    fireEvent.change(secondInput, { target: { value: '3' } });
    fireEvent.click(addButton);

    expect(screen.getByText(/Result: 8.00/i)).toBeInTheDocument();
  });

  test('handles division by zero', () => {
    render(<App />);
    
    const firstInput = screen.getByPlaceholderText(/first number/i);
    const secondInput = screen.getByPlaceholderText(/second number/i);
    const divideButton = screen.getByText(/Divide \(÷\)/i);

    fireEvent.change(firstInput, { target: { value: '10' } });
    fireEvent.change(secondInput, { target: { value: '0' } });
    fireEvent.click(divideButton);

    expect(screen.getByText(/Error: Cannot divide by zero/i)).toBeInTheDocument();
  });

  test('tracks calculation history', () => {
    render(<App />);
    
    const firstInput = screen.getByPlaceholderText(/first number/i);
    const secondInput = screen.getByPlaceholderText(/second number/i);
    const addButton = screen.getByText(/Add \(\+\)/i);

    fireEvent.change(firstInput, { target: { value: '2' } });
    fireEvent.change(secondInput, { target: { value: '3' } });
    fireEvent.click(addButton);

    expect(screen.getByText(/2 \+ 3 = 5.00/i)).toBeInTheDocument();
  });
}); 