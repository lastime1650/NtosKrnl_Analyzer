# DifZwDisplayStringWrapper

- RVA: `0x00641230`–`0x0064138D` (길이 `349` bytes)
- VA: `0x0000000140641230`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `349/349` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0064125D` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00641285` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006412B3` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006412DA` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006412F3` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006412FB` → [ZwDisplayString](../6A/ZwDisplayString_function_006AED50.md) (function, `0x006AED50`)
- `0x00641328` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064134F` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00641368` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00641297` → RVA `0x00F048B8` (`.data`; read)
- `0x006412A0` → RVA `0x00F04980` (`.data`; read)
- `0x006412AC` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00641230  4C 8B DC                        mov r11, rsp
00641233  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00641237  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0064123B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0064123F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00641243  41 56                           push r14
00641245  48 83 EC 40                     sub rsp, 0x40
00641249  33 C0                           xor eax, eax
0064124B  0F 57 C0                        xorps xmm0, xmm0
0064124E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00641253  48 8B E9                        mov rbp, rcx
00641256  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0064125A  8D 48 6D                        lea ecx, [rax + 0x6d]
0064125D  E8 D2 47 E5 FF                  call 0x140495a34
00641262  48 8B F0                        mov rsi, rax
00641265  48 85 C0                        test rax, rax
00641268  0F 84 8A 00 00 00               je 0x1406412f8
0064126E  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00641271  A8 18                           test al, 0x18
00641273  74 0C                           je 0x140641281
00641275  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0064127A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0064127F  EB 0E                           jmp 0x14064128f
00641281  A8 04                           test al, 4
00641283  74 0A                           je 0x14064128f
00641285  E8 7E 29 E9 FF                  call 0x1404d3c08
0064128A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0064128F  40 32 FF                        xor dil, dil
00641292  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00641297  40 38 3D 1A 36 8C 00            cmp byte ptr [rip + 0x8c361a], dil
0064129E  75 0C                           jne 0x1406412ac
006412A0  F7 05 D6 36 8C 00 00 08 00 00   test dword ptr [rip + 0x8c36d6], 0x800
006412AA  74 13                           je 0x1406412bf
006412AC  48 8D 0D CD 2B 8C 00            lea rcx, [rip + 0x8c2bcd]
006412B3  E8 68 53 BD FF                  call 0x140216620
006412B8  40 8A F8                        mov dil, al
006412BB  84 C0                           test al, al
006412BD  74 39                           je 0x1406412f8
006412BF  4C 8D 76 20                     lea r14, [rsi + 0x20]
006412C3  49 8B 1E                        mov rbx, qword ptr [r14]
006412C6  EB 1A                           jmp 0x1406412e2
006412C8  48 8D 43 F0                     lea rax, [rbx - 0x10]
006412CC  48 85 C0                        test rax, rax
006412CF  74 0E                           je 0x1406412df
006412D1  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006412D5  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006412DA  E8 F1 97 07 00                  call 0x1406baad0
006412DF  48 8B 1B                        mov rbx, qword ptr [rbx]
006412E2  49 3B DE                        cmp rbx, r14
006412E5  75 E1                           jne 0x1406412c8
006412E7  40 84 FF                        test dil, dil
006412EA  74 0C                           je 0x1406412f8
006412EC  48 8D 0D 8D 2B 8C 00            lea rcx, [rip + 0x8c2b8d]
006412F3  E8 88 8B D0 FF                  call 0x140349e80
006412F8  48 8B CD                        mov rcx, rbp
006412FB  E8 50 DA 06 00                  call 0x1406aed50
00641300  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00641304  48 85 F6                        test rsi, rsi
00641307  74 64                           je 0x14064136d
00641309  40 32 FF                        xor dil, dil
0064130C  40 38 3D A5 35 8C 00            cmp byte ptr [rip + 0x8c35a5], dil
00641313  75 0C                           jne 0x140641321
00641315  F7 05 61 36 8C 00 00 08 00 00   test dword ptr [rip + 0x8c3661], 0x800
0064131F  74 13                           je 0x140641334
00641321  48 8D 0D 58 2B 8C 00            lea rcx, [rip + 0x8c2b58]
00641328  E8 F3 52 BD FF                  call 0x140216620
0064132D  40 8A F8                        mov dil, al
00641330  84 C0                           test al, al
00641332  74 39                           je 0x14064136d
00641334  48 83 C6 30                     add rsi, 0x30
00641338  48 8B 1E                        mov rbx, qword ptr [rsi]
0064133B  EB 1A                           jmp 0x140641357
0064133D  48 8D 43 F0                     lea rax, [rbx - 0x10]
00641341  48 85 C0                        test rax, rax
00641344  74 0E                           je 0x140641354
00641346  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064134A  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0064134F  E8 7C 97 07 00                  call 0x1406baad0
00641354  48 8B 1B                        mov rbx, qword ptr [rbx]
00641357  48 3B DE                        cmp rbx, rsi
0064135A  75 E1                           jne 0x14064133d
0064135C  40 84 FF                        test dil, dil
0064135F  74 0C                           je 0x14064136d
00641361  48 8D 0D 18 2B 8C 00            lea rcx, [rip + 0x8c2b18]
00641368  E8 13 8B D0 FF                  call 0x140349e80
0064136D  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00641371  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00641376  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0064137B  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00641380  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00641385  48 83 C4 40                     add rsp, 0x40
00641389  41 5E                           pop r14
0064138B  C3                              ret
0064138C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwDisplayStringWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m18;
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
    result = DifGetAPIThunkContextById(result + 109, a2, a3, a4);
    if (result == 0) goto loc_006412F8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00641281;
    v_stack_m28 = v_stack_p0;
    goto loc_0064128F;
loc_00641281:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9188890)) != 0) goto loc_006412AC;
    if (((*(unsigned int *)(v_rip + 9189078)) & (0x800ULL)) == 0) goto loc_006412BF;
loc_006412AC:
    result = ExAcquireRundownProtection(v_rip + 9186253, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006412F8;
loc_006412BF:
    goto loc_006412E2;
loc_006412C8:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006412E2:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006412C8;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9186189;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwDisplayString(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_0064136D;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9188773)) != 0) goto loc_00641321;
    if (((*(unsigned int *)(v_rip + 9188961)) & (0x800ULL)) == 0) goto loc_00641334;
loc_00641321:
    result = ExAcquireRundownProtection(v_rip + 9186136, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064136D;
loc_00641334:
    v_rsi = (result) + (48);
    goto loc_00641357;
loc_0064133D:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00641357:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0064133D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9186072;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwDisplayStringWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m18;
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
    result = DifGetAPIThunkContextById(result + 109, a2, a3, a4);
    if (result == 0) goto loc_006412F8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00641281;
    v_stack_m28 = v_stack_p0;
    goto loc_0064128F;
loc_00641281:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8C361A)) != 0) goto loc_006412AC;
    if (((*(uint32_t *)(v_rip + 0x8C36D6)) & (0x800ULL)) == 0) goto loc_006412BF;
loc_006412AC:
    result = ExAcquireRundownProtection(v_rip + 9186253, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006412F8;
loc_006412BF:
    goto loc_006412E2;
loc_006412C8:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006412E2:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006412C8;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9186189;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ZwDisplayString(Arg1, a2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_0064136D;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C35A5)) != 0) goto loc_00641321;
    if (((*(uint32_t *)(v_rip + 0x8C3661)) & (0x800ULL)) == 0) goto loc_00641334;
loc_00641321:
    result = ExAcquireRundownProtection(v_rip + 9186136, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0064136D;
loc_00641334:
    local_rsi = (result) + (48);
    goto loc_00641357;
loc_0064133D:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00641357:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0064133D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9186072;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00641230&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00641230[BB_00641230]
  bb_0064126E[BB_0064126E]
  bb_00641275[BB_00641275]
  bb_00641281[BB_00641281]
  bb_00641285[BB_00641285]
  bb_0064128F[BB_0064128F]
  bb_006412A0[BB_006412A0]
  bb_006412AC[BB_006412AC]
  bb_006412BF[BB_006412BF]
  bb_006412C8[BB_006412C8]
  bb_006412D1[BB_006412D1]
  bb_006412DF[BB_006412DF]
  bb_006412E2[BB_006412E2]
  bb_006412E7[BB_006412E7]
  bb_006412EC[BB_006412EC]
  bb_006412F8[BB_006412F8]
  bb_00641309[BB_00641309]
  bb_00641315[BB_00641315]
  bb_00641321[BB_00641321]
  bb_00641334[BB_00641334]
  bb_0064133D[BB_0064133D]
  bb_00641346[BB_00641346]
  bb_00641354[BB_00641354]
  bb_00641357[BB_00641357]
  bb_0064135C[BB_0064135C]
  bb_00641361[BB_00641361]
  bb_0064136D[BB_0064136D]
  bb_0064138C[BB_0064138C]
  bb_00641230 -->|branch| bb_006412F8
  bb_00641230 -->|fallthrough| bb_0064126E
  bb_0064126E -->|branch| bb_00641281
  bb_0064126E -->|fallthrough| bb_00641275
  bb_00641275 -->|branch| bb_0064128F
  bb_00641281 -->|branch| bb_0064128F
  bb_00641281 -->|fallthrough| bb_00641285
  bb_00641285 -->|flow| bb_0064128F
  bb_0064128F -->|branch| bb_006412AC
  bb_0064128F -->|fallthrough| bb_006412A0
  bb_006412A0 -->|branch| bb_006412BF
  bb_006412A0 -->|fallthrough| bb_006412AC
  bb_006412AC -->|branch| bb_006412F8
  bb_006412AC -->|fallthrough| bb_006412BF
  bb_006412BF -->|branch| bb_006412E2
  bb_006412C8 -->|branch| bb_006412DF
  bb_006412C8 -->|fallthrough| bb_006412D1
  bb_006412D1 -->|flow| bb_006412DF
  bb_006412DF -->|flow| bb_006412E2
  bb_006412E2 -->|branch| bb_006412C8
  bb_006412E2 -->|fallthrough| bb_006412E7
  bb_006412E7 -->|branch| bb_006412F8
  bb_006412E7 -->|fallthrough| bb_006412EC
  bb_006412EC -->|flow| bb_006412F8
  bb_006412F8 -->|branch| bb_0064136D
  bb_006412F8 -->|fallthrough| bb_00641309
  bb_00641309 -->|branch| bb_00641321
  bb_00641309 -->|fallthrough| bb_00641315
  bb_00641315 -->|branch| bb_00641334
  bb_00641315 -->|fallthrough| bb_00641321
  bb_00641321 -->|branch| bb_0064136D
  bb_00641321 -->|fallthrough| bb_00641334
  bb_00641334 -->|branch| bb_00641357
  bb_0064133D -->|branch| bb_00641354
  bb_0064133D -->|fallthrough| bb_00641346
  bb_00641346 -->|flow| bb_00641354
  bb_00641354 -->|flow| bb_00641357
  bb_00641357 -->|branch| bb_0064133D
  bb_00641357 -->|fallthrough| bb_0064135C
  bb_0064135C -->|branch| bb_0064136D
  bb_0064135C -->|fallthrough| bb_00641361
  bb_00641361 -->|flow| bb_0064136D
```
