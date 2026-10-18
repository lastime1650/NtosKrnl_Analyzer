# DifMmProbeAndLockPagesWrapper

- RVA: `0x00636400`–`0x00636575` (길이 `373` bytes)
- VA: `0x0000000140636400`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A668`
- 디코드: `102`개 명령, `373/373` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00636439` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00636461` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00636499` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006364C0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006364D9` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006364E7` → [MmProbeAndLockPages](../23/MmProbeAndLockPages_function_0023B990.md) (function, `0x0023B990`)
- `0x00636510` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00636537` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00636550` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00636473` → RVA `0x00F048B8` (`.data`; read)
- `0x00636486` → RVA `0x00F04980` (`.data`; read)
- `0x00636492` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00636400  4C 8B DC                        mov r11, rsp
00636403  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00636407  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0063640B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0063640F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00636413  41 54                           push r12
00636415  41 56                           push r14
00636417  41 57                           push r15
00636419  48 83 EC 40                     sub rsp, 0x40
0063641D  33 C0                           xor eax, eax
0063641F  0F 57 C0                        xorps xmm0, xmm0
00636422  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00636427  4C 8B E1                        mov r12, rcx
0063642A  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
0063642E  B9 D9 00 00 00                  mov ecx, 0xd9
00636433  45 8B F0                        mov r14d, r8d
00636436  44 8A FA                        mov r15b, dl
00636439  E8 F6 F5 E5 FF                  call 0x140495a34
0063643E  48 8B F0                        mov rsi, rax
00636441  48 85 C0                        test rax, rax
00636444  0F 84 94 00 00 00               je 0x1406364de
0063644A  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063644D  A8 18                           test al, 0x18
0063644F  74 0C                           je 0x14063645d
00636451  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00636456  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0063645B  EB 0E                           jmp 0x14063646b
0063645D  A8 04                           test al, 4
0063645F  74 0A                           je 0x14063646b
00636461  E8 A2 D7 E9 FF                  call 0x1404d3c08
00636466  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0063646B  40 32 ED                        xor bpl, bpl
0063646E  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
00636473  40 38 2D 3E E4 8C 00            cmp byte ptr [rip + 0x8ce43e], bpl
0063647A  44 88 7C 24 2C                  mov byte ptr [rsp + 0x2c], r15b
0063647F  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00636484  75 0C                           jne 0x140636492
00636486  F7 05 F0 E4 8C 00 00 08 00 00   test dword ptr [rip + 0x8ce4f0], 0x800
00636490  74 13                           je 0x1406364a5
00636492  48 8D 0D E7 D9 8C 00            lea rcx, [rip + 0x8cd9e7]
00636499  E8 82 01 BE FF                  call 0x140216620
0063649E  40 8A E8                        mov bpl, al
006364A1  84 C0                           test al, al
006364A3  74 39                           je 0x1406364de
006364A5  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006364A9  48 8B 1F                        mov rbx, qword ptr [rdi]
006364AC  EB 1A                           jmp 0x1406364c8
006364AE  48 8D 43 F0                     lea rax, [rbx - 0x10]
006364B2  48 85 C0                        test rax, rax
006364B5  74 0E                           je 0x1406364c5
006364B7  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006364BB  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006364C0  E8 0B 46 08 00                  call 0x1406baad0
006364C5  48 8B 1B                        mov rbx, qword ptr [rbx]
006364C8  48 3B DF                        cmp rbx, rdi
006364CB  75 E1                           jne 0x1406364ae
006364CD  40 84 ED                        test bpl, bpl
006364D0  74 0C                           je 0x1406364de
006364D2  48 8D 0D A7 D9 8C 00            lea rcx, [rip + 0x8cd9a7]
006364D9  E8 A2 39 D1 FF                  call 0x140349e80
006364DE  45 8B C6                        mov r8d, r14d
006364E1  41 8A D7                        mov dl, r15b
006364E4  49 8B CC                        mov rcx, r12
006364E7  E8 A4 54 C0 FF                  call 0x14023b990
006364EC  48 85 F6                        test rsi, rsi
006364EF  74 64                           je 0x140636555
006364F1  40 32 FF                        xor dil, dil
006364F4  40 38 3D BD E3 8C 00            cmp byte ptr [rip + 0x8ce3bd], dil
006364FB  75 0C                           jne 0x140636509
006364FD  F7 05 79 E4 8C 00 00 08 00 00   test dword ptr [rip + 0x8ce479], 0x800
00636507  74 13                           je 0x14063651c
00636509  48 8D 0D 70 D9 8C 00            lea rcx, [rip + 0x8cd970]
00636510  E8 0B 01 BE FF                  call 0x140216620
00636515  40 8A F8                        mov dil, al
00636518  84 C0                           test al, al
0063651A  74 39                           je 0x140636555
0063651C  48 83 C6 30                     add rsi, 0x30
00636520  48 8B 1E                        mov rbx, qword ptr [rsi]
00636523  EB 1A                           jmp 0x14063653f
00636525  48 8D 43 F0                     lea rax, [rbx - 0x10]
00636529  48 85 C0                        test rax, rax
0063652C  74 0E                           je 0x14063653c
0063652E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00636532  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00636537  E8 94 45 08 00                  call 0x1406baad0
0063653C  48 8B 1B                        mov rbx, qword ptr [rbx]
0063653F  48 3B DE                        cmp rbx, rsi
00636542  75 E1                           jne 0x140636525
00636544  40 84 FF                        test dil, dil
00636547  74 0C                           je 0x140636555
00636549  48 8D 0D 30 D9 8C 00            lea rcx, [rip + 0x8cd930]
00636550  E8 2B 39 D1 FF                  call 0x140349e80
00636555  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0063655A  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0063655F  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00636564  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00636569  48 83 C4 40                     add rsp, 0x40
0063656D  41 5F                           pop r15
0063656F  41 5E                           pop r14
00636571  41 5C                           pop r12
00636573  C3                              ret
00636574  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmProbeAndLockPagesWrapper(__int64 a1, unsigned __int8 a2, int a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int8 v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m38 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = 0;
    result = DifGetAPIThunkContextById(217, a2, a3, a4);
    if (result == 0) goto loc_006364DE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063645D;
    v_stack_m38 = v_stack_p0;
    goto loc_0063646B;
loc_0063645D:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m2C = a2;
    v_stack_m30 = (unsigned int)((unsigned int)(a3));
    if ((*(unsigned __int8 *)(v_rip + 9233470)) != 0) goto loc_00636492;
    if (((*(unsigned int *)(v_rip + 9233648)) & (0x800ULL)) == 0) goto loc_006364A5;
loc_00636492:
    result = ExAcquireRundownProtection(v_rip + 9230823, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006364DE;
loc_006364A5:
    goto loc_006364C8;
loc_006364AE:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006364C8:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006364AE;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9230759;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = MmProbeAndLockPages(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if (result == 0) goto loc_00636555;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9233341)) != 0) goto loc_00636509;
    if (((*(unsigned int *)(v_rip + 9233529)) & (0x800ULL)) == 0) goto loc_0063651C;
loc_00636509:
    result = ExAcquireRundownProtection(v_rip + 9230704, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00636555;
loc_0063651C:
    v_rsi = (result) + (48);
    goto loc_0063653F;
loc_00636525:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_0063653F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00636525;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9230640;
        result = ExReleaseRundownProtection(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmProbeAndLockPagesWrapper(int64_t Arg1, uint8_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint8_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m38 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = 0;
    result = DifGetAPIThunkContextById(217, Arg2, Arg3, a4);
    if (result == 0) goto loc_006364DE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063645D;
    v_stack_m38 = v_stack_p0;
    goto loc_0063646B;
loc_0063645D:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m2C = Arg2;
    v_stack_m30 = (uint32_t)((uint32_t)(Arg3));
    if ((*(uint8_t *)(v_rip + 0x8CE43E)) != 0) goto loc_00636492;
    if (((*(uint32_t *)(v_rip + 0x8CE4F0)) & (0x800ULL)) == 0) goto loc_006364A5;
loc_00636492:
    result = ExAcquireRundownProtection(v_rip + 9230823, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_006364DE;
loc_006364A5:
    goto loc_006364C8;
loc_006364AE:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_006364C8:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006364AE;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9230759;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = MmProbeAndLockPages(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    if (result == 0) goto loc_00636555;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CE3BD)) != 0) goto loc_00636509;
    if (((*(uint32_t *)(v_rip + 0x8CE479)) & (0x800ULL)) == 0) goto loc_0063651C;
loc_00636509:
    result = ExAcquireRundownProtection(v_rip + 9230704, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    if ((uint8_t)(result) == 0) goto loc_00636555;
loc_0063651C:
    local_rsi = (result) + (48);
    goto loc_0063653F;
loc_00636525:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    }
loc_0063653F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00636525;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9230640;
        result = ExReleaseRundownProtection(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00636400&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00636400[BB_00636400]
  bb_0063644A[BB_0063644A]
  bb_00636451[BB_00636451]
  bb_0063645D[BB_0063645D]
  bb_00636461[BB_00636461]
  bb_0063646B[BB_0063646B]
  bb_00636486[BB_00636486]
  bb_00636492[BB_00636492]
  bb_006364A5[BB_006364A5]
  bb_006364AE[BB_006364AE]
  bb_006364B7[BB_006364B7]
  bb_006364C5[BB_006364C5]
  bb_006364C8[BB_006364C8]
  bb_006364CD[BB_006364CD]
  bb_006364D2[BB_006364D2]
  bb_006364DE[BB_006364DE]
  bb_006364F1[BB_006364F1]
  bb_006364FD[BB_006364FD]
  bb_00636509[BB_00636509]
  bb_0063651C[BB_0063651C]
  bb_00636525[BB_00636525]
  bb_0063652E[BB_0063652E]
  bb_0063653C[BB_0063653C]
  bb_0063653F[BB_0063653F]
  bb_00636544[BB_00636544]
  bb_00636549[BB_00636549]
  bb_00636555[BB_00636555]
  bb_00636574[BB_00636574]
  bb_00636400 -->|branch| bb_006364DE
  bb_00636400 -->|fallthrough| bb_0063644A
  bb_0063644A -->|branch| bb_0063645D
  bb_0063644A -->|fallthrough| bb_00636451
  bb_00636451 -->|branch| bb_0063646B
  bb_0063645D -->|branch| bb_0063646B
  bb_0063645D -->|fallthrough| bb_00636461
  bb_00636461 -->|flow| bb_0063646B
  bb_0063646B -->|branch| bb_00636492
  bb_0063646B -->|fallthrough| bb_00636486
  bb_00636486 -->|branch| bb_006364A5
  bb_00636486 -->|fallthrough| bb_00636492
  bb_00636492 -->|branch| bb_006364DE
  bb_00636492 -->|fallthrough| bb_006364A5
  bb_006364A5 -->|branch| bb_006364C8
  bb_006364AE -->|branch| bb_006364C5
  bb_006364AE -->|fallthrough| bb_006364B7
  bb_006364B7 -->|flow| bb_006364C5
  bb_006364C5 -->|flow| bb_006364C8
  bb_006364C8 -->|branch| bb_006364AE
  bb_006364C8 -->|fallthrough| bb_006364CD
  bb_006364CD -->|branch| bb_006364DE
  bb_006364CD -->|fallthrough| bb_006364D2
  bb_006364D2 -->|flow| bb_006364DE
  bb_006364DE -->|branch| bb_00636555
  bb_006364DE -->|fallthrough| bb_006364F1
  bb_006364F1 -->|branch| bb_00636509
  bb_006364F1 -->|fallthrough| bb_006364FD
  bb_006364FD -->|branch| bb_0063651C
  bb_006364FD -->|fallthrough| bb_00636509
  bb_00636509 -->|branch| bb_00636555
  bb_00636509 -->|fallthrough| bb_0063651C
  bb_0063651C -->|branch| bb_0063653F
  bb_00636525 -->|branch| bb_0063653C
  bb_00636525 -->|fallthrough| bb_0063652E
  bb_0063652E -->|flow| bb_0063653C
  bb_0063653C -->|flow| bb_0063653F
  bb_0063653F -->|branch| bb_00636525
  bb_0063653F -->|fallthrough| bb_00636544
  bb_00636544 -->|branch| bb_00636555
  bb_00636544 -->|fallthrough| bb_00636549
  bb_00636549 -->|flow| bb_00636555
```
