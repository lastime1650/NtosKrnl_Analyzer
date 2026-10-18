# PopDiagTraceMtrrError

- RVA: `0x00B71444`–`0x00B714C9` (길이 `133` bytes)
- VA: `0x0000000140B71444`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060904`
- 디코드: `28`개 명령, `133/133` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00B7146E` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00B714B1` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00B714BE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopTransitionSystemPowerStateEx](PopTransitionSystemPowerStateEx_function_00B7E8C0.md) at `0x00B7F7A6`

### Static image references
- `0x00B71448` → RVA `0x00E0A740` (`.data`; read)
- `0x00B71457` → RVA `0x00E67858` (`.data`; read)
- `0x00B71460` → RVA `0x00F0B408` (`.data`; read)
- `0x00B71467` → RVA `0x000212B0` (`.rdata`; read)
- `0x00B7147C` → RVA `0x00F0BD78` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00B7146E` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGELK` → `.text`)
  - `0x00B714B1` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGELK` → `.text`)
  - `0x00B714BE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B71444  48 83 EC 58                     sub rsp, 0x58
00B71448  48 8B 05 F1 92 29 00            mov rax, qword ptr [rip + 0x2992f1]
00B7144F  48 33 C4                        xor rax, rsp
00B71452  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00B71457  80 3D FA 63 2F 00 00            cmp byte ptr [rip + 0x2f63fa], 0
00B7145E  74 56                           je 0x140b714b6
00B71460  48 8B 0D A1 9F 39 00            mov rcx, qword ptr [rip + 0x399fa1]
00B71467  48 8D 15 42 FE 4A FF            lea rdx, [rip - 0xb501be]
00B7146E  E8 DD 0F 82 FF                  call 0x140392450
00B71473  84 C0                           test al, al
00B71475  74 3F                           je 0x140b714b6
00B71477  83 64 24 3C 00                  and dword ptr [rsp + 0x3c], 0
00B7147C  48 8D 05 F5 A8 39 00            lea rax, [rip + 0x39a8f5]
00B71483  48 8B 0D 7E 9F 39 00            mov rcx, qword ptr [rip + 0x399f7e]
00B7148A  48 8D 15 1F FE 4A FF            lea rdx, [rip - 0xb501e1]
00B71491  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B71496  41 B9 01 00 00 00               mov r9d, 1
00B7149C  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00B714A1  C7 44 24 38 04 00 00 00         mov dword ptr [rsp + 0x38], 4
00B714A9  45 33 C0                        xor r8d, r8d
00B714AC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B714B1  E8 6A B2 8A FF                  call 0x14041c720
00B714B6  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00B714BB  48 33 CC                        xor rcx, rsp
00B714BE  E8 7D B1 B3 FF                  call 0x1406ac640
00B714C3  48 83 C4 58                     add rsp, 0x58
00B714C7  C3                              ret
00B714C8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceMtrrError(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;

    v_rsp = (v_rsp) - (88);
    result = (*(unsigned __int64 *)(v_rip + 2724593)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 3105786)) == 0) goto loc_00B714B6;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 3776417), v_rip - 11862462, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_rip + 3778805;
        a1 = *(unsigned __int64 *)(v_rip + 3776382);
        a2 = v_rip - 11862497;
        v_stack_m28 = result;
        a4 = 1;
        result = v_stack_m28;
        v_stack_m20 = 4;
        a3 = 0;
        v_stack_m38 = result;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceMtrrError(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    result = (*(uint64_t *)(v_rip + 0x2992F1)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0x2F63FA)) == 0) goto loc_00B714B6;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x399FA1), v_rip - 11862462, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        result = v_rip + 3778805;
        Arg1 = *(uint64_t *)(v_rip + 0x399F7E);
        Arg2 = v_rip - 11862497;
        v_stack_m28 = result;
        a4 = 1;
        result = v_stack_m28;
        v_stack_m20 = 4;
        Arg3 = 0;
        v_stack_m38 = result;
        result = EtwWrite(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B71444&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B71444[BB_00B71444]
  bb_00B71460[BB_00B71460]
  bb_00B71477[BB_00B71477]
  bb_00B714B6[BB_00B714B6]
  bb_00B714C8[BB_00B714C8]
  bb_00B71444 -->|branch| bb_00B714B6
  bb_00B71444 -->|fallthrough| bb_00B71460
  bb_00B71460 -->|branch| bb_00B714B6
  bb_00B71460 -->|fallthrough| bb_00B71477
  bb_00B71477 -->|flow| bb_00B714B6
```
