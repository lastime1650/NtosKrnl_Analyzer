# RtlpUnwindEpilogue

- RVA: `0x003F8E90`–`0x003F9268` (길이 `984` bytes)
- VA: `0x00000001403F8E90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00098338`
- 디코드: `249`개 명령, `984/984` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003F8EE5` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x003F8F43` → [RtlpUnwindOpSlots](RtlpUnwindOpSlots_function_003F9270.md) (function, `0x003F9270`)
- `0x003F8FF4` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x003F90B9` → [RtlpVirtualPopShadowStack](RtlpVirtualPopShadowStack_function_003F92C0.md) (function, `0x003F92C0`)
- `0x003F9123` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)

### Direct callers
- [RtlpxVirtualUnwind](../2F/RtlpxVirtualUnwind_function_002F5110.md) at `0x002F5536`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x003F8EE5` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x003F8FF4` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x003F9123` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x003F9251` → [sub_006EBB6A](../6E/Unknown_function_006EBB6A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003F8E90  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
003F8E95  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
003F8E9A  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
003F8E9F  53                              push rbx
003F8EA0  56                              push rsi
003F8EA1  57                              push rdi
003F8EA2  41 54                           push r12
003F8EA4  41 55                           push r13
003F8EA6  41 56                           push r14
003F8EA8  41 57                           push r15
003F8EAA  48 83 EC 50                     sub rsp, 0x50
003F8EAE  33 DB                           xor ebx, ebx
003F8EB0  44 8B FB                        mov r15d, ebx
003F8EB3  44 8B EB                        mov r13d, ebx
003F8EB6  49 BA FF FF FE FF FF 7F 00 00   movabs r10, 0x7ffffffeffff
003F8EC0  49 B8 00 00 FF FF FF 7F 00 00   movabs r8, 0x7fffffff0000
003F8ECA  45 8B 61 08                     mov r12d, dword ptr [r9 + 8]
003F8ECE  4C 03 E1                        add r12, rcx
003F8ED1  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
003F8ED6  49 3B D2                        cmp rdx, r10
003F8ED9  77 10                           ja 0x1403f8eeb
003F8EDB  41 F6 C4 03                     test r12b, 3
003F8EDF  0F 84 71 03 00 00               je 0x1403f9256
003F8EE5  E8 E6 10 4A 00                  call 0x140899fd0
003F8EEA  CC                              int3
003F8EEB  45 0F B6 74 24 02               movzx r14d, byte ptr [r12 + 2]
003F8EF1  44 89 74 24 24                  mov dword ptr [rsp + 0x24], r14d
003F8EF6  41 8B F6                        mov esi, r14d
003F8EF9  8B FB                           mov edi, ebx
003F8EFB  45 85 F6                        test r14d, r14d
003F8EFE  74 6B                           je 0x1403f8f6b
003F8F00  8B CF                           mov ecx, edi
003F8F02  41 0F B7 4C 4C 04               movzx ecx, word ptr [r12 + rcx*2 + 4]
003F8F08  0F B7 D1                        movzx edx, cx
003F8F0B  66 C1 EA 08                     shr dx, 8
003F8F0F  8A C2                           mov al, dl
003F8F11  24 0F                           and al, 0xf
003F8F13  74 3A                           je 0x1403f8f4f
003F8F15  3C 0A                           cmp al, 0xa
003F8F17  74 36                           je 0x1403f8f4f
003F8F19  3C 02                           cmp al, 2
003F8F1B  75 09                           jne 0x1403f8f26
003F8F1D  F6 C2 F0                        test dl, 0xf0
003F8F20  0F 84 CE 02 00 00               je 0x1403f91f4
003F8F26  83 C8 FF                        or eax, 0xffffffff
003F8F29  41 3B F6                        cmp esi, r14d
003F8F2C  0F 45 F0                        cmovne esi, eax
003F8F2F  0F B7 C1                        movzx eax, cx
003F8F32  66 C1 E8 08                     shr ax, 8
003F8F36  24 0F                           and al, 0xf
003F8F38  3C 02                           cmp al, 2
003F8F3A  0F 85 2A 01 00 00               jne 0x1403f906a
003F8F40  41 FF C5                        inc r13d
003F8F43  E8 28 03 00 00                  call 0x1403f9270
003F8F48  03 F8                           add edi, eax
003F8F4A  41 3B FE                        cmp edi, r14d
003F8F4D  72 B1                           jb 0x1403f8f00
003F8F4F  49 B8 00 00 FF FF FF 7F 00 00   movabs r8, 0x7fffffff0000
003F8F59  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
003F8F61  49 BA FF FF FE FF FF 7F 00 00   movabs r10, 0x7ffffffeffff
003F8F6B  41 3B FE                        cmp edi, r14d
003F8F6E  72 0B                           jb 0x1403f8f7b
003F8F70  41 F6 04 24 20                  test byte ptr [r12], 0x20
003F8F75  0F 85 BC 00 00 00               jne 0x1403f9037
003F8F7B  41 3B F6                        cmp esi, r14d
003F8F7E  0F 82 81 02 00 00               jb 0x1403f9205
003F8F84  8B D3                           mov edx, ebx
003F8F86  89 9C 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], ebx
003F8F8D  4C 8B 8C 24 B0 00 00 00         mov r9, qword ptr [rsp + 0xb0]
003F8F95  4D 8D 69 78                     lea r13, [r9 + 0x78]
003F8F99  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
003F8F9E  66 89 9C 24 90 00 00 00         mov word ptr [rsp + 0x90], bx
003F8FA6  44 8B DB                        mov r11d, ebx
003F8FA9  4C 8B 94 24 B8 00 00 00         mov r10, qword ptr [rsp + 0xb8]
003F8FB1  48 BE 00 00 FF FF FF 7F 00 00   movabs rsi, 0x7fffffff0000
003F8FBB  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
003F8FBF  44 8B FA                        mov r15d, edx
003F8FC2  89 54 24 2C                     mov dword ptr [rsp + 0x2c], edx
003F8FC6  41 3B FE                        cmp edi, r14d
003F8FC9  0F 82 F6 00 00 00               jb 0x1403f90c5
003F8FCF  49 8B 91 98 00 00 00            mov rdx, qword ptr [r9 + 0x98]
003F8FD6  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
003F8FDB  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
003F8FE5  48 39 84 24 98 00 00 00         cmp qword ptr [rsp + 0x98], rax
003F8FED  77 18                           ja 0x1403f9007
003F8FEF  F6 C2 03                        test dl, 3
003F8FF2  74 06                           je 0x1403f8ffa
003F8FF4  E8 D7 0F 4A 00                  call 0x140899fd0
003F8FF9  CC                              int3
003F8FFA  48 8B C2                        mov rax, rdx
003F8FFD  48 3B D6                        cmp rdx, rsi
003F9000  48 0F 43 C6                     cmovae rax, rsi
003F9004  90                              nop
003F9005  8A 00                           mov al, byte ptr [rax]
003F9007  EB 0F                           jmp 0x1403f9018
003F9009  4C 8B 8C 24 B0 00 00 00         mov r9, qword ptr [rsp + 0xb0]
003F9011  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
003F9016  EB 0A                           jmp 0x1403f9022
003F9018  49 8B 02                        mov rax, qword ptr [r10]
003F901B  48 85 C0                        test rax, rax
003F901E  75 60                           jne 0x1403f9080
003F9020  8B C3                           mov eax, ebx
003F9022  85 C0                           test eax, eax
003F9024  79 76                           jns 0x1403f909c
003F9026  48 83 C4 50                     add rsp, 0x50
003F902A  41 5F                           pop r15
003F902C  41 5E                           pop r14
003F902E  41 5D                           pop r13
003F9030  41 5C                           pop r12
003F9032  5F                              pop rdi
003F9033  5E                              pop rsi
003F9034  5B                              pop rbx
003F9035  C3                              ret
003F9036  CC                              int3
003F9037  41 FF C7                        inc r15d
003F903A  41 83 FF 20                     cmp r15d, 0x20
003F903E  0F 87 B7 01 00 00               ja 0x1403f91fb
003F9044  41 0F B6 4C 24 02               movzx ecx, byte ptr [r12 + 2]
003F904A  F6 C1 01                        test cl, 1
003F904D  44 8D 49 01                     lea r9d, [rcx + 1]
003F9051  44 0F 44 C9                     cmove r9d, ecx
003F9055  49 83 C1 02                     add r9, 2
003F9059  4F 8D 0C 4C                     lea r9, [r12 + r9*2]
003F905D  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
003F9065  E9 60 FE FF FF                  jmp 0x1403f8eca
003F906A  0F B7 C1                        movzx eax, cx
003F906D  66 C1 E8 08                     shr ax, 8
003F9071  24 0F                           and al, 0xf
003F9073  3C 01                           cmp al, 1
003F9075  0F 84 C5 FE FF FF               je 0x1403f8f40
003F907B  E9 C3 FE FF FF                  jmp 0x1403f8f43
003F9080  48 3B 10                        cmp rdx, qword ptr [rax]
003F9083  72 10                           jb 0x1403f9095
003F9085  49 8B 42 08                     mov rax, qword ptr [r10 + 8]
003F9089  48 8B 08                        mov rcx, qword ptr [rax]
003F908C  48 83 E9 08                     sub rcx, 8
003F9090  48 3B D1                        cmp rdx, rcx
003F9093  76 8B                           jbe 0x1403f9020
003F9095  B8 28 00 00 C0                  mov eax, 0xc0000028
003F909A  EB 8A                           jmp 0x1403f9026
003F909C  48 8B 02                        mov rax, qword ptr [rdx]
003F909F  49 89 81 F8 00 00 00            mov qword ptr [r9 + 0xf8], rax
003F90A6  49 83 81 98 00 00 00 08         add qword ptr [r9 + 0x98], 8
003F90AE  BA 01 00 00 00                  mov edx, 1
003F90B3  44 8B C2                        mov r8d, edx
003F90B6  49 8B C9                        mov rcx, r9
003F90B9  E8 02 02 00 00                  call 0x1403f92c0
003F90BE  33 C0                           xor eax, eax
003F90C0  E9 61 FF FF FF                  jmp 0x1403f9026
003F90C5  8B C7                           mov eax, edi
003F90C7  41 0F B7 4C 44 04               movzx ecx, word ptr [r12 + rax*2 + 4]
003F90CD  66 89 8C 24 90 00 00 00         mov word ptr [rsp + 0x90], cx
003F90D5  66 C1 E9 08                     shr cx, 8
003F90D9  0F B6 C1                        movzx eax, cl
003F90DC  44 8B D8                        mov r11d, eax
003F90DF  41 C1 EB 04                     shr r11d, 4
003F90E3  44 89 5C 24 28                  mov dword ptr [rsp + 0x28], r11d
003F90E8  A8 0F                           test al, 0xf
003F90EA  0F 85 2A 01 00 00               jne 0x1403f921a
003F90F0  3B 94 24 A0 00 00 00            cmp edx, dword ptr [rsp + 0xa0]
003F90F7  0F 82 B8 00 00 00               jb 0x1403f91b5
003F90FD  4D 8B 81 98 00 00 00            mov r8, qword ptr [r9 + 0x98]
003F9104  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
003F9109  48 B9 FF FF FE FF FF 7F 00 00   movabs rcx, 0x7ffffffeffff
003F9113  48 39 8C 24 98 00 00 00         cmp qword ptr [rsp + 0x98], rcx
003F911B  77 19                           ja 0x1403f9136
003F911D  41 F6 C0 03                     test r8b, 3
003F9121  74 06                           je 0x1403f9129
003F9123  E8 A8 0E 4A 00                  call 0x140899fd0
003F9128  CC                              int3
003F9129  49 8B C0                        mov rax, r8
003F912C  4C 3B C6                        cmp r8, rsi
003F912F  48 0F 43 C6                     cmovae rax, rsi
003F9133  90                              nop
003F9134  8A 00                           mov al, byte ptr [rax]
003F9136  EB 47                           jmp 0x1403f917f
003F9138  33 DB                           xor ebx, ebx
003F913A  48 BE 00 00 FF FF FF 7F 00 00   movabs rsi, 0x7fffffff0000
003F9144  4C 8B 94 24 B8 00 00 00         mov r10, qword ptr [rsp + 0xb8]
003F914C  4C 8B 8C 24 B0 00 00 00         mov r9, qword ptr [rsp + 0xb0]
003F9154  44 8B 74 24 24                  mov r14d, dword ptr [rsp + 0x24]
003F9159  8B 94 24 A8 00 00 00            mov edx, dword ptr [rsp + 0xa8]
003F9160  8B 7C 24 20                     mov edi, dword ptr [rsp + 0x20]
003F9164  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
003F9169  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
003F916E  44 8B 5C 24 28                  mov r11d, dword ptr [rsp + 0x28]
003F9173  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
003F9178  44 8B 7C 24 2C                  mov r15d, dword ptr [rsp + 0x2c]
003F917D  EB 0A                           jmp 0x1403f9189
003F917F  49 8B 02                        mov rax, qword ptr [r10]
003F9182  48 85 C0                        test rax, rax
003F9185  75 4F                           jne 0x1403f91d6
003F9187  8B C3                           mov eax, ebx
003F9189  85 C0                           test eax, eax
003F918B  0F 88 95 FE FF FF               js 0x1403f9026
003F9191  49 83 81 98 00 00 00 08         add qword ptr [r9 + 0x98], 8
003F9199  41 8B CB                        mov ecx, r11d
003F919C  49 8B 00                        mov rax, qword ptr [r8]
003F919F  49 89 44 CD 00                  mov qword ptr [r13 + rcx*8], rax
003F91A4  49 8B 42 10                     mov rax, qword ptr [r10 + 0x10]
003F91A8  48 85 C0                        test rax, rax
003F91AB  74 08                           je 0x1403f91b5
003F91AD  4C 89 84 C8 80 00 00 00         mov qword ptr [rax + rcx*8 + 0x80], r8
003F91B5  FF C2                           inc edx
003F91B7  89 94 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], edx
003F91BE  41 83 FB 08                     cmp r11d, 8
003F91C2  72 0B                           jb 0x1403f91cf
003F91C4  41 8D 57 02                     lea edx, [r15 + 2]
003F91C8  89 94 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], edx
003F91CF  FF C7                           inc edi
003F91D1  E9 E5 FD FF FF                  jmp 0x1403f8fbb
003F91D6  4C 3B 00                        cmp r8, qword ptr [rax]
003F91D9  0F 82 B6 FE FF FF               jb 0x1403f9095
003F91DF  49 8B 42 08                     mov rax, qword ptr [r10 + 8]
003F91E3  48 8B 08                        mov rcx, qword ptr [rax]
003F91E6  48 83 E9 08                     sub rcx, 8
003F91EA  4C 3B C1                        cmp r8, rcx
003F91ED  76 98                           jbe 0x1403f9187
003F91EF  E9 A1 FE FF FF                  jmp 0x1403f9095
003F91F4  8B F7                           mov esi, edi
003F91F6  E9 34 FD FF FF                  jmp 0x1403f8f2f
003F91FB  B8 FF 00 00 C0                  mov eax, 0xc00000ff
003F9200  E9 21 FE FF FF                  jmp 0x1403f9026
003F9205  41 83 FD 02                     cmp r13d, 2
003F9209  0F 85 75 FD FF FF               jne 0x1403f8f84
003F920F  41 3B FE                        cmp edi, r14d
003F9212  0F 44 FE                        cmove edi, esi
003F9215  E9 6A FD FF FF                  jmp 0x1403f8f84
003F921A  41 3B FE                        cmp edi, r14d
003F921D  0F 83 AC FD FF FF               jae 0x1403f8fcf
003F9223  8A 84 24 91 00 00 00            mov al, byte ptr [rsp + 0x91]
003F922A  24 0F                           and al, 0xf
003F922C  3C 02                           cmp al, 2
003F922E  75 18                           jne 0x1403f9248
003F9230  45 85 DB                        test r11d, r11d
003F9233  75 13                           jne 0x1403f9248
003F9235  3B 94 24 A0 00 00 00            cmp edx, dword ptr [rsp + 0xa0]
003F923C  72 08                           jb 0x1403f9246
003F923E  49 83 81 98 00 00 00 08         add qword ptr [r9 + 0x98], 8
003F9246  FF C7                           inc edi
003F9248  41 3B FE                        cmp edi, r14d
003F924B  0F 83 7E FD FF FF               jae 0x1403f8fcf
003F9251  E9 14 29 2F 00                  jmp 0x1406ebb6a
003F9256  49 8B C4                        mov rax, r12
003F9259  4D 3B E0                        cmp r12, r8
003F925C  49 0F 43 C0                     cmovae rax, r8
003F9260  90                              nop
003F9261  8A 00                           mov al, byte ptr [rax]
003F9263  E9 83 FC FF FF                  jmp 0x1403f8eeb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpUnwindEpilogue(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p24;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p2C;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p90;
    unsigned __int8 v_stack_p91;
    unsigned __int64 v_stack_p98;
    unsigned int v_stack_pA0;
    unsigned int v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (80);
    v_rbx = 0;
loc_003F8ECA:
    v_r12 = ((unsigned int)(*(unsigned int *)(a4 + 8))) + (a1);
    v_stack_m48 = v_r12;
    if (a2 > v_r10) goto loc_003F8EEB;
    if ((((unsigned __int8)(v_r12)) & (3)) == 0) goto loc_003F9256;
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
loc_003F8EEB:
    v_stack_m64 = (unsigned int)(*(unsigned __int8 *)(v_r12 + 2));
    if ((unsigned int)(*(unsigned __int8 *)(v_r12 + 2)) == 0) goto loc_003F8F6B;
loc_003F8F00:
    a2 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_r12 + 0 * 2 + 4))) >> (8));
    result = (unsigned __int8)(((unsigned __int8)(a2)) & (15));
    if (condition_is_equal) goto loc_003F8F4F;
    if (((unsigned __int8)(result)) == 10) goto loc_003F8F4F;
    if (((unsigned __int8)(result)) != 2) goto loc_003F8F26;
    if ((((unsigned __int8)(a2)) & (240)) == 0) goto loc_003F91F4;
loc_003F8F26:
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    v_rsi = (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_r12 + 2)));
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_r12 + 2))))) != ((unsigned int)(*(unsigned __int8 *)(v_r12 + 2)))) { v_rsi = (unsigned int)(result); }
loc_003F8F2F:
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_r12 + 0 * 2 + 4))) >> (8));
    result = (unsigned __int8)((result) & (15));
    if (((unsigned __int8)(result)) != 2) goto loc_003F906A;
loc_003F8F40:
    v_r13 = (unsigned int)((0) + 1);
loc_003F8F43:
    result = RtlpUnwindOpSlots(*(unsigned __int16 *)(v_r12 + 0 * 2 + 4), a2, a3, a4);
    v_rdi = (unsigned int)((0) + ((unsigned int)(result)));
    if (((unsigned int)(v_rdi)) < ((unsigned int)(*(unsigned __int8 *)(v_r12 + 2)))) goto loc_003F8F00;
loc_003F8F4F:
loc_003F8F6B:
    if (((unsigned int)(v_rdi)) < ((unsigned int)(*(unsigned __int8 *)(v_r12 + 2)))) goto loc_003F8F7B;
    if (((*(unsigned __int8 *)(v_r12)) & (32)) != 0) goto loc_003F9037;
loc_003F8F7B:
    if (((unsigned int)(v_rsi)) < ((unsigned int)(*(unsigned __int8 *)(v_r12 + 2)))) goto loc_003F9205;
loc_003F8F84:
    v_stack_p20 = 0;
    v_stack_m50 = a5 + 120;
    v_stack_p8 = 0;
loc_003F8FBB:
    v_stack_m68 = (unsigned int)(v_rdi);
    v_stack_m5C = 0;
    if (((unsigned int)(v_rdi)) < ((unsigned int)(*(unsigned __int8 *)(v_r12 + 2)))) goto loc_003F90C5;
loc_003F8FCF:
    v_stack_m58 = *(unsigned __int64 *)(a5 + 152);
    if (v_stack_p10 > result) goto loc_003F9007;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a5 + 152))) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(*(unsigned __int16 *)(v_r12 + 0 * 2 + 4), *(unsigned __int64 *)(a5 + 152), a3, a5);
    }
    result = *(unsigned __int64 *)(a5 + 152);
    if ((*(unsigned __int64 *)(a5 + 152)) >= v_rsi) { result = v_rsi; }
loc_003F9007:
    goto loc_003F9018;
loc_003F9018:
    if (*(unsigned __int64 *)(a6) != 0) goto loc_003F9080;
loc_003F9020:
loc_003F9022:
    if (!sign_flag) goto loc_003F909C;
loc_003F9026:
    v_rsp = (v_rsp) + (80);
    return 0;
loc_003F9037:
    v_r15 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r15)) > 32) goto loc_003F91FB;
    a4 = *(unsigned __int8 *)(v_r12 + 2) + 1;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r12 + 2))) & (1)) == 0) { a4 = (unsigned int)(*(unsigned __int8 *)(v_r12 + 2)); }
    a4 = (a4) + (2);
    goto loc_003F8ECA;
loc_003F906A:
    result = (unsigned __int16)(((unsigned __int16)(v_stack_p90)) >> (8));
    result = (unsigned __int8)((result) & (15));
    if (((unsigned __int8)(result)) == 1) goto loc_003F8F40;
    goto loc_003F8F43;
loc_003F9080:
    if ((*(unsigned __int64 *)(a5 + 152)) < (*(unsigned __int64 *)(result))) goto loc_003F9095;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8))) - (8);
    if ((*(unsigned __int64 *)(a5 + 152)) <= a1) goto loc_003F9020;
loc_003F9095:
    goto loc_003F9026;
loc_003F909C:
    *(unsigned __int64 *)(v_r12 + a4 * 2 + 248) = *(unsigned __int64 *)(*(unsigned __int64 *)(a5 + 152));
    result = RtlpVirtualPopShadowStack(v_r12 + a4 * 2, 1, 1, v_r12 + a4 * 2);
    result = 0;
    goto loc_003F9026;
loc_003F90C5:
    v_stack_p90 = (unsigned __int16)(*(unsigned __int16 *)(v_r12 + (unsigned int)((unsigned int)(v_rdi)) * 2 + 4));
    a1 = (unsigned __int16)((*(unsigned __int16 *)(v_r12 + (unsigned int)((unsigned int)(v_rdi)) * 2 + 4)) >> (8));
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)(a1)))) >> (4));
    v_stack_p28 = (unsigned int)(v_r11);
    if ((((unsigned __int8)((unsigned __int8)(a1))) & (15)) != 0) goto loc_003F921A;
    if (1 < v_stack_pA0) goto loc_003F91B5;
    v_stack_p30 = *(unsigned __int64 *)(v_r12 + a4 * 2 + 152);
    if (v_stack_p98 > a1) goto loc_003F9136;
    result = (unsigned __int8)(a1);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r12 + a4 * 2 + 152))) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, 1, *(unsigned __int64 *)(v_r12 + a4 * 2 + 152), v_r12 + a4 * 2);
    }
    result = *(unsigned __int64 *)(v_r12 + a4 * 2 + 152);
    if ((*(unsigned __int64 *)(v_r12 + a4 * 2 + 152)) >= v_rsi) { result = v_rsi; }
loc_003F9136:
    goto loc_003F917F;
loc_003F917F:
    if (*(unsigned __int64 *)(a6) != 0) goto loc_003F91D6;
loc_003F9187:
loc_003F9189:
    if (sign_flag) goto loc_003F9026;
    *(unsigned __int64 *)(a5 + 120 + (unsigned int)((unsigned int)(v_r11)) * 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + a4 * 2 + 152));
    if (*(unsigned __int64 *)(a6 + 16) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 16) + (unsigned int)((unsigned int)(v_r11)) * 8 + 128) = *(unsigned __int64 *)(v_r12 + a4 * 2 + 152);
    }
    a2 = (unsigned int)((1) + 1);
    v_stack_pA8 = (unsigned int)(a2);
    if (((unsigned int)(v_r11)) >= 8) {
        a2 = v_r15 + 2;
        v_stack_pA8 = (unsigned int)(a2);
    }
    v_rdi = (unsigned int)((v_rdi) + 1);
    goto loc_003F8FBB;
loc_003F91D6:
    if ((*(unsigned __int64 *)(v_r12 + a4 * 2 + 152)) < (*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 16)))) goto loc_003F9095;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8))) - (8);
    if ((*(unsigned __int64 *)(v_r12 + a4 * 2 + 152)) <= a1) goto loc_003F9187;
    goto loc_003F9095;
loc_003F91F4:
    goto loc_003F8F2F;
loc_003F91FB:
    goto loc_003F9026;
loc_003F9205:
    if (((unsigned int)(a5 + 120)) != 2) goto loc_003F8F84;
    if (((unsigned int)(v_rdi)) == ((unsigned int)(*(unsigned __int8 *)(v_r12 + 2)))) { v_rdi = (unsigned int)((unsigned int)((unsigned int)(v_rdi))); }
    goto loc_003F8F84;
loc_003F921A:
    if (((unsigned int)(v_rdi)) >= ((unsigned int)(*(unsigned __int8 *)(v_r12 + 2)))) goto loc_003F8FCF;
    result = (unsigned __int8)((v_stack_p91) & (15));
    if (((unsigned __int8)(result)) != 2) goto loc_003F9248;
    if ((unsigned int)(v_r11) != 0) goto loc_003F9248;
    if (((unsigned int)(a2)) >= v_stack_pA0) {
    }
    v_rdi = (unsigned int)((v_rdi) + 1);
loc_003F9248:
    if (((unsigned int)(v_rdi)) >= ((unsigned int)(*(unsigned __int8 *)(v_r12 + 2)))) goto loc_003F8FCF;
loc_003F9256:
    result = v_r12;
    if (v_r12 >= (*(unsigned __int64 *)(v_r12 + a4 * 2 + 152))) { result = *(unsigned __int64 *)(v_r12 + a4 * 2 + 152); }
    goto loc_003F8EEB;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpUnwindEpilogue(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, void *Arg5, int64_t Arg6)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p24;
    uint64_t v_stack_p28;
    uint32_t v_stack_p2C;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p8;
    uint64_t v_stack_p90;
    uint8_t v_stack_p91;
    uint64_t v_stack_p98;
    uint32_t v_stack_pA0;
    uint32_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (80);
    local_rbx = 0;
loc_003F8ECA:
    local_r12 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x8))) + (Arg1);
    v_stack_m48 = local_r12;
    if (Arg2 > local_r10) goto loc_003F8EEB;
    if ((((uint8_t)(local_r12)) & (3)) == 0) goto loc_003F9256;
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
loc_003F8EEB:
    v_stack_m64 = (uint32_t)(*(uint8_t *)(local_r12 + 0x2));
    if ((uint32_t)(*(uint8_t *)(local_r12 + 0x2)) == 0) goto loc_003F8F6B;
loc_003F8F00:
    Arg2 = (uint16_t)(((uint16_t)(*(uint16_t *)(local_r12 + 0x0 * 2 + 0x4))) >> (8));
    result = (uint8_t)(((uint8_t)(Arg2)) & (15));
    if (condition_is_equal) goto loc_003F8F4F;
    if (((uint8_t)(result)) == 10) goto loc_003F8F4F;
    if (((uint8_t)(result)) != 2) goto loc_003F8F26;
    if ((((uint8_t)(Arg2)) & (240)) == 0) goto loc_003F91F4;
loc_003F8F26:
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    local_rsi = (uint32_t)((uint32_t)(*(uint8_t *)(local_r12 + 0x2)));
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)(local_r12 + 0x2))))) != ((uint32_t)(*(uint8_t *)(local_r12 + 0x2)))) { local_rsi = (uint32_t)(result); }
loc_003F8F2F:
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(local_r12 + 0x0 * 2 + 0x4))) >> (8));
    result = (uint8_t)((result) & (15));
    if (((uint8_t)(result)) != 2) goto loc_003F906A;
loc_003F8F40:
    local_r13 = (uint32_t)((0) + 1);
loc_003F8F43:
    result = RtlpUnwindOpSlots(*(uint16_t *)(local_r12 + 0x0 * 2 + 0x4), Arg2, Arg3, Arg4);
    local_rdi = (uint32_t)((0) + ((uint32_t)(result)));
    if (((uint32_t)(local_rdi)) < ((uint32_t)(*(uint8_t *)(local_r12 + 0x2)))) goto loc_003F8F00;
loc_003F8F4F:
loc_003F8F6B:
    if (((uint32_t)(local_rdi)) < ((uint32_t)(*(uint8_t *)(local_r12 + 0x2)))) goto loc_003F8F7B;
    if (((*(uint8_t *)(local_r12)) & (32)) != 0) goto loc_003F9037;
loc_003F8F7B:
    if (((uint32_t)(local_rsi)) < ((uint32_t)(*(uint8_t *)(local_r12 + 0x2)))) goto loc_003F9205;
loc_003F8F84:
    v_stack_p20 = 0;
    v_stack_m50 = Arg5 + 120;
    v_stack_p8 = 0;
loc_003F8FBB:
    v_stack_m68 = (uint32_t)(local_rdi);
    v_stack_m5C = 0;
    if (((uint32_t)(local_rdi)) < ((uint32_t)(*(uint8_t *)(local_r12 + 0x2)))) goto loc_003F90C5;
loc_003F8FCF:
    v_stack_m58 = *(uint64_t *)(arg5 + 0x98);
    if (v_stack_p10 > result) goto loc_003F9007;
    if ((((uint8_t)(*(uint64_t *)(arg5 + 0x98))) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(*(uint16_t *)(local_r12 + 0x0 * 2 + 0x4), *(uint64_t *)(arg5 + 0x98), Arg3, Arg5);
    }
    result = *(uint64_t *)(arg5 + 0x98);
    if ((*(uint64_t *)(arg5 + 0x98)) >= local_rsi) { result = local_rsi; }
loc_003F9007:
    goto loc_003F9018;
loc_003F9018:
    if (*(uint64_t *)(Arg6) != 0) goto loc_003F9080;
loc_003F9020:
loc_003F9022:
    if (!sign_flag) goto loc_003F909C;
loc_003F9026:
    local_rsp = (local_rsp) + (80);
    return 0;
loc_003F9037:
    local_r15 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r15)) > 32) goto loc_003F91FB;
    Arg4 = *(uint8_t *)(local_r12 + 0x2) + 1;
    if ((((uint8_t)(*(uint8_t *)(local_r12 + 0x2))) & (1)) == 0) { Arg4 = (uint32_t)(*(uint8_t *)(local_r12 + 0x2)); }
    Arg4 = (Arg4) + (2);
    goto loc_003F8ECA;
loc_003F906A:
    result = (uint16_t)(((uint16_t)(v_stack_p90)) >> (8));
    result = (uint8_t)((result) & (15));
    if (((uint8_t)(result)) == 1) goto loc_003F8F40;
    goto loc_003F8F43;
loc_003F9080:
    if ((*(uint64_t *)(arg5 + 0x98)) < (*(uint64_t *)(result))) goto loc_003F9095;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(Arg6 + 0x8))) - (8);
    if ((*(uint64_t *)(arg5 + 0x98)) <= Arg1) goto loc_003F9020;
loc_003F9095:
    goto loc_003F9026;
loc_003F909C:
    *(uint64_t *)(local_r12 + Arg4 * 2 + 0xF8) = *(uint64_t *)(*(uint64_t *)(arg5 + 0x98));
    result = RtlpVirtualPopShadowStack(local_r12 + Arg4 * 2, 1, 1, local_r12 + Arg4 * 2);
    result = 0;
    goto loc_003F9026;
loc_003F90C5:
    v_stack_p90 = (uint16_t)(*(uint16_t *)(local_r12 + (uint32_t)((uint32_t)(local_rdi)) * 2 + 0x4));
    Arg1 = (uint16_t)((*(uint16_t *)(local_r12 + (uint32_t)((uint32_t)(local_rdi)) * 2 + 0x4)) >> (8));
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)(Arg1)))) >> (4));
    v_stack_p28 = (uint32_t)(local_r11);
    if ((((uint8_t)((uint8_t)(Arg1))) & (15)) != 0) goto loc_003F921A;
    if (1 < v_stack_pA0) goto loc_003F91B5;
    v_stack_p30 = *(uint64_t *)(local_r12 + Arg4 * 2 + 0x98);
    if (v_stack_p98 > Arg1) goto loc_003F9136;
    result = (uint8_t)(Arg1);
    if ((((uint8_t)(*(uint64_t *)(local_r12 + Arg4 * 2 + 0x98))) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, 1, *(uint64_t *)(local_r12 + Arg4 * 2 + 0x98), local_r12 + Arg4 * 2);
    }
    result = *(uint64_t *)(local_r12 + Arg4 * 2 + 0x98);
    if ((*(uint64_t *)(local_r12 + Arg4 * 2 + 0x98)) >= local_rsi) { result = local_rsi; }
loc_003F9136:
    goto loc_003F917F;
loc_003F917F:
    if (*(uint64_t *)(Arg6) != 0) goto loc_003F91D6;
loc_003F9187:
loc_003F9189:
    if (sign_flag) goto loc_003F9026;
    *(uint64_t *)(arg5 + 0x78 + (uint32_t)((uint32_t)(local_r11)) * 8) = *(uint64_t *)(*(uint64_t *)(local_r12 + Arg4 * 2 + 0x98));
    if (*(uint64_t *)(Arg6 + 0x10) != 0) {
        *(uint64_t *)(*(uint64_t *)(Arg6 + 0x10) + (uint32_t)((uint32_t)(local_r11)) * 8 + 0x80) = *(uint64_t *)(local_r12 + Arg4 * 2 + 0x98);
    }
    Arg2 = (uint32_t)((1) + 1);
    v_stack_pA8 = (uint32_t)(Arg2);
    if (((uint32_t)(local_r11)) >= 8) {
        Arg2 = local_r15 + 2;
        v_stack_pA8 = (uint32_t)(Arg2);
    }
    local_rdi = (uint32_t)((local_rdi) + 1);
    goto loc_003F8FBB;
loc_003F91D6:
    if ((*(uint64_t *)(local_r12 + Arg4 * 2 + 0x98)) < (*(uint64_t *)(*(uint64_t *)(Arg6 + 0x10)))) goto loc_003F9095;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(Arg6 + 0x8))) - (8);
    if ((*(uint64_t *)(local_r12 + Arg4 * 2 + 0x98)) <= Arg1) goto loc_003F9187;
    goto loc_003F9095;
loc_003F91F4:
    goto loc_003F8F2F;
loc_003F91FB:
    goto loc_003F9026;
loc_003F9205:
    if (((uint32_t)(Arg5 + 120)) != 2) goto loc_003F8F84;
    if (((uint32_t)(local_rdi)) == ((uint32_t)(*(uint8_t *)(local_r12 + 0x2)))) { local_rdi = (uint32_t)((uint32_t)((uint32_t)(local_rdi))); }
    goto loc_003F8F84;
loc_003F921A:
    if (((uint32_t)(local_rdi)) >= ((uint32_t)(*(uint8_t *)(local_r12 + 0x2)))) goto loc_003F8FCF;
    result = (uint8_t)((v_stack_p91) & (15));
    if (((uint8_t)(result)) != 2) goto loc_003F9248;
    if ((uint32_t)(local_r11) != 0) goto loc_003F9248;
    if (((uint32_t)(Arg2)) >= v_stack_pA0) {
    }
    local_rdi = (uint32_t)((local_rdi) + 1);
loc_003F9248:
    if (((uint32_t)(local_rdi)) >= ((uint32_t)(*(uint8_t *)(local_r12 + 0x2)))) goto loc_003F8FCF;
loc_003F9256:
    result = local_r12;
    if (local_r12 >= (*(uint64_t *)(local_r12 + Arg4 * 2 + 0x98))) { result = *(uint64_t *)(local_r12 + Arg4 * 2 + 0x98); }
    goto loc_003F8EEB;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0 + rcx*8` | `64` | `W` |
| `Arg5` | `+ 0x78` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003F8E90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
