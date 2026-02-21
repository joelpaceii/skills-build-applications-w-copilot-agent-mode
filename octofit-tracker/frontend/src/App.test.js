
test('renders Octofit Tracker navigation', () => {
  render(<App />);
  // Check for the brand
  expect(screen.getByText(/Octofit Tracker/i)).toBeInTheDocument();
  // Check for navigation links
  expect(screen.getByText(/Activities/i)).toBeInTheDocument();
  expect(screen.getByText(/Leaderboard/i)).toBeInTheDocument();
  expect(screen.getByText(/Teams/i)).toBeInTheDocument();
  expect(screen.getByText(/Users/i)).toBeInTheDocument();
  expect(screen.getByText(/Workouts/i)).toBeInTheDocument();
});
