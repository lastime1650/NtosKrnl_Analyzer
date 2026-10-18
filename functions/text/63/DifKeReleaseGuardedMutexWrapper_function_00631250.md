# DifKeReleaseGuardedMutexWrapper

- RVA: `0x00631250`–`0x006313A0` (길이 `336` bytes)
- VA: `0x0000000140631250`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D7BC`
- 디코드: `90`개 명령, `336/336` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00631278` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006312A0` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006312CE` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006312F5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063130E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00631316` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x0063133F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00631366` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063137F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006312B2` → RVA `0x00F048B8` (`.data`; read)
- `0x006312BB` → RVA `0x00F04980` (`.data`; read)
- `0x006312C7` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00631250  48 8B C4                        mov rax, rsp
00631253  48 89 58 08                     mov qword ptr [rax + 8], rbx
00631257  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0063125B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063125F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00631263  41 56                           push r14
00631265  48 83 EC 30                     sub rsp, 0x30
00631269  48 8B E9                        mov rbp, rcx
0063126C  0F 57 C0                        xorps xmm0, xmm0
0063126F  B9 0A 01 00 00                  mov ecx, 0x10a
00631274  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
00631278  E8 B7 47 E6 FF                  call 0x140495a34
0063127D  48 8B F8                        mov rdi, rax
00631280  48 85 C0                        test rax, rax
00631283  0F 84 8A 00 00 00               je 0x140631313
00631289  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063128C  A8 18                           test al, 0x18
0063128E  74 0C                           je 0x14063129c
00631290  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00631295  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0063129A  EB 0E                           jmp 0x1406312aa
0063129C  A8 04                           test al, 4
0063129E  74 0A                           je 0x1406312aa
006312A0  E8 63 29 EA FF                  call 0x1404d3c08
006312A5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006312AA  40 32 F6                        xor sil, sil
006312AD  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
006312B2  40 38 35 FF 35 8D 00            cmp byte ptr [rip + 0x8d35ff], sil
006312B9  75 0C                           jne 0x1406312c7
006312BB  F7 05 BB 36 8D 00 00 08 00 00   test dword ptr [rip + 0x8d36bb], 0x800
006312C5  74 13                           je 0x1406312da
006312C7  48 8D 0D B2 2B 8D 00            lea rcx, [rip + 0x8d2bb2]
006312CE  E8 4D 53 BE FF                  call 0x140216620
006312D3  40 8A F0                        mov sil, al
006312D6  84 C0                           test al, al
006312D8  74 39                           je 0x140631313
006312DA  4C 8D 77 20                     lea r14, [rdi + 0x20]
006312DE  49 8B 1E                        mov rbx, qword ptr [r14]
006312E1  EB 1A                           jmp 0x1406312fd
006312E3  48 8D 43 F0                     lea rax, [rbx - 0x10]
006312E7  48 85 C0                        test rax, rax
006312EA  74 0E                           je 0x1406312fa
006312EC  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006312F0  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006312F5  E8 D6 97 08 00                  call 0x1406baad0
006312FA  48 8B 1B                        mov rbx, qword ptr [rbx]
006312FD  49 3B DE                        cmp rbx, r14
00631300  75 E1                           jne 0x1406312e3
00631302  40 84 F6                        test sil, sil
00631305  74 0C                           je 0x140631313
00631307  48 8D 0D 72 2B 8D 00            lea rcx, [rip + 0x8d2b72]
0063130E  E8 6D 8B D1 FF                  call 0x140349e80
00631313  48 8B CD                        mov rcx, rbp
00631316  E8 A5 06 C2 FF                  call 0x1402519c0
0063131B  48 85 FF                        test rdi, rdi
0063131E  74 64                           je 0x140631384
00631320  40 32 F6                        xor sil, sil
00631323  40 38 35 8E 35 8D 00            cmp byte ptr [rip + 0x8d358e], sil
0063132A  75 0C                           jne 0x140631338
0063132C  F7 05 4A 36 8D 00 00 08 00 00   test dword ptr [rip + 0x8d364a], 0x800
00631336  74 13                           je 0x14063134b
00631338  48 8D 0D 41 2B 8D 00            lea rcx, [rip + 0x8d2b41]
0063133F  E8 DC 52 BE FF                  call 0x140216620
00631344  40 8A F0                        mov sil, al
00631347  84 C0                           test al, al
00631349  74 39                           je 0x140631384
0063134B  48 83 C7 30                     add rdi, 0x30
0063134F  48 8B 1F                        mov rbx, qword ptr [rdi]
00631352  EB 1A                           jmp 0x14063136e
00631354  48 8D 43 F0                     lea rax, [rbx - 0x10]
00631358  48 85 C0                        test rax, rax
0063135B  74 0E                           je 0x14063136b
0063135D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00631361  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00631366  E8 65 97 08 00                  call 0x1406baad0
0063136B  48 8B 1B                        mov rbx, qword ptr [rbx]
0063136E  48 3B DF                        cmp rbx, rdi
00631371  75 E1                           jne 0x140631354
00631373  40 84 F6                        test sil, sil
00631376  74 0C                           je 0x140631384
00631378  48 8D 0D 01 2B 8D 00            lea rcx, [rip + 0x8d2b01]
0063137F  E8 FC 8A D1 FF                  call 0x140349e80
00631384  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00631389  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0063138E  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00631393  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00631398  48 83 C4 30                     add rsp, 0x30
0063139C  41 5E                           pop r14
0063139E  C3                              ret
0063139F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeReleaseGuardedMutexWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 24) = v_xmm0;
    result = DifGetAPIThunkContextById(266, a2, a3, a4);
    if (result == 0) goto loc_00631313;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063129C;
    v_stack_m18 = v_stack_p0;
    goto loc_006312AA;
loc_0063129C:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9254399)) != 0) goto loc_006312C7;
    if (((*(unsigned int *)(v_rip + 9254587)) & (0x800ULL)) == 0) goto loc_006312DA;
loc_006312C7:
    result = ExAcquireRundownProtection(v_rip + 9251762, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00631313;
loc_006312DA:
    goto loc_006312FD;
loc_006312E3:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006312FD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006312E3;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9251698;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExReleaseFastMutex(a1, a2, a3, a4);
    if (result == 0) goto loc_00631384;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9254286)) != 0) goto loc_00631338;
    if (((*(unsigned int *)(v_rip + 9254474)) & (0x800ULL)) == 0) goto loc_0063134B;
loc_00631338:
    result = ExAcquireRundownProtection(v_rip + 9251649, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00631384;
loc_0063134B:
    v_rdi = (result) + (48);
    goto loc_0063136E;
loc_00631354:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063136E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_00631354;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9251585;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeReleaseGuardedMutexWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x18) = v_xmm0;
    result = DifGetAPIThunkContextById(266, a2, a3, a4);
    if (result == 0) goto loc_00631313;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063129C;
    v_stack_m18 = v_stack_p0;
    goto loc_006312AA;
loc_0063129C:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8D35FF)) != 0) goto loc_006312C7;
    if (((*(uint32_t *)(v_rip + 0x8D36BB)) & (0x800ULL)) == 0) goto loc_006312DA;
loc_006312C7:
    result = ExAcquireRundownProtection(v_rip + 9251762, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00631313;
loc_006312DA:
    goto loc_006312FD;
loc_006312E3:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006312FD:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006312E3;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9251698;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExReleaseFastMutex(Arg1, a2, a3, a4);
    if (result == 0) goto loc_00631384;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D358E)) != 0) goto loc_00631338;
    if (((*(uint32_t *)(v_rip + 0x8D364A)) & (0x800ULL)) == 0) goto loc_0063134B;
loc_00631338:
    result = ExAcquireRundownProtection(v_rip + 9251649, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00631384;
loc_0063134B:
    local_rdi = (result) + (48);
    goto loc_0063136E;
loc_00631354:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0063136E:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_00631354;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9251585;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00631250&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00631250[BB_00631250]
  bb_00631289[BB_00631289]
  bb_00631290[BB_00631290]
  bb_0063129C[BB_0063129C]
  bb_006312A0[BB_006312A0]
  bb_006312AA[BB_006312AA]
  bb_006312BB[BB_006312BB]
  bb_006312C7[BB_006312C7]
  bb_006312DA[BB_006312DA]
  bb_006312E3[BB_006312E3]
  bb_006312EC[BB_006312EC]
  bb_006312FA[BB_006312FA]
  bb_006312FD[BB_006312FD]
  bb_00631302[BB_00631302]
  bb_00631307[BB_00631307]
  bb_00631313[BB_00631313]
  bb_00631320[BB_00631320]
  bb_0063132C[BB_0063132C]
  bb_00631338[BB_00631338]
  bb_0063134B[BB_0063134B]
  bb_00631354[BB_00631354]
  bb_0063135D[BB_0063135D]
  bb_0063136B[BB_0063136B]
  bb_0063136E[BB_0063136E]
  bb_00631373[BB_00631373]
  bb_00631378[BB_00631378]
  bb_00631384[BB_00631384]
  bb_0063139F[BB_0063139F]
  bb_00631250 -->|branch| bb_00631313
  bb_00631250 -->|fallthrough| bb_00631289
  bb_00631289 -->|branch| bb_0063129C
  bb_00631289 -->|fallthrough| bb_00631290
  bb_00631290 -->|branch| bb_006312AA
  bb_0063129C -->|branch| bb_006312AA
  bb_0063129C -->|fallthrough| bb_006312A0
  bb_006312A0 -->|flow| bb_006312AA
  bb_006312AA -->|branch| bb_006312C7
  bb_006312AA -->|fallthrough| bb_006312BB
  bb_006312BB -->|branch| bb_006312DA
  bb_006312BB -->|fallthrough| bb_006312C7
  bb_006312C7 -->|branch| bb_00631313
  bb_006312C7 -->|fallthrough| bb_006312DA
  bb_006312DA -->|branch| bb_006312FD
  bb_006312E3 -->|branch| bb_006312FA
  bb_006312E3 -->|fallthrough| bb_006312EC
  bb_006312EC -->|flow| bb_006312FA
  bb_006312FA -->|flow| bb_006312FD
  bb_006312FD -->|branch| bb_006312E3
  bb_006312FD -->|fallthrough| bb_00631302
  bb_00631302 -->|branch| bb_00631313
  bb_00631302 -->|fallthrough| bb_00631307
  bb_00631307 -->|flow| bb_00631313
  bb_00631313 -->|branch| bb_00631384
  bb_00631313 -->|fallthrough| bb_00631320
  bb_00631320 -->|branch| bb_00631338
  bb_00631320 -->|fallthrough| bb_0063132C
  bb_0063132C -->|branch| bb_0063134B
  bb_0063132C -->|fallthrough| bb_00631338
  bb_00631338 -->|branch| bb_00631384
  bb_00631338 -->|fallthrough| bb_0063134B
  bb_0063134B -->|branch| bb_0063136E
  bb_00631354 -->|branch| bb_0063136B
  bb_00631354 -->|fallthrough| bb_0063135D
  bb_0063135D -->|flow| bb_0063136B
  bb_0063136B -->|flow| bb_0063136E
  bb_0063136E -->|branch| bb_00631354
  bb_0063136E -->|fallthrough| bb_00631373
  bb_00631373 -->|branch| bb_00631384
  bb_00631373 -->|fallthrough| bb_00631378
  bb_00631378 -->|flow| bb_00631384
```
