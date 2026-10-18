# DifKeRemoveEntryDeviceQueueWrapper

- RVA: `0x00632200`–`0x00632364` (길이 `356` bytes)
- VA: `0x0000000140632200`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `98`개 명령, `356/356` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063222E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00632256` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00632289` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006322B0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006322C9` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006322D4` → [KeRemoveEntryDeviceQueue](../5B/KeRemoveEntryDeviceQueue_function_005BE410.md) (function, `0x005BE410`)
- `0x00632301` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00632328` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00632341` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00632268` → RVA `0x00F048B8` (`.data`; read)
- `0x00632276` → RVA `0x00F04980` (`.data`; read)
- `0x00632282` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00632200  48 8B C4                        mov rax, rsp
00632203  48 89 58 08                     mov qword ptr [rax + 8], rbx
00632207  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0063220B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063220F  57                              push rdi
00632210  41 56                           push r14
00632212  41 57                           push r15
00632214  48 83 EC 40                     sub rsp, 0x40
00632218  0F 57 C0                        xorps xmm0, xmm0
0063221B  4C 8B F9                        mov r15, rcx
0063221E  B9 FE 00 00 00                  mov ecx, 0xfe
00632223  4C 8B F2                        mov r14, rdx
00632226  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0063222A  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0063222E  E8 01 38 E6 FF                  call 0x140495a34
00632233  48 8B F0                        mov rsi, rax
00632236  48 85 C0                        test rax, rax
00632239  0F 84 8F 00 00 00               je 0x1406322ce
0063223F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00632242  A8 18                           test al, 0x18
00632244  74 0C                           je 0x140632252
00632246  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0063224B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00632250  EB 0E                           jmp 0x140632260
00632252  A8 04                           test al, 4
00632254  74 0A                           je 0x140632260
00632256  E8 AD 19 EA FF                  call 0x1404d3c08
0063225B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00632260  40 32 ED                        xor bpl, bpl
00632263  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00632268  40 38 2D 49 26 8D 00            cmp byte ptr [rip + 0x8d2649], bpl
0063226F  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00632274  75 0C                           jne 0x140632282
00632276  F7 05 00 27 8D 00 00 08 00 00   test dword ptr [rip + 0x8d2700], 0x800
00632280  74 13                           je 0x140632295
00632282  48 8D 0D F7 1B 8D 00            lea rcx, [rip + 0x8d1bf7]
00632289  E8 92 43 BE FF                  call 0x140216620
0063228E  40 8A E8                        mov bpl, al
00632291  84 C0                           test al, al
00632293  74 39                           je 0x1406322ce
00632295  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00632299  48 8B 1F                        mov rbx, qword ptr [rdi]
0063229C  EB 1A                           jmp 0x1406322b8
0063229E  48 8D 43 F0                     lea rax, [rbx - 0x10]
006322A2  48 85 C0                        test rax, rax
006322A5  74 0E                           je 0x1406322b5
006322A7  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006322AB  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006322B0  E8 1B 88 08 00                  call 0x1406baad0
006322B5  48 8B 1B                        mov rbx, qword ptr [rbx]
006322B8  48 3B DF                        cmp rbx, rdi
006322BB  75 E1                           jne 0x14063229e
006322BD  40 84 ED                        test bpl, bpl
006322C0  74 0C                           je 0x1406322ce
006322C2  48 8D 0D B7 1B 8D 00            lea rcx, [rip + 0x8d1bb7]
006322C9  E8 B2 7B D1 FF                  call 0x140349e80
006322CE  49 8B D6                        mov rdx, r14
006322D1  49 8B CF                        mov rcx, r15
006322D4  E8 37 C1 F8 FF                  call 0x1405be410
006322D9  88 44 24 38                     mov byte ptr [rsp + 0x38], al
006322DD  48 85 F6                        test rsi, rsi
006322E0  74 64                           je 0x140632346
006322E2  40 32 FF                        xor dil, dil
006322E5  40 38 3D CC 25 8D 00            cmp byte ptr [rip + 0x8d25cc], dil
006322EC  75 0C                           jne 0x1406322fa
006322EE  F7 05 88 26 8D 00 00 08 00 00   test dword ptr [rip + 0x8d2688], 0x800
006322F8  74 13                           je 0x14063230d
006322FA  48 8D 0D 7F 1B 8D 00            lea rcx, [rip + 0x8d1b7f]
00632301  E8 1A 43 BE FF                  call 0x140216620
00632306  40 8A F8                        mov dil, al
00632309  84 C0                           test al, al
0063230B  74 39                           je 0x140632346
0063230D  48 83 C6 30                     add rsi, 0x30
00632311  48 8B 1E                        mov rbx, qword ptr [rsi]
00632314  EB 1A                           jmp 0x140632330
00632316  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063231A  48 85 C0                        test rax, rax
0063231D  74 0E                           je 0x14063232d
0063231F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00632323  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00632328  E8 A3 87 08 00                  call 0x1406baad0
0063232D  48 8B 1B                        mov rbx, qword ptr [rbx]
00632330  48 3B DE                        cmp rbx, rsi
00632333  75 E1                           jne 0x140632316
00632335  40 84 FF                        test dil, dil
00632338  74 0C                           je 0x140632346
0063233A  48 8D 0D 3F 1B 8D 00            lea rcx, [rip + 0x8d1b3f]
00632341  E8 3A 7B D1 FF                  call 0x140349e80
00632346  8A 44 24 38                     mov al, byte ptr [rsp + 0x38]
0063234A  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0063234F  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00632354  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00632359  48 83 C4 40                     add rsp, 0x40
0063235D  41 5F                           pop r15
0063235F  41 5E                           pop r14
00632361  5F                              pop rdi
00632362  C3                              ret
00632363  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeRemoveEntryDeviceQueueWrapper(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(254, a2, a3, a4);
    if (result == 0) goto loc_006322CE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00632252;
    v_stack_m38 = v_stack_p0;
    goto loc_00632260;
loc_00632252:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9250377)) != 0) goto loc_00632282;
    if (((*(unsigned int *)(v_rip + 9250560)) & (0x800ULL)) == 0) goto loc_00632295;
loc_00632282:
    result = ExAcquireRundownProtection(v_rip + 9247735, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006322CE;
loc_00632295:
    goto loc_006322B8;
loc_0063229E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006322B8:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063229E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9247671;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = KeRemoveEntryDeviceQueue(a1, a2, a3, a4);
    v_stack_m20 = (unsigned __int8)(result);
    if (result == 0) goto loc_00632346;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9250252)) != 0) goto loc_006322FA;
    if (((*(unsigned int *)(v_rip + 9250440)) & (0x800ULL)) == 0) goto loc_0063230D;
loc_006322FA:
    result = ExAcquireRundownProtection(v_rip + 9247615, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00632346;
loc_0063230D:
    v_rsi = (result) + (48);
    goto loc_00632330;
loc_00632316:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00632330:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00632316;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9247551;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m20;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeRemoveEntryDeviceQueueWrapper(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(254, Arg2, a3, a4);
    if (result == 0) goto loc_006322CE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00632252;
    v_stack_m38 = v_stack_p0;
    goto loc_00632260;
loc_00632252:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8D2649)) != 0) goto loc_00632282;
    if (((*(uint32_t *)(v_rip + 0x8D2700)) & (0x800ULL)) == 0) goto loc_00632295;
loc_00632282:
    result = ExAcquireRundownProtection(v_rip + 9247735, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006322CE;
loc_00632295:
    goto loc_006322B8;
loc_0063229E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_006322B8:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063229E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9247671;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = KeRemoveEntryDeviceQueue(Arg1, Arg2, a3, a4);
    v_stack_m20 = (uint8_t)(result);
    if (result == 0) goto loc_00632346;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D25CC)) != 0) goto loc_006322FA;
    if (((*(uint32_t *)(v_rip + 0x8D2688)) & (0x800ULL)) == 0) goto loc_0063230D;
loc_006322FA:
    result = ExAcquireRundownProtection(v_rip + 9247615, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00632346;
loc_0063230D:
    local_rsi = (result) + (48);
    goto loc_00632330;
loc_00632316:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00632330:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00632316;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9247551;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m20;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00632200&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00632200[BB_00632200]
  bb_0063223F[BB_0063223F]
  bb_00632246[BB_00632246]
  bb_00632252[BB_00632252]
  bb_00632256[BB_00632256]
  bb_00632260[BB_00632260]
  bb_00632276[BB_00632276]
  bb_00632282[BB_00632282]
  bb_00632295[BB_00632295]
  bb_0063229E[BB_0063229E]
  bb_006322A7[BB_006322A7]
  bb_006322B5[BB_006322B5]
  bb_006322B8[BB_006322B8]
  bb_006322BD[BB_006322BD]
  bb_006322C2[BB_006322C2]
  bb_006322CE[BB_006322CE]
  bb_006322E2[BB_006322E2]
  bb_006322EE[BB_006322EE]
  bb_006322FA[BB_006322FA]
  bb_0063230D[BB_0063230D]
  bb_00632316[BB_00632316]
  bb_0063231F[BB_0063231F]
  bb_0063232D[BB_0063232D]
  bb_00632330[BB_00632330]
  bb_00632335[BB_00632335]
  bb_0063233A[BB_0063233A]
  bb_00632346[BB_00632346]
  bb_00632363[BB_00632363]
  bb_00632200 -->|branch| bb_006322CE
  bb_00632200 -->|fallthrough| bb_0063223F
  bb_0063223F -->|branch| bb_00632252
  bb_0063223F -->|fallthrough| bb_00632246
  bb_00632246 -->|branch| bb_00632260
  bb_00632252 -->|branch| bb_00632260
  bb_00632252 -->|fallthrough| bb_00632256
  bb_00632256 -->|flow| bb_00632260
  bb_00632260 -->|branch| bb_00632282
  bb_00632260 -->|fallthrough| bb_00632276
  bb_00632276 -->|branch| bb_00632295
  bb_00632276 -->|fallthrough| bb_00632282
  bb_00632282 -->|branch| bb_006322CE
  bb_00632282 -->|fallthrough| bb_00632295
  bb_00632295 -->|branch| bb_006322B8
  bb_0063229E -->|branch| bb_006322B5
  bb_0063229E -->|fallthrough| bb_006322A7
  bb_006322A7 -->|flow| bb_006322B5
  bb_006322B5 -->|flow| bb_006322B8
  bb_006322B8 -->|branch| bb_0063229E
  bb_006322B8 -->|fallthrough| bb_006322BD
  bb_006322BD -->|branch| bb_006322CE
  bb_006322BD -->|fallthrough| bb_006322C2
  bb_006322C2 -->|flow| bb_006322CE
  bb_006322CE -->|branch| bb_00632346
  bb_006322CE -->|fallthrough| bb_006322E2
  bb_006322E2 -->|branch| bb_006322FA
  bb_006322E2 -->|fallthrough| bb_006322EE
  bb_006322EE -->|branch| bb_0063230D
  bb_006322EE -->|fallthrough| bb_006322FA
  bb_006322FA -->|branch| bb_00632346
  bb_006322FA -->|fallthrough| bb_0063230D
  bb_0063230D -->|branch| bb_00632330
  bb_00632316 -->|branch| bb_0063232D
  bb_00632316 -->|fallthrough| bb_0063231F
  bb_0063231F -->|flow| bb_0063232D
  bb_0063232D -->|flow| bb_00632330
  bb_00632330 -->|branch| bb_00632316
  bb_00632330 -->|fallthrough| bb_00632335
  bb_00632335 -->|branch| bb_00632346
  bb_00632335 -->|fallthrough| bb_0063233A
  bb_0063233A -->|flow| bb_00632346
```
