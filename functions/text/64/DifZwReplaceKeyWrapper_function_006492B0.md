# DifZwReplaceKeyWrapper

- RVA: `0x006492B0`–`0x00649425` (길이 `373` bytes)
- VA: `0x00000001406492B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9A64`
- 디코드: `108`개 명령, `373/373` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006492EC` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00649312` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00649346` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064936C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00649385` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00649393` → [ZwReplaceKey](../6B/ZwReplaceKey_function_006B0150.md) (function, `0x006B0150`)
- `0x006493BF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006493E5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006493FE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00649322` → RVA `0x00F048B8` (`.data`; read)
- `0x00649333` → RVA `0x00F04980` (`.data`; read)
- `0x0064933F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006492B0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
006492B5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
006492BA  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
006492BF  55                              push rbp
006492C0  41 54                           push r12
006492C2  41 55                           push r13
006492C4  41 56                           push r14
006492C6  41 57                           push r15
006492C8  48 8B EC                        mov rbp, rsp
006492CB  48 83 EC 50                     sub rsp, 0x50
006492CF  33 C0                           xor eax, eax
006492D1  0F 57 C0                        xorps xmm0, xmm0
006492D4  4C 8B E9                        mov r13, rcx
006492D7  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
006492DB  4D 8B F8                        mov r15, r8
006492DE  4C 8B E2                        mov r12, rdx
006492E1  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
006492E5  8D 48 1D                        lea ecx, [rax + 0x1d]
006492E8  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
006492EC  E8 43 C7 E4 FF                  call 0x140495a34
006492F1  48 8B F0                        mov rsi, rax
006492F4  48 85 C0                        test rax, rax
006492F7  0F 84 8D 00 00 00               je 0x14064938a
006492FD  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00649300  A8 18                           test al, 0x18
00649302  74 0A                           je 0x14064930e
00649304  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00649308  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0064930C  EB 0D                           jmp 0x14064931b
0064930E  A8 04                           test al, 4
00649310  74 09                           je 0x14064931b
00649312  E8 F1 A8 E8 FF                  call 0x1404d3c08
00649317  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0064931B  45 32 F6                        xor r14b, r14b
0064931E  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
00649322  44 38 35 8F B5 8B 00            cmp byte ptr [rip + 0x8bb58f], r14b
00649329  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0064932D  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00649331  75 0C                           jne 0x14064933f
00649333  F7 05 43 B6 8B 00 00 08 00 00   test dword ptr [rip + 0x8bb643], 0x800
0064933D  74 13                           je 0x140649352
0064933F  48 8D 0D 3A AB 8B 00            lea rcx, [rip + 0x8bab3a]
00649346  E8 D5 D2 BC FF                  call 0x140216620
0064934B  44 8A F0                        mov r14b, al
0064934E  84 C0                           test al, al
00649350  74 38                           je 0x14064938a
00649352  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00649356  48 8B 1F                        mov rbx, qword ptr [rdi]
00649359  EB 19                           jmp 0x140649374
0064935B  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064935F  48 85 C0                        test rax, rax
00649362  74 0D                           je 0x140649371
00649364  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00649368  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0064936C  E8 5F 17 07 00                  call 0x1406baad0
00649371  48 8B 1B                        mov rbx, qword ptr [rbx]
00649374  48 3B DF                        cmp rbx, rdi
00649377  75 E2                           jne 0x14064935b
00649379  45 84 F6                        test r14b, r14b
0064937C  74 0C                           je 0x14064938a
0064937E  48 8D 0D FB AA 8B 00            lea rcx, [rip + 0x8baafb]
00649385  E8 F6 0A D0 FF                  call 0x140349e80
0064938A  4D 8B C7                        mov r8, r15
0064938D  49 8B D4                        mov rdx, r12
00649390  49 8B CD                        mov rcx, r13
00649393  E8 B8 6D 06 00                  call 0x1406b0150
00649398  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0064939B  48 85 F6                        test rsi, rsi
0064939E  74 63                           je 0x140649403
006493A0  40 32 FF                        xor dil, dil
006493A3  40 38 3D 0E B5 8B 00            cmp byte ptr [rip + 0x8bb50e], dil
006493AA  75 0C                           jne 0x1406493b8
006493AC  F7 05 CA B5 8B 00 00 08 00 00   test dword ptr [rip + 0x8bb5ca], 0x800
006493B6  74 13                           je 0x1406493cb
006493B8  48 8D 0D C1 AA 8B 00            lea rcx, [rip + 0x8baac1]
006493BF  E8 5C D2 BC FF                  call 0x140216620
006493C4  40 8A F8                        mov dil, al
006493C7  84 C0                           test al, al
006493C9  74 38                           je 0x140649403
006493CB  48 83 C6 30                     add rsi, 0x30
006493CF  48 8B 1E                        mov rbx, qword ptr [rsi]
006493D2  EB 19                           jmp 0x1406493ed
006493D4  48 8D 43 F0                     lea rax, [rbx - 0x10]
006493D8  48 85 C0                        test rax, rax
006493DB  74 0D                           je 0x1406493ea
006493DD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006493E1  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006493E5  E8 E6 16 07 00                  call 0x1406baad0
006493EA  48 8B 1B                        mov rbx, qword ptr [rbx]
006493ED  48 3B DE                        cmp rbx, rsi
006493F0  75 E2                           jne 0x1406493d4
006493F2  40 84 FF                        test dil, dil
006493F5  74 0C                           je 0x140649403
006493F7  48 8D 0D 82 AA 8B 00            lea rcx, [rip + 0x8baa82]
006493FE  E8 7D 0A D0 FF                  call 0x140349e80
00649403  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00649406  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0064940B  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0064940F  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00649413  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00649417  49 8B E3                        mov rsp, r11
0064941A  41 5F                           pop r15
0064941C  41 5E                           pop r14
0064941E  41 5D                           pop r13
00649420  41 5C                           pop r12
00649422  5D                              pop rbp
00649423  C3                              ret
00649424  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwReplaceKeyWrapper(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(result + 29, a2, a3, a4);
    if (result == 0) goto loc_0064938A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0064930E;
    v_stack_m58 = v_stack_p0;
    goto loc_0064931B;
loc_0064930E:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9155983)) != 0) goto loc_0064933F;
    if (((*(unsigned int *)(v_rip + 9156163)) & (0x800ULL)) == 0) goto loc_00649352;
loc_0064933F:
    result = ExAcquireRundownProtection(v_rip + 9153338, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064938A;
loc_00649352:
    goto loc_00649374;
loc_0064935B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00649374:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0064935B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9153275;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwReplaceKey(a1, a2, a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_00649403;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9155854)) != 0) goto loc_006493B8;
    if (((*(unsigned int *)(v_rip + 9156042)) & (0x800ULL)) == 0) goto loc_006493CB;
loc_006493B8:
    result = ExAcquireRundownProtection(v_rip + 9153217, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00649403;
loc_006493CB:
    v_rsi = (result) + (48);
    goto loc_006493ED;
loc_006493D4:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006493ED:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006493D4;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9153154;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwReplaceKeyWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(result + 29, Arg2, Arg3, a4);
    if (result == 0) goto loc_0064938A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0064930E;
    v_stack_m58 = v_stack_p0;
    goto loc_0064931B;
loc_0064930E:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8BB58F)) != 0) goto loc_0064933F;
    if (((*(uint32_t *)(v_rip + 0x8BB643)) & (0x800ULL)) == 0) goto loc_00649352;
loc_0064933F:
    result = ExAcquireRundownProtection(v_rip + 9153338, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0064938A;
loc_00649352:
    goto loc_00649374;
loc_0064935B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00649374:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0064935B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9153275;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = ZwReplaceKey(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_00649403;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BB50E)) != 0) goto loc_006493B8;
    if (((*(uint32_t *)(v_rip + 0x8BB5CA)) & (0x800ULL)) == 0) goto loc_006493CB;
loc_006493B8:
    result = ExAcquireRundownProtection(v_rip + 9153217, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00649403;
loc_006493CB:
    local_rsi = (result) + (48);
    goto loc_006493ED;
loc_006493D4:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_006493ED:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006493D4;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9153154;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006492B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006492B0[BB_006492B0]
  bb_006492FD[BB_006492FD]
  bb_00649304[BB_00649304]
  bb_0064930E[BB_0064930E]
  bb_00649312[BB_00649312]
  bb_0064931B[BB_0064931B]
  bb_00649333[BB_00649333]
  bb_0064933F[BB_0064933F]
  bb_00649352[BB_00649352]
  bb_0064935B[BB_0064935B]
  bb_00649364[BB_00649364]
  bb_00649371[BB_00649371]
  bb_00649374[BB_00649374]
  bb_00649379[BB_00649379]
  bb_0064937E[BB_0064937E]
  bb_0064938A[BB_0064938A]
  bb_006493A0[BB_006493A0]
  bb_006493AC[BB_006493AC]
  bb_006493B8[BB_006493B8]
  bb_006493CB[BB_006493CB]
  bb_006493D4[BB_006493D4]
  bb_006493DD[BB_006493DD]
  bb_006493EA[BB_006493EA]
  bb_006493ED[BB_006493ED]
  bb_006493F2[BB_006493F2]
  bb_006493F7[BB_006493F7]
  bb_00649403[BB_00649403]
  bb_00649424[BB_00649424]
  bb_006492B0 -->|branch| bb_0064938A
  bb_006492B0 -->|fallthrough| bb_006492FD
  bb_006492FD -->|branch| bb_0064930E
  bb_006492FD -->|fallthrough| bb_00649304
  bb_00649304 -->|branch| bb_0064931B
  bb_0064930E -->|branch| bb_0064931B
  bb_0064930E -->|fallthrough| bb_00649312
  bb_00649312 -->|flow| bb_0064931B
  bb_0064931B -->|branch| bb_0064933F
  bb_0064931B -->|fallthrough| bb_00649333
  bb_00649333 -->|branch| bb_00649352
  bb_00649333 -->|fallthrough| bb_0064933F
  bb_0064933F -->|branch| bb_0064938A
  bb_0064933F -->|fallthrough| bb_00649352
  bb_00649352 -->|branch| bb_00649374
  bb_0064935B -->|branch| bb_00649371
  bb_0064935B -->|fallthrough| bb_00649364
  bb_00649364 -->|flow| bb_00649371
  bb_00649371 -->|flow| bb_00649374
  bb_00649374 -->|branch| bb_0064935B
  bb_00649374 -->|fallthrough| bb_00649379
  bb_00649379 -->|branch| bb_0064938A
  bb_00649379 -->|fallthrough| bb_0064937E
  bb_0064937E -->|flow| bb_0064938A
  bb_0064938A -->|branch| bb_00649403
  bb_0064938A -->|fallthrough| bb_006493A0
  bb_006493A0 -->|branch| bb_006493B8
  bb_006493A0 -->|fallthrough| bb_006493AC
  bb_006493AC -->|branch| bb_006493CB
  bb_006493AC -->|fallthrough| bb_006493B8
  bb_006493B8 -->|branch| bb_00649403
  bb_006493B8 -->|fallthrough| bb_006493CB
  bb_006493CB -->|branch| bb_006493ED
  bb_006493D4 -->|branch| bb_006493EA
  bb_006493D4 -->|fallthrough| bb_006493DD
  bb_006493DD -->|flow| bb_006493EA
  bb_006493EA -->|flow| bb_006493ED
  bb_006493ED -->|branch| bb_006493D4
  bb_006493ED -->|fallthrough| bb_006493F2
  bb_006493F2 -->|branch| bb_00649403
  bb_006493F2 -->|fallthrough| bb_006493F7
  bb_006493F7 -->|flow| bb_00649403
```
