# SeQuerySecurityDescriptorInfo

- RVA: `0x00872820`–`0x00872CA4` (길이 `1,156` bytes)
- VA: `0x0000000140872820`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C644`
- 디코드: `298`개 명령, `1,156/1,156` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00872A1A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00872A6A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00872AD9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00872B40` → [RtlpFilterSacl](RtlpFilterSacl_function_008731D0.md) (function, `0x008731D0`)
- `0x00872BA3` → [RtlpFilterSacl](RtlpFilterSacl_function_008731D0.md) (function, `0x008731D0`)

### Direct callers
- [CmpSecurityMethod](CmpSecurityMethod_function_00870CC0.md) at `0x00870F56`
- [ObQuerySecurityDescriptorInfo](ObQuerySecurityDescriptorInfo_function_00873624.md) at `0x00873661`
- [IopGetSetSecurityObject](IopGetSetSecurityObject_function_00873A80.md) at `0x00873DEA`
- [ObpAllocateAndQuerySecurityDescriptorInfo](ObpAllocateAndQuerySecurityDescriptorInfo_function_0087421C.md) at `0x0087433E`
- [ObpAllocateAndQuerySecurityDescriptorInfo](ObpAllocateAndQuerySecurityDescriptorInfo_function_0087421C.md) at `0x0087436F`
- [sub_008BAA6F](../8B/Unknown_function_008BAA6F.md) at `0x008BAAAD`
- [EtwQueryPerformanceTraceInformation](../AF/EtwQueryPerformanceTraceInformation_function_00AF28A4.md) at `0x00AF2A15`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00872A1A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00872A6A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00872AD9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00872820  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00872825  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0087282A  53                              push rbx
0087282B  56                              push rsi
0087282C  57                              push rdi
0087282D  41 54                           push r12
0087282F  41 55                           push r13
00872831  41 56                           push r14
00872833  41 57                           push r15
00872835  48 81 EC 80 00 00 00            sub rsp, 0x80
0087283C  4D 8B D0                        mov r10, r8
0087283F  48 8B F2                        mov rsi, rdx
00872842  4C 8B C1                        mov r8, rcx
00872845  45 33 ED                        xor r13d, r13d
00872848  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
0087284D  45 8B FD                        mov r15d, r13d
00872850  44 89 6C 24 24                  mov dword ptr [rsp + 0x24], r13d
00872855  41 8B 0A                        mov ecx, dword ptr [r10]
00872858  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
0087285C  49 8B 01                        mov rax, qword ptr [r9]
0087285F  48 85 C0                        test rax, rax
00872862  0F 84 E8 03 00 00               je 0x140872c50
00872868  0F 10 00                        movups xmm0, xmmword ptr [rax]
0087286B  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
00872870  8B 48 10                        mov ecx, dword ptr [rax + 0x10]
00872873  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00872877  0F B7 48 02                     movzx ecx, word ptr [rax + 2]
0087287B  66 85 C9                        test cx, cx
0087287E  0F 89 64 03 00 00               jns 0x140872be8
00872884  8B 50 04                        mov edx, dword ptr [rax + 4]
00872887  85 D2                           test edx, edx
00872889  0F 84 B4 03 00 00               je 0x140872c43
0087288F  4C 8D 14 10                     lea r10, [rax + rdx]
00872893  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
00872898  4C 89 54 24 58                  mov qword ptr [rsp + 0x58], r10
0087289D  66 85 C9                        test cx, cx
008728A0  0F 89 39 03 00 00               jns 0x140872bdf
008728A6  8B 50 08                        mov edx, dword ptr [rax + 8]
008728A9  85 D2                           test edx, edx
008728AB  0F 84 8A 03 00 00               je 0x140872c3b
008728B1  4C 8D 24 10                     lea r12, [rax + rdx]
008728B5  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
008728BA  F6 C1 04                        test cl, 4
008728BD  0F 84 14 03 00 00               je 0x140872bd7
008728C3  66 85 C9                        test cx, cx
008728C6  0F 89 66 03 00 00               jns 0x140872c32
008728CC  8B 50 10                        mov edx, dword ptr [rax + 0x10]
008728CF  85 D2                           test edx, edx
008728D1  0F 84 30 03 00 00               je 0x140872c07
008728D7  48 8D 1C 10                     lea rbx, [rax + rdx]
008728DB  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
008728E0  F6 C1 10                        test cl, 0x10
008728E3  0F 85 74 02 00 00               jne 0x140872b5d
008728E9  4D 8B DD                        mov r11, r13
008728EC  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
008728F1  4C 89 5C 24 68                  mov qword ptr [rsp + 0x68], r11
008728F6  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
008728FB  49 C1 EE 10                     shr r14, 0x10
008728FF  B8 FF 7F 00 00                  mov eax, 0x7fff
00872904  66 44 23 F0                     and r14w, ax
00872908  66 44 89 74 24 52               mov word ptr [rsp + 0x52], r14w
0087290E  BF 14 00 00 00                  mov edi, 0x14
00872913  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00872917  45 8B 08                        mov r9d, dword ptr [r8]
0087291A  41 8B C1                        mov eax, r9d
0087291D  25 80 00 00 00                  and eax, 0x80
00872922  41 8B C9                        mov ecx, r9d
00872925  81 E1 00 01 00 00               and ecx, 0x100
0087292B  41 0F BA E1 10                  bt r9d, 0x10
00872930  0F 82 D9 02 00 00               jb 0x140872c0f
00872936  41 F6 C1 01                     test r9b, 1
0087293A  74 1B                           je 0x140872957
0087293C  4D 85 D2                        test r10, r10
0087293F  74 16                           je 0x140872957
00872941  41 0F B6 42 01                  movzx eax, byte ptr [r10 + 1]
00872946  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
0087294D  44 8B E8                        mov r13d, eax
00872950  8D 78 14                        lea edi, [rax + 0x14]
00872953  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00872957  41 F6 C1 02                     test r9b, 2
0087295B  74 1C                           je 0x140872979
0087295D  4D 85 E4                        test r12, r12
00872960  74 17                           je 0x140872979
00872962  41 0F B6 44 24 01               movzx eax, byte ptr [r12 + 1]
00872968  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
0087296F  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00872973  03 F8                           add edi, eax
00872975  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00872979  41 F6 C1 04                     test r9b, 4
0087297D  0F 84 FC 01 00 00               je 0x140872b7f
00872983  41 0F B6 C6                     movzx eax, r14b
00872987  66 89 84 24 C8 00 00 00         mov word ptr [rsp + 0xc8], ax
0087298F  A8 04                           test al, 4
00872991  74 1D                           je 0x1408729b0
00872993  48 85 DB                        test rbx, rbx
00872996  74 18                           je 0x1408729b0
00872998  44 0F B7 7B 02                  movzx r15d, word ptr [rbx + 2]
0087299D  41 83 C7 03                     add r15d, 3
008729A1  B9 FC FF FF FF                  mov ecx, 0xfffffffc
008729A6  44 23 F9                        and r15d, ecx
008729A9  41 03 FF                        add edi, r15d
008729AC  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
008729B0  41 81 E1 F8 03 00 00            and r9d, 0x3f8
008729B7  74 08                           je 0x1408729c1
008729B9  A8 10                           test al, 0x10
008729BB  0F 85 CF 01 00 00               jne 0x140872b90
008729C1  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
008729C9  89 38                           mov dword ptr [rax], edi
008729CB  3B 7C 24 40                     cmp edi, dword ptr [rsp + 0x40]
008729CF  0F 87 ED 01 00 00               ja 0x140872bc2
008729D5  0F 57 C0                        xorps xmm0, xmm0
008729D8  33 C0                           xor eax, eax
008729DA  0F 11 06                        movups xmmword ptr [rsi], xmm0
008729DD  89 46 10                        mov dword ptr [rsi + 0x10], eax
008729E0  C6 06 01                        mov byte ptr [rsi], 1
008729E3  B9 00 80 00 00                  mov ecx, 0x8000
008729E8  66 0B 4E 02                     or cx, word ptr [rsi + 2]
008729EC  66 89 4E 02                     mov word ptr [rsi + 2], cx
008729F0  48 8D 7E 17                     lea rdi, [rsi + 0x17]
008729F4  48 83 E7 FC                     and rdi, 0xfffffffffffffffc
008729F8  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008729FD  41 8B 00                        mov eax, dword ptr [r8]
00872A00  A8 01                           test al, 1
00872A02  0F 84 C4 01 00 00               je 0x140872bcc
00872A08  4D 85 D2                        test r10, r10
00872A0B  0F 84 BB 01 00 00               je 0x140872bcc
00872A11  45 8B C5                        mov r8d, r13d
00872A14  49 8B D2                        mov rdx, r10
00872A17  48 8B CF                        mov rcx, rdi
00872A1A  E8 21 3E E5 FF                  call 0x1406c6840
00872A1F  8B C7                           mov eax, edi
00872A21  2B C6                           sub eax, esi
00872A23  89 46 04                        mov dword ptr [rsi + 4], eax
00872A26  41 0F B7 CE                     movzx ecx, r14w
00872A2A  66 83 E1 01                     and cx, 1
00872A2E  66 0B 4E 02                     or cx, word ptr [rsi + 2]
00872A32  66 89 4E 02                     mov word ptr [rsi + 2], cx
00872A36  41 8D 45 03                     lea eax, [r13 + 3]
00872A3A  41 BD FC FF FF FF               mov r13d, 0xfffffffc
00872A40  49 23 C5                        and rax, r13
00872A43  48 03 F8                        add rdi, rax
00872A46  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00872A4B  4C 8B 84 24 C0 00 00 00         mov r8, qword ptr [rsp + 0xc0]
00872A53  41 8B 00                        mov eax, dword ptr [r8]
00872A56  A8 02                           test al, 2
00872A58  74 46                           je 0x140872aa0
00872A5A  4D 85 E4                        test r12, r12
00872A5D  74 41                           je 0x140872aa0
00872A5F  44 8B 44 24 28                  mov r8d, dword ptr [rsp + 0x28]
00872A64  49 8B D4                        mov rdx, r12
00872A67  48 8B CF                        mov rcx, rdi
00872A6A  E8 D1 3D E5 FF                  call 0x1406c6840
00872A6F  8B C7                           mov eax, edi
00872A71  2B C6                           sub eax, esi
00872A73  89 46 08                        mov dword ptr [rsi + 8], eax
00872A76  41 0F B7 CE                     movzx ecx, r14w
00872A7A  66 83 E1 02                     and cx, 2
00872A7E  66 0B 4E 02                     or cx, word ptr [rsi + 2]
00872A82  66 89 4E 02                     mov word ptr [rsi + 2], cx
00872A86  8B 44 24 28                     mov eax, dword ptr [rsp + 0x28]
00872A8A  83 C0 03                        add eax, 3
00872A8D  49 23 C5                        and rax, r13
00872A90  48 03 F8                        add rdi, rax
00872A93  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00872A98  4C 8B 84 24 C0 00 00 00         mov r8, qword ptr [rsp + 0xc0]
00872AA0  41 8B 00                        mov eax, dword ptr [r8]
00872AA3  44 0F B7 A4 24 C8 00 00 00      movzx r12d, word ptr [rsp + 0xc8]
00872AAC  A8 04                           test al, 4
00872AAE  74 48                           je 0x140872af8
00872AB0  41 0F B7 C6                     movzx eax, r14w
00872AB4  BA 0C 14 00 00                  mov edx, 0x140c
00872AB9  66 23 C2                        and ax, dx
00872ABC  66 0B C1                        or ax, cx
00872ABF  66 89 46 02                     mov word ptr [rsi + 2], ax
00872AC3  41 F6 C4 04                     test r12b, 4
00872AC7  74 2F                           je 0x140872af8
00872AC9  48 85 DB                        test rbx, rbx
00872ACC  74 2A                           je 0x140872af8
00872ACE  44 0F B7 43 02                  movzx r8d, word ptr [rbx + 2]
00872AD3  48 8B D3                        mov rdx, rbx
00872AD6  48 8B CF                        mov rcx, rdi
00872AD9  E8 62 3D E5 FF                  call 0x1406c6840
00872ADE  8B C7                           mov eax, edi
00872AE0  2B C6                           sub eax, esi
00872AE2  89 46 10                        mov dword ptr [rsi + 0x10], eax
00872AE5  41 8B C7                        mov eax, r15d
00872AE8  48 03 F8                        add rdi, rax
00872AEB  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00872AF0  4C 8B 84 24 C0 00 00 00         mov r8, qword ptr [rsp + 0xc0]
00872AF8  41 F7 00 F8 03 00 00            test dword ptr [r8], 0x3f8
00872AFF  0F 84 85 01 00 00               je 0x140872c8a
00872B05  B8 30 28 00 00                  mov eax, 0x2830
00872B0A  66 44 23 F0                     and r14w, ax
00872B0E  66 44 09 76 02                  or word ptr [rsi + 2], r14w
00872B13  41 F6 C4 10                     test r12b, 0x10
00872B17  0F 84 6D 01 00 00               je 0x140872c8a
00872B1D  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00872B22  48 85 C0                        test rax, rax
00872B25  0F 84 5F 01 00 00               je 0x140872c8a
00872B2B  45 8B 08                        mov r9d, dword ptr [r8]
00872B2E  41 81 E1 F8 03 00 00            and r9d, 0x3f8
00872B35  4C 8D 44 24 24                  lea r8, [rsp + 0x24]
00872B3A  48 8B D7                        mov rdx, rdi
00872B3D  48 8B C8                        mov rcx, rax
00872B40  E8 8B 06 00 00                  call 0x1408731d0
00872B45  8B C7                           mov eax, edi
00872B47  2B C6                           sub eax, esi
00872B49  89 46 0C                        mov dword ptr [rsi + 0xc], eax
00872B4C  8B 44 24 24                     mov eax, dword ptr [rsp + 0x24]
00872B50  48 03 F8                        add rdi, rax
00872B53  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00872B58  E9 2D 01 00 00                  jmp 0x140872c8a
00872B5D  66 85 C9                        test cx, cx
00872B60  0F 89 98 00 00 00               jns 0x140872bfe
00872B66  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00872B69  85 C9                           test ecx, ecx
00872B6B  0F 84 80 00 00 00               je 0x140872bf1
00872B71  4C 8D 1C 08                     lea r11, [rax + rcx]
00872B75  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
00872B7A  E9 72 FD FF FF                  jmp 0x1408728f1
00872B7F  41 0F B7 C6                     movzx eax, r14w
00872B83  66 89 84 24 C8 00 00 00         mov word ptr [rsp + 0xc8], ax
00872B8B  E9 20 FE FF FF                  jmp 0x1408729b0
00872B90  4D 85 DB                        test r11, r11
00872B93  0F 84 28 FE FF FF               je 0x1408729c1
00872B99  4C 8D 44 24 24                  lea r8, [rsp + 0x24]
00872B9E  33 D2                           xor edx, edx
00872BA0  49 8B CB                        mov rcx, r11
00872BA3  E8 28 06 00 00                  call 0x1408731d0
00872BA8  03 7C 24 24                     add edi, dword ptr [rsp + 0x24]
00872BAC  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00872BB0  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
00872BB5  4C 8B 84 24 C0 00 00 00         mov r8, qword ptr [rsp + 0xc0]
00872BBD  E9 FF FD FF FF                  jmp 0x1408729c1
00872BC2  B8 23 00 00 C0                  mov eax, 0xc0000023
00872BC7  E9 C4 00 00 00                  jmp 0x140872c90
00872BCC  41 BD FC FF FF FF               mov r13d, 0xfffffffc
00872BD2  E9 7C FE FF FF                  jmp 0x140872a53
00872BD7  49 8B DD                        mov rbx, r13
00872BDA  E9 FC FC FF FF                  jmp 0x1408728db
00872BDF  4C 8B 60 10                     mov r12, qword ptr [rax + 0x10]
00872BE3  E9 CD FC FF FF                  jmp 0x1408728b5
00872BE8  4C 8B 50 08                     mov r10, qword ptr [rax + 8]
00872BEC  E9 A2 FC FF FF                  jmp 0x140872893
00872BF1  4D 8B DD                        mov r11, r13
00872BF4  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
00872BF9  E9 F3 FC FF FF                  jmp 0x1408728f1
00872BFE  4C 8B 58 18                     mov r11, qword ptr [rax + 0x18]
00872C02  E9 6E FF FF FF                  jmp 0x140872b75
00872C07  49 8B DD                        mov rbx, r13
00872C0A  E9 CC FC FF FF                  jmp 0x1408728db
00872C0F  41 81 C9 FF 01 00 00            or r9d, 0x1ff
00872C16  45 89 08                        mov dword ptr [r8], r9d
00872C19  85 C0                           test eax, eax
00872C1B  74 63                           je 0x140872c80
00872C1D  85 C9                           test ecx, ecx
00872C1F  0F 85 11 FD FF FF               jne 0x140872936
00872C25  41 0F BA F1 08                  btr r9d, 8
00872C2A  45 89 08                        mov dword ptr [r8], r9d
00872C2D  E9 04 FD FF FF                  jmp 0x140872936
00872C32  48 8B 58 20                     mov rbx, qword ptr [rax + 0x20]
00872C36  E9 A0 FC FF FF                  jmp 0x1408728db
00872C3B  4D 8B E5                        mov r12, r13
00872C3E  E9 72 FC FF FF                  jmp 0x1408728b5
00872C43  4D 8B D5                        mov r10, r13
00872C46  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
00872C4B  E9 48 FC FF FF                  jmp 0x140872898
00872C50  BF 14 00 00 00                  mov edi, 0x14
00872C55  41 89 3A                        mov dword ptr [r10], edi
00872C58  3B CF                           cmp ecx, edi
00872C5A  73 07                           jae 0x140872c63
00872C5C  B8 23 00 00 C0                  mov eax, 0xc0000023
00872C61  EB 2D                           jmp 0x140872c90
00872C63  0F 57 C0                        xorps xmm0, xmm0
00872C66  33 C0                           xor eax, eax
00872C68  0F 11 02                        movups xmmword ptr [rdx], xmm0
00872C6B  89 42 10                        mov dword ptr [rdx + 0x10], eax
00872C6E  C6 02 01                        mov byte ptr [rdx], 1
00872C71  B9 00 80 00 00                  mov ecx, 0x8000
00872C76  66 0B 4A 02                     or cx, word ptr [rdx + 2]
00872C7A  66 89 4A 02                     mov word ptr [rdx + 2], cx
00872C7E  EB 10                           jmp 0x140872c90
00872C80  41 0F BA F1 07                  btr r9d, 7
00872C85  45 89 08                        mov dword ptr [r8], r9d
00872C88  EB 93                           jmp 0x140872c1d
00872C8A  EB 02                           jmp 0x140872c8e
00872C8C  EB 02                           jmp 0x140872c90
00872C8E  33 C0                           xor eax, eax
00872C90  48 81 C4 80 00 00 00            add rsp, 0x80
00872C97  41 5F                           pop r15
00872C99  41 5E                           pop r14
00872C9B  41 5D                           pop r13
00872C9D  41 5C                           pop r12
00872C9F  5F                              pop rdi
00872CA0  5E                              pop rsi
00872CA1  5B                              pop rbx
00872CA2  C3                              ret
00872CA3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeQuerySecurityDescriptorInfo(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int16 v_stack_m66;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned __int16 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (128);
    v_r13 = 0;
    v_stack_m90 = 0;
    v_stack_m94 = 0;
    v_stack_m78 = (unsigned int)((unsigned int)(*(unsigned int *)(a3)));
    if (*(unsigned __int64 *)(a4) == 0) goto loc_00872C50;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 16)));
    if (!sign_flag) goto loc_00872BE8;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 4))) == 0) goto loc_00872C43;
loc_00872893:
    v_stack_m70 = *(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 4)) * 1;
loc_00872898:
    v_stack_m60 = *(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 4)) * 1;
    if (!sign_flag) goto loc_00872BDF;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 8))) == 0) goto loc_00872C3B;
loc_008728B5:
    v_stack_m58 = *(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 8)) * 1;
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4) + 2))) & (4)) == 0) goto loc_00872BD7;
    if (!sign_flag) goto loc_00872C32;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 16))) == 0) goto loc_00872C07;
loc_008728DB:
    v_stack_m48 = *(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 16)) * 1;
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4) + 2))) & (16)) != 0) goto loc_00872B5D;
    v_stack_m88 = 0;
loc_008728F1:
    v_stack_m50 = 0;
    v_r14 = (v_stack_m68) >> (16);
    v_r14 = (unsigned __int16)((v_r14) & ((unsigned __int16)((unsigned int)(0x7FFFULL))));
    v_stack_m66 = (unsigned __int16)(v_r14);
    v_stack_m98 = 20;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) & (128));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) & (256));
    if (condition_is_below) goto loc_00872C0F;
loc_00872936:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (1)) == 0) goto loc_00872957;
    v_rdi = 20;
    if (*(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 4)) * 1 != 0) {
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 4)) * 1 + 1);
        result = result * 4 + 8;
        v_r13 = (unsigned int)(result);
        v_rdi = result + 20;
        v_stack_m98 = (unsigned int)(v_rdi);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (2)) == 0) goto loc_00872979;
    if (*(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 8)) * 1 != 0) {
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 8)) * 1 + 1);
        result = result * 4 + 8;
        v_stack_m90 = (unsigned int)(result);
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(result)));
        v_stack_m98 = (unsigned int)(v_rdi);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (4)) == 0) goto loc_00872B7F;
    v_stack_p10 = (unsigned __int16)((unsigned __int8)(v_r14));
    if ((((unsigned __int8)((unsigned __int8)(v_r14))) & (4)) == 0) goto loc_008729B0;
    v_r15 = 0;
    if (*(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 16)) * 1 != 0) {
        v_r15 = *(unsigned __int16 *)(*(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 16)) * 1 + 2);
        v_r15 = (unsigned int)((v_r15) + (3));
        a1 = 0xFFFFFFFCULL;
        v_r15 = (unsigned int)((v_r15) & ((unsigned int)(a1)));
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_r15)));
        v_stack_m98 = (unsigned int)(v_rdi);
    }
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) & (0x3F8ULL));
    if (condition_is_equal) goto loc_008729C1;
    if ((((unsigned __int8)((unsigned __int8)(v_r14))) & (16)) != 0) goto loc_00872B90;
loc_008729C1:
    *(unsigned int *)(v_stack_p18) = (unsigned int)(v_rdi);
    if (((unsigned int)(v_rdi)) > v_stack_m78) goto loc_00872BC2;
    result = 0;
    *(unsigned __int64 *)(a2) = v_xmm0;
    *(unsigned int *)(a2 + 16) = 0;
    *(unsigned __int8 *)(a2) = 1;
    a1 = (unsigned __int16)(((unsigned int)(0x8000ULL)) | (*(unsigned __int16 *)(a2 + 2)));
    *(unsigned __int16 *)(a2 + 2) = (unsigned __int16)(a1);
    v_rdi = (a2 + 23) & (-4);
    v_stack_m80 = v_rdi;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (1)) == 0) goto loc_00872BCC;
    if (*(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 4)) * 1 == 0) goto loc_00872BCC;
    result = memcpy(v_rdi, *(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 4)) * 1, (unsigned int)((unsigned int)(v_r13)), a4);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - ((unsigned int)(a2)));
    *(unsigned int *)(a2 + 4) = (unsigned int)(result);
    a1 = (unsigned __int16)(((unsigned __int16)(v_r14)) & (1));
    a1 = (unsigned __int16)((a1) | (*(unsigned __int16 *)(a2 + 2)));
    *(unsigned __int16 *)(a2 + 2) = (unsigned __int16)(a1);
    result = (v_r13 + 3) & ((unsigned int)(0xFFFFFFFCULL));
    v_rdi = (v_rdi) + (result);
    v_stack_m80 = v_rdi;
loc_00872A53:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8)))) & (2)) == 0) goto loc_00872AA0;
    result = (unsigned int)(*(unsigned int *)(v_stack_p8));
    if (*(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 8)) * 1 != 0) {
        a3 = v_stack_m90;
        a2 = *(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 8)) * 1;
        a1 = v_rdi;
        result = memcpy(a1, a2, a3, a4);
        result = (unsigned int)(v_rdi);
        result = (unsigned int)((result) - ((unsigned int)(a2)));
        *(unsigned int *)(a2 + 8) = (unsigned int)(result);
        a1 = (unsigned __int16)(v_r14);
        a1 = (unsigned __int16)((a1) & (2));
        a1 = (unsigned __int16)((a1) | (*(unsigned __int16 *)(a2 + 2)));
        *(unsigned __int16 *)(a2 + 2) = (unsigned __int16)(a1);
        result = v_stack_m90;
        result = (unsigned int)((result) + (3));
        result = (result) & ((unsigned int)(0xFFFFFFFCULL));
        v_rdi = (v_rdi) + (result);
        v_stack_m80 = v_rdi;
        a3 = v_stack_p8;
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3)))) & (4)) == 0) goto loc_00872AF8;
    result = (unsigned __int16)(((unsigned __int16)(v_r14)) & ((unsigned __int16)((unsigned int)(0x140CULL))));
    result = (unsigned __int16)((result) | ((unsigned __int16)(a1)));
    *(unsigned __int16 *)(a2 + 2) = (unsigned __int16)(result);
    if ((((unsigned __int8)(v_stack_p10)) & (4)) == 0) goto loc_00872AF8;
    if (*(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 16)) * 1 != 0) {
        a3 = *(unsigned __int16 *)(*(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 16)) * 1 + 2);
        a2 = *(unsigned __int64 *)(a4) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4) + 16)) * 1;
        a1 = v_rdi;
        result = memcpy(a1, a2, a3, a4);
        result = (unsigned int)(v_rdi);
        result = (unsigned int)((result) - ((unsigned int)(a2)));
        *(unsigned int *)(a2 + 16) = (unsigned int)(result);
        result = (unsigned int)(v_r15);
        v_rdi = (v_rdi) + (result);
        v_stack_m80 = v_rdi;
        a3 = v_stack_p8;
    }
    if (((*(unsigned int *)(a3)) & (0x3F8ULL)) == 0) goto loc_00872C8A;
    v_r14 = (unsigned __int16)((v_r14) & ((unsigned __int16)((unsigned int)(0x2830ULL))));
    if ((((unsigned __int8)(v_stack_p10)) & (16)) == 0) goto loc_00872C8A;
    if (v_stack_m88 == 0) goto loc_00872C8A;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3))) & (0x3F8ULL));
    result = RtlpFilterSacl(v_stack_m88, v_rdi, v_stack_m94, a4);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - ((unsigned int)(a2)));
    *(unsigned int *)(a2 + 12) = (unsigned int)(result);
    v_rdi = (v_rdi) + ((unsigned int)(v_stack_m94));
    v_stack_m80 = v_rdi;
    goto loc_00872C8A;
loc_00872B5D:
    if (!sign_flag) goto loc_00872BFE;
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_m94) + 12))) == 0) goto loc_00872BF1;
loc_00872B75:
    v_stack_m88 = (unsigned int)(v_stack_m94) + (unsigned int)(*(unsigned int *)((unsigned int)(v_stack_m94) + 12)) * 1;
    goto loc_008728F1;
loc_00872B7F:
    v_stack_p10 = (unsigned __int16)((unsigned __int16)(v_r14));
    goto loc_008729B0;
loc_00872B90:
    if ((unsigned int)(v_stack_m94) + (unsigned int)(*(unsigned int *)((unsigned int)(v_stack_m94) + 12)) * 1 == 0) goto loc_008729C1;
    a2 = 0;
    result = RtlpFilterSacl((unsigned int)(v_stack_m94) + (unsigned int)(*(unsigned int *)((unsigned int)(v_stack_m94) + 12)) * 1, a2, v_stack_m94, a4);
    v_rdi = (unsigned int)((v_rdi) + (v_stack_m94));
    v_stack_m98 = (unsigned int)(v_rdi);
    goto loc_008729C1;
loc_00872BC2:
    goto loc_00872C90;
loc_00872BCC:
    goto loc_00872A53;
loc_00872BD7:
    goto loc_008728DB;
loc_00872BDF:
    goto loc_008728B5;
loc_00872BE8:
    goto loc_00872893;
loc_00872BF1:
    v_stack_m88 = (unsigned int)(0xFFFFFFFCULL);
    goto loc_008728F1;
loc_00872BFE:
    goto loc_00872B75;
loc_00872C07:
    goto loc_008728DB;
loc_00872C0F:
    a4 = (unsigned int)((a4) | (511));
    *(unsigned int *)(v_stack_p8) = (unsigned int)(a4);
    if ((unsigned int)((unsigned int)(0xC0000023ULL)) == 0) goto loc_00872C80;
loc_00872C1D:
    if ((unsigned int)((unsigned int)(v_stack_m94) + (unsigned int)(*(unsigned int *)((unsigned int)(v_stack_m94) + 12)) * 1) != 0) goto loc_00872936;
    *(unsigned int *)(v_stack_p8) = (unsigned int)(a4);
    goto loc_00872936;
loc_00872C32:
    goto loc_008728DB;
loc_00872C3B:
    goto loc_008728B5;
loc_00872C43:
    v_stack_m70 = (unsigned int)(0xFFFFFFFCULL);
    goto loc_00872898;
loc_00872C50:
    *(unsigned int *)((unsigned int)(0xFFFFFFFCULL)) = 20;
    if (((unsigned int)((unsigned int)(v_stack_m94) + (unsigned int)(*(unsigned int *)((unsigned int)(v_stack_m94) + 12)) * 1)) >= 20) goto loc_00872C63;
    goto loc_00872C90;
loc_00872C63:
    result = 0;
    *(unsigned __int64 *)(a2) = v_xmm0;
    *(unsigned int *)(a2 + 16) = 0;
    *(unsigned __int8 *)(a2) = 1;
    a1 = (unsigned __int16)(((unsigned int)(0x8000ULL)) | (*(unsigned __int16 *)(a2 + 2)));
    *(unsigned __int16 *)(a2 + 2) = (unsigned __int16)(a1);
    goto loc_00872C90;
loc_00872C80:
    *(unsigned int *)(v_stack_p8) = (unsigned int)(a4);
    goto loc_00872C1D;
loc_00872C8A:
    goto loc_00872C8E;
loc_00872C8E:
    result = 0;
loc_00872C90:
    v_rsp = (v_rsp) + (128);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SeQuerySecurityDescriptorInfo(void *Arg1, void *Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint16_t v_stack_m66;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint16_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (128);
    local_r13 = 0;
    v_stack_m90 = 0;
    v_stack_m94 = 0;
    v_stack_m78 = (uint32_t)((uint32_t)(*(uint32_t *)(arg3)));
    if (*(uint64_t *)(arg4) == 0) goto loc_00872C50;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x10)));
    if (!sign_flag) goto loc_00872BE8;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x4))) == 0) goto loc_00872C43;
loc_00872893:
    v_stack_m70 = *(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x4)) * 1;
loc_00872898:
    v_stack_m60 = *(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x4)) * 1;
    if (!sign_flag) goto loc_00872BDF;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x8))) == 0) goto loc_00872C3B;
loc_008728B5:
    v_stack_m58 = *(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x8)) * 1;
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(arg4) + 0x2))) & (4)) == 0) goto loc_00872BD7;
    if (!sign_flag) goto loc_00872C32;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x10))) == 0) goto loc_00872C07;
loc_008728DB:
    v_stack_m48 = *(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x10)) * 1;
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(arg4) + 0x2))) & (16)) != 0) goto loc_00872B5D;
    v_stack_m88 = 0;
loc_008728F1:
    v_stack_m50 = 0;
    local_r14 = (v_stack_m68) >> (16);
    local_r14 = (uint16_t)((local_r14) & ((uint16_t)((uint32_t)(0x7FFFULL))));
    v_stack_m66 = (uint16_t)(local_r14);
    v_stack_m98 = 20;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) & (128));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) & (256));
    if (condition_is_below) goto loc_00872C0F;
loc_00872936:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (1)) == 0) goto loc_00872957;
    local_rdi = 20;
    if (*(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x4)) * 1 != 0) {
        result = *(uint8_t *)(*(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x4)) * 1 + 0x1);
        result = result * 4 + 8;
        local_r13 = (uint32_t)(result);
        local_rdi = result + 20;
        v_stack_m98 = (uint32_t)(local_rdi);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (2)) == 0) goto loc_00872979;
    if (*(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x8)) * 1 != 0) {
        result = *(uint8_t *)(*(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x8)) * 1 + 0x1);
        result = result * 4 + 8;
        v_stack_m90 = (uint32_t)(result);
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(result)));
        v_stack_m98 = (uint32_t)(local_rdi);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (4)) == 0) goto loc_00872B7F;
    v_stack_p10 = (uint16_t)((uint8_t)(local_r14));
    if ((((uint8_t)((uint8_t)(local_r14))) & (4)) == 0) goto loc_008729B0;
    local_r15 = 0;
    if (*(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x10)) * 1 != 0) {
        local_r15 = *(uint16_t *)(*(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x10)) * 1 + 0x2);
        local_r15 = (uint32_t)((local_r15) + (3));
        Arg1 = 0xFFFFFFFCULL;
        local_r15 = (uint32_t)((local_r15) & ((uint32_t)(Arg1)));
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_r15)));
        v_stack_m98 = (uint32_t)(local_rdi);
    }
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) & (0x3F8ULL));
    if (condition_is_equal) goto loc_008729C1;
    if ((((uint8_t)((uint8_t)(local_r14))) & (16)) != 0) goto loc_00872B90;
loc_008729C1:
    *(uint32_t *)(v_stack_p18) = (uint32_t)(local_rdi);
    if (((uint32_t)(local_rdi)) > v_stack_m78) goto loc_00872BC2;
    result = 0;
    *(uint64_t *)(arg2) = v_xmm0;
    *(uint32_t *)(arg2 + 0x10) = 0;
    *(uint8_t *)(arg2) = 1;
    Arg1 = (uint16_t)(((uint32_t)(0x8000ULL)) | (*(uint16_t *)(arg2 + 0x2)));
    *(uint16_t *)(arg2 + 0x2) = (uint16_t)(Arg1);
    local_rdi = (Arg2 + 23) & (-4);
    v_stack_m80 = local_rdi;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (1)) == 0) goto loc_00872BCC;
    if (*(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x4)) * 1 == 0) goto loc_00872BCC;
    result = memcpy(local_rdi, *(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x4)) * 1, (uint32_t)((uint32_t)(local_r13)), Arg4);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - ((uint32_t)(Arg2)));
    *(uint32_t *)(arg2 + 0x4) = (uint32_t)(result);
    Arg1 = (uint16_t)(((uint16_t)(local_r14)) & (1));
    Arg1 = (uint16_t)((Arg1) | (*(uint16_t *)(arg2 + 0x2)));
    *(uint16_t *)(arg2 + 0x2) = (uint16_t)(Arg1);
    result = (local_r13 + 3) & ((uint32_t)(0xFFFFFFFCULL));
    local_rdi = (local_rdi) + (result);
    v_stack_m80 = local_rdi;
loc_00872A53:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8)))) & (2)) == 0) goto loc_00872AA0;
    result = (uint32_t)(*(uint32_t *)(v_stack_p8));
    if (*(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x8)) * 1 != 0) {
        Arg3 = v_stack_m90;
        Arg2 = *(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x8)) * 1;
        Arg1 = local_rdi;
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
        result = (uint32_t)(local_rdi);
        result = (uint32_t)((result) - ((uint32_t)(Arg2)));
        *(uint32_t *)(arg2 + 0x8) = (uint32_t)(result);
        Arg1 = (uint16_t)(local_r14);
        Arg1 = (uint16_t)((Arg1) & (2));
        Arg1 = (uint16_t)((Arg1) | (*(uint16_t *)(arg2 + 0x2)));
        *(uint16_t *)(arg2 + 0x2) = (uint16_t)(Arg1);
        result = v_stack_m90;
        result = (uint32_t)((result) + (3));
        result = (result) & ((uint32_t)(0xFFFFFFFCULL));
        local_rdi = (local_rdi) + (result);
        v_stack_m80 = local_rdi;
        Arg3 = v_stack_p8;
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3)))) & (4)) == 0) goto loc_00872AF8;
    result = (uint16_t)(((uint16_t)(local_r14)) & ((uint16_t)((uint32_t)(0x140CULL))));
    result = (uint16_t)((result) | ((uint16_t)(Arg1)));
    *(uint16_t *)(arg2 + 0x2) = (uint16_t)(result);
    if ((((uint8_t)(v_stack_p10)) & (4)) == 0) goto loc_00872AF8;
    if (*(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x10)) * 1 != 0) {
        Arg3 = *(uint16_t *)(*(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x10)) * 1 + 0x2);
        Arg2 = *(uint64_t *)(arg4) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4) + 0x10)) * 1;
        Arg1 = local_rdi;
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
        result = (uint32_t)(local_rdi);
        result = (uint32_t)((result) - ((uint32_t)(Arg2)));
        *(uint32_t *)(arg2 + 0x10) = (uint32_t)(result);
        result = (uint32_t)(local_r15);
        local_rdi = (local_rdi) + (result);
        v_stack_m80 = local_rdi;
        Arg3 = v_stack_p8;
    }
    if (((*(uint32_t *)(arg3)) & (0x3F8ULL)) == 0) goto loc_00872C8A;
    local_r14 = (uint16_t)((local_r14) & ((uint16_t)((uint32_t)(0x2830ULL))));
    if ((((uint8_t)(v_stack_p10)) & (16)) == 0) goto loc_00872C8A;
    if (v_stack_m88 == 0) goto loc_00872C8A;
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg3))) & (0x3F8ULL));
    result = RtlpFilterSacl(v_stack_m88, local_rdi, v_stack_m94, Arg4);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - ((uint32_t)(Arg2)));
    *(uint32_t *)(arg2 + 0xC) = (uint32_t)(result);
    local_rdi = (local_rdi) + ((uint32_t)(v_stack_m94));
    v_stack_m80 = local_rdi;
    goto loc_00872C8A;
loc_00872B5D:
    if (!sign_flag) goto loc_00872BFE;
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_m94) + 0xC))) == 0) goto loc_00872BF1;
loc_00872B75:
    v_stack_m88 = (uint32_t)(v_stack_m94) + (uint32_t)(*(uint32_t *)((uint32_t)(v_stack_m94) + 0xC)) * 1;
    goto loc_008728F1;
loc_00872B7F:
    v_stack_p10 = (uint16_t)((uint16_t)(local_r14));
    goto loc_008729B0;
loc_00872B90:
    if ((uint32_t)(v_stack_m94) + (uint32_t)(*(uint32_t *)((uint32_t)(v_stack_m94) + 0xC)) * 1 == 0) goto loc_008729C1;
    Arg2 = 0;
    result = RtlpFilterSacl((uint32_t)(v_stack_m94) + (uint32_t)(*(uint32_t *)((uint32_t)(v_stack_m94) + 0xC)) * 1, Arg2, v_stack_m94, Arg4);
    local_rdi = (uint32_t)((local_rdi) + (v_stack_m94));
    v_stack_m98 = (uint32_t)(local_rdi);
    goto loc_008729C1;
loc_00872BC2:
    goto loc_00872C90;
loc_00872BCC:
    goto loc_00872A53;
loc_00872BD7:
    goto loc_008728DB;
loc_00872BDF:
    goto loc_008728B5;
loc_00872BE8:
    goto loc_00872893;
loc_00872BF1:
    v_stack_m88 = (uint32_t)(0xFFFFFFFCULL);
    goto loc_008728F1;
loc_00872BFE:
    goto loc_00872B75;
loc_00872C07:
    goto loc_008728DB;
loc_00872C0F:
    Arg4 = (uint32_t)((Arg4) | (511));
    *(uint32_t *)(v_stack_p8) = (uint32_t)(Arg4);
    if ((uint32_t)((uint32_t)(0xC0000023ULL)) == 0) goto loc_00872C80;
loc_00872C1D:
    if ((uint32_t)((uint32_t)(v_stack_m94) + (uint32_t)(*(uint32_t *)((uint32_t)(v_stack_m94) + 0xC)) * 1) != 0) goto loc_00872936;
    *(uint32_t *)(v_stack_p8) = (uint32_t)(Arg4);
    goto loc_00872936;
loc_00872C32:
    goto loc_008728DB;
loc_00872C3B:
    goto loc_008728B5;
loc_00872C43:
    v_stack_m70 = (uint32_t)(0xFFFFFFFCULL);
    goto loc_00872898;
loc_00872C50:
    *(uint32_t *)((uint32_t)(0xFFFFFFFCULL)) = 20;
    if (((uint32_t)((uint32_t)(v_stack_m94) + (uint32_t)(*(uint32_t *)((uint32_t)(v_stack_m94) + 0xC)) * 1)) >= 20) goto loc_00872C63;
    goto loc_00872C90;
loc_00872C63:
    result = 0;
    *(uint64_t *)(arg2) = v_xmm0;
    *(uint32_t *)(arg2 + 0x10) = 0;
    *(uint8_t *)(arg2) = 1;
    Arg1 = (uint16_t)(((uint32_t)(0x8000ULL)) | (*(uint16_t *)(arg2 + 0x2)));
    *(uint16_t *)(arg2 + 0x2) = (uint16_t)(Arg1);
    goto loc_00872C90;
loc_00872C80:
    *(uint32_t *)(v_stack_p8) = (uint32_t)(Arg4);
    goto loc_00872C1D;
loc_00872C8A:
    goto loc_00872C8E;
loc_00872C8E:
    result = 0;
loc_00872C90:
    local_rsp = (local_rsp) + (128);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x0` | `8` | `W` |
| `Arg2` | `+ 0x0` | `128` | `R` |
| `Arg2` | `+ 0x2` | `16` | `R` |
| `Arg2` | `+ 0x2` | `16` | `R/W` |
| `Arg2` | `+ 0x2` | `16` | `W` |
| `Arg2` | `+ 0x4` | `32` | `W` |
| `Arg2` | `+ 0x8` | `32` | `W` |
| `Arg2` | `+ 0xC` | `32` | `W` |
| `Arg2` | `+ 0x10` | `32` | `W` |
| `Arg2` | `+ 0x17` | `64` | `R` |
| `Arg3` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x0` | `32` | `W` |
| `Arg4` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00872820&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
