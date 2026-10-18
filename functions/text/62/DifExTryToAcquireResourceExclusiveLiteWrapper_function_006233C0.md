# DifExTryToAcquireResourceExclusiveLiteWrapper

- RVA: `0x006233C0`–`0x0062351F` (길이 `351` bytes)
- VA: `0x00000001406233C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `351/351` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006233EF` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00623417` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00623445` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062346C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00623485` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062348D` → [ExTryToAcquireResourceExclusiveLite](../65/ExTryToAcquireResourceExclusiveLite_function_00658E20.md) (function, `0x00658E20`)
- `0x006234BA` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006234E1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006234FA` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00623429` → RVA `0x00F048B8` (`.data`; read)
- `0x00623432` → RVA `0x00F04980` (`.data`; read)
- `0x0062343E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006233C0  4C 8B DC                        mov r11, rsp
006233C3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
006233C7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
006233CB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
006233CF  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
006233D3  41 56                           push r14
006233D5  48 83 EC 40                     sub rsp, 0x40
006233D9  33 C0                           xor eax, eax
006233DB  0F 57 C0                        xorps xmm0, xmm0
006233DE  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
006233E3  48 8B E9                        mov rbp, rcx
006233E6  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
006233EA  B9 CE 01 00 00                  mov ecx, 0x1ce
006233EF  E8 40 26 E7 FF                  call 0x140495a34
006233F4  48 8B F0                        mov rsi, rax
006233F7  48 85 C0                        test rax, rax
006233FA  0F 84 8A 00 00 00               je 0x14062348a
00623400  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00623403  A8 18                           test al, 0x18
00623405  74 0C                           je 0x140623413
00623407  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0062340C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00623411  EB 0E                           jmp 0x140623421
00623413  A8 04                           test al, 4
00623415  74 0A                           je 0x140623421
00623417  E8 EC 07 EB FF                  call 0x1404d3c08
0062341C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00623421  40 32 FF                        xor dil, dil
00623424  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00623429  40 38 3D 88 14 8E 00            cmp byte ptr [rip + 0x8e1488], dil
00623430  75 0C                           jne 0x14062343e
00623432  F7 05 44 15 8E 00 00 08 00 00   test dword ptr [rip + 0x8e1544], 0x800
0062343C  74 13                           je 0x140623451
0062343E  48 8D 0D 3B 0A 8E 00            lea rcx, [rip + 0x8e0a3b]
00623445  E8 D6 31 BF FF                  call 0x140216620
0062344A  40 8A F8                        mov dil, al
0062344D  84 C0                           test al, al
0062344F  74 39                           je 0x14062348a
00623451  4C 8D 76 20                     lea r14, [rsi + 0x20]
00623455  49 8B 1E                        mov rbx, qword ptr [r14]
00623458  EB 1A                           jmp 0x140623474
0062345A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062345E  48 85 C0                        test rax, rax
00623461  74 0E                           je 0x140623471
00623463  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00623467  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062346C  E8 5F 76 09 00                  call 0x1406baad0
00623471  48 8B 1B                        mov rbx, qword ptr [rbx]
00623474  49 3B DE                        cmp rbx, r14
00623477  75 E1                           jne 0x14062345a
00623479  40 84 FF                        test dil, dil
0062347C  74 0C                           je 0x14062348a
0062347E  48 8D 0D FB 09 8E 00            lea rcx, [rip + 0x8e09fb]
00623485  E8 F6 69 D2 FF                  call 0x140349e80
0062348A  48 8B CD                        mov rcx, rbp
0062348D  E8 8E 59 03 00                  call 0x140658e20
00623492  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00623496  48 85 F6                        test rsi, rsi
00623499  74 64                           je 0x1406234ff
0062349B  40 32 FF                        xor dil, dil
0062349E  40 38 3D 13 14 8E 00            cmp byte ptr [rip + 0x8e1413], dil
006234A5  75 0C                           jne 0x1406234b3
006234A7  F7 05 CF 14 8E 00 00 08 00 00   test dword ptr [rip + 0x8e14cf], 0x800
006234B1  74 13                           je 0x1406234c6
006234B3  48 8D 0D C6 09 8E 00            lea rcx, [rip + 0x8e09c6]
006234BA  E8 61 31 BF FF                  call 0x140216620
006234BF  40 8A F8                        mov dil, al
006234C2  84 C0                           test al, al
006234C4  74 39                           je 0x1406234ff
006234C6  48 83 C6 30                     add rsi, 0x30
006234CA  48 8B 1E                        mov rbx, qword ptr [rsi]
006234CD  EB 1A                           jmp 0x1406234e9
006234CF  48 8D 43 F0                     lea rax, [rbx - 0x10]
006234D3  48 85 C0                        test rax, rax
006234D6  74 0E                           je 0x1406234e6
006234D8  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006234DC  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006234E1  E8 EA 75 09 00                  call 0x1406baad0
006234E6  48 8B 1B                        mov rbx, qword ptr [rbx]
006234E9  48 3B DE                        cmp rbx, rsi
006234EC  75 E1                           jne 0x1406234cf
006234EE  40 84 FF                        test dil, dil
006234F1  74 0C                           je 0x1406234ff
006234F3  48 8D 0D 86 09 8E 00            lea rcx, [rip + 0x8e0986]
006234FA  E8 81 69 D2 FF                  call 0x140349e80
006234FF  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
00623503  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00623508  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0062350D  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00623512  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00623517  48 83 C4 40                     add rsp, 0x40
0062351B  41 5E                           pop r14
0062351D  C3                              ret
0062351E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExTryToAcquireResourceExclusiveLiteWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
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
    v_stack_m28 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    result = DifGetAPIThunkContextById(462, a2, a3, a4);
    if (result == 0) goto loc_0062348A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00623413;
    v_stack_m28 = v_stack_p0;
    goto loc_00623421;
loc_00623413:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9311368)) != 0) goto loc_0062343E;
    if (((*(unsigned int *)(v_rip + 9311556)) & (0x800ULL)) == 0) goto loc_00623451;
loc_0062343E:
    result = ExAcquireRundownProtection(v_rip + 9308731, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062348A;
loc_00623451:
    goto loc_00623474;
loc_0062345A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00623474:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062345A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9308667;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExTryToAcquireResourceExclusiveLite(a1, a2, a3, a4);
    v_stack_m18 = (unsigned __int8)(result);
    if (result == 0) goto loc_006234FF;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9311251)) != 0) goto loc_006234B3;
    if (((*(unsigned int *)(v_rip + 9311439)) & (0x800ULL)) == 0) goto loc_006234C6;
loc_006234B3:
    result = ExAcquireRundownProtection(v_rip + 9308614, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006234FF;
loc_006234C6:
    v_rsi = (result) + (48);
    goto loc_006234E9;
loc_006234CF:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006234E9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006234CF;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9308550;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifExTryToAcquireResourceExclusiveLiteWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
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
    v_stack_m28 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    result = DifGetAPIThunkContextById(462, a2, a3, a4);
    if (result == 0) goto loc_0062348A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00623413;
    v_stack_m28 = v_stack_p0;
    goto loc_00623421;
loc_00623413:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E1488)) != 0) goto loc_0062343E;
    if (((*(uint32_t *)(v_rip + 0x8E1544)) & (0x800ULL)) == 0) goto loc_00623451;
loc_0062343E:
    result = ExAcquireRundownProtection(v_rip + 9308731, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062348A;
loc_00623451:
    goto loc_00623474;
loc_0062345A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00623474:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062345A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9308667;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExTryToAcquireResourceExclusiveLite(Arg1, a2, a3, a4);
    v_stack_m18 = (uint8_t)(result);
    if (result == 0) goto loc_006234FF;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E1413)) != 0) goto loc_006234B3;
    if (((*(uint32_t *)(v_rip + 0x8E14CF)) & (0x800ULL)) == 0) goto loc_006234C6;
loc_006234B3:
    result = ExAcquireRundownProtection(v_rip + 9308614, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006234FF;
loc_006234C6:
    local_rsi = (result) + (48);
    goto loc_006234E9;
loc_006234CF:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006234E9:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006234CF;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9308550;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006233C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006233C0[BB_006233C0]
  bb_00623400[BB_00623400]
  bb_00623407[BB_00623407]
  bb_00623413[BB_00623413]
  bb_00623417[BB_00623417]
  bb_00623421[BB_00623421]
  bb_00623432[BB_00623432]
  bb_0062343E[BB_0062343E]
  bb_00623451[BB_00623451]
  bb_0062345A[BB_0062345A]
  bb_00623463[BB_00623463]
  bb_00623471[BB_00623471]
  bb_00623474[BB_00623474]
  bb_00623479[BB_00623479]
  bb_0062347E[BB_0062347E]
  bb_0062348A[BB_0062348A]
  bb_0062349B[BB_0062349B]
  bb_006234A7[BB_006234A7]
  bb_006234B3[BB_006234B3]
  bb_006234C6[BB_006234C6]
  bb_006234CF[BB_006234CF]
  bb_006234D8[BB_006234D8]
  bb_006234E6[BB_006234E6]
  bb_006234E9[BB_006234E9]
  bb_006234EE[BB_006234EE]
  bb_006234F3[BB_006234F3]
  bb_006234FF[BB_006234FF]
  bb_0062351E[BB_0062351E]
  bb_006233C0 -->|branch| bb_0062348A
  bb_006233C0 -->|fallthrough| bb_00623400
  bb_00623400 -->|branch| bb_00623413
  bb_00623400 -->|fallthrough| bb_00623407
  bb_00623407 -->|branch| bb_00623421
  bb_00623413 -->|branch| bb_00623421
  bb_00623413 -->|fallthrough| bb_00623417
  bb_00623417 -->|flow| bb_00623421
  bb_00623421 -->|branch| bb_0062343E
  bb_00623421 -->|fallthrough| bb_00623432
  bb_00623432 -->|branch| bb_00623451
  bb_00623432 -->|fallthrough| bb_0062343E
  bb_0062343E -->|branch| bb_0062348A
  bb_0062343E -->|fallthrough| bb_00623451
  bb_00623451 -->|branch| bb_00623474
  bb_0062345A -->|branch| bb_00623471
  bb_0062345A -->|fallthrough| bb_00623463
  bb_00623463 -->|flow| bb_00623471
  bb_00623471 -->|flow| bb_00623474
  bb_00623474 -->|branch| bb_0062345A
  bb_00623474 -->|fallthrough| bb_00623479
  bb_00623479 -->|branch| bb_0062348A
  bb_00623479 -->|fallthrough| bb_0062347E
  bb_0062347E -->|flow| bb_0062348A
  bb_0062348A -->|branch| bb_006234FF
  bb_0062348A -->|fallthrough| bb_0062349B
  bb_0062349B -->|branch| bb_006234B3
  bb_0062349B -->|fallthrough| bb_006234A7
  bb_006234A7 -->|branch| bb_006234C6
  bb_006234A7 -->|fallthrough| bb_006234B3
  bb_006234B3 -->|branch| bb_006234FF
  bb_006234B3 -->|fallthrough| bb_006234C6
  bb_006234C6 -->|branch| bb_006234E9
  bb_006234CF -->|branch| bb_006234E6
  bb_006234CF -->|fallthrough| bb_006234D8
  bb_006234D8 -->|flow| bb_006234E6
  bb_006234E6 -->|flow| bb_006234E9
  bb_006234E9 -->|branch| bb_006234CF
  bb_006234E9 -->|fallthrough| bb_006234EE
  bb_006234EE -->|branch| bb_006234FF
  bb_006234EE -->|fallthrough| bb_006234F3
  bb_006234F3 -->|flow| bb_006234FF
```
