# RtlpGenericRandomPatternWorker

- RVA: `0x003F9ED0`–`0x003FA25D` (길이 `909` bytes)
- VA: `0x00000001403F9ED0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00098474`
- 디코드: `252`개 명령, `909/909` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x003F9EFE` → [RtlpSeedGlfsr](RtlpSeedGlfsr_function_003FA270.md) (function, `0x003FA270`)

### Direct callers
- [RtlScrubMemory](RtlScrubMemory_function_003F96DC.md) at `0x003F97EB`

### Static image references
- `0x003F9EE8` → RVA `0x00002998` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003F9ED0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003F9ED5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
003F9EDA  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
003F9EDF  41 56                           push r14
003F9EE1  48 83 EC 20                     sub rsp, 0x20
003F9EE5  48 8B F9                        mov rdi, rcx
003F9EE8  4C 8D 35 A9 8A C0 FF            lea r14, [rip - 0x3f7557]
003F9EEF  33 F6                           xor esi, esi
003F9EF1  83 FE 05                        cmp esi, 5
003F9EF4  0F 83 5C 03 00 00               jae 0x1403fa256
003F9EFA  49 8B 1C F6                     mov rbx, qword ptr [r14 + rsi*8]
003F9EFE  E8 6D 03 00 00                  call 0x1403fa270
003F9F03  48 8D 97 00 10 00 00            lea rdx, [rdi + 0x1000]
003F9F0A  4C 8B D7                        mov r10, rdi
003F9F0D  4C 8B C8                        mov r9, rax
003F9F10  48 3B FA                        cmp rdi, rdx
003F9F13  73 2B                           jae 0x1403f9f40
003F9F15  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
003F9F20  49 8B C9                        mov rcx, r9
003F9F23  4D 89 0A                        mov qword ptr [r10], r9
003F9F26  4D 8B C1                        mov r8, r9
003F9F29  83 E1 0F                        and ecx, 0xf
003F9F2C  49 C1 E8 04                     shr r8, 4
003F9F30  49 83 C2 08                     add r10, 8
003F9F34  4D 8B C8                        mov r9, r8
003F9F37  4C 33 0C CB                     xor r9, qword ptr [rbx + rcx*8]
003F9F3B  4C 3B D2                        cmp r10, rdx
003F9F3E  72 E0                           jb 0x1403f9f20
003F9F40  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003F9F49  44 8B 89 E8 00 00 00            mov r9d, dword ptr [rcx + 0xe8]
003F9F50  4D 85 C9                        test r9, r9
003F9F53  74 27                           je 0x1403f9f7c
003F9F55  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
003F9F5A  4D 8D 41 FF                     lea r8, [r9 - 1]
003F9F5E  49 F7 D0                        not r8
003F9F61  4C 23 C7                        and r8, rdi
003F9F64  4C 3B C2                        cmp r8, rdx
003F9F67  73 13                           jae 0x1403f9f7c
003F9F69  0F 1F 80 00 00 00 00            nop dword ptr [rax]
003F9F70  41 0F AE 38                     clflush byte ptr [r8]
003F9F74  4D 03 C1                        add r8, r9
003F9F77  4C 3B C2                        cmp r8, rdx
003F9F7A  72 F4                           jb 0x1403f9f70
003F9F7C  4C 8B CF                        mov r9, rdi
003F9F7F  48 8B C8                        mov rcx, rax
003F9F82  4C 3B CA                        cmp r9, rdx
003F9F85  73 47                           jae 0x1403f9fce
003F9F87  41 39 09                        cmp dword ptr [r9], ecx
003F9F8A  75 29                           jne 0x1403f9fb5
003F9F8C  4C 8B D1                        mov r10, rcx
003F9F8F  41 89 09                        mov dword ptr [r9], ecx
003F9F92  49 C1 EA 20                     shr r10, 0x20
003F9F96  45 39 51 04                     cmp dword ptr [r9 + 4], r10d
003F9F9A  75 19                           jne 0x1403f9fb5
003F9F9C  4C 8B C1                        mov r8, rcx
003F9F9F  45 89 51 04                     mov dword ptr [r9 + 4], r10d
003F9FA3  41 83 E0 0F                     and r8d, 0xf
003F9FA7  48 C1 E9 04                     shr rcx, 4
003F9FAB  49 83 C1 08                     add r9, 8
003F9FAF  4A 33 0C C3                     xor rcx, qword ptr [rbx + r8*8]
003F9FB3  EB CD                           jmp 0x1403f9f82
003F9FB5  32 C0                           xor al, al
003F9FB7  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
003F9FBC  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
003F9FC1  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
003F9FC6  48 83 C4 20                     add rsp, 0x20
003F9FCA  41 5E                           pop r14
003F9FCC  C3                              ret
003F9FCD  CC                              int3
003F9FCE  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003F9FD7  44 8B 89 E8 00 00 00            mov r9d, dword ptr [rcx + 0xe8]
003F9FDE  4D 85 C9                        test r9, r9
003F9FE1  74 29                           je 0x1403fa00c
003F9FE3  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
003F9FE8  4D 8D 41 FF                     lea r8, [r9 - 1]
003F9FEC  49 F7 D0                        not r8
003F9FEF  4C 23 C7                        and r8, rdi
003F9FF2  4C 3B C2                        cmp r8, rdx
003F9FF5  73 15                           jae 0x1403fa00c
003F9FF7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
003FA000  41 0F AE 38                     clflush byte ptr [r8]
003FA004  4D 03 C1                        add r8, r9
003FA007  4C 3B C2                        cmp r8, rdx
003FA00A  72 F4                           jb 0x1403fa000
003FA00C  4C 8B D7                        mov r10, rdi
003FA00F  48 8B C8                        mov rcx, rax
003FA012  4C 3B D2                        cmp r10, rdx
003FA015  73 27                           jae 0x1403fa03e
003FA017  41 39 0A                        cmp dword ptr [r10], ecx
003FA01A  75 99                           jne 0x1403f9fb5
003FA01C  4C 8B C1                        mov r8, rcx
003FA01F  49 C1 E8 20                     shr r8, 0x20
003FA023  45 39 42 04                     cmp dword ptr [r10 + 4], r8d
003FA027  75 8C                           jne 0x1403f9fb5
003FA029  4C 8B C1                        mov r8, rcx
003FA02C  49 83 C2 08                     add r10, 8
003FA030  41 83 E0 0F                     and r8d, 0xf
003FA034  48 C1 E9 04                     shr rcx, 4
003FA038  4A 33 0C C3                     xor rcx, qword ptr [rbx + r8*8]
003FA03C  EB D4                           jmp 0x1403fa012
003FA03E  4C 8B D7                        mov r10, rdi
003FA041  4C 8B C8                        mov r9, rax
003FA044  48 3B FA                        cmp rdi, rdx
003FA047  73 2D                           jae 0x1403fa076
003FA049  0F 1F 80 00 00 00 00            nop dword ptr [rax]
003FA050  49 8B C9                        mov rcx, r9
003FA053  4D 8B C1                        mov r8, r9
003FA056  48 F7 D1                        not rcx
003FA059  49 C1 E8 04                     shr r8, 4
003FA05D  49 89 0A                        mov qword ptr [r10], rcx
003FA060  49 8B C9                        mov rcx, r9
003FA063  83 E1 0F                        and ecx, 0xf
003FA066  4D 8B C8                        mov r9, r8
003FA069  49 83 C2 08                     add r10, 8
003FA06D  4C 33 0C CB                     xor r9, qword ptr [rbx + rcx*8]
003FA071  4C 3B D2                        cmp r10, rdx
003FA074  72 DA                           jb 0x1403fa050
003FA076  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003FA07F  44 8B 89 E8 00 00 00            mov r9d, dword ptr [rcx + 0xe8]
003FA086  4D 85 C9                        test r9, r9
003FA089  74 21                           je 0x1403fa0ac
003FA08B  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
003FA090  4D 8D 41 FF                     lea r8, [r9 - 1]
003FA094  49 F7 D0                        not r8
003FA097  4C 23 C7                        and r8, rdi
003FA09A  4C 3B C2                        cmp r8, rdx
003FA09D  73 0D                           jae 0x1403fa0ac
003FA09F  90                              nop
003FA0A0  41 0F AE 38                     clflush byte ptr [r8]
003FA0A4  4D 03 C1                        add r8, r9
003FA0A7  4C 3B C2                        cmp r8, rdx
003FA0AA  72 F4                           jb 0x1403fa0a0
003FA0AC  4C 8B D7                        mov r10, rdi
003FA0AF  4C 8B C8                        mov r9, rax
003FA0B2  48 3B FA                        cmp rdi, rdx
003FA0B5  73 29                           jae 0x1403fa0e0
003FA0B7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
003FA0C0  49 8B C9                        mov rcx, r9
003FA0C3  4D 89 0A                        mov qword ptr [r10], r9
003FA0C6  4D 8B C1                        mov r8, r9
003FA0C9  83 E1 0F                        and ecx, 0xf
003FA0CC  49 C1 E8 04                     shr r8, 4
003FA0D0  49 83 C2 08                     add r10, 8
003FA0D4  4D 8B C8                        mov r9, r8
003FA0D7  4C 33 0C CB                     xor r9, qword ptr [rbx + rcx*8]
003FA0DB  4C 3B D2                        cmp r10, rdx
003FA0DE  72 E0                           jb 0x1403fa0c0
003FA0E0  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003FA0E9  44 8B 89 E8 00 00 00            mov r9d, dword ptr [rcx + 0xe8]
003FA0F0  4D 85 C9                        test r9, r9
003FA0F3  74 27                           je 0x1403fa11c
003FA0F5  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
003FA0FA  4D 8D 41 FF                     lea r8, [r9 - 1]
003FA0FE  49 F7 D0                        not r8
003FA101  4C 23 C7                        and r8, rdi
003FA104  4C 3B C2                        cmp r8, rdx
003FA107  73 13                           jae 0x1403fa11c
003FA109  0F 1F 80 00 00 00 00            nop dword ptr [rax]
003FA110  41 0F AE 38                     clflush byte ptr [r8]
003FA114  4D 03 C1                        add r8, r9
003FA117  4C 3B C2                        cmp r8, rdx
003FA11A  72 F4                           jb 0x1403fa110
003FA11C  4C 8B D7                        mov r10, rdi
003FA11F  48 8B C8                        mov rcx, rax
003FA122  4C 3B D2                        cmp r10, rdx
003FA125  73 2F                           jae 0x1403fa156
003FA127  41 39 0A                        cmp dword ptr [r10], ecx
003FA12A  0F 85 85 FE FF FF               jne 0x1403f9fb5
003FA130  4C 8B C1                        mov r8, rcx
003FA133  49 C1 E8 20                     shr r8, 0x20
003FA137  45 39 42 04                     cmp dword ptr [r10 + 4], r8d
003FA13B  0F 85 74 FE FF FF               jne 0x1403f9fb5
003FA141  4C 8B C1                        mov r8, rcx
003FA144  49 83 C2 08                     add r10, 8
003FA148  41 83 E0 0F                     and r8d, 0xf
003FA14C  48 C1 E9 04                     shr rcx, 4
003FA150  4A 33 0C C3                     xor rcx, qword ptr [rbx + r8*8]
003FA154  EB CC                           jmp 0x1403fa122
003FA156  4C 8B D2                        mov r10, rdx
003FA159  4C 8B C8                        mov r9, rax
003FA15C  0F 1F 40 00                     nop dword ptr [rax]
003FA160  49 8B C9                        mov rcx, r9
003FA163  4D 8B C1                        mov r8, r9
003FA166  48 F7 D1                        not rcx
003FA169  49 C1 E8 04                     shr r8, 4
003FA16D  49 89 4A F8                     mov qword ptr [r10 - 8], rcx
003FA171  49 83 EA 08                     sub r10, 8
003FA175  49 8B C9                        mov rcx, r9
003FA178  4D 8B C8                        mov r9, r8
003FA17B  83 E1 0F                        and ecx, 0xf
003FA17E  4C 33 0C CB                     xor r9, qword ptr [rbx + rcx*8]
003FA182  4C 3B D7                        cmp r10, rdi
003FA185  75 D9                           jne 0x1403fa160
003FA187  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003FA190  44 8B 89 E8 00 00 00            mov r9d, dword ptr [rcx + 0xe8]
003FA197  4D 85 C9                        test r9, r9
003FA19A  74 20                           je 0x1403fa1bc
003FA19C  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
003FA1A1  4D 8D 41 FF                     lea r8, [r9 - 1]
003FA1A5  49 F7 D0                        not r8
003FA1A8  4C 23 C7                        and r8, rdi
003FA1AB  4C 3B C2                        cmp r8, rdx
003FA1AE  73 0C                           jae 0x1403fa1bc
003FA1B0  41 0F AE 38                     clflush byte ptr [r8]
003FA1B4  4D 03 C1                        add r8, r9
003FA1B7  4C 3B C2                        cmp r8, rdx
003FA1BA  72 F4                           jb 0x1403fa1b0
003FA1BC  4C 8B D2                        mov r10, rdx
003FA1BF  4C 8B C8                        mov r9, rax
003FA1C2  49 8B C9                        mov rcx, r9
003FA1C5  4D 89 4A F8                     mov qword ptr [r10 - 8], r9
003FA1C9  4D 8B C1                        mov r8, r9
003FA1CC  49 83 EA 08                     sub r10, 8
003FA1D0  83 E1 0F                        and ecx, 0xf
003FA1D3  49 C1 E8 04                     shr r8, 4
003FA1D7  4D 8B C8                        mov r9, r8
003FA1DA  4C 33 0C CB                     xor r9, qword ptr [rbx + rcx*8]
003FA1DE  4C 3B D7                        cmp r10, rdi
003FA1E1  75 DF                           jne 0x1403fa1c2
003FA1E3  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003FA1EC  44 8B 89 E8 00 00 00            mov r9d, dword ptr [rcx + 0xe8]
003FA1F3  4D 85 C9                        test r9, r9
003FA1F6  74 28                           je 0x1403fa220
003FA1F8  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
003FA1FD  4D 8D 41 FF                     lea r8, [r9 - 1]
003FA201  49 F7 D0                        not r8
003FA204  4C 23 C7                        and r8, rdi
003FA207  4C 3B C2                        cmp r8, rdx
003FA20A  73 14                           jae 0x1403fa220
003FA20C  0F 1F 40 00                     nop dword ptr [rax]
003FA210  41 0F AE 38                     clflush byte ptr [r8]
003FA214  4D 03 C1                        add r8, r9
003FA217  4C 3B C2                        cmp r8, rdx
003FA21A  72 F4                           jb 0x1403fa210
003FA21C  0F 1F 40 00                     nop dword ptr [rax]
003FA220  48 8B C8                        mov rcx, rax
003FA223  48 C1 E9 20                     shr rcx, 0x20
003FA227  39 4A FC                        cmp dword ptr [rdx - 4], ecx
003FA22A  0F 85 85 FD FF FF               jne 0x1403f9fb5
003FA230  48 83 EA 08                     sub rdx, 8
003FA234  39 02                           cmp dword ptr [rdx], eax
003FA236  0F 85 79 FD FF FF               jne 0x1403f9fb5
003FA23C  48 8B C8                        mov rcx, rax
003FA23F  48 C1 E8 04                     shr rax, 4
003FA243  83 E1 0F                        and ecx, 0xf
003FA246  48 33 04 CB                     xor rax, qword ptr [rbx + rcx*8]
003FA24A  48 3B D7                        cmp rdx, rdi
003FA24D  75 D1                           jne 0x1403fa220
003FA24F  FF C6                           inc esi
003FA251  E9 9B FC FF FF                  jmp 0x1403f9ef1
003FA256  B0 01                           mov al, 1
003FA258  E9 5A FD FF FF                  jmp 0x1403f9fb7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpGenericRandomPatternWorker(__int64 a1)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m28;
    unsigned int v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (32);
    v_rsi = 0;
loc_003F9EF1:
    if (0 >= 5) goto loc_003FA256;
    result = RtlpSeedGlfsr(a1, a2, a3, a4);
    if (a1 >= (a1 + 4096)) goto loc_003F9F40;
loc_003F9F20:
    *(unsigned __int64 *)(a1) = result;
    a1 = (unsigned int)((result) & (15));
    a3 = (result) >> (4);
    v_r10 = (a1) + (8);
    a4 = (a3) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 4158807 + v_rsi * 8) + a1 * 8));
    if (v_r10 < (a1 + 4096)) goto loc_003F9F20;
loc_003F9F40:
    if ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) == 0) goto loc_003F9F7C;
    a3 = ~((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) - 1);
    a3 = (a3) & (a1);
    if (a3 >= (a1 + 4096)) goto loc_003F9F7C;
loc_003F9F70:
    a3 = (a3) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)));
    if (a3 < (a1 + 4096)) goto loc_003F9F70;
loc_003F9F7C:
loc_003F9F82:
    if (a1 >= (a1 + 4096)) goto loc_003F9FCE;
    if ((*(unsigned int *)(a1)) != ((unsigned int)(result))) goto loc_003F9FB5;
    *(unsigned int *)(a1) = (unsigned int)(result);
    v_r10 = (result) >> (32);
    if ((*(unsigned int *)(a1 + 4)) != ((unsigned int)(v_r10))) goto loc_003F9FB5;
    *(unsigned int *)(a1 + 4) = (unsigned int)(v_r10);
    a3 = (unsigned int)((result) & (15));
    a1 = (result) >> (4);
    a4 = (a1) + (8);
    a1 = (a1) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 4158807 + v_rsi * 8) + a3 * 8));
    goto loc_003F9F82;
loc_003F9FB5:
    result = 0;
loc_003F9FB7:
    v_rsp = (v_rsp) + (32);
    return result;
loc_003F9FCE:
    if ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) == 0) goto loc_003FA00C;
    a3 = ~((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) - 1);
    a3 = (a3) & (v_stack_p18);
    if (a3 >= (a1 + 4096)) goto loc_003FA00C;
loc_003FA000:
    a3 = (a3) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)));
    if (a3 < (a1 + 4096)) goto loc_003FA000;
loc_003FA00C:
loc_003FA012:
    if (v_stack_p18 >= (a1 + 4096)) goto loc_003FA03E;
    if ((*(unsigned int *)(v_stack_p18)) != 0) goto loc_003F9FB5;
    a3 = (0) >> (32);
    if ((*(unsigned int *)(v_stack_p18 + 4)) != ((unsigned int)(a3))) goto loc_003F9FB5;
    v_r10 = (v_stack_p18) + (8);
    a3 = (unsigned int)((0) & (15));
    a1 = (0) >> (4);
    a1 = (a1) ^ (*(unsigned __int64 *)(v_stack_p8 + a3 * 8));
    goto loc_003FA012;
loc_003FA03E:
    if (v_stack_p18 >= (a1 + 4096)) goto loc_003FA076;
loc_003FA050:
    a1 = ~(0);
    a3 = (0) >> (4);
    *(unsigned __int64 *)(v_stack_p18) = a1;
    a1 = (unsigned int)((0) & (15));
    v_r10 = (v_stack_p18) + (8);
    a4 = (a3) ^ (*(unsigned __int64 *)(v_stack_p8 + a1 * 8));
    if (v_r10 < (a1 + 4096)) goto loc_003FA050;
loc_003FA076:
    if ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) == 0) goto loc_003FA0AC;
    a3 = ~((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) - 1);
    a3 = (a3) & (v_stack_p18);
    if (a3 >= (a1 + 4096)) goto loc_003FA0AC;
loc_003FA0A0:
    a3 = (a3) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)));
    if (a3 < (a1 + 4096)) goto loc_003FA0A0;
loc_003FA0AC:
    if (v_stack_p18 >= (a1 + 4096)) goto loc_003FA0E0;
loc_003FA0C0:
    *(unsigned __int64 *)(v_stack_p18) = 0;
    a1 = (unsigned int)((0) & (15));
    a3 = (0) >> (4);
    v_r10 = (v_stack_p18) + (8);
    a4 = (a3) ^ (*(unsigned __int64 *)(v_stack_p8 + a1 * 8));
    if (v_r10 < (a1 + 4096)) goto loc_003FA0C0;
loc_003FA0E0:
    if ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) == 0) goto loc_003FA11C;
    a3 = ~((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) - 1);
    a3 = (a3) & (v_stack_p18);
    if (a3 >= (a1 + 4096)) goto loc_003FA11C;
loc_003FA110:
    a3 = (a3) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)));
    if (a3 < (a1 + 4096)) goto loc_003FA110;
loc_003FA11C:
loc_003FA122:
    if (v_stack_p18 >= (a1 + 4096)) goto loc_003FA156;
    if ((*(unsigned int *)(v_stack_p18)) != 0) goto loc_003F9FB5;
    a3 = (0) >> (32);
    if ((*(unsigned int *)(v_stack_p18 + 4)) != ((unsigned int)(a3))) goto loc_003F9FB5;
    v_r10 = (v_stack_p18) + (8);
    a3 = (unsigned int)((0) & (15));
    a1 = (0) >> (4);
    a1 = (a1) ^ (*(unsigned __int64 *)(v_stack_p8 + a3 * 8));
    goto loc_003FA122;
loc_003FA156:
loc_003FA160:
    a1 = ~(0);
    a3 = (0) >> (4);
    *(unsigned __int64 *)(a1 + 4096 - 8) = a1;
    v_r10 = (a1 + 4096) - (8);
    a1 = (unsigned int)((0) & (15));
    a4 = (a3) ^ (*(unsigned __int64 *)(v_stack_p8 + a1 * 8));
    if (v_r10 != v_stack_p18) goto loc_003FA160;
    if ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) == 0) goto loc_003FA1BC;
    a3 = ~((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) - 1);
    a3 = (a3) & (v_stack_p18);
    if (a3 >= (a1 + 4096)) goto loc_003FA1BC;
loc_003FA1B0:
    a3 = (a3) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)));
    if (a3 < (a1 + 4096)) goto loc_003FA1B0;
loc_003FA1BC:
loc_003FA1C2:
    *(unsigned __int64 *)(a1 + 4096 - 8) = 0;
    v_r10 = (a1 + 4096) - (8);
    a1 = (unsigned int)((0) & (15));
    a3 = (0) >> (4);
    a4 = (a3) ^ (*(unsigned __int64 *)(v_stack_p8 + a1 * 8));
    if (v_r10 != v_stack_p18) goto loc_003FA1C2;
    if ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) == 0) goto loc_003FA220;
    a3 = ~((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)) - 1);
    a3 = (a3) & (v_stack_p18);
    if (a3 >= (a1 + 4096)) goto loc_003FA220;
loc_003FA210:
    a3 = (a3) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 232)));
    if (a3 < (a1 + 4096)) goto loc_003FA210;
loc_003FA220:
    a1 = (0) >> (32);
    if ((*(unsigned int *)(a1 + 4096 - 4)) != ((unsigned int)(a1))) goto loc_003F9FB5;
    a2 = (a1 + 4096) - (8);
    if ((*(unsigned int *)(a2)) != 0) goto loc_003F9FB5;
    result = (result) >> (4);
    a1 = (unsigned int)((0) & (15));
    result = (result) ^ (*(unsigned __int64 *)(v_stack_p8 + a1 * 8));
    if (a2 != v_stack_p18) goto loc_003FA220;
    v_rsi = (unsigned int)((v_stack_p10) + 1);
    goto loc_003F9EF1;
loc_003FA256:
    goto loc_003F9FB7;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpGenericRandomPatternWorker(int64_t Arg1)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m28;
    uint32_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (32);
    local_rsi = 0;
loc_003F9EF1:
    if (0 >= 5) goto loc_003FA256;
    result = RtlpSeedGlfsr(Arg1, a2, a3, a4);
    if (Arg1 >= (Arg1 + 4096)) goto loc_003F9F40;
loc_003F9F20:
    *(uint64_t *)(Arg1) = result;
    Arg1 = (uint32_t)((result) & (15));
    a3 = (result) >> (4);
    local_r10 = (Arg1) + (8);
    a4 = (a3) ^ (*(uint64_t *)(*(uint64_t *)(v_rip - 0x3F7557 + local_rsi * 8) + Arg1 * 8));
    if (local_r10 < (Arg1 + 4096)) goto loc_003F9F20;
loc_003F9F40:
    if ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) == 0) goto loc_003F9F7C;
    a3 = ~((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) - 1);
    a3 = (a3) & (Arg1);
    if (a3 >= (Arg1 + 4096)) goto loc_003F9F7C;
loc_003F9F70:
    a3 = (a3) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)));
    if (a3 < (Arg1 + 4096)) goto loc_003F9F70;
loc_003F9F7C:
loc_003F9F82:
    if (Arg1 >= (Arg1 + 4096)) goto loc_003F9FCE;
    if ((*(uint32_t *)(Arg1)) != ((uint32_t)(result))) goto loc_003F9FB5;
    *(uint32_t *)(Arg1) = (uint32_t)(result);
    local_r10 = (result) >> (32);
    if ((*(uint32_t *)(Arg1 + 0x4)) != ((uint32_t)(local_r10))) goto loc_003F9FB5;
    *(uint32_t *)(Arg1 + 0x4) = (uint32_t)(local_r10);
    a3 = (uint32_t)((result) & (15));
    Arg1 = (result) >> (4);
    a4 = (Arg1) + (8);
    Arg1 = (Arg1) ^ (*(uint64_t *)(*(uint64_t *)(v_rip - 0x3F7557 + local_rsi * 8) + a3 * 8));
    goto loc_003F9F82;
loc_003F9FB5:
    result = 0;
loc_003F9FB7:
    local_rsp = (local_rsp) + (32);
    return result;
loc_003F9FCE:
    if ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) == 0) goto loc_003FA00C;
    a3 = ~((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) - 1);
    a3 = (a3) & (v_stack_p18);
    if (a3 >= (Arg1 + 4096)) goto loc_003FA00C;
loc_003FA000:
    a3 = (a3) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)));
    if (a3 < (Arg1 + 4096)) goto loc_003FA000;
loc_003FA00C:
loc_003FA012:
    if (v_stack_p18 >= (Arg1 + 4096)) goto loc_003FA03E;
    if ((*(uint32_t *)(v_stack_p18)) != 0) goto loc_003F9FB5;
    a3 = (0) >> (32);
    if ((*(uint32_t *)(v_stack_p18 + 0x4)) != ((uint32_t)(a3))) goto loc_003F9FB5;
    local_r10 = (v_stack_p18) + (8);
    a3 = (uint32_t)((0) & (15));
    Arg1 = (0) >> (4);
    Arg1 = (Arg1) ^ (*(uint64_t *)(v_stack_p8 + a3 * 8));
    goto loc_003FA012;
loc_003FA03E:
    if (v_stack_p18 >= (Arg1 + 4096)) goto loc_003FA076;
loc_003FA050:
    Arg1 = ~(0);
    a3 = (0) >> (4);
    *(uint64_t *)(v_stack_p18) = Arg1;
    Arg1 = (uint32_t)((0) & (15));
    local_r10 = (v_stack_p18) + (8);
    a4 = (a3) ^ (*(uint64_t *)(v_stack_p8 + Arg1 * 8));
    if (local_r10 < (Arg1 + 4096)) goto loc_003FA050;
loc_003FA076:
    if ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) == 0) goto loc_003FA0AC;
    a3 = ~((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) - 1);
    a3 = (a3) & (v_stack_p18);
    if (a3 >= (Arg1 + 4096)) goto loc_003FA0AC;
loc_003FA0A0:
    a3 = (a3) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)));
    if (a3 < (Arg1 + 4096)) goto loc_003FA0A0;
loc_003FA0AC:
    if (v_stack_p18 >= (Arg1 + 4096)) goto loc_003FA0E0;
loc_003FA0C0:
    *(uint64_t *)(v_stack_p18) = 0;
    Arg1 = (uint32_t)((0) & (15));
    a3 = (0) >> (4);
    local_r10 = (v_stack_p18) + (8);
    a4 = (a3) ^ (*(uint64_t *)(v_stack_p8 + Arg1 * 8));
    if (local_r10 < (Arg1 + 4096)) goto loc_003FA0C0;
loc_003FA0E0:
    if ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) == 0) goto loc_003FA11C;
    a3 = ~((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) - 1);
    a3 = (a3) & (v_stack_p18);
    if (a3 >= (Arg1 + 4096)) goto loc_003FA11C;
loc_003FA110:
    a3 = (a3) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)));
    if (a3 < (Arg1 + 4096)) goto loc_003FA110;
loc_003FA11C:
loc_003FA122:
    if (v_stack_p18 >= (Arg1 + 4096)) goto loc_003FA156;
    if ((*(uint32_t *)(v_stack_p18)) != 0) goto loc_003F9FB5;
    a3 = (0) >> (32);
    if ((*(uint32_t *)(v_stack_p18 + 0x4)) != ((uint32_t)(a3))) goto loc_003F9FB5;
    local_r10 = (v_stack_p18) + (8);
    a3 = (uint32_t)((0) & (15));
    Arg1 = (0) >> (4);
    Arg1 = (Arg1) ^ (*(uint64_t *)(v_stack_p8 + a3 * 8));
    goto loc_003FA122;
loc_003FA156:
loc_003FA160:
    Arg1 = ~(0);
    a3 = (0) >> (4);
    *(uint64_t *)(Arg1 + 0x1000 - 0x8) = Arg1;
    local_r10 = (Arg1 + 4096) - (8);
    Arg1 = (uint32_t)((0) & (15));
    a4 = (a3) ^ (*(uint64_t *)(v_stack_p8 + Arg1 * 8));
    if (local_r10 != v_stack_p18) goto loc_003FA160;
    if ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) == 0) goto loc_003FA1BC;
    a3 = ~((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) - 1);
    a3 = (a3) & (v_stack_p18);
    if (a3 >= (Arg1 + 4096)) goto loc_003FA1BC;
loc_003FA1B0:
    a3 = (a3) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)));
    if (a3 < (Arg1 + 4096)) goto loc_003FA1B0;
loc_003FA1BC:
loc_003FA1C2:
    *(uint64_t *)(Arg1 + 0x1000 - 0x8) = 0;
    local_r10 = (Arg1 + 4096) - (8);
    Arg1 = (uint32_t)((0) & (15));
    a3 = (0) >> (4);
    a4 = (a3) ^ (*(uint64_t *)(v_stack_p8 + Arg1 * 8));
    if (local_r10 != v_stack_p18) goto loc_003FA1C2;
    if ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) == 0) goto loc_003FA220;
    a3 = ~((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)) - 1);
    a3 = (a3) & (v_stack_p18);
    if (a3 >= (Arg1 + 4096)) goto loc_003FA220;
loc_003FA210:
    a3 = (a3) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xE8)));
    if (a3 < (Arg1 + 4096)) goto loc_003FA210;
loc_003FA220:
    Arg1 = (0) >> (32);
    if ((*(uint32_t *)(Arg1 + 0x1000 - 0x4)) != ((uint32_t)(Arg1))) goto loc_003F9FB5;
    a2 = (Arg1 + 4096) - (8);
    if ((*(uint32_t *)(a2)) != 0) goto loc_003F9FB5;
    result = (result) >> (4);
    Arg1 = (uint32_t)((0) & (15));
    result = (result) ^ (*(uint64_t *)(v_stack_p8 + Arg1 * 8));
    if (a2 != v_stack_p18) goto loc_003FA220;
    local_rsi = (uint32_t)((v_stack_p10) + 1);
    goto loc_003F9EF1;
loc_003FA256:
    goto loc_003F9FB7;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003F9ED0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
