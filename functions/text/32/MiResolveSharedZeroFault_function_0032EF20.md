# MiResolveSharedZeroFault

- RVA: `0x0032EF20`–`0x0032F717` (길이 `2,039` bytes)
- VA: `0x000000014032EF20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007642C`
- 디코드: `484`개 명령, `2,039/2,039` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0032EF52` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0032F02F` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0032F23F` → [MiGetProtoPteAddress](MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x0032F2D6` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0032F41F` → [MiPteHasShadow](MiPteHasShadow_function_0032B998.md) (function, `0x0032B998`)
- `0x0032F521` → [MiMakePrototypePteDirect](../29/MiMakePrototypePteDirect_function_00294DE0.md) (function, `0x00294DE0`)
- `0x0032F5B6` → [MiMakePrototypePteDirect](../29/MiMakePrototypePteDirect_function_00294DE0.md) (function, `0x00294DE0`)
- `0x0032F66B` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0032F67A` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0032F6FE` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0032F70D` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)

### Direct callers
- [sub_0032D782](Unknown_function_0032D782.md) at `0x0032DC5A`

### Static image references
- `0x0032EFB5` → RVA `0x00E2DC80` (`.data`; read)
- `0x0032F0BF` → RVA `0x00014578` (`.rdata`; read)
- `0x0032F402` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0032F65D` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0032EF20  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0032EF25  55                              push rbp
0032EF26  53                              push rbx
0032EF27  56                              push rsi
0032EF28  57                              push rdi
0032EF29  41 54                           push r12
0032EF2B  41 55                           push r13
0032EF2D  41 56                           push r14
0032EF2F  41 57                           push r15
0032EF31  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
0032EF36  48 81 EC C8 00 00 00            sub rsp, 0xc8
0032EF3D  33 D2                           xor edx, edx
0032EF3F  48 C7 45 77 00 00 00 00         mov qword ptr [rbp + 0x77], 0
0032EF47  4C 8B F9                        mov r15, rcx
0032EF4A  48 8D 4D 87                     lea rcx, [rbp - 0x79]
0032EF4E  44 8D 42 78                     lea r8d, [rdx + 0x78]
0032EF52  E8 E9 7C 39 00                  call 0x1406c6c40
0032EF57  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
0032EF5B  0F 57 C0                        xorps xmm0, xmm0
0032EF5E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0032EF63  48 BF F8 FF FF FF 7F 00 00 00   movabs rdi, 0x7ffffffff8
0032EF6D  48 BB 00 00 00 00 80 F6 FF FF   movabs rbx, 0xfffff68000000000
0032EF77  48 8B 30                        mov rsi, qword ptr [rax]
0032EF7A  4C 8B C6                        mov r8, rsi
0032EF7D  49 C1 E8 09                     shr r8, 9
0032EF81  4C 23 C7                        and r8, rdi
0032EF84  48 8B C3                        mov rax, rbx
0032EF87  4C 03 C0                        add r8, rax
0032EF8A  41 8B 47 20                     mov eax, dword ptr [r15 + 0x20]
0032EF8E  89 45 6F                        mov dword ptr [rbp + 0x6f], eax
0032EF91  48 8B CB                        mov rcx, rbx
0032EF94  48 C1 E1 19                     shl rcx, 0x19
0032EF98  49 8B D0                        mov rdx, r8
0032EF9B  48 C1 E2 19                     shl rdx, 0x19
0032EF9F  48 2B D1                        sub rdx, rcx
0032EFA2  48 89 4D 7F                     mov qword ptr [rbp + 0x7f], rcx
0032EFA6  48 C1 FA 10                     sar rdx, 0x10
0032EFAA  3D 00 01 00 00                  cmp eax, 0x100
0032EFAF  0F 84 FD 05 00 00               je 0x14032f5b2
0032EFB5  48 8B 0D C4 EC AF 00            mov rcx, qword ptr [rip + 0xafecc4]
0032EFBC  83 E0 1F                        and eax, 0x1f
0032EFBF  48 0D 20 00 00 F8               or rax, 0xfffffffff8000020
0032EFC5  48 C1 E0 05                     shl rax, 5
0032EFC9  48 85 C9                        test rcx, rcx
0032EFCC  74 0D                           je 0x14032efdb
0032EFCE  48 85 C8                        test rax, rcx
0032EFD1  0F 84 3F 05 00 00               je 0x14032f516
0032EFD7  48 83 C8 10                     or rax, 0x10
0032EFDB  48 C1 EA 12                     shr rdx, 0x12
0032EFDF  49 89 00                        mov qword ptr [r8], rax
0032EFE2  81 E2 F8 FF FF 3F               and edx, 0x3ffffff8
0032EFE8  48 B8 00 00 00 40 FB F6 FF FF   movabs rax, 0xfffff6fb40000000
0032EFF2  48 8B C0                        mov rax, rax
0032EFF5  48 03 D0                        add rdx, rax
0032EFF8  48 B8 68 DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedf68
0032F002  48 8B C0                        mov rax, rax
0032F005  49 BC 00 00 00 00 00 DE FF FF   movabs r12, 0xffffde0000000000
0032F00F  49 BD FF FF FF FF FF 00 00 00   movabs r13, 0xffffffffff
0032F019  49 BE FF FF FF FF FF FF FF 7F   movabs r14, 0x7fffffffffffffff
0032F023  48 3B D0                        cmp rdx, rax
0032F026  0F 84 86 00 00 00               je 0x14032f0b2
0032F02C  48 8B CA                        mov rcx, rdx
0032F02F  E8 6C 38 F5 FF                  call 0x1402828a0
0032F034  48 C1 E8 0C                     shr rax, 0xc
0032F038  49 23 C5                        and rax, r13
0032F03B  48 8D 1C 40                     lea rbx, [rax + rax*2]
0032F03F  48 C1 E3 04                     shl rbx, 4
0032F043  49 8B C4                        mov rax, r12
0032F046  48 03 D8                        add rbx, rax
0032F049  33 FF                           xor edi, edi
0032F04B  F0 48 0F BA 6B 18 3F            lock bts qword ptr [rbx + 0x18], 0x3f
0032F052  0F 82 48 04 00 00               jb 0x14032f4a0
0032F058  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
0032F05B  0F BA E0 1A                     bt eax, 0x1a
0032F05F  0F 83 A4 04 00 00               jae 0x14032f509
0032F065  48 8B 0B                        mov rcx, qword ptr [rbx]
0032F068  48 C1 E9 20                     shr rcx, 0x20
0032F06C  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
0032F06F  8D 51 01                        lea edx, [rcx + 1]
0032F072  0F BA E0 1A                     bt eax, 0x1a
0032F076  0F 83 70 04 00 00               jae 0x14032f4ec
0032F07C  48 8B 03                        mov rax, qword ptr [rbx]
0032F07F  48 B9 FF FF FF FF 00 FC FF FF   movabs rcx, 0xfffffc00ffffffff
0032F089  48 C1 E2 20                     shl rdx, 0x20
0032F08D  48 33 C2                        xor rax, rdx
0032F090  48 23 C1                        and rax, rcx
0032F093  48 33 C2                        xor rax, rdx
0032F096  48 89 03                        mov qword ptr [rbx], rax
0032F099  F0 4C 21 73 18                  lock and qword ptr [rbx + 0x18], r14
0032F09E  48 BB 00 00 00 00 80 F6 FF FF   movabs rbx, 0xfffff68000000000
0032F0A8  48 BF F8 FF FF FF 7F 00 00 00   movabs rdi, 0x7ffffffff8
0032F0B2  4D 8B 77 40                     mov r14, qword ptr [r15 + 0x40]
0032F0B6  4D 85 F6                        test r14, r14
0032F0B9  74 55                           je 0x14032f110
0032F0BB  41 8B 46 18                     mov eax, dword ptr [r14 + 0x18]
0032F0BF  4C 8D 0D B2 54 CE FF            lea r9, [rip - 0x31ab4e]
0032F0C6  45 0F B6 46 20                  movzx r8d, byte ptr [r14 + 0x20]
0032F0CB  45 32 ED                        xor r13b, r13b
0032F0CE  41 0F B6 56 21                  movzx edx, byte ptr [r14 + 0x21]
0032F0D3  41 8B 4E 30                     mov ecx, dword ptr [r14 + 0x30]
0032F0D7  49 C1 E0 20                     shl r8, 0x20
0032F0DB  4C 0B C0                        or r8, rax
0032F0DE  48 C1 E2 20                     shl rdx, 0x20
0032F0E2  41 8B 46 1C                     mov eax, dword ptr [r14 + 0x1c]
0032F0E6  48 0B D0                        or rdx, rax
0032F0E9  8B C1                           mov eax, ecx
0032F0EB  48 C1 E8 13                     shr rax, 0x13
0032F0EF  83 E0 03                        and eax, 3
0032F0F2  49 83 3C C1 10                  cmp qword ptr [r9 + rax*8], 0x10
0032F0F7  0F 84 87 05 00 00               je 0x14032f684
0032F0FD  41 8B 07                        mov eax, dword ptr [r15]
0032F100  A8 02                           test al, 2
0032F102  0F 85 E3 04 00 00               jne 0x14032f5eb
0032F108  80 E1 70                        and cl, 0x70
0032F10B  80 F9 20                        cmp cl, 0x20
0032F10E  75 15                           jne 0x14032f125
0032F110  48 81 C4 C8 00 00 00            add rsp, 0xc8
0032F117  41 5F                           pop r15
0032F119  41 5E                           pop r14
0032F11B  41 5D                           pop r13
0032F11D  41 5C                           pop r12
0032F11F  5F                              pop rdi
0032F120  5E                              pop rsi
0032F121  5B                              pop rbx
0032F122  5D                              pop rbp
0032F123  C3                              ret
0032F124  CC                              int3
0032F125  48 8B C6                        mov rax, rsi
0032F128  41 B8 08 00 00 00               mov r8d, 8
0032F12E  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
0032F134  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0032F139  49 8B 46 78                     mov rax, qword ptr [r14 + 0x78]
0032F13D  48 85 C0                        test rax, rax
0032F140  0F 89 E5 03 00 00               jns 0x14032f52b
0032F146  48 C1 EE 0C                     shr rsi, 0xc
0032F14A  4C 8D 54 24 20                  lea r10, [rsp + 0x20]
0032F14F  48 2B D6                        sub rdx, rsi
0032F152  66 C7 45 87 02 00               mov word ptr [rbp - 0x79], 2
0032F158  4C 89 55 8F                     mov qword ptr [rbp - 0x71], r10
0032F15C  48 C7 45 97 01 00 00 00         mov qword ptr [rbp - 0x69], 1
0032F164  4C 8D 62 01                     lea r12, [rdx + 1]
0032F168  4D 3B C4                        cmp r8, r12
0032F16B  4D 0F 46 E0                     cmovbe r12, r8
0032F16F  45 33 C9                        xor r9d, r9d
0032F172  49 8B C4                        mov rax, r12
0032F175  4C 89 4D 9F                     mov qword ptr [rbp - 0x61], r9
0032F179  48 C1 E0 0C                     shl rax, 0xc
0032F17D  45 33 C0                        xor r8d, r8d
0032F180  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0032F185  4C 89 45 A7                     mov qword ptr [rbp - 0x59], r8
0032F189  33 D2                           xor edx, edx
0032F18B  45 33 FF                        xor r15d, r15d
0032F18E  4D 85 E4                        test r12, r12
0032F191  0F 84 41 02 00 00               je 0x14032f3d8
0032F197  49 BB 00 D0 BE 7D FB F6 FF FF   movabs r11, 0xfffff6fb7dbed000
0032F1A1  4D 03 C9                        add r9, r9
0032F1A4  49 C1 E0 0C                     shl r8, 0xc
0032F1A8  4B 8B 34 CA                     mov rsi, qword ptr [r10 + r9*8]
0032F1AC  49 03 F0                        add rsi, r8
0032F1AF  48 81 E6 00 F0 FF FF            and rsi, 0xfffffffffffff000
0032F1B6  48 8B CE                        mov rcx, rsi
0032F1B9  48 C1 E9 09                     shr rcx, 9
0032F1BD  48 23 F9                        and rdi, rcx
0032F1C0  48 8B C3                        mov rax, rbx
0032F1C3  48 03 F8                        add rdi, rax
0032F1C6  4D 85 FF                        test r15, r15
0032F1C9  74 1D                           je 0x14032f1e8
0032F1CB  48 8D 82 00 10 00 00            lea rax, [rdx + 0x1000]
0032F1D2  48 3B F0                        cmp rsi, rax
0032F1D5  0F 85 FD 01 00 00               jne 0x14032f3d8
0032F1DB  48 F7 C7 FF 0F 00 00            test rdi, 0xfff
0032F1E2  0F 84 F0 01 00 00               je 0x14032f3d8
0032F1E8  48 8B 17                        mov rdx, qword ptr [rdi]
0032F1EB  49 8B C3                        mov rax, r11
0032F1EE  48 3B F8                        cmp rdi, rax
0032F1F1  72 2E                           jb 0x14032f221
0032F1F3  48 B8 F8 D7 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed7f8
0032F1FD  48 8B C0                        mov rax, rax
0032F200  48 3B F8                        cmp rdi, rax
0032F203  77 1C                           ja 0x14032f221
0032F205  4C 8B C2                        mov r8, rdx
0032F208  F6 C2 01                        test dl, 1
0032F20B  74 14                           je 0x14032f221
0032F20D  F6 C2 42                        test dl, 0x42
0032F210  0F 95 C1                        setne cl
0032F213  F6 C2 20                        test dl, 0x20
0032F216  0F 95 C0                        setne al
0032F219  84 C8                           test al, cl
0032F21B  0F 84 FE 01 00 00               je 0x14032f41f
0032F221  48 85 D2                        test rdx, rdx
0032F224  0F 85 4D 01 00 00               jne 0x14032f377
0032F22A  44 8D 42 0C                     lea r8d, [rdx + 0xc]
0032F22E  48 8B DE                        mov rbx, rsi
0032F231  48 C1 EB 0C                     shr rbx, 0xc
0032F235  4C 8D 4D 77                     lea r9, [rbp + 0x77]
0032F239  48 8B D3                        mov rdx, rbx
0032F23C  49 8B CE                        mov rcx, r14
0032F23F  E8 2C F7 FF FF                  call 0x14032e970
0032F244  4C 8B C0                        mov r8, rax
0032F247  48 85 C0                        test rax, rax
0032F24A  0F 84 88 01 00 00               je 0x14032f3d8
0032F250  49 8B 46 78                     mov rax, qword ptr [r14 + 0x78]
0032F254  48 85 C0                        test rax, rax
0032F257  0F 88 63 03 00 00               js 0x14032f5c0
0032F25D  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
0032F260  48 8B D7                        mov rdx, rdi
0032F263  48 C1 E2 19                     shl rdx, 0x19
0032F267  48 2B 55 7F                     sub rdx, qword ptr [rbp + 0x7f]
0032F26B  48 C1 FA 10                     sar rdx, 0x10
0032F26F  3D 00 01 00 00                  cmp eax, 0x100
0032F274  0F 84 A4 02 00 00               je 0x14032f51e
0032F27A  48 8B 0D FF E9 AF 00            mov rcx, qword ptr [rip + 0xafe9ff]
0032F281  83 E0 1F                        and eax, 0x1f
0032F284  48 0D 20 00 00 F8               or rax, 0xfffffffff8000020
0032F28A  48 C1 E0 05                     shl rax, 5
0032F28E  48 85 C9                        test rcx, rcx
0032F291  74 0D                           je 0x14032f2a0
0032F293  48 85 C8                        test rax, rcx
0032F296  0F 84 F5 01 00 00               je 0x14032f491
0032F29C  48 83 C8 10                     or rax, 0x10
0032F2A0  48 C1 EA 12                     shr rdx, 0x12
0032F2A4  48 89 07                        mov qword ptr [rdi], rax
0032F2A7  81 E2 F8 FF FF 3F               and edx, 0x3ffffff8
0032F2AD  48 B8 00 00 00 40 FB F6 FF FF   movabs rax, 0xfffff6fb40000000
0032F2B7  48 8B C0                        mov rax, rax
0032F2BA  48 03 D0                        add rdx, rax
0032F2BD  48 B8 68 DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedf68
0032F2C7  48 8B C0                        mov rax, rax
0032F2CA  48 3B D0                        cmp rdx, rax
0032F2CD  0F 84 90 00 00 00               je 0x14032f363
0032F2D3  48 8B CA                        mov rcx, rdx
0032F2D6  E8 C5 35 F5 FF                  call 0x1402828a0
0032F2DB  48 C1 E8 0C                     shr rax, 0xc
0032F2DF  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
0032F2E9  48 23 C1                        and rax, rcx
0032F2EC  48 8D 1C 40                     lea rbx, [rax + rax*2]
0032F2F0  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0032F2FA  48 C1 E3 04                     shl rbx, 4
0032F2FE  48 8B C0                        mov rax, rax
0032F301  48 03 D8                        add rbx, rax
0032F304  33 FF                           xor edi, edi
0032F306  F0 48 0F BA 6B 18 3F            lock bts qword ptr [rbx + 0x18], 0x3f
0032F30D  0F 82 ED 00 00 00               jb 0x14032f400
0032F313  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
0032F316  0F BA E0 1A                     bt eax, 0x1a
0032F31A  0F 83 64 01 00 00               jae 0x14032f484
0032F320  48 8B 0B                        mov rcx, qword ptr [rbx]
0032F323  48 C1 E9 20                     shr rcx, 0x20
0032F327  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
0032F32A  8D 51 01                        lea edx, [rcx + 1]
0032F32D  0F BA E0 1A                     bt eax, 0x1a
0032F331  0F 83 30 01 00 00               jae 0x14032f467
0032F337  48 8B 03                        mov rax, qword ptr [rbx]
0032F33A  48 B9 FF FF FF FF 00 FC FF FF   movabs rcx, 0xfffffc00ffffffff
0032F344  48 C1 E2 20                     shl rdx, 0x20
0032F348  48 33 C2                        xor rax, rdx
0032F34B  48 23 C1                        and rax, rcx
0032F34E  48 33 C2                        xor rax, rdx
0032F351  48 89 03                        mov qword ptr [rbx], rax
0032F354  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0032F35E  F0 48 21 43 18                  lock and qword ptr [rbx + 0x18], rax
0032F363  48 BB 00 00 00 00 80 F6 FF FF   movabs rbx, 0xfffff68000000000
0032F36D  49 BB 00 D0 BE 7D FB F6 FF FF   movabs r11, 0xfffff6fb7dbed000
0032F377  4C 8B 55 8F                     mov r10, qword ptr [rbp - 0x71]
0032F37B  4C 8B 45 A7                     mov r8, qword ptr [rbp - 0x59]
0032F37F  4C 8B 4D 9F                     mov r9, qword ptr [rbp - 0x61]
0032F383  49 FF C0                        inc r8
0032F386  49 8B C1                        mov rax, r9
0032F389  4C 89 45 A7                     mov qword ptr [rbp - 0x59], r8
0032F38D  48 03 C0                        add rax, rax
0032F390  41 8B 0C C2                     mov ecx, dword ptr [r10 + rax*8]
0032F394  49 8B 54 C2 08                  mov rdx, qword ptr [r10 + rax*8 + 8]
0032F399  81 E1 FF 0F 00 00               and ecx, 0xfff
0032F39F  48 81 C2 FF 0F 00 00            add rdx, 0xfff
0032F3A6  48 03 D1                        add rdx, rcx
0032F3A9  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
0032F3AD  48 C1 EA 0C                     shr rdx, 0xc
0032F3B1  4C 3B C2                        cmp r8, rdx
0032F3B4  0F 84 05 01 00 00               je 0x14032f4bf
0032F3BA  4C 3B C9                        cmp r9, rcx
0032F3BD  74 19                           je 0x14032f3d8
0032F3BF  49 FF C7                        inc r15
0032F3C2  48 8B D6                        mov rdx, rsi
0032F3C5  48 BF F8 FF FF FF 7F 00 00 00   movabs rdi, 0x7ffffffff8
0032F3CF  4D 3B FC                        cmp r15, r12
0032F3D2  0F 82 C9 FD FF FF               jb 0x14032f1a1
0032F3D8  45 84 ED                        test r13b, r13b
0032F3DB  0F 84 2F FD FF FF               je 0x14032f110
0032F3E1  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
0032F3E5  41 C1 E7 0A                     shl r15d, 0xa
0032F3E9  8B 01                           mov eax, dword ptr [rcx]
0032F3EB  44 33 F8                        xor r15d, eax
0032F3EE  41 81 E7 00 FC 03 00            and r15d, 0x3fc00
0032F3F5  44 33 F8                        xor r15d, eax
0032F3F8  44 89 39                        mov dword ptr [rcx], r15d
0032F3FB  E9 10 FD FF FF                  jmp 0x14032f110
0032F400  FF C7                           inc edi
0032F402  85 3D A4 5E C9 00               test dword ptr [rip + 0xc95ea4], edi
0032F408  0F 84 4F 02 00 00               je 0x14032f65d
0032F40E  F3 90                           pause
0032F410  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0032F414  48 85 C0                        test rax, rax
0032F417  0F 89 E9 FE FF FF               jns 0x14032f306
0032F41D  EB E1                           jmp 0x14032f400
0032F41F  E8 74 C5 FF FF                  call 0x14032b998
0032F424  48 85 C0                        test rax, rax
0032F427  0F 84 F4 FD FF FF               je 0x14032f221
0032F42D  48 8B 88 08 05 00 00            mov rcx, qword ptr [rax + 0x508]
0032F434  48 85 C9                        test rcx, rcx
0032F437  0F 84 E4 FD FF FF               je 0x14032f221
0032F43D  48 8B C7                        mov rax, rdi
0032F440  48 C1 E8 03                     shr rax, 3
0032F444  25 FF 01 00 00                  and eax, 0x1ff
0032F449  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
0032F44D  A8 20                           test al, 0x20
0032F44F  74 04                           je 0x14032f455
0032F451  49 83 C8 20                     or r8, 0x20
0032F455  49 8B D0                        mov rdx, r8
0032F458  48 83 CA 42                     or rdx, 0x42
0032F45C  A8 42                           test al, 0x42
0032F45E  49 0F 44 D0                     cmove rdx, r8
0032F462  E9 BA FD FF FF                  jmp 0x14032f221
0032F467  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0032F46B  48 C1 E2 10                     shl rdx, 0x10
0032F46F  48 33 C2                        xor rax, rdx
0032F472  48 25 FF FF 00 FC               and rax, 0xfffffffffc00ffff
0032F478  48 33 C2                        xor rax, rdx
0032F47B  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
0032F47F  E9 D0 FE FF FF                  jmp 0x14032f354
0032F484  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
0032F488  48 C1 E9 10                     shr rcx, 0x10
0032F48C  E9 96 FE FF FF                  jmp 0x14032f327
0032F491  48 0B C1                        or rax, rcx
0032F494  E9 07 FE FF FF                  jmp 0x14032f2a0
0032F499  0F 1F 80 00 00 00 00            nop dword ptr [rax]
0032F4A0  FF C7                           inc edi
0032F4A2  85 3D 04 5E C9 00               test dword ptr [rip + 0xc95e04], edi
0032F4A8  0F 84 42 02 00 00               je 0x14032f6f0
0032F4AE  F3 90                           pause
0032F4B0  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0032F4B4  48 85 C0                        test rax, rax
0032F4B7  0F 89 8E FB FF FF               jns 0x14032f04b
0032F4BD  EB E1                           jmp 0x14032f4a0
0032F4BF  49 FF C1                        inc r9
0032F4C2  45 33 C0                        xor r8d, r8d
0032F4C5  4C 89 4D 9F                     mov qword ptr [rbp - 0x61], r9
0032F4C9  4C 89 45 A7                     mov qword ptr [rbp - 0x59], r8
0032F4CD  4C 3B C9                        cmp r9, rcx
0032F4D0  0F 83 E7 FE FF FF               jae 0x14032f3bd
0032F4D6  49 8B C1                        mov rax, r9
0032F4D9  48 03 C0                        add rax, rax
0032F4DC  4D 39 44 C2 08                  cmp qword ptr [r10 + rax*8 + 8], r8
0032F4E1  0F 84 F1 FE FF FF               je 0x14032f3d8
0032F4E7  E9 CE FE FF FF                  jmp 0x14032f3ba
0032F4EC  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0032F4F0  48 C1 E2 10                     shl rdx, 0x10
0032F4F4  48 33 C2                        xor rax, rdx
0032F4F7  48 25 FF FF 00 FC               and rax, 0xfffffffffc00ffff
0032F4FD  48 33 C2                        xor rax, rdx
0032F500  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
0032F504  E9 90 FB FF FF                  jmp 0x14032f099
0032F509  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
0032F50D  48 C1 E9 10                     shr rcx, 0x10
0032F511  E9 56 FB FF FF                  jmp 0x14032f06c
0032F516  48 0B C1                        or rax, rcx
0032F519  E9 BD FA FF FF                  jmp 0x14032efdb
0032F51E  49 8B C8                        mov rcx, r8
0032F521  E8 BA 58 F6 FF                  call 0x140294de0
0032F526  E9 75 FD FF FF                  jmp 0x14032f2a0
0032F52B  4C 8B C8                        mov r9, rax
0032F52E  41 81 E1 FF 0F 00 00            and r9d, 0xfff
0032F535  49 83 F9 01                     cmp r9, 1
0032F539  0F 82 07 FC FF FF               jb 0x14032f146
0032F53F  48 C1 E8 0C                     shr rax, 0xc
0032F543  48 B9 FF FF FF FF FF FF 07 00   movabs rcx, 0x7ffffffffffff
0032F54D  48 23 C8                        and rcx, rax
0032F550  48 8B C6                        mov rax, rsi
0032F553  48 FF C9                        dec rcx
0032F556  48 C1 E8 0C                     shr rax, 0xc
0032F55A  49 03 C9                        add rcx, r9
0032F55D  48 3B C8                        cmp rcx, rax
0032F560  0F 85 E0 FB FF FF               jne 0x14032f146
0032F566  49 8B 46 48                     mov rax, qword ptr [r14 + 0x48]
0032F56A  48 85 C0                        test rax, rax
0032F56D  0F 84 D3 FB FF FF               je 0x14032f146
0032F573  48 8B 08                        mov rcx, qword ptr [rax]
0032F576  48 83 79 40 00                  cmp qword ptr [rcx + 0x40], 0
0032F57B  0F 84 C5 FB FF FF               je 0x14032f146
0032F581  8B 41 38                        mov eax, dword ptr [rcx + 0x38]
0032F584  A8 20                           test al, 0x20
0032F586  0F 85 BA FB FF FF               jne 0x14032f146
0032F58C  0F B6 41 3E                     movzx eax, byte ptr [rcx + 0x3e]
0032F590  24 0C                           and al, 0xc
0032F592  3C 04                           cmp al, 4
0032F594  0F 85 AC FB FF FF               jne 0x14032f146
0032F59A  4F 8D 04 09                     lea r8, [r9 + r9]
0032F59E  B8 80 00 00 00                  mov eax, 0x80
0032F5A3  4C 3B C0                        cmp r8, rax
0032F5A6  41 B5 01                        mov r13b, 1
0032F5A9  4C 0F 47 C0                     cmova r8, rax
0032F5AD  E9 94 FB FF FF                  jmp 0x14032f146
0032F5B2  49 8B 4F 18                     mov rcx, qword ptr [r15 + 0x18]
0032F5B6  E8 25 58 F6 FF                  call 0x140294de0
0032F5BB  E9 1B FA FF FF                  jmp 0x14032efdb
0032F5C0  48 8B 00                        mov rax, qword ptr [rax]
0032F5C3  41 0F B6 56 20                  movzx edx, byte ptr [r14 + 0x20]
0032F5C8  48 FF C8                        dec rax
0032F5CB  41 8B 4E 18                     mov ecx, dword ptr [r14 + 0x18]
0032F5CF  48 C1 E2 20                     shl rdx, 0x20
0032F5D3  48 0B D1                        or rdx, rcx
0032F5D6  48 C1 E8 0C                     shr rax, 0xc
0032F5DA  48 2B DA                        sub rbx, rdx
0032F5DD  48 3B D8                        cmp rbx, rax
0032F5E0  0F 86 77 FC FF FF               jbe 0x14032f25d
0032F5E6  E9 ED FD FF FF                  jmp 0x14032f3d8
0032F5EB  49 8B 47 38                     mov rax, qword ptr [r15 + 0x38]
0032F5EF  41 BC 00 02 00 00               mov r12d, 0x200
0032F5F5  48 C1 EE 0C                     shr rsi, 0xc
0032F5F9  48 2B D6                        sub rdx, rsi
0032F5FC  48 FF C2                        inc rdx
0032F5FF  0F 10 00                        movups xmm0, xmmword ptr [rax]
0032F602  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
0032F606  0F 29 45 87                     movaps xmmword ptr [rbp - 0x79], xmm0
0032F60A  4C 8B 55 8F                     mov r10, qword ptr [rbp - 0x71]
0032F60E  0F 29 4D 97                     movaps xmmword ptr [rbp - 0x69], xmm1
0032F612  4C 8B 4D 9F                     mov r9, qword ptr [rbp - 0x61]
0032F616  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
0032F61A  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
0032F61E  0F 29 45 A7                     movaps xmmword ptr [rbp - 0x59], xmm0
0032F622  4C 8B 45 A7                     mov r8, qword ptr [rbp - 0x59]
0032F626  0F 29 4D B7                     movaps xmmword ptr [rbp - 0x49], xmm1
0032F62A  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
0032F62E  0F 10 48 50                     movups xmm1, xmmword ptr [rax + 0x50]
0032F632  0F 29 45 C7                     movaps xmmword ptr [rbp - 0x39], xmm0
0032F636  0F 29 4D D7                     movaps xmmword ptr [rbp - 0x29], xmm1
0032F63A  F2 0F 10 48 70                  movsd xmm1, qword ptr [rax + 0x70]
0032F63F  F2 0F 11 4D F7                  movsd qword ptr [rbp - 9], xmm1
0032F644  0F 10 40 60                     movups xmm0, xmmword ptr [rax + 0x60]
0032F648  0F 29 45 E7                     movaps xmmword ptr [rbp - 0x19], xmm0
0032F64C  49 3B D4                        cmp rdx, r12
0032F64F  0F 83 34 FB FF FF               jae 0x14032f189
0032F655  4C 8B E2                        mov r12, rdx
0032F658  E9 2C FB FF FF                  jmp 0x14032f189
0032F65D  8B 05 55 74 C9 00               mov eax, dword ptr [rip + 0xc97455]
0032F663  A8 40                           test al, 0x40
0032F665  0F 84 A3 FD FF FF               je 0x14032f40e
0032F66B  E8 20 FE FD FF                  call 0x14030f490
0032F670  84 C0                           test al, al
0032F672  0F 84 96 FD FF FF               je 0x14032f40e
0032F678  8B CF                           mov ecx, edi
0032F67A  E8 E1 FD FD FF                  call 0x14030f460
0032F67F  E9 8C FD FF FF                  jmp 0x14032f410
0032F684  48 81 E6 00 00 FF FF            and rsi, 0xffffffffffff0000
0032F68B  48 C7 44 24 28 00 00 01 00      mov qword ptr [rsp + 0x28], 0x10000
0032F694  48 8B C6                        mov rax, rsi
0032F697  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0032F69C  48 C1 E8 0C                     shr rax, 0xc
0032F6A0  49 3B C0                        cmp rax, r8
0032F6A3  0F 82 67 FA FF FF               jb 0x14032f110
0032F6A9  48 8D 86 FF FF 00 00            lea rax, [rsi + 0xffff]
0032F6B0  48 C1 E8 0C                     shr rax, 0xc
0032F6B4  48 3B C2                        cmp rax, rdx
0032F6B7  0F 87 53 FA FF FF               ja 0x14032f110
0032F6BD  45 33 C9                        xor r9d, r9d
0032F6C0  66 C7 45 87 02 00               mov word ptr [rbp - 0x79], 2
0032F6C6  45 33 C0                        xor r8d, r8d
0032F6C9  48 C7 45 97 01 00 00 00         mov qword ptr [rbp - 0x69], 1
0032F6D1  4C 8D 54 24 20                  lea r10, [rsp + 0x20]
0032F6D6  4C 89 4D 9F                     mov qword ptr [rbp - 0x61], r9
0032F6DA  33 D2                           xor edx, edx
0032F6DC  4C 89 55 8F                     mov qword ptr [rbp - 0x71], r10
0032F6E0  45 8D 61 10                     lea r12d, [r9 + 0x10]
0032F6E4  4C 89 45 A7                     mov qword ptr [rbp - 0x59], r8
0032F6E8  45 33 FF                        xor r15d, r15d
0032F6EB  E9 A7 FA FF FF                  jmp 0x14032f197
0032F6F0  8B 05 C2 73 C9 00               mov eax, dword ptr [rip + 0xc973c2]
0032F6F6  A8 40                           test al, 0x40
0032F6F8  0F 84 B0 FD FF FF               je 0x14032f4ae
0032F6FE  E8 8D FD FD FF                  call 0x14030f490
0032F703  84 C0                           test al, al
0032F705  0F 84 A3 FD FF FF               je 0x14032f4ae
0032F70B  8B CF                           mov ecx, edi
0032F70D  E8 4E FD FD FF                  call 0x14030f460
0032F712  E9 99 FD FF FF                  jmp 0x14032f4b0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiResolveSharedZeroFault(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (200);
    a2 = 0;
    v_stack_p18 = 0;
    result = memset(v_stack_mD8, a2, a2 + 120, a4);
    v_stack_mE8 = v_xmm0;
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8))) >> (9);
    a3 = (a3) & (v_rdi);
    a3 = (a3) + (v_rbx);
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    a1 = (v_rbx) << (25);
    a2 = (a3) << (25);
    a2 = (a2) - (a1);
    v_stack_p20 = a1;
    a2 = (a2) >> (16);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))) == 256) goto loc_0032F5B2;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) & (31));
    result = (result) | (0xFFFFFFFFF8000020ULL);
    result = (result) << (5);
    if (*(unsigned __int64 *)(v_rip + 11529412) == 0) goto loc_0032EFDB;
    if (((result) & (*(unsigned __int64 *)(v_rip + 11529412))) == 0) goto loc_0032F516;
    result = (result) | (16);
loc_0032EFDB:
    a2 = (a2) >> (18);
    *(unsigned __int64 *)(a3) = result;
    a2 = (unsigned int)((a2) & (0x3FFFFFF8ULL));
    a2 = (a2) + (result);
    if (a2 == result) goto loc_0032F0B2;
    result = MI_READ_PTE_LOCK_FREE(a2, a2, a3, a4);
    result = (result) >> (12);
    result = (result) & (v_r13);
    v_rbx = (result + result * 2) << (4);
    v_rbx = (v_rbx) + (v_r12);
    v_rdi = 0;
loc_0032F04B:
    if (condition_is_below) goto loc_0032F4A0;
    if (condition_is_above_or_equal) goto loc_0032F509;
    a1 = (*(unsigned __int64 *)(v_rbx)) >> (32);
loc_0032F06C:
    if (condition_is_above_or_equal) goto loc_0032F4EC;
    a2 = (a1 + 1) << (32);
    result = (*(unsigned __int64 *)(v_rbx)) ^ (a2);
    result = (result) & (a1);
    result = (result) ^ (a2);
    *(unsigned __int64 *)(v_rbx) = result;
loc_0032F099:
loc_0032F0B2:
    if (*(unsigned __int64 *)(a1 + 64) == 0) goto loc_0032F110;
    v_r13 = 0;
    a3 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 64) + 32)) << (32);
    a3 = (a3) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 24)));
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 64) + 33)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 28)));
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 48))))) >> (19);
    result = (unsigned int)((result) & (3));
    if ((*(unsigned __int64 *)(v_rip - 3255118 + result * 8)) == 16) goto loc_0032F684;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (2)) != 0) goto loc_0032F5EB;
    a1 = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 48))) & (112));
    if (((unsigned __int8)(a1)) != 32) goto loc_0032F125;
loc_0032F110:
    v_rsp = (v_rsp) + (200);
    return (unsigned int)(*(unsigned int *)(a1));
loc_0032F125:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8))) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_p20 = result;
    if (!sign_flag) goto loc_0032F52B;
loc_0032F146:
    v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8))) >> (12);
    a2 = (a2) - (v_rsi);
    v_stack_mD8 = 2;
    v_stack_mD0 = v_stack_p20;
    v_stack_mC8 = 1;
    v_r12 = a2 + 1;
    if (8 <= (a2 + 1)) { v_r12 = 8; }
    a4 = 0;
    v_stack_mC0 = 0;
    result = (v_r12) << (12);
    a3 = 0;
    v_stack_p28 = result;
    v_stack_mB8 = 0;
loc_0032F189:
    a2 = 0;
    v_r15 = 0;
    if (v_r12 == 0) goto loc_0032F3D8;
loc_0032F197:
loc_0032F1A1:
    a4 = (a4) + (0);
    a3 = (a3) << (12);
    v_rsi = (*(unsigned __int64 *)(v_stack_p20 + a4 * 8)) + (a3);
    v_rsi = (v_rsi) & (0xFFFFFFFFFFFFF000ULL);
    a1 = (v_rsi) >> (9);
    v_rdi = (v_rdi) & (a1);
    v_rdi = (v_rdi) + (v_rbx);
    if (0 == 0) goto loc_0032F1E8;
    if (v_rsi != (a2 + 4096)) goto loc_0032F3D8;
    if (((v_rdi) & (0xFFFULL)) == 0) goto loc_0032F3D8;
loc_0032F1E8:
    if (v_rdi < v_r11) goto loc_0032F221;
    if (v_rdi > v_r11) goto loc_0032F221;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (1)) == 0) goto loc_0032F221;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0032F41F;
loc_0032F221:
    if (*(unsigned __int64 *)(v_rdi) != 0) goto loc_0032F377;
    v_rbx = (v_rsi) >> (12);
    result = MiGetProtoPteAddress(*(unsigned __int64 *)(a1 + 64), v_rbx, *(unsigned __int64 *)(v_rdi) + 12, v_stack_p18);
    if (result == 0) goto loc_0032F3D8;
    if (sign_flag) goto loc_0032F5C0;
loc_0032F25D:
    a2 = (v_rdi) << (25);
    a2 = (a2) - (v_stack_p20);
    a2 = (a2) >> (16);
    if (((unsigned int)((unsigned int)(v_stack_p10))) == 256) goto loc_0032F51E;
    result = (unsigned int)(((unsigned int)(v_stack_p10)) & (31));
    result = (result) | (0xFFFFFFFFF8000020ULL);
    result = (result) << (5);
    if (*(unsigned __int64 *)(v_rip + 11528703) == 0) goto loc_0032F2A0;
    if (((result) & (*(unsigned __int64 *)(v_rip + 11528703))) == 0) goto loc_0032F491;
    result = (result) | (16);
loc_0032F2A0:
    a2 = (a2) >> (18);
    *(unsigned __int64 *)(v_rdi) = result;
    a2 = (unsigned int)((a2) & (0x3FFFFFF8ULL));
    a2 = (a2) + (result);
    if (a2 == result) goto loc_0032F363;
    result = MI_READ_PTE_LOCK_FREE(a2, a2, result, v_stack_p18);
    result = (result) >> (12);
    result = (result) & (a2);
    v_rbx = (result + result * 2) << (4);
    v_rbx = (v_rbx) + (result);
    v_rdi = 0;
loc_0032F306:
    if (condition_is_below) goto loc_0032F400;
    if (condition_is_above_or_equal) goto loc_0032F484;
    a1 = (*(unsigned __int64 *)(v_rbx)) >> (32);
loc_0032F327:
    if (condition_is_above_or_equal) goto loc_0032F467;
    a2 = (a1 + 1) << (32);
    result = (*(unsigned __int64 *)(v_rbx)) ^ (a2);
    result = (result) & (a1);
    result = (result) ^ (a2);
    *(unsigned __int64 *)(v_rbx) = result;
loc_0032F354:
loc_0032F363:
loc_0032F377:
    a3 = (v_stack_mB8) + 1;
    v_stack_mB8 = a3;
    result = (v_stack_mC0) + (v_stack_mC0);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mD0 + result * 8))) & (0xFFFULL));
    a2 = (*(unsigned __int64 *)(v_stack_mD0 + result * 8 + 8)) + (0xFFFULL);
    a2 = (a2) + (a1);
    a2 = (a2) >> (12);
    if (a3 == a2) goto loc_0032F4BF;
loc_0032F3BA:
loc_0032F3BD:
    if (v_stack_mC0 == v_stack_mC8) goto loc_0032F3D8;
    v_r15 = (v_r15) + 1;
    if (v_r15 < v_r12) goto loc_0032F1A1;
loc_0032F3D8:
    if (0 == 0) goto loc_0032F110;
    v_r15 = (unsigned int)((v_r15) << (10));
    v_r15 = (unsigned int)((v_r15) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8)))));
    v_r15 = (unsigned int)((v_r15) & (0x3FC00ULL));
    v_r15 = (unsigned int)((v_r15) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8)))));
    *(unsigned int *)(v_stack_p8) = (unsigned int)(v_r15);
    goto loc_0032F110;
loc_0032F400:
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((*(unsigned int *)(v_rip + 13196964)) & ((unsigned int)(v_rdi))) == 0) goto loc_0032F65D;
loc_0032F40E:
loc_0032F410:
    if (!sign_flag) goto loc_0032F306;
    goto loc_0032F400;
loc_0032F41F:
    result = MiPteHasShadow(v_stack_p8, v_rsi, a3, v_stack_mC0);
    if (result == 0) goto loc_0032F221;
    if (*(unsigned __int64 *)(result + 1288) == 0) goto loc_0032F221;
    result = (v_rdi) >> (3);
    result = (unsigned int)((result) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (32)) != 0) {
        a3 = (a3) | (32);
    }
    a2 = (a3) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (66)) == 0) { a2 = a3; }
    goto loc_0032F221;
loc_0032F467:
    a2 = (a2) << (16);
    result = (*(unsigned __int64 *)(v_rbx + 16)) ^ (a2);
    result = (result) & (0xFFFFFFFFFC00FFFFULL);
    result = (result) ^ (a2);
    *(unsigned __int64 *)(v_rbx + 16) = result;
    goto loc_0032F354;
loc_0032F484:
    a1 = (*(unsigned __int64 *)(v_rbx + 16)) >> (16);
    goto loc_0032F327;
loc_0032F491:
    result = (result) | (a1);
    goto loc_0032F2A0;
loc_0032F4A0:
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((*(unsigned int *)(v_rip + 13196804)) & ((unsigned int)(v_rdi))) == 0) goto loc_0032F6F0;
loc_0032F4AE:
loc_0032F4B0:
    if (!sign_flag) goto loc_0032F04B;
    goto loc_0032F4A0;
loc_0032F4BF:
    a4 = (v_stack_mC0) + 1;
    a3 = 0;
    v_stack_mC0 = a4;
    v_stack_mB8 = 0;
    if (a4 >= a1) goto loc_0032F3BD;
    result = (a4) + (a4);
    if ((*(unsigned __int64 *)(v_stack_mD0 + result * 8 + 8)) == 0) goto loc_0032F3D8;
    goto loc_0032F3BA;
loc_0032F4EC:
    a2 = (a2) << (16);
    result = (*(unsigned __int64 *)(v_rbx + 16)) ^ (a2);
    result = (result) & (0xFFFFFFFFFC00FFFFULL);
    result = (result) ^ (a2);
    *(unsigned __int64 *)(v_rbx + 16) = result;
    goto loc_0032F099;
loc_0032F509:
    a1 = (*(unsigned __int64 *)(v_rbx + 16)) >> (16);
    goto loc_0032F06C;
loc_0032F516:
    result = (result) | (a1);
    goto loc_0032EFDB;
loc_0032F51E:
    result = MiMakePrototypePteDirect(0, a2, a3, a4);
    goto loc_0032F2A0;
loc_0032F52B:
    a4 = (unsigned int)((result) & (0xFFFULL));
    if (a4 < 1) goto loc_0032F146;
    result = (result) >> (12);
    a1 = (0) & (result);
    a1 = (a1) - 1;
    result = (v_rsi) >> (12);
    a1 = (a1) + (a4);
    if (a1 != result) goto loc_0032F146;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 72) == 0) goto loc_0032F146;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 72)) + 64)) == 0) goto loc_0032F146;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 72)) + 56)))) & (32)) != 0) goto loc_0032F146;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 72)) + 62)) & (12));
    if (((unsigned __int8)(result)) != 4) goto loc_0032F146;
    a3 = a4 + a4 * 1;
    if ((a4 + a4 * 1) > 128) { a3 = 128; }
    goto loc_0032F146;
loc_0032F5B2:
    result = MiMakePrototypePteDirect(*(unsigned __int64 *)(v_r15 + 24), a2, a3, a4);
    goto loc_0032EFDB;
loc_0032F5C0:
    result = (*(unsigned __int64 *)(result)) - 1;
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 64) + 32)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 24)));
    result = (result) >> (12);
    v_rbx = (v_rbx) - (a2);
    if (v_rbx <= result) goto loc_0032F25D;
    goto loc_0032F3D8;
loc_0032F5EB:
    v_rsi = (v_rsi) >> (12);
    a2 = (a2) - (v_rsi);
    a2 = (a2) + 1;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm1;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm1;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm1;
    v_stack_m68 = v_xmm1;
    v_stack_m78 = v_xmm0;
    if (a2 >= 512) goto loc_0032F189;
    goto loc_0032F189;
loc_0032F65D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13202517)))) & (64)) == 0) goto loc_0032F40E;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 24)), a2, v_stack_mB8, v_stack_mC0);
    if ((unsigned __int8)(result) == 0) goto loc_0032F40E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), a2, v_stack_mB8, v_stack_mC0);
    goto loc_0032F410;
loc_0032F684:
    v_rsi = (v_rsi) & (0xFFFFFFFFFFFF0000ULL);
    v_stack_p28 = 0x10000ULL;
    v_stack_p20 = v_rsi;
    result = (v_rsi) >> (12);
    if (result < v_stack_mB8) goto loc_0032F110;
    result = (v_rsi + 65535) >> (12);
    if (result > a2) goto loc_0032F110;
    a4 = 0;
    v_stack_mD8 = 2;
    a3 = 0;
    v_stack_mC8 = 1;
    v_stack_mC0 = 0;
    a2 = 0;
    v_stack_mD0 = v_stack_p20;
    v_stack_mB8 = 0;
    v_r15 = 0;
    goto loc_0032F197;
loc_0032F6F0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13202370)))) & (64)) == 0) goto loc_0032F4AE;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rdi)), a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0032F4AE;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), a2, a3, a4);
    goto loc_0032F4B0;
}
```

## 5. (Beta) C Style

```c
int64_t MiResolveSharedZeroFault(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (200);
    Arg2 = 0;
    v_stack_p18 = 0;
    result = memset(v_stack_mD8, Arg2, Arg2 + 120, a4);
    v_stack_mE8 = v_xmm0;
    a3 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8))) >> (9);
    a3 = (a3) & (local_rdi);
    a3 = (a3) + (local_rbx);
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    Arg1 = (local_rbx) << (25);
    Arg2 = (a3) << (25);
    Arg2 = (Arg2) - (Arg1);
    v_stack_p20 = Arg1;
    Arg2 = (Arg2) >> (16);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) == 256) goto loc_0032F5B2;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) & (31));
    result = (result) | (0xFFFFFFFFF8000020ULL);
    result = (result) << (5);
    if (*(uint64_t *)(v_rip + 0xAFECC4) == 0) goto loc_0032EFDB;
    if (((result) & (*(uint64_t *)(v_rip + 0xAFECC4))) == 0) goto loc_0032F516;
    result = (result) | (16);
loc_0032EFDB:
    Arg2 = (Arg2) >> (18);
    *(uint64_t *)(a3) = result;
    Arg2 = (uint32_t)((Arg2) & (0x3FFFFFF8ULL));
    Arg2 = (Arg2) + (result);
    if (Arg2 == result) goto loc_0032F0B2;
    result = MI_READ_PTE_LOCK_FREE(Arg2, Arg2, a3, a4);
    result = (result) >> (12);
    result = (result) & (local_r13);
    local_rbx = (result + result * 2) << (4);
    local_rbx = (local_rbx) + (local_r12);
    local_rdi = 0;
loc_0032F04B:
    if (condition_is_below) goto loc_0032F4A0;
    if (condition_is_above_or_equal) goto loc_0032F509;
    Arg1 = (*(uint64_t *)(local_rbx)) >> (32);
loc_0032F06C:
    if (condition_is_above_or_equal) goto loc_0032F4EC;
    Arg2 = (Arg1 + 1) << (32);
    result = (*(uint64_t *)(local_rbx)) ^ (Arg2);
    result = (result) & (Arg1);
    result = (result) ^ (Arg2);
    *(uint64_t *)(local_rbx) = result;
loc_0032F099:
loc_0032F0B2:
    if (*(uint64_t *)(arg1 + 0x40) == 0) goto loc_0032F110;
    local_r13 = 0;
    a3 = (*(uint8_t *)(*(uint64_t *)(arg1 + 0x40) + 0x20)) << (32);
    a3 = (a3) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x18)));
    Arg2 = (*(uint8_t *)(*(uint64_t *)(arg1 + 0x40) + 0x21)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x1C)));
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x30))))) >> (19);
    result = (uint32_t)((result) & (3));
    if ((*(uint64_t *)(v_rip - 0x31AB4E + result * 8)) == 16) goto loc_0032F684;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (2)) != 0) goto loc_0032F5EB;
    Arg1 = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x30))) & (112));
    if (((uint8_t)(Arg1)) != 32) goto loc_0032F125;
loc_0032F110:
    local_rsp = (local_rsp) + (200);
    return (uint32_t)(*(uint32_t *)(arg1));
loc_0032F125:
    result = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8))) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_p20 = result;
    if (!sign_flag) goto loc_0032F52B;
loc_0032F146:
    local_rsi = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8))) >> (12);
    Arg2 = (Arg2) - (local_rsi);
    v_stack_mD8 = 2;
    v_stack_mD0 = v_stack_p20;
    v_stack_mC8 = 1;
    local_r12 = Arg2 + 1;
    if (8 <= (Arg2 + 1)) { local_r12 = 8; }
    a4 = 0;
    v_stack_mC0 = 0;
    result = (local_r12) << (12);
    a3 = 0;
    v_stack_p28 = result;
    v_stack_mB8 = 0;
loc_0032F189:
    Arg2 = 0;
    local_r15 = 0;
    if (local_r12 == 0) goto loc_0032F3D8;
loc_0032F197:
loc_0032F1A1:
    a4 = (a4) + (0);
    a3 = (a3) << (12);
    local_rsi = (*(uint64_t *)(v_stack_p20 + a4 * 8)) + (a3);
    local_rsi = (local_rsi) & (0xFFFFFFFFFFFFF000ULL);
    Arg1 = (local_rsi) >> (9);
    local_rdi = (local_rdi) & (Arg1);
    local_rdi = (local_rdi) + (local_rbx);
    if (0 == 0) goto loc_0032F1E8;
    if (local_rsi != (Arg2 + 4096)) goto loc_0032F3D8;
    if (((local_rdi) & (0xFFFULL)) == 0) goto loc_0032F3D8;
loc_0032F1E8:
    if (local_rdi < local_r11) goto loc_0032F221;
    if (local_rdi > local_r11) goto loc_0032F221;
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (1)) == 0) goto loc_0032F221;
    Arg1 = ((((uint8_t)(*(uint64_t *)(local_rdi))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(local_rdi))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0032F41F;
loc_0032F221:
    if (*(uint64_t *)(local_rdi) != 0) goto loc_0032F377;
    local_rbx = (local_rsi) >> (12);
    result = MiGetProtoPteAddress(*(uint64_t *)(arg1 + 0x40), local_rbx, *(uint64_t *)(local_rdi) + 12, v_stack_p18);
    if (result == 0) goto loc_0032F3D8;
    if (sign_flag) goto loc_0032F5C0;
loc_0032F25D:
    Arg2 = (local_rdi) << (25);
    Arg2 = (Arg2) - (v_stack_p20);
    Arg2 = (Arg2) >> (16);
    if (((uint32_t)((uint32_t)(v_stack_p10))) == 256) goto loc_0032F51E;
    result = (uint32_t)(((uint32_t)(v_stack_p10)) & (31));
    result = (result) | (0xFFFFFFFFF8000020ULL);
    result = (result) << (5);
    if (*(uint64_t *)(v_rip + 0xAFE9FF) == 0) goto loc_0032F2A0;
    if (((result) & (*(uint64_t *)(v_rip + 0xAFE9FF))) == 0) goto loc_0032F491;
    result = (result) | (16);
loc_0032F2A0:
    Arg2 = (Arg2) >> (18);
    *(uint64_t *)(local_rdi) = result;
    Arg2 = (uint32_t)((Arg2) & (0x3FFFFFF8ULL));
    Arg2 = (Arg2) + (result);
    if (Arg2 == result) goto loc_0032F363;
    result = MI_READ_PTE_LOCK_FREE(Arg2, Arg2, result, v_stack_p18);
    result = (result) >> (12);
    result = (result) & (Arg2);
    local_rbx = (result + result * 2) << (4);
    local_rbx = (local_rbx) + (result);
    local_rdi = 0;
loc_0032F306:
    if (condition_is_below) goto loc_0032F400;
    if (condition_is_above_or_equal) goto loc_0032F484;
    Arg1 = (*(uint64_t *)(local_rbx)) >> (32);
loc_0032F327:
    if (condition_is_above_or_equal) goto loc_0032F467;
    Arg2 = (Arg1 + 1) << (32);
    result = (*(uint64_t *)(local_rbx)) ^ (Arg2);
    result = (result) & (Arg1);
    result = (result) ^ (Arg2);
    *(uint64_t *)(local_rbx) = result;
loc_0032F354:
loc_0032F363:
loc_0032F377:
    a3 = (v_stack_mB8) + 1;
    v_stack_mB8 = a3;
    result = (v_stack_mC0) + (v_stack_mC0);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mD0 + result * 8))) & (0xFFFULL));
    Arg2 = (*(uint64_t *)(v_stack_mD0 + result * 8 + 0x8)) + (0xFFFULL);
    Arg2 = (Arg2) + (Arg1);
    Arg2 = (Arg2) >> (12);
    if (a3 == Arg2) goto loc_0032F4BF;
loc_0032F3BA:
loc_0032F3BD:
    if (v_stack_mC0 == v_stack_mC8) goto loc_0032F3D8;
    local_r15 = (local_r15) + 1;
    if (local_r15 < local_r12) goto loc_0032F1A1;
loc_0032F3D8:
    if (0 == 0) goto loc_0032F110;
    local_r15 = (uint32_t)((local_r15) << (10));
    local_r15 = (uint32_t)((local_r15) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8)))));
    local_r15 = (uint32_t)((local_r15) & (0x3FC00ULL));
    local_r15 = (uint32_t)((local_r15) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8)))));
    *(uint32_t *)(v_stack_p8) = (uint32_t)(local_r15);
    goto loc_0032F110;
loc_0032F400:
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((*(uint32_t *)(v_rip + 0xC95EA4)) & ((uint32_t)(local_rdi))) == 0) goto loc_0032F65D;
loc_0032F40E:
loc_0032F410:
    if (!sign_flag) goto loc_0032F306;
    goto loc_0032F400;
loc_0032F41F:
    result = MiPteHasShadow(v_stack_p8, local_rsi, a3, v_stack_mC0);
    if (result == 0) goto loc_0032F221;
    if (*(uint64_t *)(result + 0x508) == 0) goto loc_0032F221;
    result = (local_rdi) >> (3);
    result = (uint32_t)((result) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (32)) != 0) {
        a3 = (a3) | (32);
    }
    Arg2 = (a3) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (66)) == 0) { Arg2 = a3; }
    goto loc_0032F221;
loc_0032F467:
    Arg2 = (Arg2) << (16);
    result = (*(uint64_t *)(local_rbx + 0x10)) ^ (Arg2);
    result = (result) & (0xFFFFFFFFFC00FFFFULL);
    result = (result) ^ (Arg2);
    *(uint64_t *)(local_rbx + 0x10) = result;
    goto loc_0032F354;
loc_0032F484:
    Arg1 = (*(uint64_t *)(local_rbx + 0x10)) >> (16);
    goto loc_0032F327;
loc_0032F491:
    result = (result) | (Arg1);
    goto loc_0032F2A0;
loc_0032F4A0:
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((*(uint32_t *)(v_rip + 0xC95E04)) & ((uint32_t)(local_rdi))) == 0) goto loc_0032F6F0;
loc_0032F4AE:
loc_0032F4B0:
    if (!sign_flag) goto loc_0032F04B;
    goto loc_0032F4A0;
loc_0032F4BF:
    a4 = (v_stack_mC0) + 1;
    a3 = 0;
    v_stack_mC0 = a4;
    v_stack_mB8 = 0;
    if (a4 >= Arg1) goto loc_0032F3BD;
    result = (a4) + (a4);
    if ((*(uint64_t *)(v_stack_mD0 + result * 8 + 0x8)) == 0) goto loc_0032F3D8;
    goto loc_0032F3BA;
loc_0032F4EC:
    Arg2 = (Arg2) << (16);
    result = (*(uint64_t *)(local_rbx + 0x10)) ^ (Arg2);
    result = (result) & (0xFFFFFFFFFC00FFFFULL);
    result = (result) ^ (Arg2);
    *(uint64_t *)(local_rbx + 0x10) = result;
    goto loc_0032F099;
loc_0032F509:
    Arg1 = (*(uint64_t *)(local_rbx + 0x10)) >> (16);
    goto loc_0032F06C;
loc_0032F516:
    result = (result) | (Arg1);
    goto loc_0032EFDB;
loc_0032F51E:
    result = MiMakePrototypePteDirect(0, Arg2, a3, a4);
    goto loc_0032F2A0;
loc_0032F52B:
    a4 = (uint32_t)((result) & (0xFFFULL));
    if (a4 < 1) goto loc_0032F146;
    result = (result) >> (12);
    Arg1 = (0) & (result);
    Arg1 = (Arg1) - 1;
    result = (local_rsi) >> (12);
    Arg1 = (Arg1) + (a4);
    if (Arg1 != result) goto loc_0032F146;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0x48) == 0) goto loc_0032F146;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0x48)) + 0x40)) == 0) goto loc_0032F146;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0x48)) + 0x38)))) & (32)) != 0) goto loc_0032F146;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0x48)) + 0x3E)) & (12));
    if (((uint8_t)(result)) != 4) goto loc_0032F146;
    a3 = a4 + a4 * 1;
    if ((a4 + a4 * 1) > 128) { a3 = 128; }
    goto loc_0032F146;
loc_0032F5B2:
    result = MiMakePrototypePteDirect(*(uint64_t *)(local_r15 + 0x18), Arg2, a3, a4);
    goto loc_0032EFDB;
loc_0032F5C0:
    result = (*(uint64_t *)(result)) - 1;
    Arg2 = (*(uint8_t *)(*(uint64_t *)(arg1 + 0x40) + 0x20)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x18)));
    result = (result) >> (12);
    local_rbx = (local_rbx) - (Arg2);
    if (local_rbx <= result) goto loc_0032F25D;
    goto loc_0032F3D8;
loc_0032F5EB:
    local_rsi = (local_rsi) >> (12);
    Arg2 = (Arg2) - (local_rsi);
    Arg2 = (Arg2) + 1;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm1;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm1;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm1;
    v_stack_m68 = v_xmm1;
    v_stack_m78 = v_xmm0;
    if (Arg2 >= 512) goto loc_0032F189;
    goto loc_0032F189;
loc_0032F65D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC97455)))) & (64)) == 0) goto loc_0032F40E;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x18)), Arg2, v_stack_mB8, v_stack_mC0);
    if ((uint8_t)(result) == 0) goto loc_0032F40E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), Arg2, v_stack_mB8, v_stack_mC0);
    goto loc_0032F410;
loc_0032F684:
    local_rsi = (local_rsi) & (0xFFFFFFFFFFFF0000ULL);
    v_stack_p28 = 0x10000ULL;
    v_stack_p20 = local_rsi;
    result = (local_rsi) >> (12);
    if (result < v_stack_mB8) goto loc_0032F110;
    result = (local_rsi + 65535) >> (12);
    if (result > Arg2) goto loc_0032F110;
    a4 = 0;
    v_stack_mD8 = 2;
    a3 = 0;
    v_stack_mC8 = 1;
    v_stack_mC0 = 0;
    Arg2 = 0;
    v_stack_mD0 = v_stack_p20;
    v_stack_mB8 = 0;
    local_r15 = 0;
    goto loc_0032F197;
loc_0032F6F0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC973C2)))) & (64)) == 0) goto loc_0032F4AE;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rdi)), Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0032F4AE;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), Arg2, a3, a4);
    goto loc_0032F4B0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0032EF20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
