# DifKeTryToAcquireSpinLockAtDpcLevelWrapper

- RVA: `0x00633390`–`0x006334EF` (길이 `351` bytes)
- VA: `0x0000000140633390`
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
- `0x006333BF` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006333E7` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00633415` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063343C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00633455` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063345D` → [KxTryToAcquireSpinLock](../46/KxTryToAcquireSpinLock_function_0046BE18.md) (function, `0x0046BE18`)
- `0x0063348A` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006334B1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006334CA` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006333F9` → RVA `0x00F048B8` (`.data`; read)
- `0x00633402` → RVA `0x00F04980` (`.data`; read)
- `0x0063340E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00633390  4C 8B DC                        mov r11, rsp
00633393  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00633397  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0063339B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0063339F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
006333A3  41 56                           push r14
006333A5  48 83 EC 40                     sub rsp, 0x40
006333A9  33 C0                           xor eax, eax
006333AB  0F 57 C0                        xorps xmm0, xmm0
006333AE  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
006333B3  48 8B E9                        mov rbp, rcx
006333B6  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
006333BA  B9 F2 00 00 00                  mov ecx, 0xf2
006333BF  E8 70 26 E6 FF                  call 0x140495a34
006333C4  48 8B F0                        mov rsi, rax
006333C7  48 85 C0                        test rax, rax
006333CA  0F 84 8A 00 00 00               je 0x14063345a
006333D0  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006333D3  A8 18                           test al, 0x18
006333D5  74 0C                           je 0x1406333e3
006333D7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
006333DC  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006333E1  EB 0E                           jmp 0x1406333f1
006333E3  A8 04                           test al, 4
006333E5  74 0A                           je 0x1406333f1
006333E7  E8 1C 08 EA FF                  call 0x1404d3c08
006333EC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006333F1  40 32 FF                        xor dil, dil
006333F4  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
006333F9  40 38 3D B8 14 8D 00            cmp byte ptr [rip + 0x8d14b8], dil
00633400  75 0C                           jne 0x14063340e
00633402  F7 05 74 15 8D 00 00 08 00 00   test dword ptr [rip + 0x8d1574], 0x800
0063340C  74 13                           je 0x140633421
0063340E  48 8D 0D 6B 0A 8D 00            lea rcx, [rip + 0x8d0a6b]
00633415  E8 06 32 BE FF                  call 0x140216620
0063341A  40 8A F8                        mov dil, al
0063341D  84 C0                           test al, al
0063341F  74 39                           je 0x14063345a
00633421  4C 8D 76 20                     lea r14, [rsi + 0x20]
00633425  49 8B 1E                        mov rbx, qword ptr [r14]
00633428  EB 1A                           jmp 0x140633444
0063342A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063342E  48 85 C0                        test rax, rax
00633431  74 0E                           je 0x140633441
00633433  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00633437  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063343C  E8 8F 76 08 00                  call 0x1406baad0
00633441  48 8B 1B                        mov rbx, qword ptr [rbx]
00633444  49 3B DE                        cmp rbx, r14
00633447  75 E1                           jne 0x14063342a
00633449  40 84 FF                        test dil, dil
0063344C  74 0C                           je 0x14063345a
0063344E  48 8D 0D 2B 0A 8D 00            lea rcx, [rip + 0x8d0a2b]
00633455  E8 26 6A D1 FF                  call 0x140349e80
0063345A  48 8B CD                        mov rcx, rbp
0063345D  E8 B6 89 E3 FF                  call 0x14046be18
00633462  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00633466  48 85 F6                        test rsi, rsi
00633469  74 64                           je 0x1406334cf
0063346B  40 32 FF                        xor dil, dil
0063346E  40 38 3D 43 14 8D 00            cmp byte ptr [rip + 0x8d1443], dil
00633475  75 0C                           jne 0x140633483
00633477  F7 05 FF 14 8D 00 00 08 00 00   test dword ptr [rip + 0x8d14ff], 0x800
00633481  74 13                           je 0x140633496
00633483  48 8D 0D F6 09 8D 00            lea rcx, [rip + 0x8d09f6]
0063348A  E8 91 31 BE FF                  call 0x140216620
0063348F  40 8A F8                        mov dil, al
00633492  84 C0                           test al, al
00633494  74 39                           je 0x1406334cf
00633496  48 83 C6 30                     add rsi, 0x30
0063349A  48 8B 1E                        mov rbx, qword ptr [rsi]
0063349D  EB 1A                           jmp 0x1406334b9
0063349F  48 8D 43 F0                     lea rax, [rbx - 0x10]
006334A3  48 85 C0                        test rax, rax
006334A6  74 0E                           je 0x1406334b6
006334A8  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006334AC  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006334B1  E8 1A 76 08 00                  call 0x1406baad0
006334B6  48 8B 1B                        mov rbx, qword ptr [rbx]
006334B9  48 3B DE                        cmp rbx, rsi
006334BC  75 E1                           jne 0x14063349f
006334BE  40 84 FF                        test dil, dil
006334C1  74 0C                           je 0x1406334cf
006334C3  48 8D 0D B6 09 8D 00            lea rcx, [rip + 0x8d09b6]
006334CA  E8 B1 69 D1 FF                  call 0x140349e80
006334CF  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
006334D3  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
006334D8  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
006334DD  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
006334E2  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
006334E7  48 83 C4 40                     add rsp, 0x40
006334EB  41 5E                           pop r14
006334ED  C3                              ret
006334EE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeTryToAcquireSpinLockAtDpcLevelWrapper(__int64 a1)
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
    result = DifGetAPIThunkContextById(242, a2, a3, a4);
    if (result == 0) goto loc_0063345A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006333E3;
    v_stack_m28 = v_stack_p0;
    goto loc_006333F1;
loc_006333E3:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9245880)) != 0) goto loc_0063340E;
    if (((*(unsigned int *)(v_rip + 9246068)) & (0x800ULL)) == 0) goto loc_00633421;
loc_0063340E:
    result = ExAcquireRundownProtection(v_rip + 9243243, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063345A;
loc_00633421:
    goto loc_00633444;
loc_0063342A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00633444:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063342A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9243179;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = KxTryToAcquireSpinLock(a1, a2, a3, a4);
    v_stack_m18 = (unsigned __int8)(result);
    if (result == 0) goto loc_006334CF;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9245763)) != 0) goto loc_00633483;
    if (((*(unsigned int *)(v_rip + 9245951)) & (0x800ULL)) == 0) goto loc_00633496;
loc_00633483:
    result = ExAcquireRundownProtection(v_rip + 9243126, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006334CF;
loc_00633496:
    v_rsi = (result) + (48);
    goto loc_006334B9;
loc_0063349F:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006334B9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063349F;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9243062;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeTryToAcquireSpinLockAtDpcLevelWrapper(int64_t Arg1)
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
    result = DifGetAPIThunkContextById(242, a2, a3, a4);
    if (result == 0) goto loc_0063345A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006333E3;
    v_stack_m28 = v_stack_p0;
    goto loc_006333F1;
loc_006333E3:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8D14B8)) != 0) goto loc_0063340E;
    if (((*(uint32_t *)(v_rip + 0x8D1574)) & (0x800ULL)) == 0) goto loc_00633421;
loc_0063340E:
    result = ExAcquireRundownProtection(v_rip + 9243243, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063345A;
loc_00633421:
    goto loc_00633444;
loc_0063342A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00633444:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063342A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9243179;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = KxTryToAcquireSpinLock(Arg1, a2, a3, a4);
    v_stack_m18 = (uint8_t)(result);
    if (result == 0) goto loc_006334CF;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D1443)) != 0) goto loc_00633483;
    if (((*(uint32_t *)(v_rip + 0x8D14FF)) & (0x800ULL)) == 0) goto loc_00633496;
loc_00633483:
    result = ExAcquireRundownProtection(v_rip + 9243126, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006334CF;
loc_00633496:
    local_rsi = (result) + (48);
    goto loc_006334B9;
loc_0063349F:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006334B9:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063349F;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9243062;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00633390&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00633390[BB_00633390]
  bb_006333D0[BB_006333D0]
  bb_006333D7[BB_006333D7]
  bb_006333E3[BB_006333E3]
  bb_006333E7[BB_006333E7]
  bb_006333F1[BB_006333F1]
  bb_00633402[BB_00633402]
  bb_0063340E[BB_0063340E]
  bb_00633421[BB_00633421]
  bb_0063342A[BB_0063342A]
  bb_00633433[BB_00633433]
  bb_00633441[BB_00633441]
  bb_00633444[BB_00633444]
  bb_00633449[BB_00633449]
  bb_0063344E[BB_0063344E]
  bb_0063345A[BB_0063345A]
  bb_0063346B[BB_0063346B]
  bb_00633477[BB_00633477]
  bb_00633483[BB_00633483]
  bb_00633496[BB_00633496]
  bb_0063349F[BB_0063349F]
  bb_006334A8[BB_006334A8]
  bb_006334B6[BB_006334B6]
  bb_006334B9[BB_006334B9]
  bb_006334BE[BB_006334BE]
  bb_006334C3[BB_006334C3]
  bb_006334CF[BB_006334CF]
  bb_006334EE[BB_006334EE]
  bb_00633390 -->|branch| bb_0063345A
  bb_00633390 -->|fallthrough| bb_006333D0
  bb_006333D0 -->|branch| bb_006333E3
  bb_006333D0 -->|fallthrough| bb_006333D7
  bb_006333D7 -->|branch| bb_006333F1
  bb_006333E3 -->|branch| bb_006333F1
  bb_006333E3 -->|fallthrough| bb_006333E7
  bb_006333E7 -->|flow| bb_006333F1
  bb_006333F1 -->|branch| bb_0063340E
  bb_006333F1 -->|fallthrough| bb_00633402
  bb_00633402 -->|branch| bb_00633421
  bb_00633402 -->|fallthrough| bb_0063340E
  bb_0063340E -->|branch| bb_0063345A
  bb_0063340E -->|fallthrough| bb_00633421
  bb_00633421 -->|branch| bb_00633444
  bb_0063342A -->|branch| bb_00633441
  bb_0063342A -->|fallthrough| bb_00633433
  bb_00633433 -->|flow| bb_00633441
  bb_00633441 -->|flow| bb_00633444
  bb_00633444 -->|branch| bb_0063342A
  bb_00633444 -->|fallthrough| bb_00633449
  bb_00633449 -->|branch| bb_0063345A
  bb_00633449 -->|fallthrough| bb_0063344E
  bb_0063344E -->|flow| bb_0063345A
  bb_0063345A -->|branch| bb_006334CF
  bb_0063345A -->|fallthrough| bb_0063346B
  bb_0063346B -->|branch| bb_00633483
  bb_0063346B -->|fallthrough| bb_00633477
  bb_00633477 -->|branch| bb_00633496
  bb_00633477 -->|fallthrough| bb_00633483
  bb_00633483 -->|branch| bb_006334CF
  bb_00633483 -->|fallthrough| bb_00633496
  bb_00633496 -->|branch| bb_006334B9
  bb_0063349F -->|branch| bb_006334B6
  bb_0063349F -->|fallthrough| bb_006334A8
  bb_006334A8 -->|flow| bb_006334B6
  bb_006334B6 -->|flow| bb_006334B9
  bb_006334B9 -->|branch| bb_0063349F
  bb_006334B9 -->|fallthrough| bb_006334BE
  bb_006334BE -->|branch| bb_006334CF
  bb_006334BE -->|fallthrough| bb_006334C3
  bb_006334C3 -->|flow| bb_006334CF
```
