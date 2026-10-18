# KiPreprocessFault

- RVA: `0x003D7E70`–`0x003D81DC` (길이 `876` bytes)
- VA: `0x00000001403D7E70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00093C74`
- 디코드: `218`개 명령, `876/876` bytes 표시
- 미해석 바이트: `3` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x003D7F33` → [KiOpDecode](KiOpDecode_function_003D81F0.md) (function, `0x003D81F0`)
- `0x003D7F6A` → [KiOp_Mov](KiOp_Mov_function_003D85C0.md) (function, `0x003D85C0`)
- `0x003D8048` → [KiOp_Priv](KiOp_Priv_function_003D8760.md) (function, `0x003D8760`)
- `0x003D8080` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x003D80B0` → [KiCheckForAtlThunk](KiCheckForAtlThunk_function_003D87E8.md) (function, `0x003D87E8`)
- `0x003D80D3` → [KiEnableOptionalXStateFeatures](KiEnableOptionalXStateFeatures_function_003D8BE8.md) (function, `0x003D8BE8`)
- `0x003D80F4` → [KiOpPreprocessSecureFault](KiOpPreprocessSecureFault_function_003D8B00.md) (function, `0x003D8B00`)
- `0x003D8168` → [KiOpCheckUnhandledSecurePciAccessViolation](../5C/KiOpCheckUnhandledSecurePciAccessViolation_function_005C6708.md) (function, `0x005C6708`)
- `0x003D8193` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [KiDispatchException](KiDispatchException_function_003D7650.md) at `0x003D77AE`

### Static image references
- `0x003D7EE6` → RVA `0x00FC74C0` (`ALMOSTRO`; read)
- `0x003D7EED` → RVA `0x00FC74C8` (`ALMOSTRO`; read)
- `0x003D7F56` → RVA `0x003D85C0` (`KiOp_Mov`; read)
- `0x003D7FE3` → RVA `0x006BA587` (`ExpInterlockedPopEntrySListFault`; read)
- `0x003D7FEA` → RVA `0x006BA577` (`ExpInterlockedPopEntrySListResume`; read)
- `0x003D8006` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x003D8038` → RVA `0x003D8760` (`KiOp_Priv`; read)
- `0x003D8124` → RVA `0x01201841` (`CFGRO`; read)
- `0x003D81B1` → RVA `0x3DBE83B8` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **10**
  - `0x003D8117` → [sub_006E992E](../6E/Unknown_function_006E992E.md) (`tail-transfer`)
  - `0x003D81A9` → `0x003D81E8` (`tail-transfer`)
  - `0x003D81AD` → `0x003D81EC` (`tail-transfer`)
  - `0x003D81BD` → [KiOpDecode + 0xC](KiOpDecode_function_003D81F0.md) (`tail-transfer`)
  - `0x003D81C1` → [KiOpDecode + 0x10](KiOpDecode_function_003D81F0.md) (`tail-transfer`)
  - `0x003D81C5` → [KiOpDecode + 0x14](KiOpDecode_function_003D81F0.md) (`tail-transfer`)
  - `0x003D81C9` → [KiOpDecode + 0x18](KiOpDecode_function_003D81F0.md) (`tail-transfer`)
  - `0x003D81CD` → [KiOpDecode + 0x1C](KiOpDecode_function_003D81F0.md) (`tail-transfer`)
  - `0x003D81D1` → [KiOpDecode + 0x20](KiOpDecode_function_003D81F0.md) (`tail-transfer`)
  - `0x003D81D5` → [KiOpDecode + 0x24](KiOpDecode_function_003D81F0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003D7E70  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
003D7E75  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
003D7E7A  55                              push rbp
003D7E7B  57                              push rdi
003D7E7C  41 54                           push r12
003D7E7E  41 56                           push r14
003D7E80  41 57                           push r15
003D7E82  48 8D 6C 24 C9                  lea rbp, [rsp - 0x37]
003D7E87  48 81 EC A0 00 00 00            sub rsp, 0xa0
003D7E8E  8B 01                           mov eax, dword ptr [rcx]
003D7E90  0F 57 C0                        xorps xmm0, xmm0
003D7E93  40 32 F6                        xor sil, sil
003D7E96  48 C7 45 67 FF FF FF FF         mov qword ptr [rbp + 0x67], 0xffffffffffffffff
003D7E9E  45 33 E4                        xor r12d, r12d
003D7EA1  45 0F B6 F8                     movzx r15d, r8b
003D7EA5  48 8B FA                        mov rdi, rdx
003D7EA8  48 8B D9                        mov rbx, rcx
003D7EAB  0F 11 45 C7                     movups xmmword ptr [rbp - 0x39], xmm0
003D7EAF  0F 11 45 D7                     movups xmmword ptr [rbp - 0x29], xmm0
003D7EB3  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
003D7EB7  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
003D7EBB  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
003D7EBF  0F 11 45 17                     movups xmmword ptr [rbp + 0x17], xmm0
003D7EC3  0F 11 45 27                     movups xmmword ptr [rbp + 0x27], xmm0
003D7EC7  3D 04 00 00 10                  cmp eax, 0x10000004
003D7ECC  0F 85 03 01 00 00               jne 0x1403d7fd5
003D7ED2  0F B7 47 38                     movzx eax, word ptr [rdi + 0x38]
003D7ED6  66 83 F8 10                     cmp ax, 0x10
003D7EDA  0F 84 03 01 00 00               je 0x1403d7fe3
003D7EE0  66 83 F8 33                     cmp ax, 0x33
003D7EE4  75 1B                           jne 0x1403d7f01
003D7EE6  48 8B 0D D3 F5 BE 00            mov rcx, qword ptr [rip + 0xbef5d3]
003D7EED  48 8B 15 D4 F5 BE 00            mov rdx, qword ptr [rip + 0xbef5d4]
003D7EF4  48 39 8F F8 00 00 00            cmp qword ptr [rdi + 0xf8], rcx
003D7EFB  0F 84 12 02 00 00               je 0x1403d8113
003D7F01  83 7B 18 02                     cmp dword ptr [rbx + 0x18], 2
003D7F05  41 BE 00 00 00 10               mov r14d, 0x10000000
003D7F0B  C7 03 05 00 00 C0               mov dword ptr [rbx], 0xc0000005
003D7F11  72 0A                           jb 0x1403d7f1d
003D7F13  F6 43 20 08                     test byte ptr [rbx + 0x20], 8
003D7F17  0F 85 D9 00 00 00               jne 0x1403d7ff6
003D7F1D  48 8D 45 C7                     lea rax, [rbp - 0x39]
003D7F21  45 8B CE                        mov r9d, r14d
003D7F24  45 0F B6 C7                     movzx r8d, r15b
003D7F28  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003D7F2D  48 8B D7                        mov rdx, rdi
003D7F30  48 8B CB                        mov rcx, rbx
003D7F33  E8 B8 02 00 00                  call 0x1403d81f0
003D7F38  85 C0                           test eax, eax
003D7F3A  0F 88 F0 00 00 00               js 0x1403d8030
003D7F40  40 84 F6                        test sil, sil
003D7F43  0F 85 04 02 00 00               jne 0x1403d814d
003D7F49  48 8B 75 1F                     mov rsi, qword ptr [rbp + 0x1f]
003D7F4D  48 85 F6                        test rsi, rsi
003D7F50  74 1D                           je 0x1403d7f6f
003D7F52  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
003D7F56  48 8D 0D 63 06 00 00            lea rcx, [rip + 0x663]
003D7F5D  48 3B C1                        cmp rax, rcx
003D7F60  0F 85 D2 00 00 00               jne 0x1403d8038
003D7F66  48 8D 4D C7                     lea rcx, [rbp - 0x39]
003D7F6A  E8 51 06 00 00                  call 0x1403d85c0
003D7F6F  40 32 FF                        xor dil, dil
003D7F72  85 C0                           test eax, eax
003D7F74  78 0E                           js 0x1403d7f84
003D7F76  48 85 F6                        test rsi, rsi
003D7F79  74 09                           je 0x1403d7f84
003D7F7B  0F B6 7D 27                     movzx edi, byte ptr [rbp + 0x27]
003D7F7F  40 84 FF                        test dil, dil
003D7F82  75 30                           jne 0x1403d7fb4
003D7F84  41 81 FE 00 00 00 80            cmp r14d, 0x80000000
003D7F8B  0F 84 C1 00 00 00               je 0x1403d8052
003D7F91  41 81 FE 00 00 00 08            cmp r14d, 0x8000000
003D7F98  0F 84 0E 01 00 00               je 0x1403d80ac
003D7F9E  41 81 FE 00 00 00 10            cmp r14d, 0x10000000
003D7FA5  75 0D                           jne 0x1403d7fb4
003D7FA7  F7 45 03 00 00 00 02            test dword ptr [rbp + 3], 0x2000000
003D7FAE  0F 85 AD 01 00 00               jne 0x1403d8161
003D7FB4  40 0F B6 C7                     movzx eax, dil
003D7FB8  4C 8D 9C 24 A0 00 00 00         lea r11, [rsp + 0xa0]
003D7FC0  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
003D7FC4  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
003D7FC8  49 8B E3                        mov rsp, r11
003D7FCB  41 5F                           pop r15
003D7FCD  41 5E                           pop r14
003D7FCF  41 5C                           pop r12
003D7FD1  5F                              pop rdi
003D7FD2  5D                              pop rbp
003D7FD3  C3                              ret
003D7FD4  CC                              int3
003D7FD5  2D 01 00 00 10                  sub eax, 0x10000001
003D7FDA  83 F8 0F                        cmp eax, 0xf
003D7FDD  76 27                           jbe 0x1403d8006
003D7FDF  32 C0                           xor al, al
003D7FE1  EB D5                           jmp 0x1403d7fb8
003D7FE3  48 8D 0D 9D 25 2E 00            lea rcx, [rip + 0x2e259d]
003D7FEA  48 8D 15 86 25 2E 00            lea rdx, [rip + 0x2e2586]
003D7FF1  E9 FE FE FF FF                  jmp 0x1403d7ef4
003D7FF6  45 84 FF                        test r15b, r15b
003D7FF9  74 E4                           je 0x1403d7fdf
003D7FFB  41 BE 00 00 00 08               mov r14d, 0x8000000
003D8001  E9 17 FF FF FF                  jmp 0x1403d7f1d
003D8006  48 8D 15 F3 7F C2 FF            lea rdx, [rip - 0x3d800d]
003D800D  48 98                           cdqe
003D800F  8B 8C 82 9C 81 3D 00            mov ecx, dword ptr [rdx + rax*4 + 0x3d819c]
003D8016  48 03 CA                        add rcx, rdx
003D8019  FF E1                           jmp rcx
003D801B  CC                              int3
003D801C  CC                              int3
003D801D  CC                              int3
003D801E  CC                              int3
003D801F  41 BE 00 00 00 40               mov r14d, 0x40000000
003D8025  C7 03 1D 00 00 C0               mov dword ptr [rbx], 0xc000001d
003D802B  E9 ED FE FF FF                  jmp 0x1403d7f1d
003D8030  40 32 FF                        xor dil, dil
003D8033  E9 4C FF FF FF                  jmp 0x1403d7f84
003D8038  48 8D 0D 21 07 00 00            lea rcx, [rip + 0x721]
003D803F  48 3B C1                        cmp rax, rcx
003D8042  48 8D 4D C7                     lea rcx, [rbp - 0x39]
003D8046  75 38                           jne 0x1403d8080
003D8048  E8 13 07 00 00                  call 0x1403d8760
003D804D  E9 1D FF FF FF                  jmp 0x1403d7f6f
003D8052  81 3B 05 00 00 C0               cmp dword ptr [rbx], 0xc0000005
003D8058  0F 85 56 FF FF FF               jne 0x1403d7fb4
003D805E  44 38 65 28                     cmp byte ptr [rbp + 0x28], r12b
003D8062  0F 85 4C FF FF FF               jne 0x1403d7fb4
003D8068  C7 43 18 02 00 00 00            mov dword ptr [rbx + 0x18], 2
003D806F  4C 89 63 20                     mov qword ptr [rbx + 0x20], r12
003D8073  48 C7 43 28 FF FF FF FF         mov qword ptr [rbx + 0x28], 0xffffffffffffffff
003D807B  E9 34 FF FF FF                  jmp 0x1403d7fb4
003D8080  E8 4B 2A 2E 00                  call 0x1406baad0
003D8085  E9 E5 FE FF FF                  jmp 0x1403d7f6f
003D808A  41 BE 00 00 00 80               mov r14d, 0x80000000
003D8090  C7 03 05 00 00 C0               mov dword ptr [rbx], 0xc0000005
003D8096  E9 82 FE FF FF                  jmp 0x1403d7f1d
003D809B  41 BE 00 00 00 20               mov r14d, 0x20000000
003D80A1  C7 03 94 00 00 C0               mov dword ptr [rbx], 0xc0000094
003D80A7  E9 71 FE FF FF                  jmp 0x1403d7f1d
003D80AC  48 8D 4D C7                     lea rcx, [rbp - 0x39]
003D80B0  E8 33 07 00 00                  call 0x1403d87e8
003D80B5  85 C0                           test eax, eax
003D80B7  0F 88 F7 FE FF FF               js 0x1403d7fb4
003D80BD  0F B6 7D 27                     movzx edi, byte ptr [rbp + 0x27]
003D80C1  E9 EE FE FF FF                  jmp 0x1403d7fb4
003D80C6  48 8B 53 20                     mov rdx, qword ptr [rbx + 0x20]
003D80CA  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
003D80D3  E8 10 0B 00 00                  call 0x1403d8be8
003D80D8  85 C0                           test eax, eax
003D80DA  0F 88 3F FF FF FF               js 0x1403d801f
003D80E0  B0 01                           mov al, 1
003D80E2  E9 D1 FE FF FF                  jmp 0x1403d7fb8
003D80E7  4C 8D 45 67                     lea r8, [rbp + 0x67]
003D80EB  48 8B D7                        mov rdx, rdi
003D80EE  48 8B CB                        mov rcx, rbx
003D80F1  40 B6 01                        mov sil, 1
003D80F4  E8 07 0A 00 00                  call 0x1403d8b00
003D80F9  84 C0                           test al, al
003D80FB  75 E3                           jne 0x1403d80e0
003D80FD  E9 D0 FD FF FF                  jmp 0x1403d7ed2
003D8102  C7 03 05 00 00 C0               mov dword ptr [rbx], 0xc0000005
003D8108  41 BE 00 00 00 04               mov r14d, 0x4000000
003D810E  E9 0A FE FF FF                  jmp 0x1403d7f1d
003D8113  66 83 F8 10                     cmp ax, 0x10
003D8117  0F 85 11 18 31 00               jne 0x1406e992e
003D811D  48 89 97 F8 00 00 00            mov qword ptr [rdi + 0xf8], rdx
003D8124  44 38 25 16 97 E2 00            cmp byte ptr [rip + 0xe29716], r12b
003D812B  74 B3                           je 0x1403d80e0
003D812D  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
003D8130  25 80 00 10 00                  and eax, 0x100080
003D8135  3D 80 00 10 00                  cmp eax, 0x100080
003D813A  75 A4                           jne 0x1403d80e0
003D813C  48 63 87 E8 04 00 00            movsxd rax, dword ptr [rdi + 0x4e8]
003D8143  48 89 94 38 D8 04 00 00         mov qword ptr [rax + rdi + 0x4d8], rdx
003D814B  EB 93                           jmp 0x1403d80e0
003D814D  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
003D8151  81 4D 03 00 00 00 02            or dword ptr [rbp + 3], 0x2000000
003D8158  48 89 4D 2F                     mov qword ptr [rbp + 0x2f], rcx
003D815C  E9 E8 FD FF FF                  jmp 0x1403d7f49
003D8161  48 8B D3                        mov rdx, rbx
003D8164  48 8D 4D C7                     lea rcx, [rbp - 0x39]
003D8168  E8 9B E5 1E 00                  call 0x1405c6708
003D816D  81 3B 09 00 00 10               cmp dword ptr [rbx], 0x10000009
003D8173  0F 85 3B FE FF FF               jne 0x1403d7fb4
003D8179  48 8B 43 38                     mov rax, qword ptr [rbx + 0x38]
003D817D  B9 EA 01 00 00                  mov ecx, 0x1ea
003D8182  4C 8B 4B 30                     mov r9, qword ptr [rbx + 0x30]
003D8186  4C 8B 43 28                     mov r8, qword ptr [rbx + 0x28]
003D818A  48 8B 53 20                     mov rdx, qword ptr [rbx + 0x20]
003D818E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003D8193  E8 C8 54 12 00                  call 0x1404fd660
003D8198  CC                              int3
003D8199  0F 1F 00                        nop dword ptr [rax]
003D819C  8A 80 3D 00 1F 80               mov al, byte ptr [rax - 0x7fe0ffc3]
003D81A2  3D 00 9B 80 3D                  cmp eax, 0x3d809b00
003D81A7  00 DF                           add bh, bl
003D81A9  7F 3D                           jg 0x1403d81e8
003D81AB  00 DF                           add bh, bl
003D81AD  7F 3D                           jg 0x1403d81ec
003D81AF  00 E7                           add bh, ah
003D81B1  80 3D 00 02 81 3D 00            cmp byte ptr [rip + 0x3d810200], 0
003D81B8  DF 7F 3D                        fistp qword ptr [rdi + 0x3d]
003D81BB  00 DF                           add bh, bl
003D81BD  7F 3D                           jg 0x1403d81fc
003D81BF  00 DF                           add bh, bl
003D81C1  7F 3D                           jg 0x1403d8200
003D81C3  00 DF                           add bh, bl
003D81C5  7F 3D                           jg 0x1403d8204
003D81C7  00 DF                           add bh, bl
003D81C9  7F 3D                           jg 0x1403d8208
003D81CB  00 DF                           add bh, bl
003D81CD  7F 3D                           jg 0x1403d820c
003D81CF  00 DF                           add bh, bl
003D81D1  7F 3D                           jg 0x1403d8210
003D81D3  00 DF                           add bh, bl
003D81D5  7F 3D                           jg 0x1403d8214
003D81D7  00 C6                           add dh, al
003D81D9  80                              .byte 0x80
003D81DA  3D                              .byte 0x3d
003D81DB  00                              .byte 0x00
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiPreprocessFault(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int8 v_stack_m37;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (160);
    v_rsi = 0;
    v_stack_p8 = -1;
    v_r12 = 0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) != 0x10000004ULL) goto loc_003D7FD5;
loc_003D7ED2:
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 56))) == 16) goto loc_003D7FE3;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 56))) != 51) goto loc_003D7F01;
loc_003D7EF4:
    if ((*(unsigned __int64 *)(a2 + 248)) == (*(unsigned __int64 *)(v_rip + 12514771))) goto loc_003D8113;
loc_003D7F01:
    *(unsigned int *)(a1) = 0xC0000005ULL;
    if ((*(unsigned int *)(a1 + 24)) < 2) goto loc_003D7F1D;
    if (((*(unsigned __int8 *)(a1 + 32)) & (8)) != 0) goto loc_003D7FF6;
loc_003D7F1D:
    v_stack_mA8 = v_stack_m98;
    result = KiOpDecode(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(0x10000000ULL))));
    if (sign_flag) goto loc_003D8030;
    if (0 != 0) goto loc_003D814D;
loc_003D7F49:
    if (v_stack_m40 == 0) goto loc_003D7F6F;
    if ((*(unsigned __int64 *)(v_stack_m40 + 16)) != (v_rip + 1635)) goto loc_003D8038;
    result = KiOp_Mov(v_stack_m98, a2, a3, (unsigned int)((unsigned int)((unsigned int)(0x10000000ULL))));
loc_003D7F6F:
    v_rdi = 0;
    if (sign_flag) goto loc_003D7F84;
    if (v_stack_m40 == 0) goto loc_003D7F84;
    if ((unsigned __int8)(v_stack_m38) != 0) goto loc_003D7FB4;
loc_003D7F84:
    if (((unsigned int)((unsigned int)(0x10000000ULL))) == 0x80000000ULL) goto loc_003D8052;
    if (((unsigned int)((unsigned int)(0x10000000ULL))) == 0x8000000ULL) goto loc_003D80AC;
    if (((unsigned int)((unsigned int)(0x10000000ULL))) != 0x10000000ULL) goto loc_003D7FB4;
    if (((v_stack_m5C) & (0x2000000ULL)) != 0) goto loc_003D8161;
loc_003D7FB4:
loc_003D7FB8:
    return (unsigned __int8)(v_stack_m38);
loc_003D7FD5:
    result = (unsigned int)(((unsigned __int8)(v_stack_m38)) - (0x10000001ULL));
    if (((unsigned int)(result)) <= 15) goto loc_003D8006;
loc_003D7FDF:
    result = 0;
    goto loc_003D7FB8;
loc_003D7FE3:
    goto loc_003D7EF4;
loc_003D7FF6:
    if (a3 == 0) goto loc_003D7FDF;
    goto loc_003D7F1D;
loc_003D8006:
    a1 = ((unsigned int)(*(unsigned int *)(v_rip - 4030477 + result * 4 + 4030876))) + (v_rip - 4030477);
loc_003D8030:
    v_rdi = 0;
    goto loc_003D7F84;
loc_003D8038:
    if (0 != (v_rip + 1825)) goto loc_003D8080;
    result = KiOp_Priv(v_stack_m98, v_rip - 4030477, a3, (unsigned int)((unsigned int)((unsigned int)(0x10000000ULL))));
    goto loc_003D7F6F;
loc_003D8052:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56))) != 0xC0000005ULL) goto loc_003D7FB4;
    if (v_stack_m37 != 0) goto loc_003D7FB4;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 24) = 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 32) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 40) = -1;
    goto loc_003D7FB4;
loc_003D8080:
    result = guard_dispatch_icall(v_stack_m98, v_rip - 4030477, a3, (unsigned int)((unsigned int)((unsigned int)(0x10000000ULL))));
    goto loc_003D7F6F;
loc_003D80AC:
    result = KiCheckForAtlThunk(v_stack_m98, v_rip - 4030477, a3, (unsigned int)((unsigned int)((unsigned int)(0x10000000ULL))));
    if (sign_flag) goto loc_003D7FB4;
    goto loc_003D7FB4;
loc_003D80E0:
    goto loc_003D7FB8;
loc_003D8113:
    *(unsigned __int64 *)(v_stack_m38 + 248) = v_rip - 4030477;
    if ((*(unsigned __int8 *)(v_rip + 14849814)) == 0) goto loc_003D80E0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m38 + 48))) & (0x100080ULL));
    if (((unsigned int)(result)) != 0x100080ULL) goto loc_003D80E0;
    *(unsigned __int64 *)((int)(*(unsigned int *)(v_stack_m38 + 1256)) + v_stack_m38 * 1 + 1240) = v_rip - 4030477;
    goto loc_003D80E0;
loc_003D814D:
    v_stack_m30 = v_stack_p8;
    goto loc_003D7F49;
loc_003D8161:
    result = KiOpCheckUnhandledSecurePciAccessViolation(v_stack_m98, *(unsigned __int64 *)(v_stack_m28 + 56), a3, (unsigned int)((unsigned int)((unsigned int)(0x10000000ULL))));
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56))) != 0x10000009ULL) goto loc_003D7FB4;
    v_stack_m80 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 56);
    result = KeBugCheckEx(490, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 40), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 48));
    v_rbx = (unsigned __int8)((*(unsigned __int64 *)(v_stack_m28 + 56)) + ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 56))));
    v_rbx = (unsigned __int8)((v_rbx) + ((unsigned __int8)(v_rbx)));
    v_rbx = (unsigned __int8)((v_rbx) + ((unsigned __int8)(*(unsigned __int8 *)(result - 2145451971))));
    v_rbx = (unsigned __int8)((v_rbx) + ((unsigned __int8)(v_rbx)));
    v_rbx = (unsigned __int8)((v_rbx) + ((unsigned __int8)(v_rbx)));
    v_rbx = (unsigned __int8)((v_rbx) + ((unsigned __int8)(v_rbx)));
    v_rbx = (unsigned __int8)((v_rbx) + ((unsigned __int8)(v_rbx)));
    v_rbx = (unsigned __int8)((v_rbx) + ((unsigned __int8)(v_rbx)));
    v_rbx = (unsigned __int8)((v_rbx) + ((unsigned __int8)(v_rbx)));
    v_rbx = (unsigned __int8)((v_rbx) + ((unsigned __int8)(v_rbx)));
    a2 = (unsigned __int8)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 32)) + ((unsigned __int8)(*(unsigned __int8 *)(result - 2145451971))));
    return *(unsigned __int8 *)(result - 2145451971);
}
```

## 5. (Beta) C Style

```c
int64_t KiPreprocessFault(void *Arg1, void *Arg2, uint8_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint8_t v_stack_m37;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (160);
    local_rsi = 0;
    v_stack_p8 = -1;
    local_r12 = 0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) != 0x10000004ULL) goto loc_003D7FD5;
loc_003D7ED2:
    if (((uint16_t)(*(uint16_t *)(arg2 + 0x38))) == 16) goto loc_003D7FE3;
    if (((uint16_t)(*(uint16_t *)(arg2 + 0x38))) != 51) goto loc_003D7F01;
loc_003D7EF4:
    if ((*(uint64_t *)(arg2 + 0xF8)) == (*(uint64_t *)(v_rip + 0xBEF5D3))) goto loc_003D8113;
loc_003D7F01:
    *(uint32_t *)(arg1) = 0xC0000005ULL;
    if ((*(uint32_t *)(arg1 + 0x18)) < 2) goto loc_003D7F1D;
    if (((*(uint8_t *)(arg1 + 0x20)) & (8)) != 0) goto loc_003D7FF6;
loc_003D7F1D:
    v_stack_mA8 = v_stack_m98;
    result = KiOpDecode(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(0x10000000ULL))));
    if (sign_flag) goto loc_003D8030;
    if (0 != 0) goto loc_003D814D;
loc_003D7F49:
    if (v_stack_m40 == 0) goto loc_003D7F6F;
    if ((*(uint64_t *)(v_stack_m40 + 0x10)) != (v_rip + 1635)) goto loc_003D8038;
    result = KiOp_Mov(v_stack_m98, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(0x10000000ULL))));
loc_003D7F6F:
    local_rdi = 0;
    if (sign_flag) goto loc_003D7F84;
    if (v_stack_m40 == 0) goto loc_003D7F84;
    if ((uint8_t)(v_stack_m38) != 0) goto loc_003D7FB4;
loc_003D7F84:
    if (((uint32_t)((uint32_t)(0x10000000ULL))) == 0x80000000ULL) goto loc_003D8052;
    if (((uint32_t)((uint32_t)(0x10000000ULL))) == 0x8000000ULL) goto loc_003D80AC;
    if (((uint32_t)((uint32_t)(0x10000000ULL))) != 0x10000000ULL) goto loc_003D7FB4;
    if (((v_stack_m5C) & (0x2000000ULL)) != 0) goto loc_003D8161;
loc_003D7FB4:
loc_003D7FB8:
    return (uint8_t)(v_stack_m38);
loc_003D7FD5:
    result = (uint32_t)(((uint8_t)(v_stack_m38)) - (0x10000001ULL));
    if (((uint32_t)(result)) <= 15) goto loc_003D8006;
loc_003D7FDF:
    result = 0;
    goto loc_003D7FB8;
loc_003D7FE3:
    goto loc_003D7EF4;
loc_003D7FF6:
    if (Arg3 == 0) goto loc_003D7FDF;
    goto loc_003D7F1D;
loc_003D8006:
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip - 0x3D800D + result * 4 + 0x3D819C))) + (v_rip - 4030477);
loc_003D8030:
    local_rdi = 0;
    goto loc_003D7F84;
loc_003D8038:
    if (0 != (v_rip + 1825)) goto loc_003D8080;
    result = KiOp_Priv(v_stack_m98, v_rip - 4030477, Arg3, (uint32_t)((uint32_t)((uint32_t)(0x10000000ULL))));
    goto loc_003D7F6F;
loc_003D8052:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38))) != 0xC0000005ULL) goto loc_003D7FB4;
    if (v_stack_m37 != 0) goto loc_003D7FB4;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x18) = 2;
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x20) = 0;
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x28) = -1;
    goto loc_003D7FB4;
loc_003D8080:
    result = guard_dispatch_icall(v_stack_m98, v_rip - 4030477, Arg3, (uint32_t)((uint32_t)((uint32_t)(0x10000000ULL))));
    goto loc_003D7F6F;
loc_003D80AC:
    result = KiCheckForAtlThunk(v_stack_m98, v_rip - 4030477, Arg3, (uint32_t)((uint32_t)((uint32_t)(0x10000000ULL))));
    if (sign_flag) goto loc_003D7FB4;
    goto loc_003D7FB4;
loc_003D80E0:
    goto loc_003D7FB8;
loc_003D8113:
    *(uint64_t *)(v_stack_m38 + 0xF8) = v_rip - 4030477;
    if ((*(uint8_t *)(v_rip + 0xE29716)) == 0) goto loc_003D80E0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m38 + 0x30))) & (0x100080ULL));
    if (((uint32_t)(result)) != 0x100080ULL) goto loc_003D80E0;
    *(uint64_t *)((int32_t)(*(uint32_t *)(v_stack_m38 + 0x4E8)) + v_stack_m38 * 1 + 0x4D8) = v_rip - 4030477;
    goto loc_003D80E0;
loc_003D814D:
    v_stack_m30 = v_stack_p8;
    goto loc_003D7F49;
loc_003D8161:
    result = KiOpCheckUnhandledSecurePciAccessViolation(v_stack_m98, *(uint64_t *)(v_stack_m28 + 0x38), Arg3, (uint32_t)((uint32_t)((uint32_t)(0x10000000ULL))));
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38))) != 0x10000009ULL) goto loc_003D7FB4;
    v_stack_m80 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x38);
    result = KeBugCheckEx(490, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x20), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x28), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x30));
    local_rbx = (uint8_t)((*(uint64_t *)(v_stack_m28 + 0x38)) + ((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x38))));
    local_rbx = (uint8_t)((local_rbx) + ((uint8_t)(local_rbx)));
    local_rbx = (uint8_t)((local_rbx) + ((uint8_t)(*(uint8_t *)(result - 0x7FE0FFC3))));
    local_rbx = (uint8_t)((local_rbx) + ((uint8_t)(local_rbx)));
    local_rbx = (uint8_t)((local_rbx) + ((uint8_t)(local_rbx)));
    local_rbx = (uint8_t)((local_rbx) + ((uint8_t)(local_rbx)));
    local_rbx = (uint8_t)((local_rbx) + ((uint8_t)(local_rbx)));
    local_rbx = (uint8_t)((local_rbx) + ((uint8_t)(local_rbx)));
    local_rbx = (uint8_t)((local_rbx) + ((uint8_t)(local_rbx)));
    local_rbx = (uint8_t)((local_rbx) + ((uint8_t)(local_rbx)));
    Arg2 = (uint8_t)((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x20)) + ((uint8_t)(*(uint8_t *)(result - 0x7FE0FFC3))));
    return *(uint8_t *)(result - 0x7FE0FFC3);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x18` | `32` | `W` |
| `Arg1` | `+ 0x20` | `8` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg2` | `+ 0x30` | `32` | `R` |
| `Arg2` | `+ 0x38` | `16` | `R` |
| `Arg2` | `+ 0xF8` | `64` | `R` |
| `Arg2` | `+ 0xF8` | `64` | `W` |
| `Arg2` | `+ 0x4E8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003D7E70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
