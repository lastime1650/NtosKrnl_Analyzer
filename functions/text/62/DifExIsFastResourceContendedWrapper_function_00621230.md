# DifExIsFastResourceContendedWrapper

- RVA: `0x00621230`–`0x0062138F` (길이 `351` bytes)
- VA: `0x0000000140621230`
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
- `0x0062125F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00621287` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006212B5` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006212DC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006212F5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006212FD` → [ExIsFastResourceContended](../65/ExIsFastResourceContended_function_00658660.md) (function, `0x00658660`)
- `0x0062132A` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00621351` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062136A` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00621299` → RVA `0x00F048B8` (`.data`; read)
- `0x006212A2` → RVA `0x00F04980` (`.data`; read)
- `0x006212AE` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00621230  4C 8B DC                        mov r11, rsp
00621233  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00621237  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062123B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062123F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00621243  41 56                           push r14
00621245  48 83 EC 40                     sub rsp, 0x40
00621249  33 C0                           xor eax, eax
0062124B  0F 57 C0                        xorps xmm0, xmm0
0062124E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00621253  48 8B E9                        mov rbp, rcx
00621256  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0062125A  B9 CD 01 00 00                  mov ecx, 0x1cd
0062125F  E8 D0 47 E7 FF                  call 0x140495a34
00621264  48 8B F0                        mov rsi, rax
00621267  48 85 C0                        test rax, rax
0062126A  0F 84 8A 00 00 00               je 0x1406212fa
00621270  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00621273  A8 18                           test al, 0x18
00621275  74 0C                           je 0x140621283
00621277  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0062127C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00621281  EB 0E                           jmp 0x140621291
00621283  A8 04                           test al, 4
00621285  74 0A                           je 0x140621291
00621287  E8 7C 29 EB FF                  call 0x1404d3c08
0062128C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00621291  40 32 FF                        xor dil, dil
00621294  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00621299  40 38 3D 18 36 8E 00            cmp byte ptr [rip + 0x8e3618], dil
006212A0  75 0C                           jne 0x1406212ae
006212A2  F7 05 D4 36 8E 00 00 08 00 00   test dword ptr [rip + 0x8e36d4], 0x800
006212AC  74 13                           je 0x1406212c1
006212AE  48 8D 0D CB 2B 8E 00            lea rcx, [rip + 0x8e2bcb]
006212B5  E8 66 53 BF FF                  call 0x140216620
006212BA  40 8A F8                        mov dil, al
006212BD  84 C0                           test al, al
006212BF  74 39                           je 0x1406212fa
006212C1  4C 8D 76 20                     lea r14, [rsi + 0x20]
006212C5  49 8B 1E                        mov rbx, qword ptr [r14]
006212C8  EB 1A                           jmp 0x1406212e4
006212CA  48 8D 43 F0                     lea rax, [rbx - 0x10]
006212CE  48 85 C0                        test rax, rax
006212D1  74 0E                           je 0x1406212e1
006212D3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006212D7  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006212DC  E8 EF 97 09 00                  call 0x1406baad0
006212E1  48 8B 1B                        mov rbx, qword ptr [rbx]
006212E4  49 3B DE                        cmp rbx, r14
006212E7  75 E1                           jne 0x1406212ca
006212E9  40 84 FF                        test dil, dil
006212EC  74 0C                           je 0x1406212fa
006212EE  48 8D 0D 8B 2B 8E 00            lea rcx, [rip + 0x8e2b8b]
006212F5  E8 86 8B D2 FF                  call 0x140349e80
006212FA  48 8B CD                        mov rcx, rbp
006212FD  E8 5E 73 03 00                  call 0x140658660
00621302  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00621306  48 85 F6                        test rsi, rsi
00621309  74 64                           je 0x14062136f
0062130B  40 32 FF                        xor dil, dil
0062130E  40 38 3D A3 35 8E 00            cmp byte ptr [rip + 0x8e35a3], dil
00621315  75 0C                           jne 0x140621323
00621317  F7 05 5F 36 8E 00 00 08 00 00   test dword ptr [rip + 0x8e365f], 0x800
00621321  74 13                           je 0x140621336
00621323  48 8D 0D 56 2B 8E 00            lea rcx, [rip + 0x8e2b56]
0062132A  E8 F1 52 BF FF                  call 0x140216620
0062132F  40 8A F8                        mov dil, al
00621332  84 C0                           test al, al
00621334  74 39                           je 0x14062136f
00621336  48 83 C6 30                     add rsi, 0x30
0062133A  48 8B 1E                        mov rbx, qword ptr [rsi]
0062133D  EB 1A                           jmp 0x140621359
0062133F  48 8D 43 F0                     lea rax, [rbx - 0x10]
00621343  48 85 C0                        test rax, rax
00621346  74 0E                           je 0x140621356
00621348  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062134C  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00621351  E8 7A 97 09 00                  call 0x1406baad0
00621356  48 8B 1B                        mov rbx, qword ptr [rbx]
00621359  48 3B DE                        cmp rbx, rsi
0062135C  75 E1                           jne 0x14062133f
0062135E  40 84 FF                        test dil, dil
00621361  74 0C                           je 0x14062136f
00621363  48 8D 0D 16 2B 8E 00            lea rcx, [rip + 0x8e2b16]
0062136A  E8 11 8B D2 FF                  call 0x140349e80
0062136F  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
00621373  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00621378  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0062137D  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00621382  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00621387  48 83 C4 40                     add rsp, 0x40
0062138B  41 5E                           pop r14
0062138D  C3                              ret
0062138E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExIsFastResourceContendedWrapper(__int64 a1)
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
    result = DifGetAPIThunkContextById(461, a2, a3, a4);
    if (result == 0) goto loc_006212FA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00621283;
    v_stack_m28 = v_stack_p0;
    goto loc_00621291;
loc_00621283:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9319960)) != 0) goto loc_006212AE;
    if (((*(unsigned int *)(v_rip + 9320148)) & (0x800ULL)) == 0) goto loc_006212C1;
loc_006212AE:
    result = ExAcquireRundownProtection(v_rip + 9317323, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006212FA;
loc_006212C1:
    goto loc_006212E4;
loc_006212CA:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006212E4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006212CA;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9317259;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExIsFastResourceContended(a1, a2, a3, a4);
    v_stack_m18 = (unsigned __int8)(result);
    if (result == 0) goto loc_0062136F;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9319843)) != 0) goto loc_00621323;
    if (((*(unsigned int *)(v_rip + 9320031)) & (0x800ULL)) == 0) goto loc_00621336;
loc_00621323:
    result = ExAcquireRundownProtection(v_rip + 9317206, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062136F;
loc_00621336:
    v_rsi = (result) + (48);
    goto loc_00621359;
loc_0062133F:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00621359:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062133F;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9317142;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifExIsFastResourceContendedWrapper(int64_t Arg1)
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
    result = DifGetAPIThunkContextById(461, a2, a3, a4);
    if (result == 0) goto loc_006212FA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00621283;
    v_stack_m28 = v_stack_p0;
    goto loc_00621291;
loc_00621283:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E3618)) != 0) goto loc_006212AE;
    if (((*(uint32_t *)(v_rip + 0x8E36D4)) & (0x800ULL)) == 0) goto loc_006212C1;
loc_006212AE:
    result = ExAcquireRundownProtection(v_rip + 9317323, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006212FA;
loc_006212C1:
    goto loc_006212E4;
loc_006212CA:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006212E4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006212CA;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9317259;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExIsFastResourceContended(Arg1, a2, a3, a4);
    v_stack_m18 = (uint8_t)(result);
    if (result == 0) goto loc_0062136F;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E35A3)) != 0) goto loc_00621323;
    if (((*(uint32_t *)(v_rip + 0x8E365F)) & (0x800ULL)) == 0) goto loc_00621336;
loc_00621323:
    result = ExAcquireRundownProtection(v_rip + 9317206, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062136F;
loc_00621336:
    local_rsi = (result) + (48);
    goto loc_00621359;
loc_0062133F:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00621359:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062133F;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9317142;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00621230&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00621230[BB_00621230]
  bb_00621270[BB_00621270]
  bb_00621277[BB_00621277]
  bb_00621283[BB_00621283]
  bb_00621287[BB_00621287]
  bb_00621291[BB_00621291]
  bb_006212A2[BB_006212A2]
  bb_006212AE[BB_006212AE]
  bb_006212C1[BB_006212C1]
  bb_006212CA[BB_006212CA]
  bb_006212D3[BB_006212D3]
  bb_006212E1[BB_006212E1]
  bb_006212E4[BB_006212E4]
  bb_006212E9[BB_006212E9]
  bb_006212EE[BB_006212EE]
  bb_006212FA[BB_006212FA]
  bb_0062130B[BB_0062130B]
  bb_00621317[BB_00621317]
  bb_00621323[BB_00621323]
  bb_00621336[BB_00621336]
  bb_0062133F[BB_0062133F]
  bb_00621348[BB_00621348]
  bb_00621356[BB_00621356]
  bb_00621359[BB_00621359]
  bb_0062135E[BB_0062135E]
  bb_00621363[BB_00621363]
  bb_0062136F[BB_0062136F]
  bb_0062138E[BB_0062138E]
  bb_00621230 -->|branch| bb_006212FA
  bb_00621230 -->|fallthrough| bb_00621270
  bb_00621270 -->|branch| bb_00621283
  bb_00621270 -->|fallthrough| bb_00621277
  bb_00621277 -->|branch| bb_00621291
  bb_00621283 -->|branch| bb_00621291
  bb_00621283 -->|fallthrough| bb_00621287
  bb_00621287 -->|flow| bb_00621291
  bb_00621291 -->|branch| bb_006212AE
  bb_00621291 -->|fallthrough| bb_006212A2
  bb_006212A2 -->|branch| bb_006212C1
  bb_006212A2 -->|fallthrough| bb_006212AE
  bb_006212AE -->|branch| bb_006212FA
  bb_006212AE -->|fallthrough| bb_006212C1
  bb_006212C1 -->|branch| bb_006212E4
  bb_006212CA -->|branch| bb_006212E1
  bb_006212CA -->|fallthrough| bb_006212D3
  bb_006212D3 -->|flow| bb_006212E1
  bb_006212E1 -->|flow| bb_006212E4
  bb_006212E4 -->|branch| bb_006212CA
  bb_006212E4 -->|fallthrough| bb_006212E9
  bb_006212E9 -->|branch| bb_006212FA
  bb_006212E9 -->|fallthrough| bb_006212EE
  bb_006212EE -->|flow| bb_006212FA
  bb_006212FA -->|branch| bb_0062136F
  bb_006212FA -->|fallthrough| bb_0062130B
  bb_0062130B -->|branch| bb_00621323
  bb_0062130B -->|fallthrough| bb_00621317
  bb_00621317 -->|branch| bb_00621336
  bb_00621317 -->|fallthrough| bb_00621323
  bb_00621323 -->|branch| bb_0062136F
  bb_00621323 -->|fallthrough| bb_00621336
  bb_00621336 -->|branch| bb_00621359
  bb_0062133F -->|branch| bb_00621356
  bb_0062133F -->|fallthrough| bb_00621348
  bb_00621348 -->|flow| bb_00621356
  bb_00621356 -->|flow| bb_00621359
  bb_00621359 -->|branch| bb_0062133F
  bb_00621359 -->|fallthrough| bb_0062135E
  bb_0062135E -->|branch| bb_0062136F
  bb_0062135E -->|fallthrough| bb_00621363
  bb_00621363 -->|flow| bb_0062136F
```
