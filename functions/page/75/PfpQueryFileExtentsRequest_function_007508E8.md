# PfpQueryFileExtentsRequest

- RVA: `0x007508E8`–`0x00750F97` (길이 `1,711` bytes)
- VA: `0x00000001407508E8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CB914`
- 디코드: `386`개 명령, `1,711/1,711` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007509C9` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00750A5F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00750A91` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00750AEA` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00750B2C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00750B45` → [PfpPrefetchSharedInitialize](../93/PfpPrefetchSharedInitialize_function_00939E30.md) (function, `0x00939E30`)
- `0x00750B5B` → [PfpPrefetchSharedStart](../93/PfpPrefetchSharedStart_function_00939D24.md) (function, `0x00939D24`)
- `0x00750B7A` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x00750BBB` → [PfpOpenHandleCreate](../8A/PfpOpenHandleCreate_function_008A9EDC.md) (function, `0x008A9EDC`)
- `0x00750BDC` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x00750C23` → [PfpOpenHandleCreate](../8A/PfpOpenHandleCreate_function_008A9EDC.md) (function, `0x008A9EDC`)
- `0x00750C56` → [ZwQueryVolumeInformationFile](../../text/6A/ZwQueryVolumeInformationFile_function_006AD9F0.md) (function, `0x006AD9F0`)
- `0x00750C79` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00750CC7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00750CDA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00750D34` → [ZwFsControlFile](../../text/6A/ZwFsControlFile_function_006AD7F0.md) (function, `0x006AD7F0`)
- `0x00750D57` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00750DA9` → [ZwQueryInformationFile](../../text/6A/ZwQueryInformationFile_function_006AD2F0.md) (function, `0x006AD2F0`)
- `0x00750DCC` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00750E5D` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00750E70` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00750F0B` → [PfpOpenHandleClose](../8A/PfpOpenHandleClose_function_008A9E74.md) (function, `0x008A9E74`)
- `0x00750F25` → [PfpOpenHandleClose](../8A/PfpOpenHandleClose_function_008A9E74.md) (function, `0x008A9E74`)
- `0x00750F32` → [PfpPrefetchSharedCleanup](../93/PfpPrefetchSharedCleanup_function_00939EB0.md) (function, `0x00939EB0`)
- `0x00750F3A` → [PfpPrefetchSharedDeref](../93/PfpPrefetchSharedDeref_function_00939E78.md) (function, `0x00939E78`)
- `0x00750F49` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00750F58` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00750F6A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PfQuerySuperfetchInformation](../90/PfQuerySuperfetchInformation_function_0090210C.md) at `0x00902453`

### Static image references
- `0x0075090D` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x00750A5F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00750AEA` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00750B2C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00750B7A` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x00750BDC` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x00750C56` → [ZwQueryVolumeInformationFile](../../text/6A/ZwQueryVolumeInformationFile_function_006AD9F0.md) (`PAGE` → `.text`)
  - `0x00750C79` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00750CC7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00750CDA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00750D34` → [ZwFsControlFile](../../text/6A/ZwFsControlFile_function_006AD7F0.md) (`PAGE` → `.text`)
  - `0x00750D57` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00750DA9` → [ZwQueryInformationFile](../../text/6A/ZwQueryInformationFile_function_006AD2F0.md) (`PAGE` → `.text`)
  - `0x00750DCC` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00750E70` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00750F49` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00750F58` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00750F6A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007508E8  4C 8B DC                        mov r11, rsp
007508EB  49 89 5B 10                     mov qword ptr [r11 + 0x10], rbx
007508EF  49 89 73 20                     mov qword ptr [r11 + 0x20], rsi
007508F3  57                              push rdi
007508F4  41 54                           push r12
007508F6  41 55                           push r13
007508F8  41 56                           push r14
007508FA  41 57                           push r15
007508FC  48 81 EC 70 01 00 00            sub rsp, 0x170
00750903  41 0F 29 73 C8                  movaps xmmword ptr [r11 - 0x38], xmm6
00750908  41 0F 29 7B B8                  movaps xmmword ptr [r11 - 0x48], xmm7
0075090D  48 8B 05 2C 9E 6B 00            mov rax, qword ptr [rip + 0x6b9e2c]
00750914  48 33 C4                        xor rax, rsp
00750917  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
0075091F  4C 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], r8
00750927  44 8A EA                        mov r13b, dl
0075092A  88 54 24 50                     mov byte ptr [rsp + 0x50], dl
0075092E  48 8B D9                        mov rbx, rcx
00750931  48 89 8C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rcx
00750939  0F 57 C0                        xorps xmm0, xmm0
0075093C  0F 11 84 24 90 00 00 00         movups xmmword ptr [rsp + 0x90], xmm0
00750944  33 FF                           xor edi, edi
00750946  49 89 BB 40 FF FF FF            mov qword ptr [r11 - 0xc0], rdi
0075094D  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00750952  33 C0                           xor eax, eax
00750954  41 0F 11 43 98                  movups xmmword ptr [r11 - 0x68], xmm0
00750959  49 89 43 A8                     mov qword ptr [r11 - 0x58], rax
0075095D  0F 11 84 24 80 00 00 00         movups xmmword ptr [rsp + 0x80], xmm0
00750965  44 8B F7                        mov r14d, edi
00750968  44 8B E7                        mov r12d, edi
0075096B  8B F7                           mov esi, edi
0075096D  49 89 BB 78 FF FF FF            mov qword ptr [r11 - 0x88], rdi
00750974  F3 41 0F 7F 43 80               movdqu xmmword ptr [r11 - 0x80], xmm0
0075097A  48 B8 00 00 00 00 02 00 00 00   movabs rax, 0x200000000
00750984  49 89 43 90                     mov qword ptr [r11 - 0x70], rax
00750988  49 89 BB 58 FF FF FF            mov qword ptr [r11 - 0xa8], rdi
0075098F  F3 0F 7F 84 24 F8 00 00 00      movdqu xmmword ptr [rsp + 0xf8], xmm0
00750998  49 89 83 70 FF FF FF            mov qword ptr [r11 - 0x90], rax
0075099F  C7 44 24 54 01 00 00 00         mov dword ptr [rsp + 0x54], 1
007509A7  83 79 18 38                     cmp dword ptr [rcx + 0x18], 0x38
007509AB  73 0A                           jae 0x1407509b7
007509AD  BB 06 02 00 C0                  mov ebx, 0xc0000206
007509B2  E9 1A 05 00 00                  jmp 0x140750ed1
007509B7  45 84 ED                        test r13b, r13b
007509BA  74 12                           je 0x1407509ce
007509BC  BA 38 00 00 00                  mov edx, 0x38
007509C1  44 8D 42 D0                     lea r8d, [rdx - 0x30]
007509C5  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
007509C9  E8 F2 87 19 00                  call 0x1408e91c0
007509CE  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
007509D2  0F 10 38                        movups xmm7, xmmword ptr [rax]
007509D5  0F 11 BC 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm7
007509DD  0F 10 70 10                     movups xmm6, xmmword ptr [rax + 0x10]
007509E1  0F 11 B4 24 B0 00 00 00         movups xmmword ptr [rsp + 0xb0], xmm6
007509E9  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
007509ED  0F 11 84 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm0
007509F5  F2 0F 10 48 30                  movsd xmm1, qword ptr [rax + 0x30]
007509FA  F2 0F 11 8C 24 D0 00 00 00      movsd qword ptr [rsp + 0xd0], xmm1
00750A03  66 0F 7E F8                     movd eax, xmm7
00750A07  83 F8 02                        cmp eax, 2
00750A0A  74 0A                           je 0x140750a16
00750A0C  BB 59 00 00 C0                  mov ebx, 0xc0000059
00750A11  E9 BB 04 00 00                  jmp 0x140750ed1
00750A16  66 0F 7E F3                     movd ebx, xmm6
00750A1A  F6 C3 01                        test bl, 1
00750A1D  0F 85 9B 04 00 00               jne 0x140750ebe
00750A23  8D 43 FF                        lea eax, [rbx - 1]
00750A26  3D FF FF 0F 00                  cmp eax, 0xfffff
00750A2B  0F 87 8D 04 00 00               ja 0x140750ebe
00750A31  66 48 0F 7E F0                  movq rax, xmm6
00750A36  48 C1 E8 20                     shr rax, 0x20
00750A3A  A8 01                           test al, 1
00750A3C  0F 85 7C 04 00 00               jne 0x140750ebe
00750A42  85 C0                           test eax, eax
00750A44  0F 84 74 04 00 00               je 0x140750ebe
00750A4A  3B C3                           cmp eax, ebx
00750A4C  0F 83 6C 04 00 00               jae 0x140750ebe
00750A52  41 B8 50 66 43 70               mov r8d, 0x70436650
00750A58  8B D3                           mov edx, ebx
00750A5A  B9 00 01 00 00                  mov ecx, 0x100
00750A5F  E8 8C 16 43 00                  call 0x140b820f0
00750A64  4C 8B F0                        mov r14, rax
00750A67  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00750A6C  48 85 C0                        test rax, rax
00750A6F  75 0A                           jne 0x140750a7b
00750A71  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00750A76  E9 56 04 00 00                  jmp 0x140750ed1
00750A7B  66 0F 6F C7                     movdqa xmm0, xmm7
00750A7F  66 0F 73 D8 08                  psrldq xmm0, 8
00750A84  45 84 ED                        test r13b, r13b
00750A87  74 56                           je 0x140750adf
00750A89  66 0F 7E C0                     movd eax, xmm0
00750A8D  A8 01                           test al, 1
00750A8F  74 05                           je 0x140750a96
00750A91  E8 3A 95 14 00                  call 0x140899fd0
00750A96  66 0F 6F C7                     movdqa xmm0, xmm7
00750A9A  66 0F 73 D8 08                  psrldq xmm0, 8
00750A9F  66 48 0F 7E C2                  movq rdx, xmm0
00750AA4  48 8D 04 13                     lea rax, [rbx + rdx]
00750AA8  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
00750AB2  48 3B C1                        cmp rax, rcx
00750AB5  77 05                           ja 0x140750abc
00750AB7  48 3B C2                        cmp rax, rdx
00750ABA  73 28                           jae 0x140750ae4
00750ABC  8A 01                           mov al, byte ptr [rcx]
00750ABE  8B 9C 24 B0 00 00 00            mov ebx, dword ptr [rsp + 0xb0]
00750AC5  0F 10 B4 24 B0 00 00 00         movups xmm6, xmmword ptr [rsp + 0xb0]
00750ACD  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
00750AD5  0F 10 BC 24 A0 00 00 00         movups xmm7, xmmword ptr [rsp + 0xa0]
00750ADD  EB 05                           jmp 0x140750ae4
00750ADF  66 48 0F 7E C2                  movq rdx, xmm0
00750AE4  44 8B C3                        mov r8d, ebx
00750AE7  49 8B CE                        mov rcx, r14
00750AEA  E8 51 5D F7 FF                  call 0x1406c6840
00750AEF  90                              nop
00750AF0  D1 EB                           shr ebx, 1
00750AF2  FF CB                           dec ebx
00750AF4  66 41 39 3C 5E                  cmp word ptr [r14 + rbx*2], di
00750AF9  0F 85 BF 03 00 00               jne 0x140750ebe
00750AFF  66 0F 6F C6                     movdqa xmm0, xmm6
00750B03  66 0F 73 D8 04                  psrldq xmm0, 4
00750B08  66 41 0F 7E C5                  movd r13d, xmm0
00750B0D  41 D1 ED                        shr r13d, 1
00750B10  B8 5C 00 00 00                  mov eax, 0x5c
00750B15  66 43 39 04 6E                  cmp word ptr [r14 + r13*2], ax
00750B1A  0F 85 9E 03 00 00               jne 0x140750ebe
00750B20  8D 50 34                        lea edx, [rax + 0x34]
00750B23  8D 48 E4                        lea ecx, [rax - 0x1c]
00750B26  41 B8 50 66 53 43               mov r8d, 0x43536650
00750B2C  E8 BF 15 43 00                  call 0x140b820f0
00750B31  48 8B F0                        mov rsi, rax
00750B34  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00750B39  48 85 C0                        test rax, rax
00750B3C  0F 84 2F FF FF FF               je 0x140750a71
00750B42  48 8B C8                        mov rcx, rax
00750B45  E8 E6 92 1E 00                  call 0x140939e30
00750B4A  C7 46 38 0F 00 00 00            mov dword ptr [rsi + 0x38], 0xf
00750B51  C7 46 3C 96 00 00 00            mov dword ptr [rsi + 0x3c], 0x96
00750B58  48 8B CE                        mov rcx, rsi
00750B5B  E8 C4 91 1E 00                  call 0x140939d24
00750B60  8B D8                           mov ebx, eax
00750B62  85 C0                           test eax, eax
00750B64  0F 88 67 03 00 00               js 0x140750ed1
00750B6A  66 43 89 3C 6E                  mov word ptr [r14 + r13*2], di
00750B6F  49 8B D6                        mov rdx, r14
00750B72  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
00750B7A  E8 E1 2D D1 FF                  call 0x140463960
00750B7F  8B D8                           mov ebx, eax
00750B81  85 C0                           test eax, eax
00750B83  0F 88 48 03 00 00               js 0x140750ed1
00750B89  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00750B8E  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00750B92  41 BF 20 00 00 00               mov r15d, 0x20
00750B98  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00750B9D  C7 44 24 20 80 01 10 00         mov dword ptr [rsp + 0x20], 0x100180
00750BA5  45 33 C9                        xor r9d, r9d
00750BA8  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
00750BB0  48 8B D6                        mov rdx, rsi
00750BB3  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
00750BBB  E8 1C 93 15 00                  call 0x1408a9edc
00750BC0  8B D8                           mov ebx, eax
00750BC2  85 C0                           test eax, eax
00750BC4  0F 88 07 03 00 00               js 0x140750ed1
00750BCA  66 43 C7 04 6E 5C 00            mov word ptr [r14 + r13*2], 0x5c
00750BD1  49 8B D6                        mov rdx, r14
00750BD4  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
00750BDC  E8 7F 2D D1 FF                  call 0x140463960
00750BE1  8B D8                           mov ebx, eax
00750BE3  85 C0                           test eax, eax
00750BE5  0F 88 E6 02 00 00               js 0x140750ed1
00750BEB  48 8D 84 24 10 01 00 00         lea rax, [rsp + 0x110]
00750BF3  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00750BF8  C7 44 24 30 80 00 00 00         mov dword ptr [rsp + 0x30], 0x80
00750C00  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00750C05  C7 44 24 20 80 00 10 00         mov dword ptr [rsp + 0x20], 0x100080
00750C0D  45 33 C9                        xor r9d, r9d
00750C10  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
00750C18  48 8B D6                        mov rdx, rsi
00750C1B  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
00750C23  E8 B4 92 15 00                  call 0x1408a9edc
00750C28  8B D8                           mov ebx, eax
00750C2A  85 C0                           test eax, eax
00750C2C  0F 88 9F 02 00 00               js 0x140750ed1
00750C32  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
00750C3A  45 8D 4F F8                     lea r9d, [r15 - 8]
00750C3E  4C 8D 84 24 30 01 00 00         lea r8, [rsp + 0x130]
00750C46  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
00750C4E  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
00750C56  E8 95 CD F5 FF                  call 0x1406ad9f0
00750C5B  8B D8                           mov ebx, eax
00750C5D  3D 03 01 00 00                  cmp eax, 0x103
00750C62  75 1B                           jne 0x140750c7f
00750C64  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00750C69  45 33 C9                        xor r9d, r9d
00750C6C  45 33 C0                        xor r8d, r8d
00750C6F  BA AE 10 00 00                  mov edx, 0x10ae
00750C74  B9 91 01 00 00                  mov ecx, 0x191
00750C79  E8 E2 C9 DA FF                  call 0x1404fd660
00750C7E  CC                              int3
00750C7F  B9 00 00 00 C0                  mov ecx, 0xc0000000
00750C84  23 C1                           and eax, ecx
00750C86  3B C1                           cmp eax, ecx
00750C88  0F 84 43 02 00 00               je 0x140750ed1
00750C8E  8B 84 24 38 01 00 00            mov eax, dword ptr [rsp + 0x138]
00750C95  89 84 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], eax
00750C9C  44 8B AC 24 D0 00 00 00         mov r13d, dword ptr [rsp + 0xd0]
00750CA4  44 89 6C 24 70                  mov dword ptr [rsp + 0x70], r13d
00750CA9  45 3B EF                        cmp r13d, r15d
00750CAC  45 0F 47 FD                     cmova r15d, r13d
00750CB0  41 81 FF 00 00 A0 00            cmp r15d, 0xa00000
00750CB7  0F 87 F0 FC FF FF               ja 0x1407509ad
00750CBD  4D 85 E4                        test r12, r12
00750CC0  74 0A                           je 0x140750ccc
00750CC2  33 D2                           xor edx, edx
00750CC4  49 8B CC                        mov rcx, r12
00750CC7  E8 A4 1B 43 00                  call 0x140b82870
00750CCC  41 8B D7                        mov edx, r15d
00750CCF  B9 00 01 00 00                  mov ecx, 0x100
00750CD4  41 B8 50 66 46 65               mov r8d, 0x65466650
00750CDA  E8 11 14 43 00                  call 0x140b820f0
00750CDF  4C 8B E0                        mov r12, rax
00750CE2  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00750CE7  48 85 C0                        test rax, rax
00750CEA  0F 84 81 FD FF FF               je 0x140750a71
00750CF0  44 89 7C 24 48                  mov dword ptr [rsp + 0x48], r15d
00750CF5  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00750CFA  C7 44 24 38 08 00 00 00         mov dword ptr [rsp + 0x38], 8
00750D02  48 8D 84 24 D8 00 00 00         lea rax, [rsp + 0xd8]
00750D0A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00750D0F  C7 44 24 28 73 00 09 00         mov dword ptr [rsp + 0x28], 0x90073
00750D17  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00750D1F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00750D24  45 33 C9                        xor r9d, r9d
00750D27  45 33 C0                        xor r8d, r8d
00750D2A  33 D2                           xor edx, edx
00750D2C  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00750D34  E8 B7 CA F5 FF                  call 0x1406ad7f0
00750D39  8B D8                           mov ebx, eax
00750D3B  3D 03 01 00 00                  cmp eax, 0x103
00750D40  75 1B                           jne 0x140750d5d
00750D42  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00750D47  45 33 C9                        xor r9d, r9d
00750D4A  45 33 C0                        xor r8d, r8d
00750D4D  BA EC 10 00 00                  mov edx, 0x10ec
00750D52  B9 91 01 00 00                  mov ecx, 0x191
00750D57  E8 04 C9 DA FF                  call 0x1404fd660
00750D5C  CC                              int3
00750D5D  85 C0                           test eax, eax
00750D5F  78 1A                           js 0x140750d7b
00750D61  4C 8B AC 24 98 00 00 00         mov r13, qword ptr [rsp + 0x98]
00750D69  44 89 AC 24 D0 00 00 00         mov dword ptr [rsp + 0xd0], r13d
00750D71  41 39 3C 24                     cmp dword ptr [r12], edi
00750D75  74 0F                           je 0x140750d86
00750D77  8B DF                           mov ebx, edi
00750D79  EB 79                           jmp 0x140750df4
00750D7B  3D 11 00 00 C0                  cmp eax, 0xc0000011
00750D80  0F 85 19 01 00 00               jne 0x140750e9f
00750D86  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
00750D8E  41 B9 08 00 00 00               mov r9d, 8
00750D94  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00750D99  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
00750DA1  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00750DA9  E8 42 C5 F5 FF                  call 0x1406ad2f0
00750DAE  8B D8                           mov ebx, eax
00750DB0  3D 03 01 00 00                  cmp eax, 0x103
00750DB5  75 1B                           jne 0x140750dd2
00750DB7  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00750DBC  45 33 C9                        xor r9d, r9d
00750DBF  45 33 C0                        xor r8d, r8d
00750DC2  BA 27 11 00 00                  mov edx, 0x1127
00750DC7  B9 91 01 00 00                  mov ecx, 0x191
00750DCC  E8 8F C8 DA FF                  call 0x1404fd660
00750DD1  CC                              int3
00750DD2  85 C0                           test eax, eax
00750DD4  0F 88 F7 00 00 00               js 0x140750ed1
00750DDA  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00750DDF  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
00750DE7  BB 11 00 00 C0                  mov ebx, 0xc0000011
00750DEC  0F 10 B4 24 B0 00 00 00         movups xmm6, xmmword ptr [rsp + 0xb0]
00750DF4  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00750DFC  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00750E00  0F 11 38                        movups xmmword ptr [rax], xmm7
00750E03  0F 11 70 10                     movups xmmword ptr [rax + 0x10], xmm6
00750E07  0F 10 84 24 C0 00 00 00         movups xmm0, xmmword ptr [rsp + 0xc0]
00750E0F  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
00750E13  F2 0F 10 84 24 D0 00 00 00      movsd xmm0, qword ptr [rsp + 0xd0]
00750E1C  F2 0F 11 40 30                  movsd qword ptr [rax + 0x30], xmm0
00750E21  81 FB 11 00 00 C0               cmp ebx, 0xc0000011
00750E27  75 06                           jne 0x140750e2f
00750E29  89 7C 24 54                     mov dword ptr [rsp + 0x54], edi
00750E2D  EB 47                           jmp 0x140750e76
00750E2F  44 39 6C 24 70                  cmp dword ptr [rsp + 0x70], r13d
00750E34  73 0F                           jae 0x140750e45
00750E36  89 7C 24 54                     mov dword ptr [rsp + 0x54], edi
00750E3A  BB 23 00 00 C0                  mov ebx, 0xc0000023
00750E3F  89 5C 24 74                     mov dword ptr [rsp + 0x74], ebx
00750E43  EB 31                           jmp 0x140750e76
00750E45  40 38 7C 24 50                  cmp byte ptr [rsp + 0x50], dil
00750E4A  74 16                           je 0x140750e62
00750E4C  41 8B D5                        mov edx, r13d
00750E4F  41 B8 08 00 00 00               mov r8d, 8
00750E55  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
00750E5D  E8 5E 83 19 00                  call 0x1408e91c0
00750E62  45 8B C5                        mov r8d, r13d
00750E65  49 8B D4                        mov rdx, r12
00750E68  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
00750E70  E8 CB 59 F7 FF                  call 0x1406c6840
00750E75  90                              nop
00750E76  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
00750E7E  C7 00 38 00 00 00               mov dword ptr [rax], 0x38
00750E84  EB 4B                           jmp 0x140750ed1
00750E86  8B D8                           mov ebx, eax
00750E88  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
00750E8C  33 FF                           xor edi, edi
00750E8E  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00750E93  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00750E98  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
00750E9D  EB 32                           jmp 0x140750ed1
00750E9F  3D 05 00 00 80                  cmp eax, 0x80000005
00750EA4  75 2B                           jne 0x140750ed1
00750EA6  45 03 FF                        add r15d, r15d
00750EA9  E9 02 FE FF FF                  jmp 0x140750cb0
00750EAE  8B D8                           mov ebx, eax
00750EB0  33 FF                           xor edi, edi
00750EB2  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00750EB7  8B F7                           mov esi, edi
00750EB9  44 8B E7                        mov r12d, edi
00750EBC  EB 13                           jmp 0x140750ed1
00750EBE  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00750EC3  EB 0C                           jmp 0x140750ed1
00750EC5  8B D8                           mov ebx, eax
00750EC7  33 FF                           xor edi, edi
00750EC9  44 8B F7                        mov r14d, edi
00750ECC  8B F7                           mov esi, edi
00750ECE  44 8B E7                        mov r12d, edi
00750ED1  39 7C 24 54                     cmp dword ptr [rsp + 0x54], edi
00750ED5  74 15                           je 0x140750eec
00750ED7  81 FB 11 00 00 C0               cmp ebx, 0xc0000011
00750EDD  74 08                           je 0x140750ee7
00750EDF  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
00750EE5  75 05                           jne 0x140750eec
00750EE7  BB 01 00 00 C0                  mov ebx, 0xc0000001
00750EEC  49 BF 00 00 00 00 04 00 00 00   movabs r15, 0x400000000
00750EF6  4C 85 BC 24 08 01 00 00         test qword ptr [rsp + 0x108], r15
00750EFE  74 10                           je 0x140750f10
00750F00  48 8B D6                        mov rdx, rsi
00750F03  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
00750F0B  E8 64 8F 15 00                  call 0x1408a9e74
00750F10  4C 85 BC 24 28 01 00 00         test qword ptr [rsp + 0x128], r15
00750F18  74 10                           je 0x140750f2a
00750F1A  48 8B D6                        mov rdx, rsi
00750F1D  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
00750F25  E8 4A 8F 15 00                  call 0x1408a9e74
00750F2A  48 85 F6                        test rsi, rsi
00750F2D  74 10                           je 0x140750f3f
00750F2F  48 8B CE                        mov rcx, rsi
00750F32  E8 79 8F 1E 00                  call 0x140939eb0
00750F37  48 8B CE                        mov rcx, rsi
00750F3A  E8 39 8F 1E 00                  call 0x140939e78
00750F3F  4D 85 F6                        test r14, r14
00750F42  74 0A                           je 0x140750f4e
00750F44  33 D2                           xor edx, edx
00750F46  49 8B CE                        mov rcx, r14
00750F49  E8 22 19 43 00                  call 0x140b82870
00750F4E  4D 85 E4                        test r12, r12
00750F51  74 0A                           je 0x140750f5d
00750F53  33 D2                           xor edx, edx
00750F55  49 8B CC                        mov rcx, r12
00750F58  E8 13 19 43 00                  call 0x140b82870
00750F5D  8B C3                           mov eax, ebx
00750F5F  48 8B 8C 24 48 01 00 00         mov rcx, qword ptr [rsp + 0x148]
00750F67  48 33 CC                        xor rcx, rsp
00750F6A  E8 D1 B6 F5 FF                  call 0x1406ac640
00750F6F  4C 8D 9C 24 70 01 00 00         lea r11, [rsp + 0x170]
00750F77  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00750F7B  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
00750F7F  41 0F 28 73 F0                  movaps xmm6, xmmword ptr [r11 - 0x10]
00750F84  41 0F 28 7B E0                  movaps xmm7, xmmword ptr [r11 - 0x20]
00750F89  49 8B E3                        mov rsp, r11
00750F8C  41 5F                           pop r15
00750F8E  41 5E                           pop r14
00750F90  41 5D                           pop r13
00750F92  41 5C                           pop r12
00750F94  5F                              pop rdi
00750F95  C3                              ret
00750F96  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfpQueryFileExtentsRequest(__int64 a1, unsigned __int8 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned int v_stack_m124;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m144;
    unsigned __int8 v_stack_m148;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m168;
    unsigned int v_stack_m170;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    v_rsp = (v_rsp) - (368);
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm6;
    *(unsigned __int64 *)(v_rsp - 72) = v_xmm7;
    result = (*(unsigned __int64 *)(v_rip + 7052844)) ^ (v_rsp);
    v_stack_m50 = result;
    v_stack_mB0 = a3;
    v_stack_m148 = a2;
    v_stack_mB8 = a1;
    v_stack_m108 = v_xmm0;
    v_rdi = 0;
    *(unsigned __int64 *)(v_rsp - 192) = 0;
    v_stack_m120 = 0;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 104) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 88) = 0;
    v_stack_m118 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 136) = 0;
    *(unsigned __int64 *)(v_rsp - 128) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 112) = 0;
    *(unsigned __int64 *)(v_rsp - 168) = 0;
    v_stack_mA0 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 144) = 0;
    v_stack_m144 = 1;
    if ((*(unsigned int *)(a1 + 24)) >= 56) goto loc_007509B7;
loc_007509AD:
    goto loc_00750ED1;
loc_007509B7:
    if (a2 != 0) {
        a2 = 56;
        a3 = a2 - 48;
        a1 = *(unsigned __int64 *)(a1 + 16);
        result = ProbeForWrite(a1, a2, a3, a4);
    }
    v_stack_mF8 = v_xmm7;
    v_stack_mE8 = v_xmm6;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm1;
    if (((unsigned int)(*(unsigned __int64 *)((unsigned int)(0xC0000206ULL) + 16))) == 2) goto loc_00750A16;
    goto loc_00750ED1;
loc_00750A16:
    if ((((unsigned __int8)((unsigned int)(0xC0000059ULL))) & (1)) != 0) goto loc_00750EBE;
    if (((unsigned int)((unsigned int)(0xC0000059ULL) - 1)) > 0xFFFFFULL) goto loc_00750EBE;
    result = ((unsigned int)(0xC0000059ULL) - 1) >> (32);
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00750EBE;
    if ((unsigned int)(result) == 0) goto loc_00750EBE;
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(0xC0000059ULL)))) goto loc_00750EBE;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(0xC0000059ULL))), (unsigned int)(0x70436650ULL), a4);
    v_stack_m140 = result;
    if (result != 0) goto loc_00750A7B;
loc_00750A71:
    goto loc_00750ED1;
loc_00750A7B:
    if (a2 == 0) goto loc_00750ADF;
    if ((((unsigned __int8)(result)) & (1)) != 0) {
        result = ExRaiseDatatypeMisalignment(256, (unsigned int)((unsigned int)((unsigned int)(0xC0000059ULL))), (unsigned int)(0x70436650ULL), a4);
    }
    if (((unsigned int)(0xC000009AULL) + (unsigned int)((unsigned int)((unsigned int)(0xC0000059ULL))) * 1) > 256) goto loc_00750ABC;
    if (((unsigned int)(0xC000009AULL) + (unsigned int)((unsigned int)((unsigned int)(0xC0000059ULL))) * 1) >= ((unsigned int)((unsigned int)((unsigned int)(0xC0000059ULL))))) goto loc_00750AE4;
loc_00750ABC:
    goto loc_00750AE4;
loc_00750ADF:
loc_00750AE4:
    result = memcpy(result, v_stack_mF0, (unsigned int)((unsigned int)((unsigned int)(v_stack_mE8))), a4);
    v_rbx = (unsigned int)(((unsigned int)(v_stack_mE8)) >> (1));
    v_rbx = (unsigned int)((v_rbx) - 1);
    if ((*(unsigned __int16 *)(result + v_rbx * 2)) != 0) goto loc_00750EBE;
    v_r13 = (unsigned int)((a2) >> (1));
    if ((*(unsigned __int16 *)(result + v_r13 * 2)) != 92) goto loc_00750EBE;
    result = ExAllocatePool2(92 - 28, 92 + 52, (unsigned int)(0x43536650ULL), a4);
    v_stack_m138 = result;
    if (result == 0) goto loc_00750A71;
    result = PfpPrefetchSharedInitialize(result, 92 + 52, (unsigned int)(0x43536650ULL), a4);
    *(unsigned int *)(result + 56) = 15;
    *(unsigned int *)(result + 60) = 150;
    result = PfpPrefetchSharedStart(result, 92 + 52, (unsigned int)(0x43536650ULL), a4);
    if (sign_flag) goto loc_00750ED1;
    *(unsigned __int16 *)(result + v_r13 * 2) = 0;
    result = RtlInitUnicodeStringEx(v_stack_m118, result, (unsigned int)(0x43536650ULL), a4);
    if (sign_flag) goto loc_00750ED1;
    v_stack_m160 = 0;
    v_stack_m168 = 0;
    v_stack_m170 = 32;
    v_stack_m178 = 0x100180ULL;
    a4 = 0;
    result = PfpOpenHandleCreate(v_stack_m88, result, v_stack_m118, a4);
    if (sign_flag) goto loc_00750ED1;
    *(unsigned __int16 *)(result + v_r13 * 2) = 92;
    result = RtlInitUnicodeStringEx(v_stack_m118, result, v_stack_m118, a4);
    if (sign_flag) goto loc_00750ED1;
    v_stack_m160 = v_stack_m88;
    v_stack_m168 = 128;
    v_stack_m170 = 32;
    v_stack_m178 = 0x100080ULL;
    a4 = 0;
    result = PfpOpenHandleCreate(v_stack_mA8, result, v_stack_m118, a4);
    if (sign_flag) goto loc_00750ED1;
    v_stack_m178 = 1;
    result = ZwQueryVolumeInformationFile(v_stack_m88, v_stack_m108, v_stack_m68, 32 - 8);
    if (((unsigned int)(result)) == 259) {
        v_stack_m178 = 0;
        a4 = 0;
        a3 = 0;
        a2 = 0x10AEULL;
        a1 = 401;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_00750ED1;
    v_stack_mD8 = (unsigned int)((unsigned int)(v_stack_m60));
    v_stack_m128 = (unsigned int)((unsigned int)(v_stack_mC8));
    v_r15 = 32;
    if (((unsigned int)((unsigned int)(v_stack_mC8))) > 32) { v_r15 = (unsigned int)((unsigned int)(v_stack_mC8)); }
loc_00750CB0:
    if (((unsigned int)(v_r15)) > 0xA00000ULL) goto loc_007509AD;
    result = (unsigned int)(v_stack_m60);
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_r15)), (unsigned int)(0x65466650ULL), a4);
    v_stack_m130 = result;
    if (result == 0) goto loc_00750A71;
    v_stack_m150 = (unsigned int)(v_r15);
    v_stack_m158 = result;
    v_stack_m160 = 8;
    v_stack_m168 = v_stack_mC0;
    v_stack_m170 = 0x90073ULL;
    v_stack_m178 = v_stack_m108;
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = ZwFsControlFile(v_stack_mA8, a2, a3, a4);
    if (((unsigned int)(result)) == 259) {
        v_stack_m178 = 0;
        a4 = 0;
        a3 = 0;
        a2 = 0x10ECULL;
        a1 = 401;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (sign_flag) goto loc_00750D7B;
    v_stack_mC8 = (unsigned int)(v_stack_m100);
    if ((*(unsigned int *)(result)) == 0) goto loc_00750D86;
    goto loc_00750DF4;
loc_00750D7B:
    if (((unsigned int)(result)) != 0xC0000011ULL) goto loc_00750E9F;
loc_00750D86:
    v_stack_m178 = 6;
    result = ZwQueryInformationFile(v_stack_mA8, v_stack_m108, v_stack_m120, 8);
    if (((unsigned int)(result)) == 259) {
        v_stack_m178 = 0;
        a4 = 0;
        a3 = 0;
        a2 = 0x1127ULL;
        a1 = 401;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (sign_flag) goto loc_00750ED1;
    v_stack_mE0 = v_stack_m120;
loc_00750DF4:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB8 + 16)) = v_xmm7;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB8 + 16) + 16) = v_xmm6;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB8 + 16) + 32) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB8 + 16) + 48) = v_xmm0;
    if (((unsigned int)((unsigned int)(0xC0000011ULL))) != 0xC0000011ULL) goto loc_00750E2F;
    v_stack_m144 = 0;
    goto loc_00750E76;
loc_00750E2F:
    if (v_stack_m128 >= ((unsigned int)(v_stack_m100))) goto loc_00750E45;
    v_stack_m144 = 0;
    v_stack_m124 = (unsigned int)((unsigned int)(0xC0000023ULL));
    goto loc_00750E76;
loc_00750E45:
    result = *(unsigned __int64 *)(v_stack_mB8 + 16);
    if (v_stack_m148 != 0) {
        a2 = (unsigned int)(v_stack_m100);
        a3 = 8;
        a1 = v_stack_mD0;
        result = ProbeForWrite(a1, a2, a3, a4);
    }
    result = memcpy(v_stack_mD0, result, (unsigned int)((unsigned int)(v_stack_m100)), a4);
loc_00750E76:
    *(unsigned int *)(v_stack_mB0) = 56;
    goto loc_00750ED1;
loc_00750E9F:
    if (((unsigned int)(v_stack_mB0)) != 0x80000005ULL) goto loc_00750ED1;
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(v_r15)));
    goto loc_00750CB0;
loc_00750EBE:
    goto loc_00750ED1;
loc_00750ED1:
    if (v_stack_m144 == 0) goto loc_00750EEC;
    if (((unsigned int)((unsigned int)(0xC000000DULL))) == 0xC0000011ULL) goto loc_00750EE7;
    v_rbx = (unsigned int)(0xC000000DULL);
    if (((unsigned int)((unsigned int)(0xC000000DULL))) == 0xC0000023ULL) {
        v_rbx = 0xC0000001ULL;
    }
    result = v_stack_mB0;
    if (((v_stack_m90) & (v_r15)) != 0) {
        a2 = result;
        a1 = v_stack_mA8;
        result = PfpOpenHandleClose(a1, a2, (unsigned int)((unsigned int)(v_stack_m100)), a4);
    }
    if (((v_stack_m70) & (v_r15)) != 0) {
        a2 = result;
        a1 = v_stack_m88;
        result = PfpOpenHandleClose(a1, a2, (unsigned int)((unsigned int)(v_stack_m100)), a4);
    }
    if (result != 0) {
        a1 = result;
        result = PfpPrefetchSharedCleanup(a1, a2, (unsigned int)((unsigned int)(v_stack_m100)), a4);
        a1 = result;
        result = PfpPrefetchSharedDeref(a1, a2, (unsigned int)((unsigned int)(v_stack_m100)), a4);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)(v_stack_m100)), a4);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)(v_stack_m100)), a4);
    }
    a1 = (v_stack_m50) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)((unsigned int)(v_stack_m100)), a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PfpQueryFileExtentsRequest(void *Arg1, uint8_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint32_t v_stack_m124;
    uint32_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m144;
    uint8_t v_stack_m148;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint32_t v_stack_m168;
    uint32_t v_stack_m170;
    uint32_t v_stack_m178;
    uint64_t v_stack_m28;
    uint64_t v_stack_m50;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    local_rsp = (local_rsp) - (368);
    *(uint64_t *)(local_rsp - 0x38) = v_xmm6;
    *(uint64_t *)(local_rsp - 0x48) = v_xmm7;
    result = (*(uint64_t *)(v_rip + 0x6B9E2C)) ^ (local_rsp);
    v_stack_m50 = result;
    v_stack_mB0 = Arg3;
    v_stack_m148 = Arg2;
    v_stack_mB8 = Arg1;
    v_stack_m108 = v_xmm0;
    local_rdi = 0;
    *(uint64_t *)(local_rsp - 0xC0) = 0;
    v_stack_m120 = 0;
    result = 0;
    *(uint64_t *)(local_rsp - 0x68) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x58) = 0;
    v_stack_m118 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x88) = 0;
    *(uint64_t *)(local_rsp - 0x80) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x70) = 0;
    *(uint64_t *)(local_rsp - 0xA8) = 0;
    v_stack_mA0 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x90) = 0;
    v_stack_m144 = 1;
    if ((*(uint32_t *)(arg1 + 0x18)) >= 56) goto loc_007509B7;
loc_007509AD:
    goto loc_00750ED1;
loc_007509B7:
    if (Arg2 != 0) {
        Arg2 = 56;
        Arg3 = Arg2 - 48;
        Arg1 = *(uint64_t *)(arg1 + 0x10);
        result = ProbeForWrite(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_mF8 = v_xmm7;
    v_stack_mE8 = v_xmm6;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm1;
    if (((uint32_t)(*(uint64_t *)((uint32_t)(0xC0000206ULL) + 0x10))) == 2) goto loc_00750A16;
    goto loc_00750ED1;
loc_00750A16:
    if ((((uint8_t)((uint32_t)(0xC0000059ULL))) & (1)) != 0) goto loc_00750EBE;
    if (((uint32_t)((uint32_t)(0xC0000059ULL) - 1)) > 0xFFFFFULL) goto loc_00750EBE;
    result = ((uint32_t)(0xC0000059ULL) - 1) >> (32);
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00750EBE;
    if ((uint32_t)(result) == 0) goto loc_00750EBE;
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(0xC0000059ULL)))) goto loc_00750EBE;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(0xC0000059ULL))), (uint32_t)(0x70436650ULL), Arg4);
    v_stack_m140 = result;
    if (result != 0) goto loc_00750A7B;
loc_00750A71:
    goto loc_00750ED1;
loc_00750A7B:
    if (Arg2 == 0) goto loc_00750ADF;
    if ((((uint8_t)(result)) & (1)) != 0) {
        result = ExRaiseDatatypeMisalignment(256, (uint32_t)((uint32_t)((uint32_t)(0xC0000059ULL))), (uint32_t)(0x70436650ULL), Arg4);
    }
    if (((uint32_t)(0xC000009AULL) + (uint32_t)((uint32_t)((uint32_t)(0xC0000059ULL))) * 1) > 256) goto loc_00750ABC;
    if (((uint32_t)(0xC000009AULL) + (uint32_t)((uint32_t)((uint32_t)(0xC0000059ULL))) * 1) >= ((uint32_t)((uint32_t)((uint32_t)(0xC0000059ULL))))) goto loc_00750AE4;
loc_00750ABC:
    goto loc_00750AE4;
loc_00750ADF:
loc_00750AE4:
    result = memcpy(result, v_stack_mF0, (uint32_t)((uint32_t)((uint32_t)(v_stack_mE8))), Arg4);
    local_rbx = (uint32_t)(((uint32_t)(v_stack_mE8)) >> (1));
    local_rbx = (uint32_t)((local_rbx) - 1);
    if ((*(uint16_t *)(result + local_rbx * 2)) != 0) goto loc_00750EBE;
    local_r13 = (uint32_t)((Arg2) >> (1));
    if ((*(uint16_t *)(result + local_r13 * 2)) != 92) goto loc_00750EBE;
    result = ExAllocatePool2(92 - 28, 92 + 52, (uint32_t)(0x43536650ULL), Arg4);
    v_stack_m138 = result;
    if (result == 0) goto loc_00750A71;
    result = PfpPrefetchSharedInitialize(result, 92 + 52, (uint32_t)(0x43536650ULL), Arg4);
    *(uint32_t *)(result + 0x38) = 15;
    *(uint32_t *)(result + 0x3C) = 150;
    result = PfpPrefetchSharedStart(result, 92 + 52, (uint32_t)(0x43536650ULL), Arg4);
    if (sign_flag) goto loc_00750ED1;
    *(uint16_t *)(result + local_r13 * 2) = 0;
    result = RtlInitUnicodeStringEx(v_stack_m118, result, (uint32_t)(0x43536650ULL), Arg4);
    if (sign_flag) goto loc_00750ED1;
    v_stack_m160 = 0;
    v_stack_m168 = 0;
    v_stack_m170 = 32;
    v_stack_m178 = 0x100180ULL;
    Arg4 = 0;
    result = PfpOpenHandleCreate(v_stack_m88, result, v_stack_m118, Arg4);
    if (sign_flag) goto loc_00750ED1;
    *(uint16_t *)(result + local_r13 * 2) = 92;
    result = RtlInitUnicodeStringEx(v_stack_m118, result, v_stack_m118, Arg4);
    if (sign_flag) goto loc_00750ED1;
    v_stack_m160 = v_stack_m88;
    v_stack_m168 = 128;
    v_stack_m170 = 32;
    v_stack_m178 = 0x100080ULL;
    Arg4 = 0;
    result = PfpOpenHandleCreate(v_stack_mA8, result, v_stack_m118, Arg4);
    if (sign_flag) goto loc_00750ED1;
    v_stack_m178 = 1;
    result = ZwQueryVolumeInformationFile(v_stack_m88, v_stack_m108, v_stack_m68, 32 - 8);
    if (((uint32_t)(result)) == 259) {
        v_stack_m178 = 0;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = 0x10AEULL;
        Arg1 = 401;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_00750ED1;
    v_stack_mD8 = (uint32_t)((uint32_t)(v_stack_m60));
    v_stack_m128 = (uint32_t)((uint32_t)(v_stack_mC8));
    local_r15 = 32;
    if (((uint32_t)((uint32_t)(v_stack_mC8))) > 32) { local_r15 = (uint32_t)((uint32_t)(v_stack_mC8)); }
loc_00750CB0:
    if (((uint32_t)(local_r15)) > 0xA00000ULL) goto loc_007509AD;
    result = (uint32_t)(v_stack_m60);
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_r15)), (uint32_t)(0x65466650ULL), Arg4);
    v_stack_m130 = result;
    if (result == 0) goto loc_00750A71;
    v_stack_m150 = (uint32_t)(local_r15);
    v_stack_m158 = result;
    v_stack_m160 = 8;
    v_stack_m168 = v_stack_mC0;
    v_stack_m170 = 0x90073ULL;
    v_stack_m178 = v_stack_m108;
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = ZwFsControlFile(v_stack_mA8, Arg2, Arg3, Arg4);
    if (((uint32_t)(result)) == 259) {
        v_stack_m178 = 0;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = 0x10ECULL;
        Arg1 = 401;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (sign_flag) goto loc_00750D7B;
    v_stack_mC8 = (uint32_t)(v_stack_m100);
    if ((*(uint32_t *)(result)) == 0) goto loc_00750D86;
    goto loc_00750DF4;
loc_00750D7B:
    if (((uint32_t)(result)) != 0xC0000011ULL) goto loc_00750E9F;
loc_00750D86:
    v_stack_m178 = 6;
    result = ZwQueryInformationFile(v_stack_mA8, v_stack_m108, v_stack_m120, 8);
    if (((uint32_t)(result)) == 259) {
        v_stack_m178 = 0;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = 0x1127ULL;
        Arg1 = 401;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (sign_flag) goto loc_00750ED1;
    v_stack_mE0 = v_stack_m120;
loc_00750DF4:
    *(uint64_t *)(*(uint64_t *)(v_stack_mB8 + 0x10)) = v_xmm7;
    *(uint64_t *)(*(uint64_t *)(v_stack_mB8 + 0x10) + 0x10) = v_xmm6;
    *(uint64_t *)(*(uint64_t *)(v_stack_mB8 + 0x10) + 0x20) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(v_stack_mB8 + 0x10) + 0x30) = v_xmm0;
    if (((uint32_t)((uint32_t)(0xC0000011ULL))) != 0xC0000011ULL) goto loc_00750E2F;
    v_stack_m144 = 0;
    goto loc_00750E76;
loc_00750E2F:
    if (v_stack_m128 >= ((uint32_t)(v_stack_m100))) goto loc_00750E45;
    v_stack_m144 = 0;
    v_stack_m124 = (uint32_t)((uint32_t)(0xC0000023ULL));
    goto loc_00750E76;
loc_00750E45:
    result = *(uint64_t *)(v_stack_mB8 + 0x10);
    if (v_stack_m148 != 0) {
        Arg2 = (uint32_t)(v_stack_m100);
        Arg3 = 8;
        Arg1 = v_stack_mD0;
        result = ProbeForWrite(Arg1, Arg2, Arg3, Arg4);
    }
    result = memcpy(v_stack_mD0, result, (uint32_t)((uint32_t)(v_stack_m100)), Arg4);
loc_00750E76:
    *(uint32_t *)(v_stack_mB0) = 56;
    goto loc_00750ED1;
loc_00750E9F:
    if (((uint32_t)(v_stack_mB0)) != 0x80000005ULL) goto loc_00750ED1;
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(local_r15)));
    goto loc_00750CB0;
loc_00750EBE:
    goto loc_00750ED1;
loc_00750ED1:
    if (v_stack_m144 == 0) goto loc_00750EEC;
    if (((uint32_t)((uint32_t)(0xC000000DULL))) == 0xC0000011ULL) goto loc_00750EE7;
    local_rbx = (uint32_t)(0xC000000DULL);
    if (((uint32_t)((uint32_t)(0xC000000DULL))) == 0xC0000023ULL) {
        local_rbx = 0xC0000001ULL;
    }
    result = v_stack_mB0;
    if (((v_stack_m90) & (local_r15)) != 0) {
        Arg2 = result;
        Arg1 = v_stack_mA8;
        result = PfpOpenHandleClose(Arg1, Arg2, (uint32_t)((uint32_t)(v_stack_m100)), Arg4);
    }
    if (((v_stack_m70) & (local_r15)) != 0) {
        Arg2 = result;
        Arg1 = v_stack_m88;
        result = PfpOpenHandleClose(Arg1, Arg2, (uint32_t)((uint32_t)(v_stack_m100)), Arg4);
    }
    if (result != 0) {
        Arg1 = result;
        result = PfpPrefetchSharedCleanup(Arg1, Arg2, (uint32_t)((uint32_t)(v_stack_m100)), Arg4);
        Arg1 = result;
        result = PfpPrefetchSharedDeref(Arg1, Arg2, (uint32_t)((uint32_t)(v_stack_m100)), Arg4);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)(v_stack_m100)), Arg4);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)(v_stack_m100)), Arg4);
    }
    Arg1 = (v_stack_m50) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)((uint32_t)(v_stack_m100)), Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007508E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
