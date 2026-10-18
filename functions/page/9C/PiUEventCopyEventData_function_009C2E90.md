# PiUEventCopyEventData

- RVA: `0x009C2E90`–`0x009C323C` (길이 `940` bytes)
- VA: `0x00000001409C2E90`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009F7CC`
- 디코드: `240`개 명령, `940/940` bytes 표시
- 미해석 바이트: `3` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x009C2F82` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009C3030` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009C3039` → [CmValidateDeviceInterfaceName](../8F/CmValidateDeviceInterfaceName_function_008F1A40.md) (function, `0x008F1A40`)
- `0x009C30C7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009C31CA` → [RtlStringCchLengthW](../../text/43/RtlStringCchLengthW_function_00435A70.md) (function, `0x00435A70`)

### Direct callers
- [PiUEventHandleGetEvent](PiUEventHandleGetEvent_function_009C2C30.md) at `0x009C2CCB`

### Static image references
- `0x009C2FB3` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x009C3048` → RVA `0x00B0D4E0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x009C2F82` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009C3030` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009C30C7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009C31CA` → [RtlStringCchLengthW](../../text/43/RtlStringCchLengthW_function_00435A70.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x009C313A` → [sub_00B2F220 + 0xC](../B2/Unknown_function_00B2F220.md) (`tail-transfer`)
  - `0x009C31EF` → [sub_00B2F220](../B2/Unknown_function_00B2F220.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009C2E90  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
009C2E95  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
009C2E9A  56                              push rsi
009C2E9B  57                              push rdi
009C2E9C  41 56                           push r14
009C2E9E  48 83 EC 20                     sub rsp, 0x20
009C2EA2  33 ED                           xor ebp, ebp
009C2EA4  44 8B DA                        mov r11d, edx
009C2EA7  48 89 6C 24 58                  mov qword ptr [rsp + 0x58], rbp
009C2EAC  4C 8B F1                        mov r14, rcx
009C2EAF  8B DD                           mov ebx, ebp
009C2EB1  83 FA 40                        cmp edx, 0x40
009C2EB4  0F 82 A5 01 00 00               jb 0x1409c305f
009C2EBA  41 39 50 48                     cmp dword ptr [r8 + 0x48], edx
009C2EBE  4D 8D 50 48                     lea r10, [r8 + 0x48]
009C2EC2  0F 87 97 01 00 00               ja 0x1409c305f
009C2EC8  41 0F B6 42 04                  movzx eax, byte ptr [r10 + 4]
009C2ECD  88 41 04                        mov byte ptr [rcx + 4], al
009C2ED0  41 0F B6 42 05                  movzx eax, byte ptr [r10 + 5]
009C2ED5  88 41 05                        mov byte ptr [rcx + 5], al
009C2ED8  41 8B 42 18                     mov eax, dword ptr [r10 + 0x18]
009C2EDC  89 41 08                        mov dword ptr [rcx + 8], eax
009C2EDF  41 0F 10 42 08                  movups xmm0, xmmword ptr [r10 + 8]
009C2EE4  0F 11 41 0C                     movups xmmword ptr [rcx + 0xc], xmm0
009C2EE8  41 8B 42 18                     mov eax, dword ptr [r10 + 0x18]
009C2EEC  83 F8 03                        cmp eax, 3
009C2EEF  0F 85 B3 00 00 00               jne 0x1409c2fa8
009C2EF5  49 8D 42 40                     lea rax, [r10 + 0x40]
009C2EF9  48 85 C0                        test rax, rax
009C2EFC  0F 84 FA 02 00 00               je 0x1409c31fc
009C2F02  41 B9 C8 00 00 00               mov r9d, 0xc8
009C2F08  41 8B C9                        mov ecx, r9d
009C2F0B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
009C2F10  66 39 18                        cmp word ptr [rax], bx
009C2F13  74 0A                           je 0x1409c2f1f
009C2F15  48 83 C0 02                     add rax, 2
009C2F19  48 83 E9 01                     sub rcx, 1
009C2F1D  75 F1                           jne 0x1409c2f10
009C2F1F  48 85 C9                        test rcx, rcx
009C2F22  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009C2F27  0F 45 DD                        cmovne ebx, ebp
009C2F2A  0F 84 D6 02 00 00               je 0x1409c3206
009C2F30  4C 2B C9                        sub r9, rcx
009C2F33  48 85 C9                        test rcx, rcx
009C2F36  74 5A                           je 0x1409c2f92
009C2F38  4D 85 C9                        test r9, r9
009C2F3B  74 55                           je 0x1409c2f92
009C2F3D  B9 F8 FF FF FF                  mov ecx, 0xfffffff8
009C2F42  42 8D 14 4D 59 00 00 00         lea edx, [r9*2 + 0x59]
009C2F4A  48 23 D1                        and rdx, rcx
009C2F4D  49 03 D2                        add rdx, r10
009C2F50  0F B7 4A 0A                     movzx ecx, word ptr [rdx + 0xa]
009C2F54  83 E9 24                        sub ecx, 0x24
009C2F57  8D 79 3C                        lea edi, [rcx + 0x3c]
009C2F5A  44 3B DF                        cmp r11d, edi
009C2F5D  0F 82 FC 00 00 00               jb 0x1409c305f
009C2F63  0F 10 42 0C                     movups xmm0, xmmword ptr [rdx + 0xc]
009C2F67  44 8B C1                        mov r8d, ecx
009C2F6A  41 0F 11 46 24                  movups xmmword ptr [r14 + 0x24], xmm0
009C2F6F  8B 42 28                        mov eax, dword ptr [rdx + 0x28]
009C2F72  48 83 C2 2C                     add rdx, 0x2c
009C2F76  41 89 4E 38                     mov dword ptr [r14 + 0x38], ecx
009C2F7A  49 8D 4E 3C                     lea rcx, [r14 + 0x3c]
009C2F7E  41 89 46 34                     mov dword ptr [r14 + 0x34], eax
009C2F82  E8 B9 38 D0 FF                  call 0x1406c6840
009C2F87  41 C7 46 1C 01 00 00 00         mov dword ptr [r14 + 0x1c], 1
009C2F8F  41 89 3E                        mov dword ptr [r14], edi
009C2F92  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
009C2F97  8B C3                           mov eax, ebx
009C2F99  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
009C2F9E  48 83 C4 20                     add rsp, 0x20
009C2FA2  41 5E                           pop r14
009C2FA4  5F                              pop rdi
009C2FA5  5E                              pop rsi
009C2FA6  C3                              ret
009C2FA7  CC                              int3
009C2FA8  FF C8                           dec eax
009C2FAA  83 F8 0A                        cmp eax, 0xa
009C2FAD  0F 87 49 02 00 00               ja 0x1409c31fc
009C2FB3  48 8D 15 46 D0 63 FF            lea rdx, [rip - 0x9c2fba]
009C2FBA  48 98                           cdqe
009C2FBC  8B 8C 82 10 32 9C 00            mov ecx, dword ptr [rdx + rax*4 + 0x9c3210]
009C2FC3  48 03 CA                        add rcx, rdx
009C2FC6  FF E1                           jmp rcx
009C2FC8  CC                              int3
009C2FC9  CC                              int3
009C2FCA  CC                              int3
009C2FCB  CC                              int3
009C2FCC  49 8D 52 48                     lea rdx, [r10 + 0x48]
009C2FD0  48 85 D2                        test rdx, rdx
009C2FD3  0F 84 23 02 00 00               je 0x1409c31fc
009C2FD9  41 B8 FF 7F 00 00               mov r8d, 0x7fff
009C2FDF  48 8B C2                        mov rax, rdx
009C2FE2  41 8B C8                        mov ecx, r8d
009C2FE5  66 39 18                        cmp word ptr [rax], bx
009C2FE8  74 0A                           je 0x1409c2ff4
009C2FEA  48 83 C0 02                     add rax, 2
009C2FEE  48 83 E9 01                     sub rcx, 1
009C2FF2  75 F1                           jne 0x1409c2fe5
009C2FF4  48 85 C9                        test rcx, rcx
009C2FF7  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009C2FFC  0F 45 DD                        cmovne ebx, ebp
009C2FFF  0F 84 A2 01 00 00               je 0x1409c31a7
009C3005  4C 2B C1                        sub r8, rcx
009C3008  48 85 C9                        test rcx, rcx
009C300B  74 85                           je 0x1409c2f92
009C300D  42 8D 3C 45 36 00 00 00         lea edi, [r8*2 + 0x36]
009C3015  44 3B DF                        cmp r11d, edi
009C3018  72 45                           jb 0x1409c305f
009C301A  41 0F 10 42 38                  movups xmm0, xmmword ptr [r10 + 0x38]
009C301F  4E 8D 04 45 02 00 00 00         lea r8, [r8*2 + 2]
009C3027  49 8D 4E 34                     lea rcx, [r14 + 0x34]
009C302B  41 0F 11 46 24                  movups xmmword ptr [r14 + 0x24], xmm0
009C3030  E8 0B 38 D0 FF                  call 0x1406c6840
009C3035  49 8D 56 34                     lea rdx, [r14 + 0x34]
009C3039  E8 02 EA F2 FF                  call 0x1408f1a40
009C303E  8B D8                           mov ebx, eax
009C3040  85 C0                           test eax, eax
009C3042  0F 88 4A FF FF FF               js 0x1409c2f92
009C3048  48 8B 05 91 A4 14 00            mov rax, qword ptr [rip + 0x14a491]
009C304F  49 89 46 34                     mov qword ptr [r14 + 0x34], rax
009C3053  41 89 6E 1C                     mov dword ptr [r14 + 0x1c], ebp
009C3057  41 89 3E                        mov dword ptr [r14], edi
009C305A  E9 33 FF FF FF                  jmp 0x1409c2f92
009C305F  BB 23 00 00 C0                  mov ebx, 0xc0000023
009C3064  E9 29 FF FF FF                  jmp 0x1409c2f92
009C3069  49 8D 52 38                     lea rdx, [r10 + 0x38]
009C306D  48 85 D2                        test rdx, rdx
009C3070  0F 84 86 01 00 00               je 0x1409c31fc
009C3076  41 B9 C8 00 00 00               mov r9d, 0xc8
009C307C  48 8B C2                        mov rax, rdx
009C307F  41 8B C9                        mov ecx, r9d
009C3082  66 39 18                        cmp word ptr [rax], bx
009C3085  74 0A                           je 0x1409c3091
009C3087  48 83 C0 02                     add rax, 2
009C308B  48 83 E9 01                     sub rcx, 1
009C308F  75 F1                           jne 0x1409c3082
009C3091  48 85 C9                        test rcx, rcx
009C3094  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009C3099  0F 45 DD                        cmovne ebx, ebp
009C309C  0F 84 52 01 00 00               je 0x1409c31f4
009C30A2  4C 2B C9                        sub r9, rcx
009C30A5  48 85 C9                        test rcx, rcx
009C30A8  0F 84 E4 FE FF FF               je 0x1409c2f92
009C30AE  42 8D 3C 4D 26 00 00 00         lea edi, [r9*2 + 0x26]
009C30B6  44 3B DF                        cmp r11d, edi
009C30B9  72 A4                           jb 0x1409c305f
009C30BB  4E 8D 04 4D 02 00 00 00         lea r8, [r9*2 + 2]
009C30C3  49 8D 4E 24                     lea rcx, [r14 + 0x24]
009C30C7  E8 74 37 D0 FF                  call 0x1406c6840
009C30CC  41 C7 46 1C 03 00 00 00         mov dword ptr [r14 + 0x1c], 3
009C30D4  41 89 3E                        mov dword ptr [r14], edi
009C30D7  E9 B6 FE FF FF                  jmp 0x1409c2f92
009C30DC  49 8D 52 38                     lea rdx, [r10 + 0x38]
009C30E0  48 85 D2                        test rdx, rdx
009C30E3  0F 84 13 01 00 00               je 0x1409c31fc
009C30E9  41 B9 C8 00 00 00               mov r9d, 0xc8
009C30EF  48 8B C2                        mov rax, rdx
009C30F2  41 8B C9                        mov ecx, r9d
009C30F5  66 39 18                        cmp word ptr [rax], bx
009C30F8  74 0A                           je 0x1409c3104
009C30FA  48 83 C0 02                     add rax, 2
009C30FE  48 83 E9 01                     sub rcx, 1
009C3102  75 F1                           jne 0x1409c30f5
009C3104  48 85 C9                        test rcx, rcx
009C3107  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009C310C  0F 45 DD                        cmovne ebx, ebp
009C310F  0F 84 9F 00 00 00               je 0x1409c31b4
009C3115  4C 2B C9                        sub r9, rcx
009C3118  48 85 C9                        test rcx, rcx
009C311B  0F 84 71 FE FF FF               je 0x1409c2f92
009C3121  42 8D 3C 4D 26 00 00 00         lea edi, [r9*2 + 0x26]
009C3129  44 3B DF                        cmp r11d, edi
009C312C  0F 82 2D FF FF FF               jb 0x1409c305f
009C3132  4E 8D 04 4D 02 00 00 00         lea r8, [r9*2 + 2]
009C313A  E9 ED C0 16 00                  jmp 0x140b2f22c
009C313F  0F 57 C0                        xorps xmm0, xmm0
009C3142  41 C7 46 34 FF FF FF FF         mov dword ptr [r14 + 0x34], 0xffffffff
009C314A  41 C7 46 1C 01 00 00 00         mov dword ptr [r14 + 0x1c], 1
009C3152  41 89 6E 38                     mov dword ptr [r14 + 0x38], ebp
009C3156  41 0F 11 46 24                  movups xmmword ptr [r14 + 0x24], xmm0
009C315B  41 C7 06 3C 00 00 00            mov dword ptr [r14], 0x3c
009C3162  E9 2B FE FF FF                  jmp 0x1409c2f92
009C3167  49 8D 52 38                     lea rdx, [r10 + 0x38]
009C316B  48 85 D2                        test rdx, rdx
009C316E  0F 84 88 00 00 00               je 0x1409c31fc
009C3174  41 B9 C8 00 00 00               mov r9d, 0xc8
009C317A  48 8B CA                        mov rcx, rdx
009C317D  41 8B C1                        mov eax, r9d
009C3180  66 39 19                        cmp word ptr [rcx], bx
009C3183  74 0A                           je 0x1409c318f
009C3185  48 83 C1 02                     add rcx, 2
009C3189  48 83 E8 01                     sub rax, 1
009C318D  75 F1                           jne 0x1409c3180
009C318F  48 85 C0                        test rax, rax
009C3192  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009C3197  0F 45 DD                        cmovne ebx, ebp
009C319A  74 13                           je 0x1409c31af
009C319C  4C 2B C8                        sub r9, rax
009C319F  48 85 C0                        test rax, rax
009C31A2  E9 74 FF FF FF                  jmp 0x1409c311b
009C31A7  4C 8B C5                        mov r8, rbp
009C31AA  E9 59 FE FF FF                  jmp 0x1409c3008
009C31AF  4C 8B CD                        mov r9, rbp
009C31B2  EB EB                           jmp 0x1409c319f
009C31B4  4C 8B CD                        mov r9, rbp
009C31B7  E9 5C FF FF FF                  jmp 0x1409c3118
009C31BC  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
009C31C1  BA C8 00 00 00                  mov edx, 0xc8
009C31C6  49 8D 4A 38                     lea rcx, [r10 + 0x38]
009C31CA  E8 A1 28 A7 FF                  call 0x140435a70
009C31CF  8B D8                           mov ebx, eax
009C31D1  85 C0                           test eax, eax
009C31D3  0F 88 B9 FD FF FF               js 0x1409c2f92
009C31D9  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
009C31DE  42 8D 3C 45 26 00 00 00         lea edi, [r8*2 + 0x26]
009C31E6  44 3B DF                        cmp r11d, edi
009C31E9  0F 82 70 FE FF FF               jb 0x1409c305f
009C31EF  E9 2C C0 16 00                  jmp 0x140b2f220
009C31F4  4C 8B CD                        mov r9, rbp
009C31F7  E9 A9 FE FF FF                  jmp 0x1409c30a5
009C31FC  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009C3201  E9 8C FD FF FF                  jmp 0x1409c2f92
009C3206  4C 8B CD                        mov r9, rbp
009C3209  E9 25 FD FF FF                  jmp 0x1409c2f33
009C320E  66 90                           nop
009C3210  3F                              .byte 0x3f
009C3211  31 9C 00 CC 2F 9C 00            xor dword ptr [rax + rax + 0x9c2fcc], ebx
009C3218  FC                              cld
009C3219  31 9C 00 67 31 9C 00            xor dword ptr [rax + rax + 0x9c3167], ebx
009C3220  FC                              cld
009C3221  31 9C 00 FC 31 9C 00            xor dword ptr [rax + rax + 0x9c31fc], ebx
009C3228  FC                              cld
009C3229  31 9C 00 FC 31 9C 00            xor dword ptr [rax + rax + 0x9c31fc], ebx
009C3230  69 30 9C 00 BC 31               imul esi, dword ptr [rax], 0x31bc009c
009C3236  9C                              pushfq
009C3237  00 DC                           add ah, bl
009C3239  30                              .byte 0x30
009C323A  9C                              pushfq
009C323B  00                              .byte 0x00
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiUEventCopyEventData(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_rsp = (v_rsp) - (32);
    v_rbp = 0;
    v_stack_p20 = 0;
    if (a2 < 64) goto loc_009C305F;
    if ((*(unsigned int *)(a3 + 72)) > a2) goto loc_009C305F;
    *(unsigned __int8 *)(a1 + 4) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 72 + 4));
    *(unsigned __int8 *)(a1 + 5) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 72 + 5));
    *(unsigned int *)(a1 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 72 + 24)));
    *(unsigned __int64 *)(a1 + 12) = v_xmm0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 72 + 24)))) != 3) goto loc_009C2FA8;
    if (a3 + 72 + 64 == 0) goto loc_009C31FC;
loc_009C2F10:
    if ((*(unsigned __int16 *)(a3 + 72 + 64)) == 0) goto loc_009C2F1F;
    result = (a3 + 72 + 64) + (2);
    a1 = (200) - (1);
    if (condition_is_not_equal) goto loc_009C2F10;
loc_009C2F1F:
    v_rbx = (unsigned int)(0xC000000DULL);
    if (a1 != 0) { v_rbx = 0; }
    if (a1 == 0) goto loc_009C3206;
    a4 = (200) - (a1);
loc_009C2F33:
    if (a1 == 0) goto loc_009C2F92;
    if (a4 == 0) goto loc_009C2F92;
    a2 = (a4 * 2 + 89) & ((unsigned int)(0xFFFFFFF8ULL));
    a2 = (a2) + (a3 + 72);
    a1 = (unsigned int)((*(unsigned __int16 *)(a2 + 10)) - (36));
    if (((unsigned int)((unsigned int)(a2))) < ((unsigned int)(a1 + 60))) goto loc_009C305F;
    *(unsigned __int64 *)(a1 + 36) = v_xmm0;
    a2 = (a2) + (44);
    *(unsigned int *)(a1 + 56) = (unsigned int)(a1);
    *(unsigned int *)(a1 + 52) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 40)));
    result = memcpy(a1 + 60, a2, (unsigned int)((unsigned int)(a1)), a4);
    *(unsigned int *)(a1 + 28) = 1;
    *(unsigned int *)(a1) = (unsigned int)(a1 + 60);
loc_009C2F92:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)(v_rbx));
loc_009C2FA8:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - 1);
    if (((unsigned int)(result)) > 10) goto loc_009C31FC;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip - 10235834 + result * 4 + 10236432))) + (v_rip - 10235834);
loc_009C305F:
    goto loc_009C2F92;
loc_009C31FC:
    goto loc_009C2F92;
loc_009C3206:
    goto loc_009C2F33;
}
```

## 5. (Beta) C Style

```c
int64_t PiUEventCopyEventData(void *Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p58;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    local_rsp = (local_rsp) - (32);
    local_rbp = 0;
    v_stack_p20 = 0;
    if (Arg2 < 64) goto loc_009C305F;
    if ((*(uint32_t *)(arg3 + 0x48)) > Arg2) goto loc_009C305F;
    *(uint8_t *)(arg1 + 0x4) = (uint8_t)(*(uint8_t *)(arg3 + 0x48 + 0x4));
    *(uint8_t *)(arg1 + 0x5) = (uint8_t)(*(uint8_t *)(arg3 + 0x48 + 0x5));
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x48 + 0x18)));
    *(uint64_t *)(arg1 + 0xC) = v_xmm0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x48 + 0x18)))) != 3) goto loc_009C2FA8;
    if (Arg3 + 72 + 64 == 0) goto loc_009C31FC;
loc_009C2F10:
    if ((*(uint16_t *)(arg3 + 0x48 + 0x40)) == 0) goto loc_009C2F1F;
    result = (Arg3 + 72 + 64) + (2);
    Arg1 = (200) - (1);
    if (condition_is_not_equal) goto loc_009C2F10;
loc_009C2F1F:
    local_rbx = (uint32_t)(0xC000000DULL);
    if (Arg1 != NULL) { local_rbx = 0; }
    if (Arg1 == NULL) goto loc_009C3206;
    a4 = (200) - (Arg1);
loc_009C2F33:
    if (Arg1 == NULL) goto loc_009C2F92;
    if (a4 == 0) goto loc_009C2F92;
    Arg2 = (a4 * 2 + 89) & ((uint32_t)(0xFFFFFFF8ULL));
    Arg2 = (Arg2) + (Arg3 + 72);
    Arg1 = (uint32_t)((*(uint16_t *)(Arg2 + 0xA)) - (36));
    if (((uint32_t)((uint32_t)(Arg2))) < ((uint32_t)(Arg1 + 60))) goto loc_009C305F;
    *(uint64_t *)(arg1 + 0x24) = v_xmm0;
    Arg2 = (Arg2) + (44);
    *(uint32_t *)(arg1 + 0x38) = (uint32_t)(Arg1);
    *(uint32_t *)(arg1 + 0x34) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x28)));
    result = memcpy(Arg1 + 60, Arg2, (uint32_t)((uint32_t)(Arg1)), a4);
    *(uint32_t *)(arg1 + 0x1C) = 1;
    *(uint32_t *)(arg1) = (uint32_t)(Arg1 + 60);
loc_009C2F92:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)(local_rbx));
loc_009C2FA8:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - 1);
    if (((uint32_t)(result)) > 10) goto loc_009C31FC;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip - 0x9C2FBA + result * 4 + 0x9C3210))) + (v_rip - 10235834);
loc_009C305F:
    goto loc_009C2F92;
loc_009C31FC:
    goto loc_009C2F92;
loc_009C3206:
    goto loc_009C2F33;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x4` | `8` | `W` |
| `Arg1` | `+ 0x5` | `8` | `W` |
| `Arg1` | `+ 0x8` | `32` | `W` |
| `Arg1` | `+ 0xC` | `128` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `W` |
| `Arg1` | `+ 0x24` | `128` | `R` |
| `Arg1` | `+ 0x34` | `32` | `W` |
| `Arg1` | `+ 0x38` | `32` | `W` |
| `Arg1` | `+ 0x3C` | `64` | `R` |
| `Arg3` | `+ 0x4` | `8` | `R` |
| `Arg3` | `+ 0x5` | `8` | `R` |
| `Arg3` | `+ 0x8` | `128` | `R` |
| `Arg3` | `+ 0x18` | `32` | `R` |
| `Arg3` | `+ 0x40` | `64` | `R` |
| `Arg3` | `+ 0x48` | `32` | `R` |
| `Arg3` | `+ 0x48` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009C2E90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
