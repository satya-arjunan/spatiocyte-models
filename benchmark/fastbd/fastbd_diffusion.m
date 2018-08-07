%function[nA,nB,nC]=Fast_Brownian_Dynamics
function[XA]=fast_BD_diffusion(duration,L,nA,R,D)

%Algorithm simulating the reaction A+B<->C with the crowder-free algorithm

%Visualise=false; %Shows real-time visualisation of system
%h=waitbar(0,'Simulating...');
nA=nA
duration=duration
rC=R%   %0.05; %crowder radius
  %2; %initial particle numbers
Ncr=0; % Number of crowders
dt=2*R*R/3/D  %1e-04; %Time step
nSim=int32(duration/dt)%1e04; %Number of simulation steps

%phi=Ncr*((4/3)*pi*rC^3); % Proportion of volume occupied by crowders
XA=unifrnd(0,L,[3,nA]);
%if Visualise==true
%    figure;
%    hold on;
%    plot3(XA(1,:),XA(2,:),XA(3,:),'.')
%    drawnow
%end
%duration = 10
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

i=1;
tic
while i<nSim
    nA(i+1)=nA(i);
    
    % Update A particle positions
    for j=1:nA(i)
        prop=normrnd(0,sqrt(2*D*dt),[3,1]);
        if rand<pi*rC^2*Ncr*sqrt(sum(prop.^2))
            XA(:,j)=XA(:,j);
        else
            XA(:,j)=mod(XA(:,j)+prop,L);
        end
    end   
   
    % Visualisation
    %if Visualise==true
    %    cla;
    %    hold on;
    %    if nA(i)>=1
    %        plot3(XA(1,:),XA(2,:),XA(3,:),'.')
    %    end
    %    axis([0 L 0 L 0 L])
    %    drawnow
    %end

    i=i+1;
end
%close(h);
toc
end

