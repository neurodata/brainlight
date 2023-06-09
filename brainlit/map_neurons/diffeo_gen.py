import numpy as np
import torch
import matplotlib.pyplot as plt


# an interp function
def interp(x, I, phii, **kwargs):
    # note I want components of phi to be at the end
    # components of I should be at the beginning
    # this does make composing two transformations a bit weird
    # start by scaling to -1,1
    phii_ = torch.clone(phii)
    for i in range(3):
        phii_[..., i] -= x[i][0]
        phii_[..., i] /= x[i][-1] - x[i][0]
    phii_ *= 2.0
    phii_ -= 1.0

    # we need xyz at the end, and in the order xyz (not zyx)
    # check if I'm using batches
    if I.ndim == 4:
        add_batch = True
    elif I.ndim == 5:
        add_batch = False
    else:
        raise Exception("Image should be 4 or 5 dim")

    if add_batch:
        Iin = I[None]
        phii_in = phii_[None]
    else:
        Iin = I
        phii_in = phii_
    output = torch.nn.functional.grid_sample(
        Iin,
        torch.flip(phii_in, (-1,)),
        align_corners=True,
        padding_mode="border",
        **kwargs
    )
    # remove batch dimension
    if add_batch:
        output = output[0]
    return output


def expR(xv, v0, K, n=10, visualize=False, return_forward=True):
    """
    Riemannian exponential, todo

    Parameters
    ----------
    xv : list of arrays
        Location of pixels in v.
    v : velocity at time 0
        Recall shape is rowxcolxsicex3
    K : array
        kernel in fft domain
    n : int
        number of timesteps

    visualie : bool
        only supported with no batch

    Returns
    -------
    phii : array
        inverse deformation used to transform images
    Notes
    -----
    pt = Dphi^{-T}(phi_t^{-1}) p0(phi_t^{-1})|Dphii^{-1}|
       = Dphii^{T} p0(phii)|Dphii^{-1}|
    """

    use_batch = v0.ndim == 5
    if not use_batch:
        permute0 = (-1, -4, -3, -2)
        permute1 = (-3, -2, -1, -4)
    else:
        permute0 = (0, -1, -4, -3, -2)
        permute1 = (0, -3, -2, -1, -4)

    # initialize p at time 0
    p0 = torch.fft.ifftn(
        torch.fft.fftn(v0, dim=(-2, -3, -4)) / K[..., None], dim=(-2, -3, -4)
    ).real
    # initialize phii at time 0
    XV = torch.stack(
        torch.meshgrid([torch.as_tensor(x) for x in xv], indexing="ij"), -1
    )
    # initialize dv
    dv = [x[1].item() - x[0].item() for x in xv]

    phii = XV.clone()
    if use_batch:
        phii = phii[None].repeat(v0.shape[0], 1, 1, 1, 1)
        XV = XV[None].repeat(v0.shape[0], 1, 1, 1, 1)

    if visualize and not use_batch:
        fig, ax = plt.subplots(1, 3)

    # we take n timesteps

    if return_forward:
        vsave = []
    for t in range(n):
        # we need to calculate p at time t
        # first we just deform it
        p = interp(xv, p0.permute(*permute0), phii).permute(*permute1)
        # then we need the jacobian
        Dphii = torch.stack(torch.gradient(phii, dim=(-4, -3, -2), spacing=dv), -1)
        # and the determinant (over the last two axes)
        detDphii = torch.linalg.det(Dphii)
        # then we will multiply

        p = (Dphii.transpose(-1, -2) @ p[..., None])[..., 0] * detDphii[..., None]
        # now we calculate v
        v = torch.fft.ifftn(
            torch.fft.fftn(p, dim=(-2, -3, -4)) * K[..., None], dim=(-2, -3, -4)
        ).real
        if return_forward:
            vsave.append(v)
        # now we update phii
        Xs = XV - v / n
        phii = interp(xv, (phii - XV).permute(*permute0), Xs).permute(*permute1) + Xs

        if visualize and not use_batch:
            pshow = np.array(p[p0.shape[1] // 2, :, :, :])
            pshow -= np.min(pshow, axis=(0, 1, 2))
            pshow /= np.max(pshow, axis=(0, 1, 2))
            ax[0].cla()
            ax[0].imshow(pshow)

            vshow = np.array(v[p0.shape[1] // 2, :, :, :])
            vshow -= np.min(vshow, axis=(0, 1, 2))
            vshow /= np.max(vshow, axis=(0, 1, 2))
            ax[1].cla()
            ax[1].imshow(vshow)

            fig.canvas.draw()
    if not return_forward:
        return phii
    else:
        phi = XV.clone()
        for v in reversed(vsave):
            Xs = XV + v / n
            phi = interp(xv, (phii - XV).permute(*permute0), Xs).permute(*permute1) + Xs
        return phi
